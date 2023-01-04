#Transactions API
This is a Django-based REST API for managing transactions and users. It includes the following features:

List of known users (friends)
Creating, updating, and deleting transactions
Associating transactions with sets of users to split them across
Spending categories for transactions
Django's built-in authentication system to authenticate users
Django's built-in ORM to store data in an SQLite database

##Installation
To install and set up the API, follow these steps:

Clone the repository and navigate to the root directory:

git clone https://github.com/YOUR_USERNAME/transactions-api.git
cd transactions-api

##Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate

##Install the required dependencies:
pip install -r requirements.txt

##Migrate the database:
python manage.py migrate

##Create a superuser account:
python manage.py createsuperuser

##Start the development server:
python manage.py runserver
The API will be available at http://localhost:8000/.

#Endpoints

The following API endpoints are available:

/users/: List of known users
/transactions/: List of transactions
You can use HTTP methods such as GET, POST, PUT, and DELETE to perform actions on these endpoints.

#Authentication

The API uses Django's built-in authentication system to authenticate users. To make authenticated requests, you will need to include a Authorization: Token YOUR_TOKEN header in your request, where YOUR_TOKEN is the token for the user you want to authenticate as. You can obtain a user's token by sending a POST request to the /api-token-auth/ endpoint with the user's username and password.

