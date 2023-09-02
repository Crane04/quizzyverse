const exam_st = document.querySelector("#exam_st")
        const exam_end = document.querySelector("#exam_end")
        const date = new Date()
        const year = date.getFullYear()
        const month = String(date.getMonth() + 1).padStart(2, "0")
        const day = String(date.getDate()).padStart(2, "0")
        const hour = String(date.getHours()).padStart(2, "0")
        const minutes = String(date.getMinutes()).padStart(2, "0")
        const sub_btn = document.querySelector("button")

        exam_st.min = exam_end.min = `${year}-${month}-${day}T${hour}:${minutes}`
        
        sub_btn.addEventListener("click", function(e){
            if(!exam_st.value || !exam_end.value){
                e.preventDefault()
                alert("Date Fields cannot be empty!")
            }

            else if(exam_st.value >= exam_end.value){
                e.preventDefault()
                alert("The Exam End Date must be farther than the Start Date!")
            }else{
                const confirm_submission = confirm("Do you want to submit?")
                if(!confirm_submission){
                    e.preventDefault()
                }
            }

        })