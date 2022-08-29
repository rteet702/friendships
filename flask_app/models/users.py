from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __repr__(self):
        return f'<User: {self.first_name}> Object'

    @classmethod
    def get_friendships(cls):
        query = """SELECT CONCAT_WS(' ', users.first_name, users.last_name) as User,CONCAT_WS(' ', users2.first_name, users2.last_name) as Friend FROM users
                LEFT JOIN friendships ON user_id = users.id or friend_id = users.id
                LEFT JOIN users as users2 ON (user_id = users2.id and users2.id <> users.id) or (friend_id = users2.id and users2.id <> users.id);"""
        return connectToMySQL('friendships_schema').query_db(query)

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        connectToMySQL('friendships_schema').query_db(query, data)