import json
import os
import requests
import hashlib

SRV_ADDR = 'localhost'
SRV_PORT = '8888'
AUTH_API_URI = 'auth'
USR_API_URI = 'users'
AUTH_HEADER_NAME = 'X-Request-Checksum'
API_TOKEN_HEADER = 'Badsec-Authentication-Token'

def get_endpoint(server, port, end_point, proto='http'):
  return '{}://{}:{}/{}'.format(proto, server, port, end_point)

def get_auth_token(api_auth_uri, token_header):
  resp = requests.head(api_auth_uri)
  resp.raise_for_status()
  return resp.headers.get(token_header, None)

def get_users(api_usr_url, auth_token, retry_num=3, usr_endpoint=USR_API_URI):
  salt = '/'.join([auth_token, usr_endpoint]).encode('utf-8')
  header_value = hashlib.sha256(salt)
  resp = None
  while retry_num:
    resp = requests.get(api_usr_url, headers={AUTH_HEADER_NAME: header_value.hexdigest()})
    if resp.ok:
      break
  return resp


if __name__ == '__main__':
  auth_uri = get_endpoint(SRV_ADDR, SRV_PORT, AUTH_API_URI)
  usr_uri = get_endpoint(SRV_ADDR, SRV_PORT, USR_API_URI)

  token = get_auth_token(auth_uri, API_TOKEN_HEADER)
  resp = get_users(usr_uri, token)
  if not resp or not resp.text:
    os._exit(1)

  ids = [id.decode() for id in resp.iter_lines()]
  if ids:
    print(json.dumps(ids))
    os._exit(0)
  os._exit(1)