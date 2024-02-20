#!/usr/bin/node

const argv = require('process').argv;
const request = require('request');

const _url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

function makeRequests (urls) {
  const _url = urls.shift();
  request(_url, (error, response, body) => {
    if (urls.length) {
      makeRequests(urls);
    }
    if (error) {
      console.log(error);
    }

    console.log(JSON.parse(body).name);
  });
}

request(_url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const characters = JSON.parse(body).characters;

  makeRequests(characters);
});
