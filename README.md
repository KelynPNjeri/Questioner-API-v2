[![Build Status](https://travis-ci.com/KelynPNjeri/Questioner-API-v2.svg?branch=develop)](https://travis-ci.com/KelynPNjeri/Questioner-API-v2)       [![Maintainability](https://api.codeclimate.com/v1/badges/16c431ceeaa710544007/maintainability)](https://codeclimate.com/github/KelynPNjeri/Questioner-API-v2/maintainability)        [![Coverage Status](https://coveralls.io/repos/github/KelynPNjeri/Questioner-API-v2/badge.svg?branch=develop)](https://coveralls.io/github/KelynPNjeri/Questioner-API-v2?branch=develop)      [![BCH compliance](https://bettercodehub.com/edge/badge/KelynPNjeri/Questioner-API-v2?branch=develop)](https://bettercodehub.com/)      [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
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
