import requests

import flask
import base64

app = flask.Flask(__name__)


@app.route("/")
def index():
    username = flask.request.args.get("username")

    # process username here......
    #username=base64.b64encode(username.encode())

    # After processing, send to target server
    session = requests.session()
    response = session.get("http://www.pentest.com:49153/userinfo.php?username=" + username,proxies={'http':'http://127.0.0.1:8080'})
    return response.text  # receive response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)