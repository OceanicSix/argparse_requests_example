# pip3 install beautifulsoup4
from bs4 import BeautifulSoup
import requests

# After receiving html code from requests
post_data={"username":"sean","password":"1234"}

response=requests.post("http://www.pentest.com:49153/login.php",
 				data=post_data)
html=response.text

beauty_obj=BeautifulSoup(html,'html.parser')
pretty=str(beauty_obj)
print(pretty)