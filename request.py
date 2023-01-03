import requests
post_data={"username":"sean","password":"kali"}

response=requests.post("http://www.pentest.com:49153/login.php",
 				data=post_data)
HTML=response.text
print(HTML)