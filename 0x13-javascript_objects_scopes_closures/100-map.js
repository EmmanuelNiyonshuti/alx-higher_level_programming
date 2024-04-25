#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);
//Multiplies each number in a list with it's index using map function.
const newList = list.map((x, i) => x * i);
console.log(newList);