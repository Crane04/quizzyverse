const calculator= document.querySelector(".calculator")
const calc_box = document.querySelector(".question-box input")
const answer_box = document.querySelector(".answer-box")

function calculator_state(state){
    calculator.style.display = state
}
function solve(){
    calc_ = calc_box.value
    calc_ = calc_.replace("^", "**")
    calc_ = calc_.replace("÷", "/")
    calc_ = calc_.replace("×", "*")
    let answer = eval(calc_)
    
    if (!answer){
        answer_box.innerText = "0"
    }else{
        if(typeof answer == "number"){
            answer_box.innerText = answer.toFixed(7)
        }else{
            answer_box.innerText = answer
        }
    }
}
let conv_trig = Math.PI /180
function Sin(num){
    return Math.sin(conv_trig * num)
}
function Cos(num){
    return Math.cos(conv_trig * num)
}
function Tan(num){
    if(num===90||num===270) {
        return 'Undefined'
    }else{
        return Math.tan(conv_trig*num)
    }
}
function Log(num){
    return Math.log10(num)
}

let conv_inv_trig = 180/Math.PI
function aSin(num){

    return (Math.asin(num)*conv_inv_trig)
}
function aCos(num){
    
    return Math.acos(num)*conv_inv_trig
}
function aTan(num){
    
    return Math.atan(num)*180/Math.PI
}
function Sqrt(num){
    return Math.sqrt(num)
}

