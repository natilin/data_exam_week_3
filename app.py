from controller.player_controller import player_bluprint
from service.seed_service import seed_db


from flask import Flask, request, jsonify

from repository.json_repository import fighters
from routes.cat_controller import cat_bluprint
from routes.fighter_routes import fighters_bp

app = Flask(__name__)

@app.route('/<int:nati_id>', methods=['GET'])
def enosh(nati_id):
    return jsonify({ 'id': nati_id }), 200

@app.route('/search', methods=['GET'])
def enosh2():
    data = request.args.get("matanel")
    return jsonify({ 'data': data }), 200

if __name__ == '__main__':
    seed_db()
    app.register_blueprint(player_bluprint, url_prefix="/api/players")
    app.run(debug=True)


