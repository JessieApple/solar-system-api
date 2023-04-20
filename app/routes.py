from flask import Blueprint

class Planet:
    def __init__(self,id,name,description,has_humans=False):
        self.id = id
        self.name = name
        self.description = description
        self.has_humans = has_humans 
        
    
