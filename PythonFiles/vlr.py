# TODO:
# define functions for getting specific players, teams
# define functions for converting the results into json objects to pass back to godot
# create a python (flasK?) local server to use to create requests 

import sys
import json
import vlrdevapi as vlr
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/main')
def main():
    args = sys.argv
    playerId = args[1]
    profile = vlr.players.profile(4)

    data = {
        "name": profile.handle,
        "realname": profile.real_name,
        "country": profile.country
    }

    return f"TEST CASE: {profile.handle}"

@app.route('/player/<playerId>')
def get_player(playerId):
    p = vlr.players.profile(playerId)
    if p:
        return p.handle
    else:
        return f"ERROR: PLAYER {playerId} NOT FOUND"

if __name__ == "__main__":
    main()