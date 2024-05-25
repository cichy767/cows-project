from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import init_db, db_session
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)