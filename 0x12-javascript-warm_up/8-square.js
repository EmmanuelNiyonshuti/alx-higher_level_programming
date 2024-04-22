#!/usr/bin/node

const square = 'X';
const arg = process.argv[2];
if (isNaN(arg)) { console.log('Missing Size'); } for (let i = 0; i < arg; i++) { console.log(square.repeat(arg)); }
