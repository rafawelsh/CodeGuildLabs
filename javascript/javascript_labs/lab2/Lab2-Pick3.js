//2.passwordGenerator.js

function passwordGenerator(length) {
  var chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz";
  var password = '';

  for (var i=0; i<length; i++) {
      let char = Math.floor(Math.random() * chars.length);
      password += chars[char]
  }
  console.log(password)
}
