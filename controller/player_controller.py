from flask import Blueprint, request, jsonify

player_bluprint = Blueprint("players", __name__)

@player_bluprint.route('/', methods=['GET'])
def search_player():
    position = request.args.get("position")
    jsonify({'success': True if mew else False }), 200
