//1.grading.js

//DOM Selectors
const btn = document.querySelector("#button");
const grades =  document.querySelector("#gradeInput");
const letterGrade =  document.querySelector("#display");


//function
const updateDisplay = (value) => {
  letterGrade.innerText = value
}


// Default display text
updateDisplay('Letter Grade: ')


//Event Listener
btn.addEventListener("click", (evt) => {
    // evt.preventDefault()
    let grade = parseFloat(grades.value);
    console.log(typeof(grade))
    let lt = ''
    let sign = ''
    let one_unit = grade % 10


    if (grade >= 90) {
        lt = 'A'
    } else if (grade >= 80){
        lt = 'B'
    } else if (grade >= 70){
        lt = 'C'
    } else if (grade >= 60){
        lt = 'D'
    } else {
        lt = 'F'
    }

    if (one_unit >= 7){
      sign = '+'
    } else if (one_unit <= 3){
      sign = '-'
    } else {
      sign = ''
    }

    let final = lt + sign
    updateDisplay('Letter grade: '+final)
})
