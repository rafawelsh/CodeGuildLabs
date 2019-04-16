//3.creditCardValidator.js

//DOM Selectors
const card = document.querySelector("#credit");
const btn = document.querySelector("#button");
const valid = document.querySelector("#display");


//function
const updateDisplay = (value) => {
  valid.innerText = value
}

const validate = (card) => {
  console.log('card input:',typeof(card), card)
  let string = card.toString();
  console.log('string input:',typeof(string), string)
  const strings = string.split('').map(function(item) {
    return parseInt(item, 10);
    }
  );

  let checkDigit = strings.pop().toString();
  let revCheckDigit = strings.reverse();

  for (let i=0; i<revCheckDigit.length; i+=2) {
    revCheckDigit[i] *= 2
    if (revCheckDigit[i] >= 10){
      revCheckDigit[i] -= 9;
    }
  }

  let sum = revCheckDigit.reduce(add);
  function add(accumulator, a) {
      return accumulator + a;
  }
  console.log('sum input:',typeof(sum), sum)

  let checker = sum.toString()
  console.log('checker input:',typeof(checker), checker)
  return (checker[1] === checkDigit ? 'Valid' : 'Not Valid')
}

// Default display text
updateDisplay('345')


//Event listener
btn.addEventListener("click", (evt) =>{
  const output = validate(card.value)
  updateDisplay(output)
 })


// validate("4556737586899855")
