const express = require('express');
const mongoose = require('mongoose');
require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
require('dotenv').config();
const app = express();
mongoose.connect(process.env.DB_URI);
app.use('/', require('./routes'));
const app = express();
mongoose.connect(process.env.DB_URI);
app.use('/', require('./routes'));
const app = express();
mongoose.connect(process.env.DB_URI);
app.use('/', require('./routes'));
// Finalize server setup
// Finalize server setup
