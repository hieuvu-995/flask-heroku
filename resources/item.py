from flask_restful import Resource, reqparse
from models.item import ItemModel

class Item(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument(
        "price",
        type = float,
        required = True,
        help = "This field cannot be blank"
    )
    parse.add_argument(
        "store_id",
        type = int,
        required =  True,
        help = "This field cannot be blank"
    )

    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"messaage": "Item not found"}

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message":"Item name '{}' is already exists".format(name)}
        data = Item.parse.parse_args()
        new_item = ItemModel(name, data["price"], data["store_id"])
        try:
            new_item.save_to_db()
        except:
            return {"message":"Error when create new item"}

        return new_item.json()

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message":"item deleted"}

    def put(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            data = Item.parse.parse_args()
            new_item = Item(name, **data)
            try:
                new_item.save_to_db()
                return new_item.json()
            except:
                return {"message":"Error when update item"}
        return {"message":"Item not found"}

class ItemList(Resource):
    def get(self):
        return {"item":list(map(lambda x:x.json(), ItemModel.query.all() ))}