""" 
TODO:
- PRE FRANCHISING - get ONLY players from tier 1 international events as format is different
- POST FRANCHISING - get each TIER 1 TEAM for each year, including their data for each player for that year
- TIER 2 - get ONLY the teams who go into ascension (?)

- need to 

"""

import json
import vlrdevapi as vlr
import time

test_file_name = "test"

def main():
    print(f"Fetching events...")
    events = get_tier_one_events()
    print(f"{len(events)} events found.")

    trimmed_events = [
        {
            "id": e.id,
            "name": e.name,
            "start_date": e.start_date.isoformat() if e.start_date else None,
            "end_date": e.end_date.isoformat() if e.end_date else None,
        }
        for e in events
    ]

    print(f"Writing to file...")
    write_json_to_file(test_file_name, trimmed_events)
    print(f"Saved to {test_file_name}.json")


def write_json_to_file(file, data):
    # from https://www.geeksforgeeks.org/python/saving-text-json-and-csv-to-a-file-in-python/
    filename = file + ".json"

    out_file = open(filename, "w") 
    json.dump(data, out_file, indent = 6) 
    
    out_file.close() 

def get_tier_one_events():
    events = []
    page = 1
    # number of completed events maxes out at 268 as of 01/07/2026
    while len(events) < 263:
        events += vlr.events.list_events(tier="vct", page=page, status="completed")
        page += 1
                      
    vct_events = list(filter(event_filter_vct, events))
    return vct_events

# attempts to filter to just VCT events
def event_filter_vct(e):
    return "Stage 1" in e.name or "Stage 2" in e.name or "Kickoff" in e.name or "Valorant Masters" in e.name or "Valorant Champions" in e.name
    
# checks if the vlr api is working before we actually start scraping :)
if __name__ == "__main__" and vlr.check_status():
    print(f"VLR is up...")
    main()