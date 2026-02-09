const username = prompt("Enter username:");
const password = prompt("Enter password:");

if (username === "admin" && password === "1234") {
  console.log("Login successful");
} else {
  console.log("Invalid username or password");
}