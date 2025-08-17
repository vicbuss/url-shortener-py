import os

from flask import Flask

from src.routes.routes import redirect_controller_bp, url_controller_bp

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(
	__name__,
	template_folder=os.path.join(BASE_DIR, 'public', 'templates'),
	static_folder=os.path.join(BASE_DIR, 'public', 'static'),
)

app.register_blueprint(url_controller_bp)
app.register_blueprint(redirect_controller_bp)

if __name__ == '__main__':
	app.run(debug=True)
