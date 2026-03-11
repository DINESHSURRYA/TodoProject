# DS Todos (Django)

A Todo application built with Django, utilizing PostgreSQL for the database and `django-environ` for environment variable management.

## Project Structure

The project follows a standard Django layout:

```text
TodoProject/
├── todos/                  # The main app folder
│   ├── migrations/         # Database migrations
│   ├── static/             # Static files (CSS, JS, images)
│   ├── templates/          # HTML templates
│   ├── models.py           # Database models/tables
│   ├── urls.py             # App-specific URL routes
│   └── views.py            # View functions to handle HTTP requests
├── TodoProject/        
│   ├── settings.py         # Main project configuration
│   └── urls.py             # Global URL mapping
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables file
```

## Prerequisites

- Python 3.x
- [PostgreSQL](https://www.postgresql.org/) (optional if you use a cloud DB like Neon, or fallback to SQLite)

## Setup and Installation

### Quick Setup (Windows)

You can run the entire setup automatically using the included `run_project.ps1` script.

1. Open PowerShell and navigate to the project directory:
   ```powershell
   cd path\to\TodoProject
   ```
2. Execute the script:
   ```powershell
   .\run_project.ps1
   ```
   *This script will automatically create a virtual environment (`venv`), activate it, install dependencies from `requirements.txt`, apply database migrations, and start the development server.*

---

### Manual Setup (Platform Independent)

If you prefer to set up manually or you are on Linux/macOS, follow these steps:

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**
   - On **Windows (PowerShell)**: `.\venv\Scripts\Activate.ps1`
   - On **Windows (Command Prompt)**: `.\venv\Scripts\activate.bat`
   - On **Linux/macOS**: `source venv/bin/activate`

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables (`.env`)

Create a `.env` file in the root directory (alongside `manage.py`). It should contain the following settings:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True

# Database Configuration (PostgreSQL/NeonDB)
# Format: postgres://USER:PASSWORD@HOST:PORT/NAME
DATABASE_URL=postgresql://neondb_owner:password@host.aws.neon.tech/neondb?sslmode=require

# Optional Local Database
LOCAL_DATABASE_URL=postgresql://postgres:password@localhost:5432/postgres
```
*Note: Ensure `.env` is listed in your `.gitignore` to prevent leaking sensitive credentials like `SECRET_KEY` and `DATABASE_URL`.*

## Running the Server

Once your dependencies are installed and the `.env` file is configured:

1. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

2. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

3. Open your browser and navigate to:
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Built With

- [Django](https://www.djangoproject.com/) - High-level Python web framework
- [Neon](https://neon.tech/) / [PostgreSQL](https://www.postgresql.org/) - Relational database
- [django-environ](https://django-environ.readthedocs.io/en/latest/) - Environment variable configuration
