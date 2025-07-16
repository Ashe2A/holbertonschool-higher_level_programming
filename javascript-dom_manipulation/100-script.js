#!/usr/bin/node
document.addEventListener('DOMContentLoaded', async () => {
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');
  const elements = document.querySelector('.my_list');

  addItem.addEventListener('click', () => {
    const element = document.createElement('li');
    element.appendChild(document.createTextNode('Item'));
    elements.appendChild(element);
  });

  removeItem.addEventListener('click', () => {
    elements.removeChild(elements.lastChild);
  });

  clearList.addEventListener('click', () => {
    elements.textContent = '';
  });
});
