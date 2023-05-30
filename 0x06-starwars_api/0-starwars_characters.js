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

function then1Clbk (bdy) {
  // return the characters list from the json response body
  return bdy.characters;
}

function then2Clbk (urlsList) {
  // return a list of promises whose fulfillment to retrieve in order
  const namePromises = [];
  let namePromise;
  for (const url of urlsList) {
    // create a Promise for each url; to be resolved by Promise.all()
    namePromise = new Promise(function (resolve, reject) {
      request(url, { json: true }, function (err, res, bdy) {
        if (res.statusCode !== 200) {
          console.log(res.statusCode);
          reject(err);
        } else {
          resolve(bdy.name);
        }
      });
    });
    namePromises.push(namePromise);
  }
  return namePromises;
}

function then3Clbk (promises) {
  // return a list of results/names representing the fulfilment of the promises in order
  return Promise.all(promises);
}

function then4Clbk (namesList) {
  // print the names, in order of their URLs
  for (const name of namesList) {
    console.log(name);
  }
}

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

prom
  .then(then1Clbk)
  .then(then2Clbk)
  .then(then3Clbk)
  .then(then4Clbk)
  .catch(function (err) {
    console.log(err);
  });
