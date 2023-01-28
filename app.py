import sys

sys.path.append(".")  # so submodules can import app

from waitress import serve
from flask import Flask, jsonify, request
from db import rooms, users
from resources.user import blp as UserBlueprint
from resources.room import blp as RoomBlueprint
from flask_smorest import Api
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret12345'
jwt = JWTManager(app)
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Store_Rest_Api"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.0"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cds.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(UserBlueprint)
api.register_blueprint(RoomBlueprint)

app.debug = True

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_user


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
