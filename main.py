#!/usr/bin/env python

import logging
import os

import webapp2
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

class HomeHandler(webapp2.RequestHandler):
    def get(self): 
        _template_values = {}
        _path = os.path.join(os.path.dirname(__file__), 'index_template.html')
        self.response.out.write(template.render(_path, _template_values))

class AboutHandler(webapp2.RequestHandler):
    def get(self): 
        _template_values = {}
        _template_values["nav-active"] = "about.html"
        _path = os.path.join(os.path.dirname(__file__), 'about_template.html')
        self.response.out.write(template.render(_path, _template_values))

class WorkHandler(webapp2.RequestHandler):
    def get(self): 
        _template_values = {}
        _template_values["nav-active"] = "work.html"
        _path = os.path.join(os.path.dirname(__file__), 'work_template.html')
        self.response.out.write(template.render(_path, _template_values))

app = webapp2.WSGIApplication( \
    [\
    ('/',HomeHandler), \
    ('/index.html',HomeHandler), \
    ('/about.html',AboutHandler), \
    ('/work.html',WorkHandler), \
    ], \
    debug=True)