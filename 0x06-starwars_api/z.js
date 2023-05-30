#!/usr/bin/node

const request = require('request');

// const url = 'https://swapi-api.alx-tools.com/api/starships/9/';

const filmID = process.argv[2];
if (!filmID) {
  // filmID is undefined
  console.log('Usage: <cmd> <film-id>');
  process.exit(1);
}

const url2 = `https://swapi-api.alx-tools.com/api/films/${filmID}/`;

const prom = new Promise(function (resolve, reject) {
  request(url2, { json: true }, function (err, res, bdy) {
    if (res.statusCode !== 200) {
      console.log(res.statusCode);
      reject(err);
    } else {
      resolve(bdy);
    }
  });
});

async function f () {
  const bdy = await prom;
  console.log(bdy);
}

f();
	
