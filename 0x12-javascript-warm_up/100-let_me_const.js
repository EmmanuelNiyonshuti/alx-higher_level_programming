#!/usr/bin/node

//initializing a variable without it's declaration first, it results in making that variable global automatically.
//The reason behind this behavior is, initialization without declaration is the same as initializing 
//the variable into the window object like this window.myVal = 10.

myVar = 333;

module.exports = myVar;