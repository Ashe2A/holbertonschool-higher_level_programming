#!/usr/bin/node
const addItem = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');

addItem.addEventListener('click', () => {
  const item = document.createElement('li');
  item.appendChild(document.createTextNode('Item'));
  myList.appendChild(item);
});
