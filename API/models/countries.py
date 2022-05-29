from pydantic import BaseModel

class Country(BaseModel):
    country:str
    
class UpdateCountryName(BaseModel):
    country:str
  
class UpdateData(BaseModel):
    number:str