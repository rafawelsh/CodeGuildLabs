const addButton = document.querySelector('.addButton');
const todoInput = document.querySelector('.todoInput');
const todoConsole = document. querySelector('.todoConsole');

class item {
    constructor(itemName){
        this.createDiv(itemName);
    }

    createDiv(itemName){
        // adding the input type
        let input = document.createElement('input');
        input.value = itemName;
        input.disabled = true;
        input.classList.add('item_input');
        input.type = 'text';

        // adding the sections that will expand when adding new items
        let itemBox = document.createElement('div');
        itemBox.classList.add('item');

        let editButton = document.createElement('a');
        editButton.innerHTML = '<i class="fas fa-pencil-alt"></i>'
        editButton.classList.add('editButton');

        let removeButton = document.createElement('a');
        removeButton.innerHTML = '<i class="fas fa-trash-alt"></i>'
        removeButton.classList.add('removeButton')

        // this code actually makes the items show up for each new div
        todoConsole.appendChild(itemBox);

        itemBox.appendChild(input);
        itemBox.appendChild(editButton);
        itemBox.appendChild(removeButton);

        // this code is listening on the page for the click to fire the function
        editButton.addEventListener('click', () => this.edit(input));

        removeButton.addEventListener('click', () => this.remove(itemBox));

    }

    // these are teh function form above that are fired
    edit(input){
        input.disabled = !input.disabled;
    }

    remove(item){
        todoConsole.removeChild(item);
    }
}

// these are lines that pertain to the submit button
function check(){
    if(todoInput.value != ""){
        new item(todoInput.value);
        todoInput.value = "";
    }
}

addButton.addEventListener('click', check);
window.addEventListener('keydown', (e) => {
    if(e.which == 13){
        check();
    }
})
