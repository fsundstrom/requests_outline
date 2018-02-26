import os
import requests
import json
import re
import pprint
from flask import request, abort, render_template
from app import app

# create index page
#########################
@app.route('/')
def index():
 
  # we are getting the info provied by flask for the conneciton 
  # ref http://werkzeug.pocoo.org/docs/wrappers/#werkzeug.wrappers.BaseRequest.remote_addr

  # get remote ip
  ip = request.environ['REMOTE_ADDR']
  head = request.headers
  geo_data = __get_ip_info(ip)
  if not geo_data.status_code == 200: return abort(r.status_code)
  if geo_data.text:
    print geo_data.json()

  # retirm template with info 
  return render_template("index.html", lookup_ip=ip, headers=head, geo_data=geo_data.json())

# Get Host info
##########################
@app.route('/host/<host>', methods=["GET"])
def get_host(host):
 
  # demo showing how to make a call 

  call = 'dig '+host+' +noall +answer |tail -1'
  output = os.popen(call).read()
  ip = re.sub(r'^.*\t','',output)
  return render_template("index.html", lookup_ip=ip)

####################################################################################
# Private methods, helpers and error handlers                                      #
####################################################################################

# get ip info from free geoip
def __get_ip_info(ip):
  print ip
  return requests.get(
               __format_uri(app.config['API_HOST_ENDPOINT']+ip),
               # Not usded auth=__get_auth(),
               # Not used params=__get_params(ip),
               headers=app.config['HEADERS'],
               verify=False,
              )

# set basic auth for Infoblox API
def __get_auth():
  return HTTPBasicAuth(app.config['USERNAME'], app.config['PASSWORD'])

# this is for Flask not used at this time
def __get_params(params={}):
  #params.update(config['API_QUERY'])
  return params

# Fromat URL for API call
def __format_uri(endpoint):
  return '{0}{1}'.format(app.config['API_HOST'], endpoint)




# default error handler
@app.errorhandler(400)
def bad_request(error):
  return "Bad request: %s" % error, 400
