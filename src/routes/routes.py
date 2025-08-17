from flask import Blueprint

from src.controllers.url_controller import shorten
from src.controllers.redirect_controller import redirection, redirect_user

url_controller_bp = Blueprint("url_controller", __name__)

url_controller_bp.route("/", methods=["GET", "POST"])(shorten)

redirect_controller_bp = Blueprint("redirect_controller", __name__)
redirect_controller_bp.route("/<string:slug>", methods=["GET"])(redirection)
redirect_controller_bp.route("/redirect", methods=["POST"])(redirect_user)
