import pymongo, json
import pandas as pd
from CRENDECIAIS import *

class databaseConnect:
        def __init__(self,  db_database, client_url) -> None:
                self.db_database = db_database
                self.client_url = client_url
                self.db = self.db_connect()
        
        def collection_connect(self, db_collection):        
                self.col = self.db.get_collection(db_collection)
        
        def db_connect(self):
                self.client = pymongo.MongoClient(self.client_url)
                db = self.client.get_database(self.db_database)
                return db
                
        
        def insert_data(self,data):
                json_data = json.loads(data.to_json(orient = 'records'))
                result = self.col.insert_many(json_data)
        
        def update_data(self,myquery,newvalues):
                self.col.update_one(myquery, newvalues)


        def fetch_data(self, query_string=""):
                if query_string:
                        data = self.col.find_one({"date":query_string})
                else:
                        data = self.col.find_one()
                if data:
                        return data
                return  ""
        


                
        

      