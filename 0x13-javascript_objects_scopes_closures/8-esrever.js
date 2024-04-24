#!/usr/bin/node

/**
 * Reverses the order of elements in a given list.
 * @param {Array} list - The list to be reversed.
 * @returns {Array} - The reversed list.
 */
exports.esrever = function (list) {
  const reverseList = [];
  let i = list.length - 1;
  while (i >= 0) {
    reverseList.push(list[i]);
    i--;
  }
  return (reverseList);
};
