from routes.user import create_user, get_users, delete_user, edit_user
class User_Controller:
    def create_user(self):
        return create_user()
    def get_user(self):
        return get_users()
    def delete_user(self):
        return delete_user()
    def edit_user(self):
        return edit_user()
    