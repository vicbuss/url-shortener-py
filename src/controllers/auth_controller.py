from typing import Union

from flask import (
	abort,
	flash,
	jsonify,
	redirect,
	render_template,
	request,
	session,
	url_for,
)
from werkzeug import Response

from src.services.auth_service import AuthenticationSevice


class AuthController:
	def __init__(self, auth_service: AuthenticationSevice) -> None:
		self.__auth_service = auth_service

	def register(self) -> Union[Response, str]:
		if request.method == 'POST':
			username = request.form['username'].strip()
			password = request.form['password'].strip()
			confirm_password = request.form['confirm_password'].strip()

			try:
				if password != confirm_password:
					abort(400)
				username_is_available = self.__auth_service.check_username_availability(
					username
				)
				if not username_is_available:
					abort(400)

				self.__auth_service.register(username=username, password=password)
				return redirect(url_for('auth_controller.login'))
			except Exception:
				abort(500)

		return render_template('register.html')

	def check_username(self) -> Response:
		username = request.args.get('username')

		if username is None:
			abort(400)

		username_is_available = self.__auth_service.check_username_availability(username)

		available = {'available': username_is_available}

		return jsonify(available)

	def login(self) -> Union[Response, str]:
		if request.method == 'POST':
			username = request.form['username'].strip()
			password = request.form['password'].strip()

			user = self.__auth_service.validate_credentials(
				username=username, password=password
			)

			if user:
				session['user_id'] = user.username
				session['role'] = user.role
				return redirect(url_for('url_controller.shorten'))
			else:
				flash('Invalid username or password', 'danger')

		return render_template('login.html')

	def logout(self) -> Response:
		session.clear()
		return redirect(url_for('auth_controller.login'))
