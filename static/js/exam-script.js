        // Declare Variables

     const count_answered = document.querySelector("#count-answered"),
                total_questions = document.querySelector("#total-questions"),
                unit_questions = document.querySelectorAll(".unit-question"),
                submit = document.querySelector("#submit"),
                q_num = document.querySelectorAll("span.q-num"),
                radios = document.querySelectorAll("input[type='radio']")

        total_questions.innerText = unit_questions.length



/*Number of answered questions*/
let count_checked = setInterval(() => {
    let checked_radios = document.querySelectorAll("input[type='radio']:checked")
    answered_questions = checked_radios.length
    count_answered.innerText = answered_questions
}, 1000);

        
        /*answered questions*/

function check(num){
    document.querySelectorAll(".pagination-number")[num].classList.add("answered")
}


submit.addEventListener("click", function(e){

    if (confirm("Are you sure you want to submit?")) {

        e.disabled = true
        } else {
            e.preventDefault()
        }
    })

// Question Numbering
for(let i = 0; i<q_num.length; i++){
    q_num[i].innerText = i + 1 + ". "
}


for (var i = 0; i< radios.length; i++){
    if (i % 4 == 0){
        var groupId = Math.floor(i / 4)
    }
    radios[i].setAttribute("onclick", "check("+ groupId +")")
}