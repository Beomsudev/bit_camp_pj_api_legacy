from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from config import postgresqlConfig
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.user import UserRegister
