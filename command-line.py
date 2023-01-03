from cmd import Cmd
from time import time

import requests
class Terminal(Cmd):
    prompt = '> '

    def default(self, payload):
        data={"username":f'{payload}', "password": "I don't care"} # Set payload here
        start=time()
        r =requests.post("http://www.pentest.com:49153/login.php", data=data,proxies={"http":"http://127.0.0.1:8080"},allow_redirects=False)

        stop=time()
        print(f'status code is {r.status_code}; Content-length is {r.headers["Content-Length"]}; Respnse time is {stop-start}') ## return status code , content-length and process time

terminal = Terminal()
terminal.cmdloop()
