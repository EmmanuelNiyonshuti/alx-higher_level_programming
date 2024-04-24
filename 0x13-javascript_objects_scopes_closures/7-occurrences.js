#!/usr/bin/node

// Define a function named nbOccurences that takes two parameters:
// - list: an array in which to search for occurrences of searchElement
// - searchElement: the element to search for within the list

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let count = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      count += 1;
    }
    i++;
  }
  return count;
};
