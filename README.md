# Anaconda Coding Challenge

## __Anaconda Rock Paper Scissor__

## Prerequisites 

## System Dependencies

- Make sure your system is up-to-date.

# Host

## System Dependencies

- Run the below command to install python system dependencies as well as Poetry installed.

```bash
$ sudo apt-get install libffi-dev
$ sudo apt-get install libpq-dev python-dev libssl-dev
```

- Install NodeJS and NPM as system dependencies

NPM version: 8.11.0

NodeJS: v16.16.0

With [NVM](https://npm.github.io/installation-setup-docs/installing/using-a-node-version-manager.html) the following command can be executed to install it 
```bash
$ nvm install v16.16.0
```

## Python Dependencies

- Installing Python Packages

```bash
$ poetry shell
$ poetry install
```

- Locally running Uvicorn Server

```bash
$ uvicorn main:app --reload
```

Backend runs at [http://localhost:8000](http://localhost:8000)

Documentation is provided at [http://localhost:8000/docs](http://localhost:8000/docs)

## VueJS dependencies

Enter the **frontend** directory

```bash
$ cd frontend
```

```bash
$ npm install
```

```bash
$ npm run dev
```

Frontend runs at [http://localhost:5173](http://localhost:5173)

## Python Type Checking

```bash
poetry run python3 -m mypy .
```
