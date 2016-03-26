#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.api import users
import webapp2
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexHandler(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        # self.response.write(template.render({'there': 'HOME'}))
         # Checks for active Google account session
        user = users.get_current_user()

        if user:
            nick = user.nickname() 
            nick = nick.split('@')[0]
            self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
            self.response.write(template.render({'there': nick, 'loginbutton': users.create_logout_url('/'), 'loginorout': 'logout'}))
            self.response.write('Hello, ' + nick)
        else:
            self.response.write(template.render({'loginbutton': users.create_login_url('/'), 'loginorout': 'login'}))
            # self.response.write(template.render({'there': 'hello'})

# class FamilyHandler(webapp2.RequestHandler):
#     def get(self):
#         template = JINJA_ENVIRONMENT.get_template('templates/family.html')
#         self.response.write(template.render())


# class FoodHandler(webapp2.RequestHandler):
#     def get(self):
#         template = JINJA_ENVIRONMENT.get_template('templates/food.html')
#         self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    # ('/index.html', IndexHandler),
    # ('/family.html', FamilyHandler),
    # ('/food.html', FoodHandler)
], debug=True)
