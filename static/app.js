const apiUrl = 'http://127.0.0.1:5000';

function showRegister() {
    document.getElementById('auth').style.display = 'none';
    document.getElementById('register').style.display = 'block';
}

function showLogin() {
    document.getElementById('register').style.display = 'none';
    document.getElementById('auth').style.display = 'block';
}

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch(`${apiUrl}/auth/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.token) {
            localStorage.setItem('token', data.token);
            document.getElementById('auth').style.display = 'none';
            document.getElementById('tasks').style.display = 'block';
            getTasks();
        } else {
            alert('Login failed!');
        }
    });
}

function register() {
    const username = document.getElementById('reg_username').value;
    const password = document.getElementById('reg_password').value;

    fetch(`${apiUrl}/auth/register`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        showLogin();
    });
}

function getTasks() {
    fetch(`${apiUrl}/tasks`, {
        headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
    })
    .then(response => response.json())
    .then(tasks => {
        const taskList = document.getElementById('task-list');
        taskList.innerHTML = '';
        tasks.forEach(task => {
            const taskItem = document.createElement('div');
            taskItem.innerHTML = `<strong>${task.title}</strong>: ${task.description}`;
            taskList.appendChild(taskItem);
        });
    });
}

function createTask() {
    const title = document.getElementById('task_title').value;
    const description = document.getElementById('task_description').value;

    fetch(`${apiUrl}/tasks`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
        },
        body: JSON.stringify({ title, description })
    })
    .then(response => response.json())
    .then(task => {
        getTasks();
    });
}

function logout() {
    localStorage.removeItem('token');
    document.getElementById('tasks').style.display = 'none';
    document.getElementById('auth').style.display = 'block';
}
