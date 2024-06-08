# PostgreSQL Docker Initialization

## Project Description

This project demonstrates how to set up a PostgreSQL database using Docker. It includes the creation of a new schema and table, and the loading of data from a CSV file into the Dockerized PostgreSQL instance. The Python script included connects to the database and executes a query to count the number of records in the specified table.

## Project Structure

- `postgres_docker_init/`
  - `data/`: Contains the CSV file to be loaded into the PostgreSQL table.
  - `infra_setup/`: Contains the SQL script to create the schema, table, and load data.
  - `docker-compose.yml`: Docker Compose file to configure and run the PostgreSQL service.
- `src/`: Contains Python scripts for interacting with the PostgreSQL database.

## Setup Instructions

### Prerequisites

- Docker and Docker Compose installed on your machine
- Python 3 installed

### Steps

1. **Clone the repository and create a new branch:**

   ```sh
   git clone git@github.com:Victor-Akinode/projects-assessments.git #for SSH and 
   https://github.com/Victor-Akinode/projects-assessments.git #for HTTPS
   cd projects-assessments
   git checkout -b assignment
