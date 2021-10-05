
from flask_restful import Resource, reqparse
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {"message":"Store not found"}

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message":"This name already exists"}
        new_store = StoreModel(name)
        try:
            new_store.save_to_db()
        except:
            return {"message":"Error when create new store"}
        return new_store.json()
class StoreList(Resource):
    def get(self):
        return {"message":[store.json() for store in StoreModel.query.all()]}