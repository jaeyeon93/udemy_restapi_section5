# -*- coding:utf-8 -*-

from flask import Flask #request
from flask_restful import Api #, Resource,reqparse
from flask_jwt import JWT #, jwt_required
from security import authenticate, identity
# resource는 api가 리턴하는 값들?로 생각할 수 있다
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'jaeyeon'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth
# jwt create an new endpoint?

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
