from flask import Blueprint, jsonify, request
from src.ultils.constants import methods, path

from src.controllers.user import create_user_controller, get_all_users_controller

user = Blueprint("user", __name__)


@user.route("/create", methods=["POST", "GET"])
def create_user():
    if request.method == "GET":
        return jsonify({"code": 200, "message": "OK"})
    """Get data from request client side"""
    data = request.get_json()
    print(data)
    return create_user_controller(data)


@user.route("/get-users", methods=["GET"])
def get_all_users():
    try:
        """Convert ImmutableMultiDict to dict"""
        data = request.args.to_dict(flat=True)
        return get_all_users_controller(data)
    except Exception as e:
        print(f"Error at get all user  router: {e}")
        return jsonify({"code": 3, "message": "Error when recieve data from client"})
