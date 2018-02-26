from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)

#set up default config needed by request and not used in this demo
app.config.update(dict(
  API_HOST='https://freegeoip.net',
  API_HOST_ENDPOINT='/json/',
  HEADERS={'Accept': 'application/json'},
  USERNAME='Not_Used',
  PASSWORD='Not_USed',

))
from app import views

