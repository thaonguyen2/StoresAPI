import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        user = UserModel.find_by_username(data['username'])
        if user:
            return {"message": "A user with username '{}' already exists.".format(user.username)}, 400

        user = UserModel(**data)
        print(user.id)
        user.save_to_db()

        return {"message": "User created successfully."}