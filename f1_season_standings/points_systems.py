def get_count_best_n(year) -> str | int | None:

    # Determine how many best results count towards the drivers' standings for a given year.

    if 1950 <= year <= 1953:
        return 4
    elif year in [1954, 1955, 1956, 1957, 1959, 1961, 1962, 1966]:
        return 5
    elif year in [1958, 1960, 1963, 1964, 1965]:
        return 6
    elif year in [1967, 1969, 1971]:
        # best 5 out of first 6 races, best 4 out of last 5 races
        return 'split_5of6_4of5'
    elif year in [1968, 1972]:
        # best 5 out of first 6 races, best 5 out of last 6 races
        return 'split_5of6_5of6'
    elif year == 1970:
        # best 6 out of first 7 races, best 5 out of last 6 races
        return 'split_6of7_5of6'
    elif year in [1973, 1974]:
        # best 7 out of first 8 races, best 6 out of last 7 races
        return 'split_7of8_6of7'
    elif year == 1975:
        # best 6 out of first 7 races, best 6 out of last 7 races
        return 'split_6of7_6of7'
    elif year in [1976, 1978]:
        # best 7 out of first 8 races, best 7 out of last 8 races
        return 'split_7of8_7of8'
    elif year == 1977:
        # best 8 out of first 9 races, best 7 out of last 8 races
        return 'split_8of9_7of8'
    elif year == 1979:
        # best 4 out of first 7 races, best 4 out of last 8 races
        return 'split_4of7_4of8'
    elif year == 1980:
        # best 5 out of first 7 races, best 5 out of last 7 races
        return 'split_5of7_5of7'
    elif 1981 <= year <= 1990:
        return 11
    elif year >= 1991:
        return None
    else:
        return None
    
def get_team_count_best_n(year) -> str | int | None:
   
    # Determine how many best results count towards the CONSTRUCTORS' standings for a given year.
   
    if 1950 <= year <= 1957:
        return None  # no championship
    elif year in [1959, 1961, 1962, 1966]:
        return 5
    elif year in [1958, 1960, 1963, 1964, 1965]:
        return 6
    elif year in [1967, 1969, 1971]:
        return 'split_5of6_4of5'
    elif year in [1968, 1972]:
        return 'split_5of6_5of6'
    elif year == 1970:
        return 'split_6of7_5of6'
    elif year in [1973, 1974]:
        return 'split_7of8_6of7'
    elif year == 1975:
        return 'split_6of7_6of7'
    elif year in [1976, 1978]:
        return 'split_7of8_7of8'
    elif year == 1977:
        return 'split_8of9_7of8'
    elif year >= 1979:
        return None  # all results
    else:
        return None