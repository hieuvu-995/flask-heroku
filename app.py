from flask import Flask
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import ItemList, Item
from flask_restful import Api
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/hieuvu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)
jwt = JWT(app, authenticate, identity) #/auth

# @app.before_first_request
# def create_tables():
#     db.create_all()


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

# @app.route("/item/<string:name>", methods=["POST", "GET"])
# def get(name):
#     return {"student": name}

if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)