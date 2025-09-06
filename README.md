# Slugger - A URL Shortener

## Video Demo: https://youtu.be/nJx6oIDu0XI

## 📖 Overview

This is a custom-built **URL shortener** implemented in **Python, Flask, and Redis**.  
It was designed not just as a practical tool, but as a demonstration of skills in **backend development, caching strategies, security-aware design, and clean architecture**.

Unlike many basic URL shorteners, this project emphasizes:

- **Performance** through Redis-based caching with sliding expiration.
- **Security** with robust URL validation and integration with the Google Safe Browsing API.
- **Reliability** by generating unique, opaque slugs with Blowfish encryption to avoid collisions and ensure consistency.

This project follows a clean **MVC architecture** with dependency injection, repository patterns, and external service abstraction. These design choices were made to keep the codebase modular, testable, and easily extendable.

---

## 🚀 Features

- Shorten long URLs into compact slugs
- Expirable URLs with **sliding expiration (TTI strategy in Redis)**
- Unique, compact, and opaque slugs generated with **Blowfish**
- Robust URL safety validation logic to mitigate **SSRF attacks**
- URL safety validation using the **Google Safe Browsing API**
- Clean **Bootstrap frontend** with custom error pages

---
## 🏗️ Architecture & Design Choices

- **MVC Architecture**: The project is structured around a clear separation of concerns:
  - **Models** for URL mappings and domain entities
  - **Views** built with Flask templates and Bootstrap
  - **Controllers** handling request routing and application logic

- **Dependency Injection**: Interfaces are defined for repositories and services, making it easy to swap implementations.

- **Repository Pattern**: Encapsulates persistence logic, keeping the application core independent of the database layer.

- **External Service Abstraction**: Google Safe Browsing integration is wrapped in an abstraction layer, so it can be replaced or extended without affecting core logic.

- **Security by Design**: 
  - URLs are validated against SSRF vectors before being persisted.  
  - Safe Browsing API integration adds an extra layer of protection.  

- **Scalability Considerations**: 
  - Redis chosen for performance and support of sliding expiration.  
  - Slug generation with Blowfish ensures uniqueness and opacity even with sequential IDs.  
  
---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Database/Cache**: Redis
- **Frontend**: Bootstrap

---

## ⚡ Getting Started

### Prerequisites

- Python 3.8+
- Redis (can be local install or Docker)
    
This project uses [uv](https://docs.astral.sh/uv/) for dependency management and virtual environments.

---

### 1. Clone the Repository

```bash
git clone https://github.com/vicbuss/url-shortener-py.git
cd <repo-name>
```

---

### 2. Install Dependencies

```bash
uv sync
```

---
### 3. Configure environment

Create a `.flaskenv` file in the project root:

```ini
FLASK_APP=src.app
FLASK_ENV=development
FLASK_DEBUG=1
```

Create a `.env` file with your [Google Safe Browsing](https://developers.google.com/safe-browsing) API key

```ini
SAFE_BROWSING_KEY="your-key-here"
```

Generate a binary key file called `test.key` used for Blowfish-based slug generation:

```python
import os

def main():
    key = os.urandom(16)
    with open("test.key", "wb") as f:
        f.write(key)

if __name__ == "__main__":
    main()
```

Then paste the `test.key` binary in your project root.

---
### 4. Redis Configuration

By default, the project expects a **non-password protected Redis instance** running on `localhost:6379`.

You can override these defaults by setting the following environment variables:

```ini
REDIS_HOST=your-redis-host
REDIS_PORT=your-redis-port
REDIS_PWD=your-redis-password
```

#### Quick Redis Startup (Docker)

If you don’t have Redis installed locally, you can start one quickly with Docker:

```bash
docker run -p 6379:6379 --name url-shortener-redis redis
```

---

### 5. Run the Application

You can run the application locally with uv:

```bash
uv run flask run
```

---
## 📖 Usage

- Open **[http://localhost:5000](http://localhost:5000)** in your browser
- Enter a long URL to receive a shortened link
- Use the shortened link to redirect back to the original URL

---
## 📈 Future Improvements

- User accounts and authentication
- Admin dashboard
- Prepare the project for production deployment by containerizing it with Docker and serving it through Nginx

---
## 📜 License

This project is licensed under the MIT License.

