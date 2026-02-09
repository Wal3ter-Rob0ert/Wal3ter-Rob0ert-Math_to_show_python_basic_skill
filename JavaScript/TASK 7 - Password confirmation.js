let password = "";

while (password.length < 8) {
  password = prompt("Enter a password (at least 8 characters):");

  if (password.length < 8) {
    console.log("Password too short, try again");
  }
}

console.log("Password accepted");