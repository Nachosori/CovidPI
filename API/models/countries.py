from pydantic import BaseModel

class Country(BaseModel):
    country:str
    
class UpdateCountryName(BaseModel):
    country:str
  
class UpdateConfirmedData(BaseModel):
    number:str