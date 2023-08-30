var nameError = document.getElementById('name-error');
var mailError = document.getElementById('email-error');
var passError = document.getElementById('pass-error');
var retypeError = document.getElementById('retype-pass-error');
var registerError = document.getElementById('register-error');


function validateMail() {
    var email = document.getElementById('email').value;
    var atIndex = email.indexOf('@');
    if (atIndex === -1) {
        mailError.innerHTML = 'Invalid email format';
        return false;
    }
    var username = email.slice(0, atIndex);
    var domain = email.slice(atIndex + 1);
    if (domain !== 'av.students.amrita.edu') {
        mailError.innerHTML = 'Use Amrita Mail';
        return false;
    }
    if (email.length == 0) {
        mailError.innerHTML = 'Email is required';
        return false;
    }
    mailError.innerHTML = '<i class="fas fa-check-circle"></i>';
    return true;
}

function validatePassword() {
    var password = document.getElementById('password').value;
    if (password.length < 8) {
        passError.innerHTML = 'Must be 8 characters long';
        return false;
    }

    // Check if the password contains at least one uppercase letter
    if (!password.match(/[A-Z]/)) {
        passError.innerHTML = 'At least one uppercase';
        return false;
    }

    // Check if the password contains at least one lowercase letter
    if (!password.match(/[a-z]/)) {
        passError.innerHTML = 'At least one lowercase';
        return false;
    }

    // Check if the password contains at least one digit
    if (!password.match(/[0-9]/)) {
        passError.innerHTML = 'At least one digit';
        return false;
    }

    // Check if the password contains at least one special character
    if (!password.match(/[^A-Za-z0-9]/)) {
        passError.innerHTML = 'At least one special character';
        return false;
    }

    // If all checks passed, the password is valid
    passError.innerHTML = '<i class="fas fa-check-circle"></i>';
    return true;
}
function validateRePassword() {
    var password = document.getElementById('password').value;
    var repassword = document.getElementById('retype-password').value;
    if (password !== repassword) {
        retypeError.innerHTML = 'Passwords do not match';
        return false;
    }
    retypeError.innerHTML = '<i class="fas fa-check-circle"></i>';
    return true;
}

function validateRegister() {
    if (!validateMail()) {
        registerError.innerHTML = 'Invalid email';
        return false;
    }

    if (!validatePassword()) {
        registerError.innerHTML = 'Invalid password';
        return false;
    }

    if (!validateRePassword()) {
        registerError.innerHTML = 'Passwords do not match';
        return false;
    }

    return true;
}
