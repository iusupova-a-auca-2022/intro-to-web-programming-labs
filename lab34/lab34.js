// Lab 1
let a = 12;
let b = -25;

console.log("Addition:", a + b);
console.log("Subtraction:", a - b);
console.log("Multiplication:", a * b);
console.log("Division:", a / b);
console.log("Modulus:", a % b);
console.log("Exponentiation:", a ** b);

// Lab 2
let userAge = prompt("Enter your age:");
let isRegistered = prompt("Are you regestered? Yes or No");

if (userAge >= 18 && (isRegistered == "Yes" || isRegistered == "yes")) {
    console.log("You can vote!");
} else {
    console.log("You can't vote!");
}

// Lab 3
let numOne = 31;
let numTwo = 90;

if (numOne > numTwo) {
    console.log("Number One is greater than Number Two!");
} else if (numOne < numTwo) {
    console.log("Number Two is greater than Number One!");
} else {
    console.log("Both numbers are equal!");
}

// Lab 4
let num = 8;

if (num > 0) {
    console.log("Number " + num + " is positive.");
} else if (num < 0) {
    console.log("Number " + num + " is negative.");
} else {
    console.log("Number " + num + " is zero.");
}

// Lab 5
let day = prompt("Enter a day of the week:")

switch(day) {
    case "Monday":
        console.log("Start of the week.");
        break;
    case "Wednesday":
        console.log("Middle of the week.");
        break;
    case "Friday":
        console.log("Weekend is near.");
        break;
    case "Sunday":
        console.log("Rest day!");
        break;
    default:
        console.log("Regular day.")
}

// Lab 6
let n = 2;
let result = (n % 2 == 0) ? "even" : "odd";

console.log("Number is", result);