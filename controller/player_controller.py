from dataclasses import asdict
from service.player_dto_service import get_players_by_pos_and_season_to_dto, get_players_by_pos_ato_dto

from flask import Blueprint, request, jsonify

player_bluprint = Blueprint("players", __name__)


@player_bluprint.route('/', methods=['GET'])
def search_player():
    position = request.args.get("position")
    season = request.args.get("season")
    if season:
        res = get_players_by_pos_and_season_to_dto(position, season.upper())
    else:
        res = get_players_by_pos_ato_dto(position)

    return jsonify([asdict(p) for p in res]), 200


