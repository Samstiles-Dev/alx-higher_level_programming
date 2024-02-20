#!/usr/bin/node
// Js Script that takes a url, makes a get request
// and prints the status

const args = process.argv;

const request = require('request');

request(args[2], function (error, response, body) {
  if (error) console.error(error);
  console.log('code:', response.statusCode);
});
