# Encrypt File PDF

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black) [![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE.txt)

API for encrypt file PDF.

<img src="https://github.com/20Scoops-CNX/encrypt-pdf-python/blob/master/arts/image-1.png?raw=true" width="100%">


# Install

Make sure your uesed python3 and clone this repository

- Manual
    ```js
    1. cd src
    2. pip install -r requirements.txt
    3. python app.py
    ```
- Docker Compose
    ```js
    docker-compose up -d --build
    ```

# Code Style 
This project we used Black
```
pip install black
```

# API

Endpoint: `/encrypt-pdf`

Method: `POST`

| Parameter  | Description| 
| :---         |     :---     |
| file   | File for encrypt (.pdf only) | 
| password | your key for encrypt file |