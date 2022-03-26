from flask import Blueprint, jsonify, request
from src.ultils.constants import methods, path

from src.controllers.user import (
    create_user_controller,
    delete_user_controller,
    get_all_users_controller,
    delete_user_controller,
    get_user_by_id_controller,
    update_user_controller,
)

user = Blueprint("user", __name__)

"""Create new User"""


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


"""Delete user [DELETE]"""


@user.route("/delete", methods=["DELETE"])
def delete_user():
    try:
        userID = request.args.get("id")
        return delete_user_controller(userID)
    except:
        return jsonify({"code": 2, "message": "Error from server"})

    try:
        """Convert ImmutableMultiDict to dict"""
        data = request.args.to_dict(flat=True)
        return get_all_users_controller(data)
    except Exception as e:
        print(f"Error at get all user  router: {e}")
        return jsonify({"code": 3, "message": "Error when recieve data from client"})


"""Get user by id user [GET]"""


@user.route("/get-by-id", methods=["GET"])
def get_user_by_id():
    try:
        userID = request.args.get("id")
        return get_user_by_id_controller(userID)
    except:
        return jsonify({"code": 2, "message": "Error from server"})


"""Update user by id user [GET]"""


@user.route("/update", methods=["PUT"])
def update_user():
    try:
        data = request.get_json()
        print(data)
        return update_user_controller(data)
    except:
        return jsonify({"code": 2, "message": "Error from server"})
