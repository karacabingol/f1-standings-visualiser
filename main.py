import argparse
import matplotlib.pyplot as plt
from f1_season_standings.fetcher import fetch_season_data
from f1_season_standings.points_systems import get_count_best_n, get_team_count_best_n
from f1_season_standings.standings import create_cumulative_standings_drivers, create_cumulative_standings_teams
from f1_season_standings.visualiser import plot_championship_progression

def generate_season_charts(year: int) -> None:
    print(f">>>> main.py has started <<<<")
    print(f"Generating charts for {year} season...")

    current_year = datetime.datetime.now().year
    if year < 1950 or year > current_year:
        print(f"Year {year} is out of range. Please enter a year between 1950 and {current_year}.")
        return
    
    constructors_valid = year >= 1958  # Constructors' championship started in 1958

    races_data = fetch_season_data(year)
    print(f"Fetched data: {len(races_data)} races")

    if not races_data:
        print(f"No data available for year {year}. Cannot generate charts")
        return

    count_best_n = get_count_best_n(year)
    team_count_best_n = get_team_count_best_n(year)
    print(f"Count best n: {count_best_n}, team best n: {team_count_best_n}")

    try:
        races_list, driver_standings = create_cumulative_standings_drivers(races_data, count_best_n)
        if constructors_valid:
            _, team_standings = create_cumulative_standings_teams(races_data, team_count_best_n, year)
        else:
            team_standings = None
        print("Standings created")
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Clear matplotlib state
    plt.clf()
    plt.cla()
    plt.close("all")

    # Plot and save driver championship
    plot_championship_progression(races_list, driver_standings,
                                  "F1 Driver Championship Progression", year)
    plt.savefig(f"{year}_driver_championship.png", bbox_inches="tight", dpi=300)
    plt.close()
    print("Driver championship chart saved")

    # Plot and save constructor championship
    if constructors_valid and team_standings:
        plot_championship_progression(races_list, team_standings,
                                    "F1 Constructor Championship Progression", year)
        plt.savefig(f"{year}_constructor_championship.png", bbox_inches="tight", dpi=300)
        plt.close()
        print("Constructor championship chart saved")


    # Plot interactive driver championship
    # plot_championship_progression(races_list, driver_standings, "F1 Driver Championship Progression", year)
    # Plot interactive constructor championship
    # plot_championship_progression(races_list, team_standings, "F1 Constructor Championship Progression", year)

def main() -> None:
    parser = argparse.ArgumentParser(description="Visualise Formula 1 driver or constructor standings for a season")
    parser.add_argument("-y", "--year", type=int, required=True, help="Enter a year to visualise, e.g. 1950")

    args = parser.parse_args()
    year = args.year

    try:
        generate_season_charts(year)
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")

if __name__ == "__main__":
    main()