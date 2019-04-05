from mongoengine import *

#The below function connects to FortinetDB Database on Atlas Cluster.
connect(db='FortinetDB',host="mongodb+srv://ShivaKumar:AMDInstagram@fortinetdb-i8rsn.azure.mongodb.net/FortinetDB?retryWrites=true")


class GetData(Document):
    Restaurant_ID = LongField()
    Restaurant_Name = StringField()
    Cuisines = StringField()
    Average_Cost_for_two = IntField()
    Currency = StringField()
    Has_Table_booking = StringField()
    Has_Online_delivery = StringField()
    Aggregate_rating = FloatField()
    Rating_color = StringField()
    Rating_text = StringField()
    Votes = LongField()

    meta={'collection':'Restaurant_data'}