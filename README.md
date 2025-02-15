# Housemate FastAPI + PostgreSQL

A backend API for managing housemates' work schedules, built with FastAPI and PostgreSQL.

## Tech Stack
- **FastAPI** - High-performance Python web framework
- **PostgreSQL** - Relational database for storing schedules and users
- **SQLAlchemy** - ORM for database interactions
- **Alembic** - Database migrations

## Installation

### Prerequisites
- Python 3.10+
- PostgreSQL installed and running

### Clone the Repository
```sh
git clone https://github.com/yourusername/housemate-fastapi-postgres.git
cd housemate-fastapi-postgres
```

### Setup Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file in the root directory and configure the following variables:
```ini
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_SERVER=
POSTGRES_PORT=
POSTGRES_DB=

GOOGLE_CLIENT_ID = 
GOOGLE_CLIENT_SECRET = 
GOOGLE_REDIRECT_URI = 

JWT_SECRET_KEY = 
```

### Start the Server
```sh
uvicorn app.main:app --reload
```
API will be available at: `http://127.0.0.1:8000`

## License
This project is licensed under the MIT License.


