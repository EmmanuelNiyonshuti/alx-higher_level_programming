#!/usr/bin/node
// Increments and calls a function
// This function takes in two parameters.
// - number: the number to be incremented.
// - theFunction: The function to execute.

exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
