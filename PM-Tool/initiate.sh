#!/bin/bash

# Set up initial server and database connections for main-system
cd main-system
touch server.js
echo "const express = require('express');" >> server.js
echo "const mongoose = require('mongoose');" >> server.js
echo "require('dotenv').config();" >> server.js

# Identify necessary utility functions and middleware for sub-system
cd ../sub-system
touch utils.js
echo "// Utility functions go here" >> utils.js
touch middleware.js
echo "// Middleware functions go here" >> middleware.js
