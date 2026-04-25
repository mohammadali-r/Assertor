# Assertor

**Assertor** is a structured API testing framework designed to enforce correctness through clean architecture, service abstraction, and schema validation.

It provides a scalable foundation for validating REST APIs with clarity, discipline, and maintainability.

---

## 🚀 Overview

Assertor is built around a layered architecture that separates concerns between test logic, API interaction, and validation.

```text
tests → services → client → API
```

This design ensures:

* Clean and readable tests
* Reusable API logic
* Centralized request handling
* Easy extensibility for large test suites

---

## 🧱 Project Structure

```
assertor/
│
├── client/        # HTTP client layer (handles all requests)
├── services/      # API abstraction layer (business logic)
├── models/        # Data validation schemas (Pydantic)
├── tests/         # Test cases (pytest)
├── config/        # Environment configurations
├── utils/         # Logging and helpers
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Features

* ✅ Layered architecture (client / service / test)
* ✅ Centralized HTTP handling
* ✅ Schema validation using Pydantic
* ✅ Environment-based configuration
* ✅ Pytest-based execution
* ✅ Extensible logging support
* ✅ Scalable for large API test suites

---

## 🧪 Example Test

```python
def test_get_user(user_service):
    user, status = user_service.get_user(1)

    assert status == 200
    assert user.id == 1
```

---

## 🔧 Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/assertor.git
cd assertor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment

Edit:

```
config/dev.yaml
```

Example:

```yaml
base_url: https://jsonplaceholder.typicode.com
```

---

## ▶️ Run Tests

```bash
pytest -v
```

---

## 🧠 Architecture Principles

### 1. Separation of Concerns

* Tests focus only on assertions
* Services handle API behavior
* Client manages HTTP communication

---

### 2. Reusability

API logic is centralized in service classes, reducing duplication across tests.

---

### 3. Validation First

All responses are validated using structured models to ensure contract correctness.

---

### 4. Extensibility

The framework is designed to easily integrate:

* Logging
* Retry mechanisms
* Authentication layers
* Reporting tools

---

## 🧭 Vision

Assertor is not just a test suite — it is a verification layer.

It aims to provide a disciplined approach to API testing where correctness is enforced through structure, not scattered assertions.

---

## 📄 License

MIT License
