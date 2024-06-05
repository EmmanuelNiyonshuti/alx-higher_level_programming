#!/usr/bin/node
// - computes the number of tasks completed by user id.
// - use the module request

const r = require('request');

const url = process.argv[2];

r(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const tasks = JSON.parse(body);
  const completedTask = {};
  for (let i = 0; i < tasks.length; i++) {
    const task = tasks[i];
    if (task.completed === true) {
      if (!Object.prototype.hasOwnProperty.call(completedTask, task.userId)) {
        completedTask[task.userId] = 0;
      }
      completedTask[task.userId]++;
    }
  }
  console.log(completedTask);
});
