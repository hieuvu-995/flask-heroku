from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument(
        "username",
        type = str,
        required = True,
        help = "This field cannnot be blank"

    )
    parse.add_argument(
        "password",
        type = str,
        required = True,
        help = "This field cannnot be blank"

    )

    def post(self, username):
        if UserModel.find_by_username(username):
            return {"message":"username already exists"}
        data = UserRegister.parse.parse_args()
        new_account = UserModel(**data)
        try:
            new_account.save_to_db()
        except:
            {"message":"Error when create new account"}
        return {"message":"Account has been created"}