from flask import Blueprint, jsonify


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

@planets_bp.route("", methods=["GET"])
def handle_planets():
    response = []
    for planet in planets:
        response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "has humans": planet.has_humans
        })
    return jsonify(response)
#test

@planets_bp.route("/<id>",methods = ['GET'])
def one_planet(id):
    for planet in planets:
        if planet.id == int(id):
            return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "has humans": planet.has_humans
            }, 200 

    
