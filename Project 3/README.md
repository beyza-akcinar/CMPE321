# About the project
This is an application about a movie database system in which different types of users interact.

## Prerequisites

- Python 3.x
- Django Framework 3.x
- MySQL
- Other dependencies listed in `requirements.txt`


## Setup

1. Download the code and navigate to the project directory.

2. Create and activate a virtual environment by these commands.

python3 -m venv venv
source venv/bin/activate

3. Install required dependencies:

pip3 install -r requirements.txt

4. Create a MySQL database and configure the database settings in 'settings.py'. Then run the following commands:

python3 manage.py makemigrations
python3 manage.py migrate

5. Start the development server by this command:

python3 manage.py runserver

## Usage

Visit the homepage at the port given to view and interact with the movie ticketing system.