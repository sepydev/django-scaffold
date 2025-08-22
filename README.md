# Django 5 Project Scaffold

A modern, production-ready Django 5 project structure with best practices, modular architecture, and comprehensive tooling using UV for dependency management.

## 🚀 Features

- **Django 5.0+** with latest features and security updates
- **UV dependency management** with `pyproject.toml` configuration
- **Modular app structure** with clean separation of concerns
- **Split settings** for different environments (development, production, testing)
- **Custom User model** with extended fields
- **Docker support** with separate dev/prod configurations
- **Comprehensive middleware** for security and logging
- **Service layer pattern** for business logic
- **Signal handling** for decoupled event processing
- **Extensive utilities** for common operations
- **Code quality tools** with Black, isort, Ruff, and mypy
- **Type hints** and comprehensive testing setup

## 📁 Project Structure

```
django-scaffold/
├── manage.py
├── pyproject.toml          # UV dependency management
├── uv.lock                 # UV lockfile for reproducible builds
├── ruff.toml              # Ruff linting configuration
├── .yamllint              # YAML linting configuration
├── Dockerfile             # Multi-stage Docker configuration
├── docker-compose.yml     # Production Docker Compose
├── docker-compose.override.yml  # Development overrides
├── .env.example           # Environment variables template
├── LICENSE
└── README.md
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── wsgi.py
│   ├── urls.py
│   └── settings/
│       ├── __init__.py
│       ├── base.py         # Common settings
│       ├── development.py  # Development settings (PostgreSQL)
│       └── production.py   # Production settings (PostgreSQL + SSL)
├── apps/
│   ├── __init__.py
│   └── your-apps
├── core/
│   ├── __init__.py
│   ├── middleware.py       # Custom middleware
│   ├── utils.py           # Utility functions
│   └── signals.py         # Global signals
├── static/                # Static files
├── media/                 # User uploads
├── templates/             # Global templates
├── tests/                 # Test files
└── fixtures/              # Data fixtures
```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.13+
- [UV](https://docs.astral.sh/uv/) package manager

### Local Development

1. **Clone the repository**
   ```bash
   git clone git@github.com:sepydev/django-scaffold.git
   cd django-scaffold
   ```

2. **Install UV** (if not already installed)

Linux :
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
MacOS (with Homebrew):
   ```bash
   brew install uv
   ```

3. **Install dependencies**
   ```bash
   uv sync
   ```

4. **Environment configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Database setup**
   ```bash
   uv run python manage.py makemigrations
   uv run python manage.py migrate
   uv run python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   uv run python manage.py runserver
   ```

### Docker Development

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Run migrations**
   ```bash
   docker-compose exec app python manage.py migrate
   ```

3. **Create superuser**
   ```bash
   docker-compose exec app python manage.py createsuperuser
   ```

4. **Access the application**
   - Application: http://localhost:8811
   - Database: PostgreSQL 16.9 with health checks

## 🏗️ Architecture

### Dependency Management with UV

The project uses UV for fast, reliable dependency management:

- **pyproject.toml**: Main configuration file with all dependencies
- **Dependency groups**: Organized by purpose (develop, linter, test, type)
- **Lock file**: `uv.lock` ensures reproducible builds
- **Fast installs**: UV's Rust-based resolver for speed

### Settings Structure

- **base.py**: Common settings using `django-environ` with PostgreSQL default
- **development.py**: Development settings with PostgreSQL and debug toolbar
- **production.py**: Production settings with PostgreSQL, SSL, and security headers  
- **database.py**: Centralized database configuration functions for all environments

### Docker Configuration

The project uses a **multi-stage Dockerfile** with optimized builds:

- **Base stage**: Python 3.13 with UV dependency management
- **Dev stage**: For development with bind-mounted source code
- **Prod stage**: Production-ready with static files and Gunicorn

**Key Docker Features:**
- Modern PostgreSQL 16.9 with health checks
- Automatic dependency installation with UV
- Production-ready migrations and static collection
- Environment file support with `.env`

### App Structure

- **apps/**: Contains all Django apps
- **core/**: Shared utilities, middleware, and signals
- **config/**: Project configuration and settings

### Key Components

- **Custom User Model**: Extended user model with additional fields
- **Service Layer**: Business logic separated from views
- **Custom Middleware**: Request processing and security headers
- **Signal Handlers**: Decoupled event processing
- **Utilities**: Common helper functions and classes

## �� Development Tools

### Code Quality

```bash
# Lint code with Ruff (replaces flake8)
uv run ruff check .

# Fix auto-fixable issues with Ruff
uv run ruff check --fix .

# Security checks
uv run bandit -r .

# Type checking
uv run mypy .

# Run all quality checks
uv run pre-commit run --all-files
```

### Testing

```bash
# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=apps --cov=core --cov-report=html

# Run specific test
uv run pytest apps/users/tests/test_models.py
```

### Dependency Management

```bash
# Add new dependency
uv add django-extensions

# Add development dependency
uv add --group develop ipython

# Update dependencies
uv sync --upgrade

# Install production only
uv sync --no-group develop --no-group test --no-group linter --no-group type
```

## 🚀 Deployment

### Production Deployment

1. **Build production image**
   ```bash
   docker build --target prod -t django-scaffold:latest .
   ```

2. **Environment variables**
   - Set production environment variables in `.env`
   - Configure database with `DATABASE_URL` or individual `DB_*` variables
   - Set `DEBUG=False` and proper `SECRET_KEY`

3. **Run production container**
   ```bash
   docker run -p 8000:8000 --env-file .env django-scaffold:latest
   ```

4. **Or use Docker Compose for production**
   ```bash
   docker-compose up --build
   ```

### Docker Build Targets

The multi-stage Dockerfile provides different targets:

```bash
# Development build (with development tools)
docker build --target dev -t django-scaffold:dev .

# Production build (optimized, no dev dependencies)
docker build --target prod -t django-scaffold:prod .
```

### Environment Variables

Key environment variables for production:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to False in production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DB_*`: Database configuration
- `EMAIL_*`: Email service configuration
- `REDIS_URL`: Redis connection URL

## 📚 Usage Examples

### Creating a New App

```bash
# Create new app
uv run python manage.py startapp myapp apps/myapp

# Add to INSTALLED_APPS in settings/base.py
LOCAL_APPS = [
    'apps.myapp.apps.MyappConfig',  # Add this
]
```

### Running Management Commands

```bash
# Django commands with UV
uv run python manage.py collectstatic
uv run python manage.py shell
uv run python manage.py dbshell

# Custom management commands
uv run python manage.py your_custom_command
```

## 🔒 Security Features

- Custom middleware for security headers
- CSRF protection
- XSS protection
- Secure cookie settings for production
- Input validation utilities
- Proper secret management with environment variables

## 📈 Monitoring and Logging

- Structured logging configuration
- Request/response timing middleware
- User activity signals
- Health check endpoint (for production)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes following the project structure
4. Run tests and linting with UV
5. Submit a pull request

```bash
# Before committing
uv run black .
uv run isort .
uv run ruff check .
uv run mypy .
uv run pytest
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For questions and support, please open an issue in the repository.
