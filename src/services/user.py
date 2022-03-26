from flask import Response, json, jsonify
from bcrypt import hashpw, checkpw, gensalt
from src.models.user import User

from src import db

"""[POST]"""


def create_user_service(data):
    try:
        """Get Data"""
        fullName = data["fullName"]
        address = data["address"]
        email = data["email"]
        phonenumber = data["phonenumber"]
        password = data["password"]
        genderID = data["genderID"]
        roleID = data["roleID"]
        """Verify"""
        if (
            not fullName
            or not address
            or not email
            or not phonenumber
            or not password
            or not genderID
            or not roleID
        ):
            return jsonify({"code": 1, "message": "Missing required params"})
        """Handle data and return result"""

        """Hash password"""
        hashed = hashpw(password.encode("utf-8"), gensalt())

        """ Create new User"""
        newUser = User(fullName, genderID, address, phonenumber, email, hashed, roleID)

        # Insert new user
        db.session.add(newUser)
        db.session.commit()
        return jsonify({"code": 0, "message": "user has created"})
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Error from server"})


def formartUsers(usersRaw):
    users = []
    for item in usersRaw.items:
        user = {
            "id": item.id,
            "fullName": item.fullName,
            "genderID": item.genderID,
            "address": item.address,
            "phonenumber": item.phonenumber,
            "email": item.email,
            "roleID": item.roleID,
        }
        users.append(user)
    return users


"""[GET]"""


def get_all_users_servive(data):
    try:
        page = data["page"] or "1"
        per_page = data["per_page"] or "10"

        """Check digit"""
        if not page.isdigit() or not per_page.isdigit():
            page = 1
            per_page = 10
        else:
            page = int(page)
            per_page = int(per_page)
        usersRaw = User.query.paginate(per_page=per_page, page=page, error_out=True)
        print(usersRaw.pages)
        """Format data users"""
        users = formartUsers(usersRaw)

        """Send data to client"""
        return jsonify(
            {
                "data": {
                    "users": users,
                    "per_page": usersRaw.per_page,
                    "current_page": usersRaw.page,
                    "total_pages": usersRaw.pages,
                },
                "code": 0,
                "message": "Get all users success",
            }
        )
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Get all users fail"})
