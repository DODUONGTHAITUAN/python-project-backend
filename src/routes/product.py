from flask import Blueprint


product = Blueprint("product", __name__)


"""[GET] Get all products - pagnation"""


@product.route("/get-all-products", methods=["GET"])
def get_all_products():
    return "hello world"


"""[PUT] update product"""


@product.route("/update", methods=["PUT"])
def update_product():
    pass


"""[POST] create new Product"""


@product.route("/create", methods=["POST"])
def create_product():
    pass


"""[DELETE] delete product"""


@product.route("/delete", methods=["DELETE"])
def delete_product():
    pass
