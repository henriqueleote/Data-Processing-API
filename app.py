from flask import Flask

from data import DataAccessObject

app = Flask(__name__)

dao = DataAccessObject("data.json")