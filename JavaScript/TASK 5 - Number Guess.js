const secretNumber = 7;
let guess = null;

while (guess !== secretNumber) {
  guess = Number(prompt("Guess the number:"));

  if (guess !== secretNumber) {
    console.log("Wrong number, try again");
  }
}

console.log("Correct!");