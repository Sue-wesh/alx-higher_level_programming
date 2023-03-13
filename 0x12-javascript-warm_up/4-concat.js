#!/usr/bin/node
console.log(typeof process.argv[2] === 'undefined' ? 'undefined is undefined' : process.argv[3] === 'undefined' ? process.argv[2] + ' is undefined ' :  process.argv[2] + ' is ' + process.argv[3])
