""" 
TODO:
- PRE FRANCHISING - get ONLY players from tier 1 international events as format is different
- POST FRANCHISING - get each TIER 1 TEAM for each year, including their data for each player for that year
- TIER 2 - get ONLY the teams who go into ascension (?)

- need to 

"""

import json
import vlrdevapi as vlr # type: ignore (stops warning :)

TEST_FILE_NAME = "test"

def main():
    print(f"Fetching events...")
    events = get_tier_one_events()
    print(f"{len(events)} events found.")
    print(f"Writing to file...")
    write_json_to_file(TEST_FILE_NAME, events)
    print(f"Saved to {TEST_FILE_NAME}.json")

def write_json_to_file(file, data):
    # from https://www.geeksforgeeks.org/python/saving-text-json-and-csv-to-a-file-in-python/
    filename = file + ".json"

    out_file = open(filename, "w") 
    json.dump(data, out_file, indent = 6) 
    
    out_file.close() 

def get_tier_one_events():
    events = []

    with open('eventids.txt', 'r') as file:
        for line in file:
            print(int(line.strip()))
            print(vlr.events.info(event_id = 353)).name
            print(vlr.events.info(event_id = int(line.strip())).name)
            events = events + vlr.events.info(event_id = int(line.strip()))
    
    trimmed_events = [
        {
            "id": e.id,
            "name": e.name,
            "start_date": e.start_date.isoformat() if e.start_date else None,
            "end_date": e.end_date.isoformat() if e.end_date else None,
        }
        for e in events
    ]

    return trimmed_events
    
# checks if the vlr api is working before we actually start scraping :)
if __name__ == "__main__" and vlr.check_status():
    print(f"VLR is up...")
    main()