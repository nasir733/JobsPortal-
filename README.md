# Secure Job Portal

A Django web application with functionalities for user authentication, email verification, job scraping, and custom middleware for saving user information.

## Features
- User registration and login
- Email verification for newly registered users
- Job scraping from the website WeWorkRemotely
- Dashboard page to view scraped jobs
- Custom middleware for saving user IP address and device type

## Requirements
- Django 3.2 or higher
- Python 3.8 or higher
- requests library

## Installation
1. Clone the repository
```bash
git clone https://github.com/nasir733/[SecureJobsPortal].git
```
2. Change into the project directory
```bash
cd [repository]
```
3. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```
4. Install the required packages
```bash
pip install -r requirements.txt
```
5. Apply migrations
```bash
python manage.py migrate
```
6. Collect static files
```bash
python manage.py collectstatic
```
7. Run the development server
```bash
python manage.py runserver
```

## Usage
 1. Register a new user or login with an existing account
 1. Verify your email address through the link sent to your email
 2. In development you can see the sent email in the terminal through which you ran ``` bash python manage.py runserver ```
1. Access the dashboard page to view scraped jobs
2. Logout when finished

## Custom Middleware
The custom middleware is located in the middleware.py file in the config directory. It is responsible for saving the user's IP address and device type to the database upon successful login or registration. This information can be accessed and used as needed by the rest of the application.

## License
This project is licensed under the MIT License.

## Acknowledgements
 - WeWorkRemotely for providing the job scraping data.

## Contact 
For any queries or issues please raise an issue on GitHub.


