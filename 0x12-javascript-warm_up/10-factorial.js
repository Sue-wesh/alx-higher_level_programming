#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
	console.log(1);
}
else {
  function factorial (num) {
    while (num > 0) {
      return num * factorial(num - 1);
    }
  }
}
