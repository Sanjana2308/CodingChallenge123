class UserNotFound(Exception):
    def __init__(self, user_id):
        super().__init__(f"User with {user_id} not found")