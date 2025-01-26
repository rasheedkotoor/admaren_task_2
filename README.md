# 📝 SnipBox - Backend API

SnipBox is a short note-saving app that lets users save short notes and organize them using tags.

## 📌 Features

- ✅ User authentication with JWT
- ✅ Create, read, update, and delete snippets
- ✅ Organize snippets using tags
- ✅ Secure API endpoints

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository

```sh
git clone https://github.com/yourusername/snipbox.git
cd snipbox_project
```

### 2️⃣ Create & activate a virtual environment

```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Install dependencies

```sh
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```sh
python manage.py migrate
```

### 5️⃣ Create a superuser

```sh
python manage.py createsuperuser
```

### 6️⃣ Run the development server

```sh
python manage.py runserver
```

---

## 🛠 API Endpoints

| Method     | Endpoint                 | Description           |
| ---------- | ------------------------ | --------------------  |
| **POST**   | `/auth/register/`        | Register new user     |
| **POST**   | `/auth/login/`           | Login & get JWT token |
| **POST**   | `/auth/refresh/`         | Refresh JWT token     |
| **GET**    | `/snippets/`             | Get all snippets      |
| **POST**   | `/snippets/create/`      | Create a new snippet  |
| **GET**    | `/snippets/{id}/`        | Get snippet details   |
| **PUT**    | `/snippets/{id}/update/` | Update a snippet      |
| **DELETE** | `/snippets/{id}/delete/` | Delete a snippet      |
| **GET**    | `/tags/`                 | List all tags         |
| **GET**    | `/tags/{id}/`            | Get snippets by tag   |

---

## 💪 Running Tests

To run the test cases:

```sh
python manage.py test
```

---

## 💡 Notes

- Ensure `.env` file contains necessary environment variables:
  - DJANGO_SECRET_KEY=
  - DEBUG=
  - DB_NAME=
  - DB_USER=
  - DB_PASSWORD=
  - DB_HOST=
  - DB_PORT=
- Use `Postman` or `cURL` to test API endpoints.
  - postman collection; `SnipBox_Backend_API_collection.json` is added in the root folder

---


