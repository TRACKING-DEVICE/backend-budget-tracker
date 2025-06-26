# backend-budget-tracker
#  Budget Tracker API

This is the **backend** for a Budget Tracker web application. It allows users to **sign up**, **log in**, and **track their income and expenses** by category. Users can also view **summary reports**.

Built with **Python**, **Flask**, **SQLAlchemy**, and **JWT authentication**.



##  Technologies Used

- Python 3.8+
- Flask
- Flask SQLAlchemy
- Flask JWT Extended
- PostgreSQL or SQLite (dev)
- Postman (for API testing)



##  Features

 User Authentication (Register/Login using JWT)
 CRUD operations for Transactions and Categories
 Category-based organization (e.g. Rent, Food, Salary)
 Expense Summary Report per user
 Persistent data with SQLAlchemy ORM



##  Project Structure

backend-budget-tracker/
 app.py 
 config.py 
 seed.py

 models/

 init.py 
 user.py
 category.py
 transaction.py

 controllers/
 
 init.py
 auth_controller.py
 transaction_controller.py
 routes.py 
 Pipefile
 Pipfile.lock
 README.md 


Copy
Edit



##  Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/budget-tracker-backend.git
cd budget-tracker-backend
2. Create a Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pipenv install -r requirements.txt
4. Run the App
bash
Copy
Edit
python app.py
By default, it runs on: http://127.0.0.1:5000/

 Seeding the Database 
bash
Copy
Edit
python seed.py
Populates the database with sample users, categories, and transactions.

 API Endpoints (Use Postman or curl)
 Auth
Method	Endpoint	Description
POST	/register	Register new user
POST	/login	Login and get token

 Transactions
Method	Endpoint	Description
POST	/transactions	Add a new transaction (JWT)
GET	/summary	Get category summary (JWT)

All protected routes require:

makefile
Copy
Edit
Authorization: Bearer <your_token_here>
 Example JWT Auth Flow
POST /register → Create a new user

POST /login → Get access_token

Use that token in headers for /transactions and /summary

 Contributing
PRs are welcome! Please open issues and help improve the project.

 License
MIT License

 Author
Jesse Yegon 
Tjay Earl