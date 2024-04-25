#!/usr/bin/node

// t imports a dictionary of occurrences by user id and computes a dictionary of user ids by
// occurrence

const dict = require('./101-data').dict;

const newUserDict = {};
for (const userId in dict) {
  const occurances = dict[userId];
  if (!newUserDict[occurances]) {
    newUserDict[occurances] = [];
  }
  newUserDict[occurances].push(userId);
}
console.log(newUserDict);
