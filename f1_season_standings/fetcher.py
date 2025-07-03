import fastf1
from fastf1 import events
from pathlib import Path

def fetch_season_data(year, cache_dir = "f1_cache") -> dict[str, list[list[str | float]]]:
    Path(cache_dir).mkdir(parents=True, exist_ok=True)
    fastf1.Cache.enable_cache(cache_dir)

    try:
        schedule = events.get_event_schedule(year)
    except Exception as e:
        print(f"Error fetching schedule via FastF1: {e}")
        return {}
    
    results = {}
    for _, row in schedule.iterrows():
        race_name = row['EventName']
        round_num = row['RoundNumber']
        print(f"Loading results for {race_name} (round {round_num})...")

        try:
            session = fastf1.get_session(year, race_name, 'R')
            session.load(telemetry=False, laps=False, weather=False)
            res = session.results
        except Exception as e:
            print(f"Error loading result data: {e}")
            continue

        race_results = []
        for _, dr in res.iterrows():
            driver = dr['FullName']
            constructor = dr['TeamName']
            points = float(dr['Points'])
            race_results.append([driver, constructor, points])

        results[race_name] = race_results

    return results