class Users:
    def __init__(self, user_id, user_name, password, role):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.role = role

    # Getters
    def get_user_id(self):
        return self.user_id

    def get_user_name(self):
        return self.user_name

    def get_password(self):
        return self.password

    def get_role(self):
        return self.role

    # Setters
    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_password(self, password):
        self.password = password

    def set_role(self, role):
        self.role = role