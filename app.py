from flask import Flask
from config import app, db
from controller.ativ_controller import routes

app.register_blueprint(routes)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)