// =====================================
// LOGIN FORM
// =====================================

var myInput = document.getElementById("password");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");


// When the user clicks on the password field, show the message box
myInput.onfocus = function() {
  document.getElementById("message").style.display = "block";
}


// When the user clicks outside of the password field, hide the message box
myInput.onblur = function() {
  document.getElementById("message").style.display = "none";
}


// When the user starts to type something inside the password field
myInput.onkeyup = function() {
  // Validate lowercase letters
  var lowerCaseLetters = /[a-z]/g;
  if(myInput.value.match(lowerCaseLetters)) {  
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
  }
  
  // Validate capital letters
  var upperCaseLetters = /[A-Z]/g;
  if(myInput.value.match(upperCaseLetters)) {  
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }

  // Validate numbers
  var numbers = /[0-9]/g;
  if(myInput.value.match(numbers)) {  
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }
  
  // Validate length
  if(myInput.value.length >= 8) {
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }
}

// END OF PASSWORD VALIDATION



// SHOW PASSWORD

function myFunction() {
    var login_password = document.getElementById("password");
    if (login_password.type === "password") {
        login_password.type = "text";
    } else {
        login_password.type = "password";
    }
}

// =====================================
// END OF LOGIN FORM
// =====================================


// =====================================
// USER REGISTRATION FORM
// =====================================

var password_register = document.getElementById("password_register");
var letter_password_register = document.getElementById("letter_password_register");
var capital_password_register = document.getElementById("capital_password_register");
var number_password_register = document.getElementById("number_password_register");
var length_password_register = document.getElementById("length_password_register");


// When the user clicks on the password field, show the message box
password_register.onfocus = function() {
  document.getElementById("message_password_register").style.display = "block";
}


// When the user clicks outside of the password field, hide the message box
password_register.onblur = function() {
  document.getElementById("message_password_register").style.display = "none";
}


// When the user starts to type something inside the password field
password_register.onkeyup = function() {
  // Validate lowercase letters
  var lowerCaseLetters = /[a-z]/g;
  if(password_register.value.match(lowerCaseLetters)) {  
    letter_password_register.classList.remove("invalid");
    letter_password_register.classList.add("valid");
  } else {
    letter_password_register.classList.remove("valid");
    letter_password_register.classList.add("invalid");
  }
  
  // Validate capital letters
  var upperCaseLetters = /[A-Z]/g;
  if(password_register.value.match(upperCaseLetters)) {  
    capital_password_register.classList.remove("invalid");
    capital_password_register.classList.add("valid");
  } else {
    capital_password_register.classList.remove("valid");
    capital_password_register.classList.add("invalid");
  }

  // Validate numbers
  var numbers = /[0-9]/g;
  if(password_register.value.match(numbers)) {  
    number_password_register.classList.remove("invalid");
    number_password_register.classList.add("valid");
  } else {
    number_password_register.classList.remove("valid");
    number_password_register.classList.add("invalid");
  }
  
  // Validate length
  if(password_register.value.length >= 8) {
    length_password_register.classList.remove("invalid");
    length_password_register.classList.add("valid");
  } else {
    length_password_register.classList.remove("valid");
    length_password_register.classList.add("invalid");
  }
}

// END OF PASSWORD VALIDATION



// SHOW PASSWORD

function myRegisterPasswordFunction() {
    var first_password_register = document.getElementById("password_register");
    if (first_password_register.type === "password") {
      first_password_register.type = "text";
    } else {
      first_password_register.type = "password";
    }
}

// End of passowrd




// Confrm password

var confirm_password_register = document.getElementById("confirm_password_register");
var letter_confirm_password_register = document.getElementById("letter_confirm_password_register");
var capital_confirm_password_register = document.getElementById("capital_confirm_password_register");
var number_confirm_password_register = document.getElementById("number_confirm_password_register");
var length_confirm_password_register = document.getElementById("length_confirm_password_register");


// When the user clicks on the password field, show the message box
confirm_password_register.onfocus = function() {
  document.getElementById("message_confirm_password_register").style.display = "block";
}


// When the user clicks outside of the password field, hide the message box
confirm_password_register.onblur = function() {
  document.getElementById("message_confirm_password_register").style.display = "none";
}


// When the user starts to type something inside the password field
confirm_password_register.onkeyup = function() {
  // Validate lowercase letters
  var lowerCaseLetters = /[a-z]/g;
  if(confirm_password_register.value.match(lowerCaseLetters)) {  
    letter_confirm_password_register.classList.remove("invalid");
    letter_confirm_password_register.classList.add("valid");
  } else {
    letter_confirm_password_register.classList.remove("valid");
    letter_confirm_password_register.classList.add("invalid");
  }
  
  // Validate capital letters
  var upperCaseLetters = /[A-Z]/g;
  if(confirm_password_register.value.match(upperCaseLetters)) {  
    capital_confirm_password_register.classList.remove("invalid");
    capital_confirm_password_register.classList.add("valid");
  } else {
    capital_confirm_password_register.classList.remove("valid");
    capital_confirm_password_register.classList.add("invalid");
  }

  // Validate numbers
  var numbers = /[0-9]/g;
  if(confirm_password_register.value.match(numbers)) {  
    number_confirm_password_register.classList.remove("invalid");
    number_confirm_password_register.classList.add("valid");
  } else {
    number_confirm_password_register.classList.remove("valid");
    number_confirm_password_register.classList.add("invalid");
  }
  
  // Validate length
  if(confirm_password_register.value.length >= 8) {
    length_confirm_password_register.classList.remove("invalid");
    length_confirm_password_register.classList.add("valid");
  } else {
    length_confirm_password_register.classList.remove("valid");
    length_confirm_password_register.classList.add("invalid");
  }
}

// END OF PASSWORD VALIDATION



// SHOW PASSWORD

function myRegisterConfirmPasswordFunction() {
    var second_confirm_password_register = document.getElementById("confirm_password_register");
    if (second_confirm_password_register.type === "password") {
      second_confirm_password_register.type = "text";
    } else {
      second_confirm_password_register.type = "password";
    }
}


// End of confirm password


// =====================================
// END OF USER REGISTRATION FORM
// =====================================