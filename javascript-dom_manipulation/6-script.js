#!/usr/bin/node
starWarsCharacter();

async function starWarsCharacter () {
  const urlFetch = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
  const urlJson = await urlFetch.json();
  const character = document.querySelector('#character');
  character.textContent = urlJson.name;
}
