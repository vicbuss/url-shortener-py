from functools import wraps
from typing import Callable, TypeVar, Union

from flask import abort, redirect, session, url_for
from typing_extensions import ParamSpec
from werkzeug import Response

P = ParamSpec('P')
R = TypeVar('R')


def login_required(f: Callable[P, R]) -> Callable[P, Union[R, Response]]:
	@wraps(f)
	def decorated_function(*args: P.args, **kwargs: P.kwargs) -> Union[R, Response]:
		if 'user_id' not in session:
			return redirect(url_for('auth_controller.login'))
		return f(*args, **kwargs)

	return decorated_function


def admin_only(f: Callable[P, R]) -> Callable[P, Union[R, Response]]:
	@wraps(f)
	def decorated_function(*args: P.args, **kwargs: P.kwargs) -> Union[R, Response]:
		if session.get('role') != 'admin':
			return abort(403)
		return f(*args, **kwargs)

	return decorated_function
