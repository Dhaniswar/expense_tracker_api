# expense_tracker_api
This is the expense tracker api


# Django Expense Tracker API

A RESTful API for tracking expenses and income with user authentication and tax calculation features.

## Features

- User registration and login with JWT authentication
- CRUD operations for expense/income records
- Automatic tax calculation (flat or percentage)
- Data isolation between regular users
- Superuser access to all records
- Paginated API responses

## Tech Stack
- **Documentation**: Swagger/OpenAPI

## Requirements

- Python 3.12.0
- pip package manager
- Django REST Framework
- djangorestframework-simplejwt

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Dhaniswar/expense_tracker_api.git

cd expense_tracker_api

2. Create and Activate virtual environment

3. Configure env variables like sendgrid default email and api key

4. Run requiremnts.txt file:

- pip install -r requiremtns.txt

5. Run Django server 

6. You will be access swagger UI on this uel

http://127.0.0.1/api/docs/
