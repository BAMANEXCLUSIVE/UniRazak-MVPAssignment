require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');

const app = express();
const PORT = process.env.PORT || 4000;

app.get('/', (req, res) => {
    res.send('Welcome to the Main System!');
});

app.listen(PORT, () => console.log(`Main system running on port ${PORT}`));