<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">FCMB Backend System</h3>


---

<p align="center"> This is the backend service for FCMB, providing real-time banking operations through APIs. The system enables account balance retrieval, recent transactions lookup, and customer information access via Django.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This Django backend application serves as the core API system for FCMB operations. It exposes RESTful APIs for real-time banking data, such as account balance retrieval, recent transactions, and customer information. The system is designed to handle critical banking services with a secure and scalable architecture.

## 🏁 Getting Started <a name = "getting_started"></a>

Follow these instructions to set up the backend application on your local machine for development and testing.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9+
- Django 3.2+
- PostgreSQL (for database)
- Elasticsearch (optional, depending on features)

Install Python dependencies with:

```bash
pip install -r requirements.txt
```

### Installing

1. **Clone the repository**:

```bash
git clone https://github.com/your-repo/fcmb-backend.git
cd fcmb-backend
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Set up environment variables**:

```bash
cp .env.example .env
```

Fill in the necessary environment variables such as:

- PostgreSQL credentials
- Django secret key

4. **Migrate the database**:

```bash
python manage.py migrate
```

5. **Run the server**:

```bash
python manage.py runserver
```

Now the backend API is running locally at `http://127.0.0.1:8000`.

## 🔧 Running the tests <a name = "tests"></a>

To run the automated tests:

```bash
python manage.py test
```

### Break down into end-to-end tests

Tests are implemented to ensure the system works as expected across various endpoints, such as retrieving account balance and customer information.

Example:

```bash
# Run end-to-end tests
python manage.py test accounts.tests
```

### Coding style tests

For code quality and linting:

```bash
flake8 .
```

## 🎈 Usage <a name="usage"></a>

The backend exposes several APIs:

- **Retrieve account balance**:
  - `GET /api/accounts/by-account-number/{account_number}/`
  
  Example:

  ```bash
  curl http://127.0.0.1:8000/api/accounts/by-account-number/1234567890/
  ```

- **Retrieve recent transactions**:
  - `GET /api/transactions/by-account-number/{account_number}/`

- **Retrieve customer information**:
  - `GET /api/customers/{account_number}/`

Each API requires the account number as a path parameter.

## 🚀 Deployment <a name = "deployment"></a>

To deploy the backend to production:

1. Set up a production PostgreSQL database and update your `.env` file with the credentials.
2. Run migrations to set up the database schema:

```bash
python manage.py migrate
```

3. Serve the Django application using a WSGI server like Gunicorn:

```bash
gunicorn fcmb_backend.wsgi:application
```

4. Use a reverse proxy like NGINX to handle requests and serve the application.

## ⛏️ Built Using <a name = "built_using"></a>

- [Django](https://www.djangoproject.com/) - Web framework
- [PostgreSQL](https://www.postgresql.org/) - Database
- [Gunicorn](https://gunicorn.org/) - WSGI server for deployment

## ✍️ Authors <a name = "authors"></a>

- [@seunfunmi-adegoke](https://github.com/seunfunmi-adegoke) - Backend development


## 🎉 Acknowledgments <a name = "acknowledgement"></a>

- Special thanks to the Django and PostgreSQL communities for their continuous support and resources.
# chatbot-backend
