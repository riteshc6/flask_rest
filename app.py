from flask import Flask
# Capital letter initials signify that a class is being imported
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)  # Creates an instance of Flask cass
api = Api(app)

users = [
    {
        "name" : "Ram",
        "age" : 24,
        "occupation" : "Manager"
    },
    {
        "name" : "Rohan",
        "age" : 32,
        "occupation" : "Data Analyst"
    },
    {
        "name" : "Raj",
        "age" : 30,
        "occupation" : "Backend Engineer"
    }
]

# Creating API endpoints by defining User resource class

class User(Resource):
    
    # Retrieve User Details
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "user not found", 404        

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if (name == user['name']):
                return f"User with name {name} already exists", 400

        user = {
            "name" : name,
            "age" : args["age"],
            "occupation" : args["occuption"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparser.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name" : args["user"],
            "age" : args["age"],
            "occupation" : args["occupation"]
        }
        users.append(user)
        return user, 201        


    def delete(self, name):         
        global users
        users = [user for user in users if user["name"] != name]
        return f"{name} is deleted.", 200

api.add_resource(User, "/user/<string:name>")
app.run(debug=True)    