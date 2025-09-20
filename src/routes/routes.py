from flask import Blueprint

from src.controllers.auth_controller import AuthController
from src.controllers.redirect_controller import RedirectController
from src.controllers.url_controller import URLController
from src.infrastructure.factories.service_factories import (
	make_auth_service,
	make_url_shortening_service,
	make_url_validation_service,
)

url_validation_service = make_url_validation_service()
url_shortening_service = make_url_shortening_service()
auth_service = make_auth_service()

url_controller_bp = Blueprint('url_controller', __name__)
url_controller = URLController(url_validation_service, url_shortening_service)
url_controller_bp.add_url_rule(
	'/', view_func=url_controller.shorten, methods=['GET', 'POST']
)

redirect_controller_bp = Blueprint('redirect_controller', __name__)
redirect_controller = RedirectController(url_shortening_service, url_validation_service)
redirect_controller_bp.add_url_rule(
	'/<string:slug>', view_func=redirect_controller.redirection, methods=['GET']
)
redirect_controller_bp.add_url_rule(
	'/redirect', view_func=redirect_controller.redirect_user, methods=['POST']
)

auth_controller_bp = Blueprint('auth_controller', __name__)
auth_controller = AuthController(auth_service)
auth_controller_bp.add_url_rule(
	'/register', view_func=auth_controller.register, methods=['GET', 'POST']
)
auth_controller_bp.add_url_rule(
	'/check-username',
	view_func=auth_controller.check_username,
	methods=['GET'],
)
auth_controller_bp.add_url_rule(
	'/login', view_func=auth_controller.login, methods=['GET', 'POST']
)
