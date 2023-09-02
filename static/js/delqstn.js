const del_btn = document.querySelectorAll("form button")

for(let i = 0; i<del_btn.length; i++){
    del_btn[i].addEventListener("click", function(e){
        if(confirm("Are you sure you want to delete?")){
            console.log("Deleting...");
        }else{
            e.preventDefault()
        }
    })
}