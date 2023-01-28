from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from db import users
from waitress import serve
from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required

blp = Blueprint("users", __name__, description="operations on users")

@blp.route("/login")
class UserLogin(MethodView):
    def post(self):
        request_data = request.get_json()
        req_username_id = request_data["username"]
        req_password = request_data["password"]
        for user in users:
            if user["name"] == req_username_id:
                if user["password"] == req_password:
                    access_token = create_access_token(identity=req_username_id)
                    return jsonify(access_token=access_token)
            return jsonify("Login failed"), 401



@blp.route("/api/user/<id>")
class User(MethodView):
    def get(self, id):
        for user in users:
            if user["id"] == id:
                return jsonify(user), 200
        return jsonify({}), 404
    @jwt_required()
    def post(self, id):
        request_data = request.get_json()
        email = request_data["email"]
        name = request_data["name"]
        password = request_data["password"]
        new_user = {"id":id, "email": email,"name": name, "password": password}
        if new_user:
            users.append(new_user)
            return jsonify(new_user), 200
