from flask import Blueprint, jsonify, request, make_response
from app import db
from app.models.planet import Planet

# class Planet:
#     def __init__(self,id,name,description,has_humans=False):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.has_humans = has_humans 
        
# planet1 = Planet(1,"Mars","Big and red!")
# planet2 = Planet(2, "Venus","Super hot!")
# planet3 = Planet(3, "Earth","Great place with oxgen!",True)

# planets = [planet1,planet2,planet3]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ['POST'])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(name = request_body["name"],
                        description = request_body['description'],
                        has_humans = request_body["has_humans"])
    
    db.session.add(new_planet)
    db.session.commit() 
    
    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name = name_query)
    else:
        planets = Planet.query.all()
        
    planets_response = []
    
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "has_humans": planet.has_humans
        })
    return jsonify(planets_response)



@planets_bp.route("/<id>",methods = ['GET'])
def read_one_planet(id):
    try: 
        id = int(id)
    except ValueError:
        return {"message": f"{id} is an invalid planet id"}, 400
    planet = Planet.query.get_or_404(id)
    
    return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "has_humans": planet.has_humans
        }, 200

@planets_bp.route("/<id>",methods = ['PUT'])
def update_one_planet(id):
    try: 
        id = int(id)
    except ValueError:
        return {"message": f"{id} is an invalid planet id"}, 400
    planet = Planet.query.get_or_404(id)
    
    request_body = request.get_json()
    planet.name = request_body['name']
    planet.description = request_body['description']
    planet.has_humans = request_body["has_humans"]
    
    db.session.commit()
    
    return {
            "message":'planet has been updated successfully' 
        }, 200


@planets_bp.route("/<id>", methods=["DELETE"])
def delete_one_planet(id):
    try: 
        id = int(id)
    except ValueError:
        return {"message": f"{id} is an invalid planet id"}, 400
    planet = Planet.query.get_or_404(id)

    db.session.delete(planet)
    db.session.commit()

    return {
        "message": "planet has been successfully deleted"
    }, 200