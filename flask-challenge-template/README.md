# Volleyball Flask Challenge
The goal of this exercise is to assess candidates' backend development skills using Flask and Flask extensions.

There are multiple correct ways to implement a solution for this challenge. Done is better than perfect.

## Prerequisites
- Python 3.8+
- pip / virtualenv / poetry (your choice)
- PostgreSQL or SQLite (for local development)
- Flask 2.x+
- Flask RESTful or Flask API
- SQLAlchemy (for ORM)


## Project Setup
Clone the project
```
git clone git@github.com
```

Install the dependencies
```
pip install -r requirements.txt
```

Apply the migrations(make sure the database exists)
```
flask db upgrade
```

Run the development server
```
flask run
``` 

Check the project running on localhost: 
[http://localhost:8080/](http://localhost:8080/)

#### Please set up your working environment before the interview (working server), so we don't spend time installing anything.

## Project Description
You’ve been hired to help the Volleyball Federation build a basic backend system to manage online ticket sales for the upcoming season.

The system should expose REST APIs to perform the following tasks:
- User signup and login
- Adding new stadiums
- Defining matches
- Defining seat arrangements for each match

To test the API, you can use Postman or cURL for making requests to the endpoints. 

## Requirements
**What we're expecting:**

- Flask project with modular, well-structured apps
- Code is clean, readable, and well-documented
- Unit tests covering business logic

**What we're NOT expecting:**
- Mobile responsive solution
- A frontend UI

## Stack
* Python 3.8+
* Flask 2.x+
* Flask RESTful or Flask API
* SQLAlchemy ORM
* PostgreSQL or SQLite
* Flask-Login (for user authentication)
* Flask-WTF (for forms and CSRF protection)
Use any other packages that help speed up your development or improve code quality.

## Submission
Please clone the repository and create a private repository on your own account. Then, create a new branch and submit a Pull Request with your proposed solution. Make sure to add and request review on the PR.

## Evaluation Criteria
We'll be looking at the following criteria when assessing candidate submissions:
- Project architecture
- Code simplicity and clarity
- Git history, including comments in the PR

**Good luck!**
