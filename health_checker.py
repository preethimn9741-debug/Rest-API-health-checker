import json
import requests
import csv
import time


with open("config.json") as f:
    config = json.load(f)

apis = config["apis"]
results = []


for api in apis:
    try:
        start_time = time.time()
        response = requests.get(api, timeout=5)
        response_time = int((time.time() - start_time) * 1000)

        status_code = response.status_code
        status = "UP" if status_code == 200 else "DOWN"

        results.append([api, status_code, response_time, status])

    except requests.exceptions.RequestException as e:
        results.append([api, "ERROR", "timeout", "DOWN"])


with open("api_health.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["API", "Status Code", "Response Time (ms)", "Status"])
    writer.writerows(results)


with open("api_health.html", "w") as f:
    f.write("<html><body><h2>API Health Report</h2><table border='1'>")
    f.write("<tr><th>API</th><th>Status Code</th><th>Response Time</th><th>Status</th></tr>")

    for api, code, time_ms, status in results:
        color = "green" if status == "UP" else "red"
        f.write(
            f"<tr><td>{api}</td><td>{code}</td>"
            f"<td>{time_ms}</td><td style='color:{color}'>{status}</td></tr>"
        )

    f.write("</table></body></html>")

print("Health check completed. Reports generated.")                          
