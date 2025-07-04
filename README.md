# Django Expense Tracker API

A RESTful API for tracking expenses and income with user authentication and tax calculation features.

## Features

- **JWT Authentication**: Secure user registration/login with token-based auth
- **Expense/Income Tracking**: Record all financial transactions
- **Automatic Tax Calculation**: Supports both flat and percentage taxes
- **User Isolation**: Users only see their own records
- **Admin Access**: Superusers can view all records
- **Financial Summary**: Get totals for expenses, income, and net balance
- **Pagination**: Efficient handling of large datasets
- **Swagger Documentation**: Interactive API documentation

## Requirements

- Python 3.12.0+
- pip package manager
- Django REST Framework
- djangorestframework-simplejwt

## Installation

Follow these steps to set up the project:

```bash
# 1. Clone the repository
git clone https://github.com/Dhaniswar/expense_tracker_api.git
cd expense_tracker_api

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
echo "SECRET_KEY=your_django_secret_key" > .env
echo "DEBUG=True" >> .env
echo "EMAIL_HOST_USER=your_sendgrid_email" >> .env
echo "EMAIL_HOST_PASSWORD=your_sendgrid_api_key" >> .env

# 5. Apply database migrations
python manage.py migrate

# 6. Create superuser for admin access
python manage.py createsuperuser

# 7. Run development server
python manage.py runserver

# 6. You can access swagger UI on this url

http://127.0.0.1/api/docs/
