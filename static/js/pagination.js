// Declare Variables

const pagination_btns = document.querySelectorAll(".pagination button")
const pagination_numbers = document.querySelector(".pagination")
const paginatedList = document.querySelector("form");
const prev = document.querySelector("#prev")
const next = document.querySelector("#next")

// Questions Per Page
const paginationLimit = 1;
const pageCount = Math.ceil(unit_questions.length / paginationLimit);
let currentPage;

const appendPageNumber = (index) => {
        const pageNumber = document.createElement("button");
        pageNumber.className = "pagination-number";
        pageNumber.innerHTML = index;
        pageNumber.setAttribute("page-index", index);
        pageNumber.setAttribute("aria-label", "Page " + index);
        pagination_numbers.appendChild(pageNumber);
};
const getPaginationNumbers = () => {
    for (let i = 1; i <= pageCount; i++) {
        appendPageNumber(i);
    }
};


const setCurrentPage = (pageNum) => {
    currentPage = pageNum;

    handleActivePageNumber();
    handlePageButtonsStatus();
    const prevRange = (pageNum - 1) * paginationLimit;
    const currRange = pageNum * paginationLimit;
    unit_questions.forEach((item, index) => {
        item.classList.add("hidden");
        if (index >= prevRange && index < currRange) {
            item.classList.remove("hidden");
        }
    });
};
window.addEventListener("load", () => {
    getPaginationNumbers();
    setCurrentPage(1);

    prev.addEventListener("click", () => {
        setCurrentPage(currentPage - 1);
    });
    next.addEventListener("click", () => {
        setCurrentPage(currentPage + 1);
    });

document.querySelectorAll(".pagination-number").forEach((button) => {
    const pageIndex = Number(button.getAttribute("page-index"));
        if (pageIndex) {
            button.addEventListener("click", () => {
                setCurrentPage(pageIndex);
            });
        }
    });
});

const disableButton = (button) => {
    button.classList.add("disabled");
    button.setAttribute("disabled", true);
};
const enableButton = (button) => {
    button.classList.remove("disabled");
    button.removeAttribute("disabled");
};
const handlePageButtonsStatus = () => {
    if (currentPage === 1) {
        disableButton(prev);
    } else {
        enableButton(prev);
    }
    if (pageCount === currentPage) {
        disableButton(next);
    } else {
        enableButton(next);
    }
};
const handleActivePageNumber = () => {
    document.querySelectorAll(".pagination-number").forEach((button) => {
        button.classList.remove("active");

        const pageIndex = Number(button.getAttribute("page-index"));
        if (pageIndex == currentPage) {
            button.classList.add("active");
        }
    });
};
