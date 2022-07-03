from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

db = [
    {'trader': "Aditya", "trader_id":"1","instrument_id":"APPL","instrument_name":"Apple"},
    {'trader': "Shubham", "trader_id":"2","instrument_id":"APPL","instrument_name":"Apple"},
    {'trader': "Alok", "trader_id":"3","instrument_id":"SWGY","instrument_name":"Swiggy"},
    {'trader': "Rahul", "trader_id":"4","instrument_id":"APPL","instrument_name":"Apple"},
    {'trader': "Ritik", "trader_id":"5","instrument_id":"SWGY","instrument_name":"Swiggy"},
    {'trader': "Bob", "trader_id":"6","instrument_id":"AZN","instrument_name":"Amazon"},
    {'trader': "Yuvraj", "trader_id":"7","instrument_id":"PNP","instrument_name":"Phonepe"},
    {'trader': "Rishav", "trader_id":"8","instrument_id":"AZN","instrument_name":"Amazon"},
    {'trader': "Annie", "trader_id":"9","instrument_id":"APPL","instrument_name":"Apple"},
    {'trader': "Archer", "trader_id":"10","instrument_id":"MTA","instrument_name":"Meta"},
    {'trader': "James", "trader_id":"11","instrument_id":"MTA","instrument_name":"Meta"},
    {'trader': "Thanos", "trader_id":"12","instrument_id":"PNP","instrument_name":"Phonepe"} 
]

class City(BaseModel):
    trader: int
    trader_id: str
    instrument_id:str
    instrument_name:str
@app.get('/')
def index():
    return {'Hello' : 'Traders'}

@app.get('/traders')
def get_cities():
    return db

@app.get('/traders/{trader_id}')
def get_city(trader_id: int):
    return db[trader_id-1] 

