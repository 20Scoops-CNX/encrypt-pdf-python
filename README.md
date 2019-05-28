# Encrypt File PDF

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

API for encrypt file PDF.

![](./arts/image-1.png)


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


# API

Endpoint: `/encrypt-pdf`

Method: `POST`

| Parameter  | Description| 
| :---         |     :---     |
| file   | File for encrypt (.pdf only) | 
| password | your key for encrypt file |