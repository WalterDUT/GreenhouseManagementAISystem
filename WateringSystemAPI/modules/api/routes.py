from flask import Flask, render_template, jsonify, Blueprint

from modules.database import collection as db
from bson.json_util import dumps
mod = Blueprint('api', __name__, template_folder='templates')
@mod.route('/')
def api():
    # return dumps(db.getAll())
    return "cc di t me"
