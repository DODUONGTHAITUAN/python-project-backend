from src.services.user import create_user_service, get_all_users_servive


def create_user_controller(data):
    return create_user_service(data)


def get_all_users_controller(data):
    return get_all_users_servive(data)
