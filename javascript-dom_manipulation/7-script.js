#!/usr/bin/node
starWarsMovies();

async function starWarsMovies () {
  const urlFetch = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
  const urlJson = await urlFetch.json();

  const titles = document.querySelector('#list_movies');
  const results = urlJson.results;
  for (let i = 0; i < results.length; i++) {
    const title = document.createElement('li');
    title.appendChild(document.createTextNode(results[i].title));
    titles.appendChild(title);
  }
}
