from app.models.user import User
from flask import make_response, jsonify, request
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class HelloWord(Resource):
    
    def get(self):
        users = User.query.all()
        users = users.dump(users).data
        return {"status": "success","data":users}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = json.load(json_data)
        if errors:
            return errors, 422
        user = User.query.filter_by(username=data['username']).first()
        if  user :
            return {'message': 'User already exists'}, 400
        # username ,email , password
        # check if username exists
        # check if email exists
        # create a user
        # create api_key
        user = User(firstname = json_data['firstname'],
                lastname = json_data['lastname'],
                email = json_data['email'],
                password = json_data['password'],
                username = json_data['username'],)
        db.session.add(user)
        db.session.commit()

        result = User.dump(user).data

        return {"status": 'success', 'data': result}, 201


    # def get(self):

    #     return make_response(jsonify({'message':'hello world'}),200)