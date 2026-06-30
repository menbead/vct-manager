# TODO:
# define functions for getting specific players, teams
# define functions for converting the results into json objects to pass back to godot
# create a python (flasK?) local server to use to create requests 

import sys
import json
import vlrdevapi as vlr

def main():
    args = sys.argv
    playerId = args[1]
    profile = vlr.players.profile(4)


    data = {
        "name": profile.handle,
        "realname": profile.real_name,
        "country": profile.country
    }

    print(profile.handle)


if __name__ == "__main__":
    main()