# Twitter-API

Twitter-API is an API server written in FastAPI, which is a modern, fast (high-performance), web framework for building APIs with Python.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements of this project.

```bash
pip install -r requirements.txt
```

## Usage

To run the application, you need to tell your terminal the application to work with by exporting the environment variables that connects the application to your database.
By default the application sets username as root, password as password, host as localhost, port as 3306 and "twitter" as the database's name.
You can modify it by sets those environment variables. 
For instance, using Powershell it would look like this:
` $env:USERNAME = "your username" `
` $env:PASSWORD = "your password" `
` $env:HOST = "your host machine" `
` $env:PORT = "port number" `
` $env:DB_NAME = "your database name" `

Afterwards you can run the application:

` python main.py `

This command will start the web server on your localhost on port 8000 by default.
