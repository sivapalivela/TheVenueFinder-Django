from mongoengine import *
# Create your models here.
connect('FortinetDB',username='ShivaKumar', password='AMDInstagram', authentication_source='FortinetDB')

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