#!/usr/bin/node
const header = document.querySelector('header');
const toggleHeader = document.querySelector('#toggle_header');

toggleHeader.addEventListener('click', () => {
  if (header.classList.contains('green')) {
    header.classList.add('red');
    header.classList.remove('green');
  } else {
    header.classList.add('green');
    header.classList.remove('red');
  }
});
