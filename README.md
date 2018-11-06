# BugSlayer API

The web service powering our services.

## Usage

Make sure you have Python 3.6+ installed, then create a new [virtual environment](https://virtualenv.pypa.io/en/latest/).

Once the virtual environment for the project has been created simply:

1. Clone the repository
2. Run `$ pip install -r requirements.txt`
3. Run the migrations with `$ python manage.py migrate`
4. Create a super user account with `$ python manage.py createsuperuser`
5. Start the development server with `$ python manage.py runserver`
6. That's it, enjoy!
