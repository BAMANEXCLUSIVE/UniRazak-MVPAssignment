#!/bin/bash

# Create a new directory for your project
mkdir PM-Tool
cd PM-Tool

# Initialize a new Node.js project
npm init -y

# Install Express
npm install express

# Create a basic server file
touch index.js

# Create main-system and sub-system directories
mkdir main-system
mkdir sub-system

# Install additional frameworks
npm install react vue @nestjs/core koa

# Install additional dependencies
npm install mongoose dotenv axios winston jsonwebtoken
