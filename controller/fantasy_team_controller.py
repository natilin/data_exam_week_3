from flask import Blueprint, request, jsonify
from service import fantasy_team_service
fantasy_team_bluprint = Blueprint("fantasy_team", __name__)


@fantasy_team_bluprint.route('/', methods=['POST'])
def create_fantasy_team():
    data = request.json
    new_team = fantasy_team_service.create_fantasy_team(data)
    if new_team:
        return jsonify(new_team), 201
    else:
        return jsonify("ERROR"), 400
