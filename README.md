# Employee Management System

A simple **Employee Management System** built with **FastAPI**, allowing CRUD operations on employee data stored in a local JSON file.

## 🚀 Features

- Add a new employee
- View all employees or a single employee by ID
- Update employee details (with ID match validation)
- Delete an employee
- All data stored and managed in a JSON file

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) – Web framework
- [Uvicorn](https://www.uvicorn.org/) – ASGI server
- Python 3.10+
- JSON (as a simple database)

## 📁 Project Structure

```

employee-management-system/
├── employees.json         # JSON database
├── main.py                # FastAPI app
├── models.py              # Pydantic models
├── requirements.txt       # Project dependencies
└── README.md              # Project info

````

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/SaiTarun212002/employee-management.git
cd employee-management
````

### 2. Create and Activate Virtual Environment (optional)

```bash
python -m venv fastapienv
source fastapienv/bin/activate  # macOS/Linux
fastapienv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
uvicorn main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the interactive API docs (Swagger UI).

## 🔄 API Endpoints

| Method | Endpoint           | Description                          |
| ------ | ------------------ | ------------------------------------ |
| GET    | `/employees`       | Get all employees                    |
| GET    | `/employees/{eid}` | Get employee by ID                   |
| POST   | `/employees`       | Add a new employee                   |
| PUT    | `/employees/{eid}` | Update employee (ID must match body) |
| DELETE | `/employees/{eid}` | Delete employee by ID                |

## 🧪 Sample JSON Data

```json
[
  {
    "eid": 12,
    "ename": "tarun",
    "email": "narasimhasaitarun@gmail.com",
    "depart": "IT",
    "designation": "assistant system engineer",
    "salary": 50000,
    "joining_date": "07/28/2023"
  }
]
```

## 🙋‍♂️ Author

* **Sai Tarun**
* GitHub: [@SaiTarun212002](https://github.com/SaiTarun212002)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

