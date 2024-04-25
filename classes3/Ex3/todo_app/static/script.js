// static/script.js

document.addEventListener('DOMContentLoaded', function() {
    const taskForm = document.getElementById('task-form');
    const taskInput = document.getElementById('task-input');
    const taskList = document.getElementById('task-list');

    taskForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const taskContent = taskInput.value.trim();
        if (taskContent !== '') {
            addTask(taskContent);
            taskInput.value = '';
        }
    });

    taskList.addEventListener('click', function(event) {
        const target = event.target;
        if (target.classList.contains('delete-btn')) {
            deleteTask(target.parentElement);
        } else if (target.classList.contains('edit-btn')) {
            editTask(target.parentElement);
        }
    });

    function addTask(content) {
        const newTask = document.createElement('li');
        newTask.innerHTML = `
            <span>${content}</span>
            <button class="edit-btn">Edit</button>
            <button class="delete-btn">Delete</button>
        `;
        taskList.appendChild(newTask);
    }

    function deleteTask(taskElement) {
        taskElement.remove();
    }

    function editTask(taskElement) {
        const contentSpan = taskElement.querySelector('span');
        const newContent = prompt('Enter new task content:', contentSpan.textContent);
        if (newContent !== null && newContent.trim() !== '') {
            contentSpan.textContent = newContent.trim();
        }
    }
});
