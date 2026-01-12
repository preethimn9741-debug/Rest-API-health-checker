# REST API Health Checker

This project is a **REST API Health Checker** built using **Python**.  
It monitors the availability and response status of multiple APIs and reports whether they are **UP or DOWN**.  
The project supports configuration-based API checks, logging, report generation, and has been extended into a **Flask web application with testing support**.

---

##  Features

- Checks health of multiple REST APIs
- Measures response status and response time
- Supports configuration using JSON file
- Generates health reports (CSV / HTML)
- Flask-based web interface
- Database-backed API storage
- Interactive JavaScript frontend
- Automated test cases using pytest
- Robust error and timeout handling

---

## Technologies Used

- **Python**
- **Flask** – Web framework
- **Requests** – HTTP calls
- **SQLite** – Database
- **HTML & JavaScript** – Frontend
- **Pytest** – Testing framework

---

##  Project Structure

api-health-checker/
│
├── app.py # Flask web application

├── health_checker.py # Core API health check logic

├── database.py # Database & CRUD operations

├── config.json # API configuration file

├── api_health.csv # Generated CSV health report

├── api_health.html # Generated HTML health report

├── templates/

│ └── index.html # Web UI

├── static/

│ └── script.js # JavaScript for interactivity

├── tests/

│ ├── test_app.py # Flask API tests

│ └── test_health.py # Health checker logic tests

└── requirements.txt

## Installation & Setup

1. Clone / Open Project

   cd api-health-checker

2. Create virtual environment (optional)

   python -m venv venv
   
   venv\Scripts\activate

3. Install dependencies

   pip install -r requirements.txt

4. Start Flask App

   python app.py

 5.Running Test Cases 
 
   python -m pytest
   
## How It Works (Simple Flow)

1. APIs are read from database / config file

2. Requests are sent using requests

3. Response time and status are captured

4. Results are stored and displayed

5. Errors and timeouts are handled safely

6. UI displays results dynamically

## output 

| API                                              | Status | Response Time |
| ------------------------------------------------ | ------ | ------------- |
| [https://api.github.com](https://api.github.com) | UP     | 120 ms        |
| [https://invalid.api](https://invalid.api)       | DOWN   | timeout       |

## terminal output screenshort

<img width="1260" height="576" alt="Screenshot 2026-01-12 150648" src="https://github.com/user-attachments/assets/2bb577be-722f-432a-9aaf-661b852aa1f2" />

## Conclusion

This project demonstrates real-world backend development practices such as API monitoring, error handling, REST architecture, database integration, frontend interaction, and automated testing.




    


