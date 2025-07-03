

def create_cumulative_standings_drivers(races_data, count_best_n = None) -> tuple[list[str], list[dict[str, float]]]:
    # Create cumulative standings for drivers based on points system for a given year.
    # If count_best_n is None, all results are counted.
    # If count_best_n is an integer, it specifies how many best results to count.

    
    if not races_data:
        raise ValueError("No race data provided")
    
    if isinstance(count_best_n, int):
        if count_best_n <= 0:
            raise ValueError("count_best_n must be positive")
    
    if isinstance(count_best_n, str) and count_best_n.startswith("split"):
        
        # (first part best results, first part length, second part best results, total races)
        split_rules = {
            "split_5of6_4of5": (5, 6, 4, 11),
            "split_5of6_5of6": (5, 6, 5, 12),
            "split_6of7_5of6": (6, 7, 5, 13),
            "split_7of8_6of7": (7, 8, 6, 15),
            "split_6of7_6of7": (6, 7, 6, 14),
            "split_7of8_7of8": (7, 8, 7, 16),
            "split_8of9_7of8": (8, 9, 7, 17),
            "split_4of7_4of8": (4, 7, 4, 15),
            "split_5of7_5of7": (5, 7, 5, 14)
        }

        if count_best_n not in split_rules:
            raise ValueError(f"Split rule not recognised")
        
        best_first, first_len, best_second, total_len = split_rules[count_best_n]

         # initialize standings
        driver_points = {}
        driver_all_points = {}
        races_list = []
        driver_standings = []
        
        for race_index, (race, results) in enumerate(races_data.items()):
            for driver, _, points in results:
                if driver not in driver_all_points:
                    driver_all_points[driver] = []
                driver_all_points[driver].append(points)
                
                # first chunk
                if race_index + 1 <= first_len:
                    selected_points = sorted(driver_all_points[driver][:first_len], reverse=True)[:best_first]
                # second chunk
                else:
                    first_chunk_points = sorted(driver_all_points[driver][:first_len], reverse=True)[:best_first]
                    second_chunk_points = sorted(driver_all_points[driver][first_len:], reverse=True)[:best_second]
                    selected_points = first_chunk_points + second_chunk_points
                
                driver_points[driver] = sum(selected_points)

            races_list.append(race)
            driver_standings.append(dict(driver_points))
        
        return races_list, driver_standings
    
    else:
        driver_points = {}
        driver_all_points = {}
        races_list = []
        driver_standings = []
        
        for race, results in races_data.items():
            for driver, _, points in results:
                if driver not in driver_points:
                    driver_points[driver] = 0
                    driver_all_points[driver] = []

                driver_all_points[driver].append(points)
                if count_best_n:
                    driver_points[driver] = sum(sorted(driver_all_points[driver], reverse = True)[:count_best_n])    
                else:
                    driver_points[driver] += points
            
            races_list.append(race)
            driver_standings.append(dict(driver_points))
        
        return races_list, driver_standings
    

def create_cumulative_standings_teams(races_data, count_best_n=None, year=None) -> tuple[list[str], list[dict[str, float]]]:
    if not races_data:
        raise ValueError("No race data provided")
    
    if year is None:
        raise ValueError("Year must be provided")

    if isinstance(count_best_n, int):
        if count_best_n <= 0:
            raise ValueError("count_best_n must be positive")

    # define split rules
    split_rules = {
        "split_5of6_4of5": (5, 6, 4, 11),
        "split_5of6_5of6": (5, 6, 5, 12),
        "split_6of7_5of6": (6, 7, 5, 13),
        "split_7of8_6of7": (7, 8, 6, 15),
        "split_6of7_6of7": (6, 7, 6, 14),
        "split_7of8_7of8": (7, 8, 7, 16),
        "split_8of9_7of8": (8, 9, 7, 17),
        "split_4of7_4of8": (4, 7, 4, 15),
        "split_5of7_5of7": (5, 7, 5, 14)
    }

    use_split = isinstance(count_best_n, str) and count_best_n in split_rules

    if use_split:
        best_first, first_len, best_second, total_len = split_rules[count_best_n]

    team_points = {}
    team_all_points = {}
    races_list = []
    team_standings = []

    for race_index, (race, results) in enumerate(races_data.items()):
        if year < 1979:
            # best finishing car only
            team_best_result = {}
            for _, team, points in results:
                if team not in team_best_result:
                    team_best_result[team] = points
                else:
                    team_best_result[team] = max(team_best_result[team], points)
            # store
            for team, best_points in team_best_result.items():
                if team not in team_all_points:
                    team_all_points[team] = []
                team_all_points[team].append(best_points)

                if use_split:
                    if race_index + 1 <= first_len:
                        selected_points = sorted(team_all_points[team][:first_len], reverse=True)[:best_first]
                    else:
                        first_chunk = sorted(team_all_points[team][:first_len], reverse=True)[:best_first]
                        second_chunk = sorted(team_all_points[team][first_len:], reverse=True)[:best_second]
                        selected_points = first_chunk + second_chunk
                    team_points[team] = sum(selected_points)
                elif isinstance(count_best_n, int):
                    team_points[team] = sum(sorted(team_all_points[team], reverse=True)[:count_best_n])
                else:
                    team_points[team] = sum(team_all_points[team])
        else:
            # after 1979 all cars count
            for _, team, points in results:
                if team not in team_all_points:
                    team_all_points[team] = []
                team_all_points[team].append(points)

                if use_split:
                    if race_index + 1 <= first_len:
                        selected_points = sorted(team_all_points[team][:first_len], reverse=True)[:best_first]
                    else:
                        first_chunk = sorted(team_all_points[team][:first_len], reverse=True)[:best_first]
                        second_chunk = sorted(team_all_points[team][first_len:], reverse=True)[:best_second]
                        selected_points = first_chunk + second_chunk
                    team_points[team] = sum(selected_points)
                elif isinstance(count_best_n, int):
                    team_points[team] = sum(sorted(team_all_points[team], reverse=True)[:count_best_n])
                else:
                    team_points[team] = sum(team_all_points[team])

        races_list.append(race)
        team_standings.append(dict(team_points))

    return races_list, team_standings