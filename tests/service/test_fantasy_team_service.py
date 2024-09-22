from service.fantasy_team_service import create_fantasy_team


def test_create_fantasy_team():
    new_team = create_fantasy_team({
        "team_name": "fantasya",
        "PG_player": "burksal01",
        "SG_player": "robinor01",
        "SF_player": "gordoaa01",
        "PF_player": "henryaa01",
        "C_player": "schofad01"

})
    assert new_team
