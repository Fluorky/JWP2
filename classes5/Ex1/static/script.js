// static/script.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('add-task-form');
    const taskInput = document.getElementById('task-input');
    const taskList = document.getElementById('task-list');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const description = taskInput.value;
        if (description.trim() !== '') {
            addTask(description);
            taskInput.value = '';
        }
    });

    taskList.addEventListener('click', function(event) {
        if (event.target.classList.contains('delete-task')) {
            const taskItem = event.target.parentElement;
            const taskId = taskItem.dataset.id;
            deleteTask(taskId, taskItem);
        }
        if (event.target.classList.contains('edit-task')) {
            const taskItem = event.target.parentElement;
            const taskId = taskItem.dataset.id;
            editTask(taskId, taskItem);
        }
    });

    function addTask(description) {
        fetch('/add_task', {
            method: 'POST',
            body: JSON.stringify({ description: description }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            const taskItem = createTaskItem(data.id, description);
            taskList.appendChild(taskItem);
        });
    }

    function deleteTask(id, taskItem) {
        fetch(`/delete_task/${id}`, {
            method: 'DELETE'
        })
        .then(response => {
            if (response.ok) {
                taskItem.remove();
            }
        });
    }

    function editTask(id, taskItem) {
        const description = prompt('Enter new description:');
        if (description !== null) {
            fetch(`/edit_task/${id}`, {
                method: 'PUT',
                body: JSON.stringify({ description: description }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                if (response.ok) {
                    taskItem.querySelector('span').textContent = description;
                }
            });
        }
    }

    function createTaskItem(id, description) {
        const li = document.createElement('li');
        li.dataset.id = id;
        li.innerHTML = `
            <span>${description}</span>
            <button class="edit-task">Edit</button>
            <button class="delete-task">Delete</button>
        `;
        return li;
    }
});
