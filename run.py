from app import app
from db import db

db.init_app(app)

## This is how we create SQL db and tables on the go
@app.before_first_request
def create_tables():
    db.create_all()
