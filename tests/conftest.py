import pytest 
from app import create_app, db
from app.models.planet import Planet
from flask.signals import request_finished

@pytest.fixture
def app():
    app = create_app(test_config=True)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()
    
    with app.app_context():
        db.create_all()
        yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_planets(app):
    earth = Planet(name="Earth", description="Kinda cool", has_humans=True)
    pluto = Planet(name="Pluto", description="It's a planet", has_humans=False)

    db.session.add_all([earth, pluto])
    db.session.commit()