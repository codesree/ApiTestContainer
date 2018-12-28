from pymongo import MongoClient
import datetime
import json
import requests
import logging
import uuid,os
from oauthlib import oauth2
from requests.auth import HTTPBasicAuth
from test_gate import test_rating_db


class rating_Engine_Build():

    def __init__(self,buildfor,factor):
        rtbuild = buildfor
        global ratingenums
        ratefact = test_rating_db(rtbuild)
        ratingenums = ratefact.rating_engine_factors(rtbuild,factor)



    def startBuild(self,dictator):
        # dictator = {
        #   "persons": [],
        #     "organisations": [],
        #     "cars": [],
        #     "buildings": [],
        #     "contents": [],
        #     "allRisk": [],
        #     "caravanTrailers": [],
        #     "addresses": [],
        #     "contact": [],
        #     "computers": [],
        #     "watercrafts": [],
        #     "motorCycles": [],
        #     "personalAccident": [],
        #     "personalLiability": [],
        
        # }
        try:
            assert dictator['organsations'] is not None
        except:
            pass

    def gender_testload(self,usrfact):

        ratingenums = []













