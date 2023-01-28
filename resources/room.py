from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from db import rooms
from waitress import serve
from flask import Flask, jsonify, request

blp = Blueprint("rooms", __name__, description="operations on rooms")
#@jwt_required()
@blp.route("/api/room/<id>")
class Room(MethodView):
    def get(self, id):
        for room in rooms:
            if room["id"] == id:
                return jsonify(room)
        return jsonify({}), 404

#@jwt_required()
@blp.route("/api/my_rooms")
class AllRooms(MethodView):
    def post(self):
        user_rooms = []
        request_data = request.get_json()
        id = request_data["id"]
        for room in rooms:
            if room["user_id"] == id:
                user_rooms.append(room)
        if user_rooms:
            return jsonify(user_rooms), 200
        return jsonify({}), 404