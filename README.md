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
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── wsgi.py
│   ├── urls.py
│   └── settings/
│       ├── __init__.py
│       ├── base.py
│       ├── development.py
│       ├── production.py
│       └── testing.py
├── apps/
│   ├── __init__.py
│   └── your-apps
├── core/
│   ├── __init__.py
│   ├── middleware.py
│   ├── utils.py
│   └── signals.py
├── static/
├── media/
├── templates/
├── tests/
├── fixtures/
├── Dockerfile.dev
├── Dockerfile.prod
├── docker-compose.yml
├── .env.example
└── README.md
```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.11+
- [UV](https://docs.astral.sh/uv/) package manager

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd django-scaffold
   ```

2. **Install UV** (if not already installed)
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
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
   docker-compose exec web uv run python manage.py migrate
   ```

3. **Create superuser**
   ```bash
   docker-compose exec web uv run python manage.py createsuperuser
   ```

## 🏗️ Architecture

### Dependency Management with UV

The project uses UV for fast, reliable dependency management:

- **pyproject.toml**: Main configuration file with all dependencies
- **Dependency groups**: Organized by purpose (develop, linter, test, type)
- **Lock file**: `uv.lock` ensures reproducible builds
- **Fast installs**: UV's Rust-based resolver for speed

### Settings Structure

- **base.py**: Common settings using `django-environ`
- **development.py**: Development-specific settings (SQLite, debug toolbar)
- **production.py**: Production settings (PostgreSQL, security headers)
- **testing.py**: Test-specific settings (in-memory database, fast hashers)

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

## 🔧 Development Tools

### Code Quality

```bash
# Format code
uv run black .
uv run isort .

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
   docker build -f Dockerfile.prod -t django-scaffold:latest .
   ```

2. **Environment variables**
   - Set production environment variables
   - Configure database, Redis, email settings
   - Set DEBUG=False and proper SECRET_KEY

3. **Run production container**
   ```bash
   docker run -p 8000:8000 --env-file .env django-scaffold:latest
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
    'apps.users.apps.UsersConfig',
    'apps.myapp.apps.MyappConfig',  # Add this
]
```

### Using Services

```python
# In views
from apps.users.services import UserService

def my_view(request):
    user_data = UserService.get_user_data(request.user)
    return JsonResponse(user_data)
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
