from flask import Blueprint

from src.controllers.url_controller import index, shorten

url_controller_bp = Blueprint("url_mapping", __name__)

url_controller_bp.route("/", methods=["GET"])(index)
url_controller_bp.route("/shorten", methods=["POST"])(shorten)