#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
  console.log('Missing number of occurences');
} else {
  for (let x = 0; x < num; x++) {
    console.log('C is fun');
  }
}
