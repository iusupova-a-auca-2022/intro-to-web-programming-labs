// Lab 1
for (let i = 1; i <= 10; i++) {
    console.log(i);
}

// Lab 2
let num = 10;

while (num != 0) {
    console.log(num);
    num--;
}

// Lab 3
let userInput;

do {
    userInput = prompt("Enter a number greater than 10:");
} while(userInput <= 10);

console.log("Valid input:", userInput);

// Lab 4
let fruits = ["apple", "pear", "banana", "orange", "kiwi"];

for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

// Lab 5
let i = 0;

while (i < fruits.length) {
    console.log(fruits[i]);
    i++;
}

// Lab 6
let numbers = [3, 7, 12, 5, 9];

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] == 12) {
        console.log("Number 12 is found.");
        break;
    }

    console.log(numbers[i]);
}

// Lab 7
let numbersA = [1, 2, 3, 4, 5, 6, 7];

for (let i = 0; i < numbersA.length; i++) {
    if (numbersA[i] == 5) {
        continue;
    }

    console.log(numbersA[i]);
}