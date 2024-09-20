from controller.player_controller import player_bluprint
from service.seed_service import seed_db
from flask import Flask, request, jsonify

app = Flask(__name__)

if __name__ == '__main__':
    seed_db()
    app.register_blueprint(player_bluprint, url_prefix="/api/players")
    app.run(debug=True)


