from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __repr__(self):
        return f'<User: {self.first_name}> Object ID: {self.id}'

    @classmethod
    def get_friendships(cls):
        query = """SELECT CONCAT_WS(' ', users.first_name, users.last_name) as User,CONCAT_WS(' ', users2.first_name, users2.last_name) as Friend FROM users
                LEFT JOIN friendships ON user_id = users.id or friend_id = users.id
                LEFT JOIN users as users2 ON (user_id = users2.id and users2.id <> users.id) or (friend_id = users2.id and users2.id <> users.id);"""
        return connectToMySQL('friendships_schema').query_db(query)

    @classmethod
    def add_friendship(cls, data):
        test_query = "SELECT EXISTS( SELECT 1 FROM friendships WHERE (user_id = %(first_user)s AND friend_id = %(second_user)s) OR (user_id = %(second_user)s AND friend_id = %(first_user)s)) as exist;"
        query = "INSERT INTO friendships (user_id, friend_id) VALUES (%(first_user)s, %(second_user)s)"

        double_check = connectToMySQL('friendships_schema').query_db(test_query,data)
        if double_check[0]['exist'] == 0:
            print('Creating Entry.')
            connectToMySQL('friendships_schema').query_db(query, data)
        else:
            print('Entry already exists.')

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('friendships_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        connectToMySQL('friendships_schema').query_db(query, data)