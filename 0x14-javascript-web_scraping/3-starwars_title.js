#!/usr/bin/node
// Js Script dat prints star wars movie title
// if id arg is passed

const _id = process.argv[2];
const request = require('request');
const _url = `https://swapi-api.alx-tools.com/api/films/${_id}`;
request(_url, (error, reponse, body) => {
  if (error) console.log(error);
  const movie = JSON.parse(body);
  console.log(movie.title);
});
