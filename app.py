#!/usr/bin/env python

import os
import web
import requests
import json


from config import CONFIG_FILE, DEBUG, SENSU_API_URI, SENSU_API_USER, SENSU_API_PASS, load_config, validate_api_key

# SHA2
urls = (
    '/', 'Index',
    '/results/([A-Fa-f0-9]{64})', 'CheckCollector'
)

api_config = load_config(CONFIG_FILE)


class Index(object):

    def GET(self):
        return 'Welcome to the Sensu Check Collector!'


class CheckCollector(object):

    def GET(self, api_key):
        return web.nomethod()

    def POST(self, api_key):
        try:
            data = json.loads(web.data())
            if DEBUG: print(json.dumps(data))
        except ValueError as e:
            raise web.badrequest('Invalid JSON request data')

        if not validate_api_key(api_key, api_config, data):
            raise web.forbidden('Invalid API Key')

        try:
            headers = {'Content-type': 'application/json'}
            if SENSU_API_USER and SENSU_API_PASS:
                if DEBUG: print "AUTH: SENSU_API_USER, XXX"
                auth=(SENSU_API_USER, SENSU_API_PASS)
            else:
                auth=None
            r = requests.post(SENSU_API_URI, json=data, headers=headers, auth=auth)
            r.raise_for_status()
            return web.accepted()
        except requests.exceptions.RequestException as e:
            print(e)
            raise web.internalerror('RequestException calling Sensu')


if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = DEBUG

    app.run()
