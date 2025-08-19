from flask import redirect, render_template, request
from werkzeug.wrappers import Response


def redirection(slug: str) -> str:
	long_url = 'https://google.com'
	return render_template('redirection_confirmation.html', slug=slug, long_url=long_url)


def redirect_user() -> Response:
	slug = request.form['slug']
	long_url = 'https://google.com'
	return redirect(long_url)
