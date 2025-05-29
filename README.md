# AutoNest Core

AutoNest Core is the backend API service for AutoNest (an online car dealership platform) built with Django and Django REST Framework with PostgreSQL database integration.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Environment Configuration](#environment-configuration)
- [Local Development Setup](#local-development-setup)
- [Database Configuration](#database-configuration)
- [Running the Application](#running-the-application)
- [Troubleshooting Common Issues](#troubleshooting-common-issues)

## Prerequisites

Before setting up the project, ensure you have the following installed:

### For Local Development

- Python 3.8 or higher
- PostgreSQL 17 or higher
- Git

### For Docker Setup

- Docker
- Docker Compose

## Environment Configuration

Create a `.env` file in the project root directory with the following configuration:

```env
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=autonest_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

**Important Notes:**

- Set `DEBUG=False` in production
- Update `ALLOWED_HOSTS` with your domain names for production
- Use strong passwords for production databases
- The application is configured for UTC+6 timezone

## Local Development Setup

### 1. Clone the Repository

```bash
# Linux/macOS/Windows
git clone https://github.com/luqisha/AutoNest-Core
cd autonest-core
```

### 2. Create Virtual Environment

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
# Linux/macOS/Windows
pip install -r requirements.txt
```

### 4. Database Setup

#### Install PostgreSQL

**Linux (Ubuntu/Debian):**

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

**Windows:**

- Download PostgreSQL from [official website](https://www.postgresql.org/download/windows/)
- Run the installer and follow the setup wizard
- While installing set the username and password both as `postgres`

#### Create Database

```bash
# Linux/macOS
sudo -u postgres psql
CREATE DATABASE autonest_db;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE autonest_db TO postgres;
\q

# Windows (using psql command line)
psql -U postgres
CREATE DATABASE autonest_db;
\q
```

### 5. Run Migrations

```bash
# Linux/macOS/Windows
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
# Linux/macOS/Windows
python manage.py createsuperuser
```

## Database Configuration

### PostgreSQL Settings

The application connects to PostgreSQL using the following configuration from your `.env` file:

- **Database Name:** autonest_db
- **Username:** postgres
- **Password:** postgres
- **Host (for local setup):** localhost
- **Port:** 5432

### Database Connection Testing

Test your database connection:

```bash
# Linux/macOS/Windows
python manage.py dbshell
```

If successful, you should see the PostgreSQL prompt.

## Running the Application

### Local Development Server

```bash
# Linux/macOS/Windows
python manage.py runserver
```

The application will be available at `http://localhost:8000`

### Custom Port

```bash
# Linux/macOS/Windows
python manage.py runserver 0.0.0.0:8001
```

## Troubleshooting Common Issues

#### 1. Database Connection Error

- Ensure PostgreSQL service is running
- Verify database credentials in `.env` file
- Check if the database exists

#### 2. Port Already in Use

```bash
# Linux/macOS
lsof -ti:8000 | xargs kill -9

# Windows (Command Prompt) [replace <PID> with actual number]
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Windows (PowerShell)
Get-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess | Stop-Process
```
