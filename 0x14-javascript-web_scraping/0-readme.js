#!/usr/bin/node
// Js Script that reads & writes into a file

const args = process.argv;
const fs = require('fs');

fs.readFile(args[2], 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data.toString());
});
