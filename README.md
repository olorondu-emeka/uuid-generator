# uuid-generator

A simple uuid generator list

## Brief Description

Generates a key-value pair containing a timestamp as the key and a uuid as the value.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for testing purposes.

### Prerequisites

System requirements for this project to work includes:

- Python/Python3
- Docker

### Installation

To install the dependencies, create and run a virtual environment with the following commands:

```bash
pip install virtualenv
virtualenv myenv
source myenv/Scripts/activate
```

Once this has been done, install the redis-client dependency with the following command:

```bash
pip install redis
```

### Running the project

To run the project on your local machine, navigate to the project directory and run the following command

```bash
docker-compose up -d
python index.py
```

The first command spins up a docker container running redis using the `docker-compose.yml` file, while the second commmand runs the `index.py` file.

You could also interact with the **redis-cli** using the following command:

```bash
docker exec -it uuid-generator_redis_1 redis-cli
```

This starts the **redis-cli** on your local machine.

### API Request

This project has only a single route, which is a **GET** request that can be accessed on:

```bash
http://localhost:5000/
```

## Built With

- [Python](https://python.org/)
- [Redis](https://redis.io/)
