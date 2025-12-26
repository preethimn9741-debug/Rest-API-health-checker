# REST API Health Checker

## Project Description
This project checks the health of multiple REST APIs.
It sends HTTP requests to configured API endpoints, measures response time, determines whether each API is UP or DOWN, and generates health reports in CSV and HTML formats.

---

## Files
- `health_checker.py` – Main health check script
- `config.json` – List of API URLs to check
- `api_health.csv` – Generated CSV health report
- `api_health.html` – Generated HTML health report
- `README.md` – Project documentation

---

## How the Script Works
1. Reads API URLs from `config.json`
2. Sends a GET request to each API
3. Measures response time in milliseconds
4. Captures HTTP status code
5. Marks API status as:
   - `UP` (status code 200)
   - `DOWN` (error or non-200 response)
6. Writes results to:
   - `api_health.csv`
   - `api_health.html`

---

## Configuration
The `config.json` file contains the list of APIs to check.

Example:
```json
{
  "apis": [
    "https://api.github.com",
    "https://jsonplaceholder.typicode.com/posts"
  ]
}

How to Run
python health_checker.py

Output

After execution:

api_health.csv contains the health status in CSV format

api_health.html contains a formatted HTML report

A completion message is printed in the console

## Conclusion

This project provides a simple way to monitor the health of REST APIs.

It checks API availability, measures response time, and generates clear CSV and HTML reports.

The script is easy to run and helps quickly identify APIs that are up or down.


