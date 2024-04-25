#!/usr/bin/node
// Define and export a function named callMeMoby
// This function takes two parameters:
// -x: The number of times to execute theFunction.
// - theFunction: The function to be executed x times.

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
