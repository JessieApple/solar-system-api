from flask import Blueprint

class Planet:
    def __init__(self,id,name,description,has_humans=False):
        self.id = id
        self.name = name
        self.description = description
        self.has_humans = has_humans 
        
planet1 = Planet(1,"Mars","Big and red!")
planet2 = Planet(2, "Venus","Super hot!")
planet3 = Planet(3, "Earth","Great place with oxgen!",True)

planets = [planet1,planet2,planet3]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


    
