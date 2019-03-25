[![BCH compliance](https://bettercodehub.com/edge/badge/KelynPNjeri/Questioner-API-v2?branch=develop)](https://bettercodehub.com/)      [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# Questioner API(Version 2)
Questioner web app, is an online platform that crowd-sources questions from users about meetups.

## API ENDPOINTS
- This is the Version 2 API of the Questioner Web App REST API. It saves all the entered data to a database.
#### Questions Endpoint.
| API Endpoint  | Description | Methods |
| ------------- | ------------- | ------------- |
| /api/v2/questions  | Create a question for a specific meetup  | POST  |
| /api/v2/questions  | Get all questions for a specific meetup  | GET  |
| /api/v2/questions/<question id> | Get a specific question  | GET  |
| /api/v2/questions/<question-id>/upvote  | Upvote a specific question.  | PATCH  |
|/api/v2/questions/<question-id>/downvote  | Downvote a specific question. | PATCH |

#### Comments Endpoint.
| API Endpoint  | Description | Methods |
| ------------- | ------------- | ------------- |
| /api/v2/comments  | Add a comment to a question.  | POST  |
| /api/v2/comments  | Retrieve all comments for a question.  | GET  |

#### Authentication Endpoint.
| API Endpoint  | Description | Methods |
| ------------- | ------------- | ------------- |
| /api/v2/auth/register  | Register a new user on Questioner  | POST  |
| /api/v2/auth/login  | Login a user on Questioner  | GET  |

#### Meetups Endpoint
| API Endpoint  | Description | Methods |
| ------------- | ------------- | ------------- |
| /api/v2/meetups  | Get all meetups  | GET  |
| /api/v2/meetups  | Create a meetup  | POST  |
| /api/v2/meetups/<meetup-id>  | Delete a meetup  | DELETE  |
|/api/v2/meetups/<meetup-id> | Get a specific meetup record  | GET  |
|/api/v2/meetups/<meetup-id>/rsvps  | Respond to meetup RSVP  | POST  |

## Getting Started
To get started:
1. Git clone the repository using `https://github.com/KelynPNjeri/Questioner-API-v2.git`

### Prerequisites
For the API to run smoothly tou will need the following:
```
1. Python 3.6 or higher installed.
2. Pip3
3. Virtualenv
```
### Installing
> __Installation Guide.__

1. Git clone the repository using `https://github.com/KelynPNjeri/Questioner-API-v2.git`.
2. Through your terminal, navigate to the location with the cloned repository.
3. Open the cloned repo folder using your terminal.
4. You're currently on the `develop` branch.
5. Set up a virtual environment:
    > Using virtualenv: `virtualenv -p python3 env`
6. To activate the virtual environment:
    > Using virtualenv: `source env/bin/activate`
7. Install the packages:
    > Using virtualenv: `pip3 install -r requirements.txt`
8. There is already a `.env` file containing all the necessary environment variables.
9. Export all the environment variables by running `source .env`.
11. Create two databases named:
    1. questioner.
    2. test_questioner.
12. To launch your app now, use `python run.py`.
13. On Postman or Insomnia, first register a user so a to be able to access all the endpoints since some of them are secured.
14. Login the registered user.
13. Test the other endpoints on Postman or on Insomnia.

## Running the tests
To view all the unit tests, from your root directory of the project (Inside cloned repository folder), run `pytest --cov=app`

### Style Guide.
PEP 8

## Deployment
[Heroku](https://questioner-kelyn.herokuapp.com/) - Questioner Web API deployment.

## Built With
* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used,
* [Postgresql](https://www.postgresql.org/) - The Database used.
* [Flask Restplus](https://flask-restplus.readthedocs.io/en/stable/) - The web framework used.

## Authors
* **Kelyn Paul Njeri.** 

## Acknowledgments
* Andela Kenya.
* Andela Developer Challenge.
