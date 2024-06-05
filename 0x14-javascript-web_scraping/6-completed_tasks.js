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
    const completedTasksByUserId = {};

    tasks.forEach(task => {
        if (task.completed === true) {
            if (completedTasksByUserId.hasOwnProperty(task.userId)) {
                completedTasksByUserId[task.userId]++;
            } else {
                completedTasksByUserId[task.userId] = 1;
            }
        }
    });
    console.log(completedTasksByUserId);
});