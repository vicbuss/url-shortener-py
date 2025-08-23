import os

from flask import Flask, render_template

from src.routes.routes import redirect_controller_bp, url_controller_bp

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(
	__name__,
	template_folder=os.path.join(BASE_DIR, 'public', 'templates'),
	static_folder=os.path.join(BASE_DIR, 'public', 'static'),
)

app.register_blueprint(url_controller_bp)
app.register_blueprint(redirect_controller_bp)


@app.errorhandler(404)
def handle_404(error: Exception) -> str:
	return render_template('error.html', code=404, message='Page Not Found')


@app.errorhandler(422)
def handle_422(error: Exception) -> str:
	return render_template('error.html', code=422, message='Unprocessable URL')


@app.errorhandler(500)
def handle_500(error: Exception) -> str:
	return render_template('error.html', code=500, message='Internal Server Error')


if __name__ == '__main__':
	app.run(debug=True)
