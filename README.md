---
date: 2024-04-15T13:21:18.339437
author: AutoGPT <info@agpt.co>
---

# Password Strength Checker API

Based on the user's requirements and the information gathered, the task involves creating an endpoint in a FastAPI application that performs comprehensive password strength analysis. The analysis will consider various factors including the password's length, complexity (incorporating uppercase and lowercase letters, numbers, and special characters), and adherence to recommended security practices (such as avoiding sequential or repeated characters). Additionally, the endpoint will check the password against known data breaches and common passwords lists to further ensure its robustness. 

The endpoint will return a score indicating the password's strength (categorized as weak, medium, or strong) and provide actionable suggestions for improving password security if necessary. To implement this, the tech stack will include Python for programming, FastAPI as the API framework, PostgreSQL for database needs (if storing analysis results or user data is required), and Prisma as the ORM for efficient database interactions. 

The implementation strategy will leverage the `passlib` library for hashing and validating password strength, and the `pydantic` library for data validation within FastAPI. Additionally, integration with APIs that offer data breach checks and common password lists will be necessary to enhance the analysis. 

A sample implementation approach for the FastAPI endpoint was previously provided, focusing on basic criteria like password length. The solution will expand on this by integrating complexity checks and the comparison with data breach and common password lists to offer a more sophisticated password strength validation system.

## What you'll need to run this
* An unzipper (usually shipped with your OS)
* A text editor
* A terminal
* Docker
  > Docker is only needed to run a Postgres database. If you want to connect to your own
  > Postgres instance, you may not have to follow the steps below to the letter.


## How to run 'Password Strength Checker API'

1. Unpack the ZIP file containing this package

2. Adjust the values in `.env` as you see fit.

3. Open a terminal in the folder containing this README and run the following commands:

    1. `poetry install` - install dependencies for the app

    2. `docker-compose up -d` - start the postgres database

    3. `prisma generate` - generate the database client for the app

    4. `prisma db push` - set up the database schema, creating the necessary tables etc.

4. Run `uvicorn project.server:app --reload` to start the app

## How to deploy on your own GCP account
1. Set up a GCP account
2. Create secrets: GCP_EMAIL (service account email), GCP_CREDENTIALS (service account key), GCP_PROJECT, GCP_APPLICATION (app name)
3. Ensure service account has following permissions: 
    Cloud Build Editor
    Cloud Build Service Account
    Cloud Run Developer
    Service Account User
    Service Usage Consumer
    Storage Object Viewer
4. Remove on: workflow, uncomment on: push (lines 2-6)
5. Push to master branch to trigger workflow
