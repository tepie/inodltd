#!/usr/bin/env python

import logging
import os
import math

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
        _path = os.path.join(os.path.dirname(__file__), 'about_template.html')
        self.response.out.write(template.render(_path, _template_values))

class WorkHandler(webapp2.RequestHandler):
    def get(self): 
        _template_values = {}
        _path = os.path.join(os.path.dirname(__file__), 'work_template.html')
        self.response.out.write(template.render(_path, _template_values))

class WorkDetailHandler(webapp2.RequestHandler):
    def get(self): 
        _template_values = {}

        if self.request.path == "/work-ext-patios-landscaping.html":
            _template_values["work_detail_heading_title"] = "Exterior Patios and Landscaping"

            _template_values["sections"] = []
            
            section = {}
            section["heading"] = "Pergola"
            section["before"] = None
            section["after"] = ['exterior_pergola_IMG_0283-thumb.jpg','exterior_pergola_IMG_0284-thumb.jpg','exterior_pergola_IMG_0286-thumb.jpg']
            
            section["before_cols"] = 0 #math.floor(12 / len(section["before"]))
            section["after_cols"] = int(math.floor(12 / len(section["after"])))

            _template_values["sections"].append(section)

            section = {}
            section["heading"] = "Walkway"
            section["before"] = ['exterior_walkway_IMG_0310-med.jpg']
            section["after"] = ['exterior_walkway_IMG_0249-med.jpg']

            section["before_cols"] = int(math.floor(12 / len(section["before"])))
            section["after_cols"] = int(math.floor(12 / len(section["after"])))

            _template_values["sections"].append(section)

            section = {}
            section["heading"] = "Stone Landscaping"
            section["before"] = ['exterior_stone_landscaping_IMG_0278-thumb.jpg','exterior_stone_landscaping_IMG_0279-thumb.jpg','exterior_stone_landscaping_IMG_0268-thumb.jpg']
            section["after"] = ['exterior_stone_landscaping_IMG_0269-thumb.jpg',
                'exterior_stone_landscaping_IMG_0270-thumb.jpg',
                'exterior_stone_landscaping_IMG_0271-thumb.jpg',
                'exterior_stone_landscaping_IMG_0272-thumb.jpg']
                #'exterior_stone_landscaping_IMG_0274-thumb.jpg',
                #'exterior_stone_landscaping_IMG_0275-thumb.jpg',
                #'exterior_stone_landscaping_IMG_0276-thumb.jpg']

            section["before_cols"] = int(math.floor(12 / len(section["before"])))
            section["after_cols"] = int(math.floor(12 / len(section["after"])))

            _template_values["sections"].append(section)

            section = {}
            section["heading"] = "Landscaping"
            section["before"] = ['landscape_design_before_001-thumb.png']
            section["after"] = ['landscape_design_after_001-thumb.png']

            section["before_cols"] = int(math.floor(12 / len(section["before"])))
            section["after_cols"] = int(math.floor(12 / len(section["after"])))

            _template_values["sections"].append(section)

            section = {}
            section["heading"] = "Red Stone Patio"
            section["before"] = None
            section["after"] = ['patio_after_002-thumb.png']

            section["before_cols"] = 0
            section["after_cols"] = int(math.floor(12 / len(section["after"])))

            _template_values["sections"].append(section)

            section = {}
            section["heading"] = "Grey Stone Patio"
            section["before"] = None
            section["after"] = ['patio_after_001-med.png']

            section["before_cols"] = 0
            section["after_cols"] = int(math.floor(12 / len(section["after"])))

            _template_values["sections"].append(section)

            section = {}
            section["heading"] = "Exterior Brick Repair"
            section["before"] = ['exterior_brick_repair_IMG_0250-thumb.jpg','exterior_brick_repair_IMG_0251-thumb.jpg']
            section["after"] = ['exterior_brick_repair_IMG_0253-thumb.jpg','exterior_brick_repair_IMG_0254-thumb.jpg']

            section["before_cols"] = int(math.floor(12 / len(section["before"])))
            section["after_cols"] = int(math.floor(12 / len(section["after"])))

            _template_values["sections"].append(section)

        elif self.request.path == "/work-ext-deck-construction.html":
            _template_values["work_detail_heading_title"] = "Exterior Deck Construction"

            _template_values["sections"] = []

            section = {}
            section["heading"] = "Deck with Side Fence"
            section["before"] = ['deck_before_001-thumb.png','deck_mid_001-thumb.png','deck_mid_002-thumb.png']
            section["after"] = ['deck_mid_003-thumb.png','deck_after_001-thumb.png']

            section["before_cols"] = int(math.floor(12 / len(section["before"])))
            section["after_cols"] = int(math.floor(12 / len(section["after"])))

            _template_values["sections"].append(section)

            section = {}
            section["heading"] = "Deck with Front Bench"
            section["before"] = ['deck_before_002-thumb.jpg']
            section["after"] = ['deck_after_002-2-thumb.jpg','deck_after_002-1-thumb.jpg']

            section["before_cols"] = int(math.floor(12 / len(section["before"])))
            section["after_cols"] = int(math.floor(12 / len(section["after"])))

            _template_values["sections"].append(section)

            section = {}
            section["heading"] = "Ground Level Deck"
            section["before"] = ['exterior_deck_bench_step_IMG_0304-thumb.jpg','exterior_deck_bench_step_IMG_0314-thumb.jpg']
            section["after"] = ['exterior_deck_bench_step_IMG_0313-thumb.jpg','exterior_deck_bench_step_IMG_0312-thumb.jpg']

            section["before_cols"] = int(math.floor(12 / len(section["before"])))
            section["after_cols"] = int(math.floor(12 / len(section["after"])))

            _template_values["sections"].append(section)

            section = {}
            section["heading"] = "Small Deck"
            section["before"] = ['exterior_small_deck_IMG_0264-thumb.jpg']
            section["after"] = ['exterior_small_deck_IMG_0265-thumb.jpg']

            section["before_cols"] = int(math.floor(12 / len(section["before"])))
            section["after_cols"] = int(math.floor(12 / len(section["after"])))

            _template_values["sections"].append(section)

            section = {}
            section["heading"] = "Front Porch Rebuild"
            section["before"] = ['front_porch_rebuild_before_001-thumb.png']
            section["after"] = ['front_porch_rebuild_after_001-thumb.png']

            section["before_cols"] = int(math.floor(12 / len(section["before"])))
            section["after_cols"] = int(math.floor(12 / len(section["after"])))

            _template_values["sections"].append(section)

            section = {}
            section["heading"] = "Draw Bridge Deck Steps"
            section["before"] = None
            section["after"] = ['exterior_deck_ramp_IMG_0273-thumb.jpg']

            section["before_cols"] = 0
            section["after_cols"] = int(math.floor(12 / len(section["after"])))

            _template_values["sections"].append(section)


        elif self.request.path == "/work-int-kitchen.html":
            _template_values["work_detail_heading_title"] = "Interior Kitchen Remodeling"

            _template_values["sections"] = []

            section = {}
            section["heading"] = "Kitchen Remodel"
            section["before"] = None
            section["after"] = ['interior_kitech_remodel_IMG_0291-thumb.jpg','interior_kitech_remodel_IMG_0290-thumb.jpg','interior_kitech_remodel_IMG_0289-thumb.jpg']

            section["before_cols"] = 0
            section["after_cols"] = int(math.floor(12 / len(section["after"])))

            _template_values["sections"].append(section)

            section = {}
            section["heading"] = "Kitchen Remodel"
            section["before"] = ['interior_room_kitchen_remodel_IMG_0292-thumb.jpg','interior_room_kitchen_remodel_IMG_0293-thumb.jpg','interior_room_kitchen_remodel_IMG_0298-thumb.jpg']
            section["after"] = ['interior_room_kitchen_remodel_IMG_0295-thumb.jpg','interior_room_kitchen_remodel_IMG_0296-thumb.jpg','interior_room_kitchen_remodel_IMG_0300-thumb.jpg','interior_room_kitchen_remodel_IMG_0303-thumb.jpg']

            section["before_cols"] = int(math.floor(12 / len(section["before"])))
            section["after_cols"] = int(math.floor(12 / len(section["after"])))

            _template_values["sections"].append(section)

        elif self.request.path == "/work-int-repair.html":
            _template_values["work_detail_heading_title"] = "Interior Repair"

            _template_values["sections"] = []

            section = {}
            section["heading"] = "Room Remodel"
            section["before"] = ['interior_room_remodel_IMG_0257-thumb.jpg','interior_room_remodel_IMG_0258-thumb.jpg','interior_room_remodel_IMG_0261-thumb.jpg']
            section["after"] = ['interior_room_remodel_IMG_0263-thumb.jpg','interior_room_remodel_IMG_0266-thumb.jpg','interior_room_remodel_IMG_0267-thumb.jpg']

            section["before_cols"] = int(math.floor(12 / len(section["before"])))
            section["after_cols"] = int(math.floor(12 / len(section["after"])))

            _template_values["sections"].append(section)


        _path = os.path.join(os.path.dirname(__file__), 'work_detail_template.html')
        self.response.out.write(template.render(_path, _template_values))
        
class ContactHandler(webapp2.RequestHandler):
    def get(self): 
        _template_values = {}
        _path = os.path.join(os.path.dirname(__file__), 'contact_template.html')
        self.response.out.write(template.render(_path, _template_values))

app = webapp2.WSGIApplication( \
    [\
    ('/',HomeHandler), \
    ('/index.html',HomeHandler), \
    ('/about.html',AboutHandler), \
    ('/work.html',WorkHandler), \
    ('/work-ext-patios-landscaping.html',WorkDetailHandler), \
    ('/work-ext-deck-construction.html',WorkDetailHandler), \
    ('/work-int-kitchen.html',WorkDetailHandler), \
    ('/work-int-repair.html',WorkDetailHandler), \
    ('/contact.html',ContactHandler), \
    ], \
    debug=True)