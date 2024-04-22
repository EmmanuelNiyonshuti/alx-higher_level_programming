#!/usr/bin/node

const c = 'C is fun';
const arg = process.argv[2];
if (isNaN(arg)) { console.log('Missing number of occurances'); } for (let i = 0; i < arg; i++) { console.log(c); }
