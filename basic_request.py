#!/usr/local/bin/python2.7

# load modules 

import json
import re
import requests
import sys
from pprint import pprint
from requests.auth import HTTPBasicAuth

#################
# Default vars  #
#################

# define default config
config = {}
config.update(dict(
  API_HOST='https://freegeoip.net',
  API_HOST_ENDPOINT='/json/',
  HEADERS={'Accept': 'application/json'},
  USERNAME='Not_Used',
  PASSWORD='Not_USed',
))

#############
# Main code #
#############

def main():
 
  #print config including defaults from Flask if we were using flask
  #print 'Defult request config'
  #pprint (config)

  # set ip to 2nd line object
  ip = str(sys.argv[1])
  # set match to ~ IP address format
  pattern = re.compile("[1-2]?[0-9]?[0-9]?\.[1-2]?[0-9]?[0-9]?\.[1-2]?[0-9]?[0-9]?")
  if pattern.match(ip):
     r =  __get_ip_info(ip)
     if not r.status_code == 200: return abort(r.status_code)
     pprint(r.json())




  else:
    print "input was not A IP"
    exit()


####################################################################################
# Private methods, helpers and error handlers                                      #
####################################################################################

# get ip info from free geoip
def __get_ip_info(ip):
  print ip
  return requests.get(
               __format_uri(config['API_HOST_ENDPOINT']+ip),
               # Not usded auth=__get_auth(),
               # Not used params=__get_params(ip),
               headers=config['HEADERS'],
               verify=False,
              )

# set basic auth for Infoblox API
def __get_auth():
  return HTTPBasicAuth(config['USERNAME'], config['PASSWORD'])

# this is for Flask not used at this time
def __get_params(params={}):
  #params.update(config['API_QUERY'])
  return params

# Fromat URL for API call
def __format_uri(endpoint):
  return '{0}{1}'.format(config['API_HOST'], endpoint)


########
# MAIN #
########

# run def main 
if __name__== "__main__":
  main()
