// src/app.js

const express = require('express');

const employee = require('./controllers/employee.controler');

const app = express();

app.use(express.json());

app.get('/employees', employee.getAll);

module.exports = app;