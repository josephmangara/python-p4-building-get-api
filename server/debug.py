#!/usr/bin/env python3

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game, Review, User, db

fake = Faker()

if __name__ == '__main__':
   # Create and configure the Flask application
    from flask import Flask
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

     # Initialize the SQLAlchemy extension with the app
    db.init_app(app)
    
    # Create the database tables
    with app.app_context():
        db.create_all()

        engine = create_engine('sqlite:///app.db')
        Session = sessionmaker(bind=engine)
        session = Session()

        import ipdb; ipdb.set_trace()
