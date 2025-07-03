# F1 Standings Visualiser

## Introduction

This is a command-line application to visualise Formula 1 drivers' and constructors' championship standings across a given season. The script fetches race data, applies historical points counting rules, and plots championship progressions as line charts.

## How It Works

The application uses FastF1 API to retrieve data on historic Formula 1 results. The user has to enter a year in the command line (denoted by "-y" or "--year"). It then processes the data for the selected year through and outputs two PNG files, one for the drivers' standings and one for the constructors' standings of that particular season (unless year is between 1950 and 1957, in which case one PNG file will be created, as the constructors' championship only began in 1958). These PNG files show the championship progression round by round, highlighting the how the championship battles unfolded.

## Implementation

The package consists of several .py files.

- **fetcher.py**: uses the [FastF1 API](https://docs.fastf1.dev/) to download the inputted season’s race schedule and results for a given year. A local cache is used to avoid repeatedly downloading the same data.
- **points_systems.py**: automatically applies the correct points rules depending pn the chosen year, including “best N results” rules that were used historically to calculate standings. See: [Formula 1 points scoring systems](https://en.wikipedia.org/wiki/List_of_Formula_One_World_Championship_points_scoring_systems#Points_scoring_systems)
- **standings.py**: processes each race’s results to build cumulative championship standings for both drivers and constructors, respecting the points system of that era.
- **visualiser.py**: plots the championship points progression over the course of the season for the top drivers and teams using matplotlib, highlighting title battles as they develop.
- **main.py**: generates line charts and saves them as PNG files in your working directory, named with the relevant year for easy reference.

The project has the dependencies [argparse](https://docs.python.org/3/library/argparse.html), [datetime](https://docs.python.org/3/library/datetime.html), [fastf1](https://docs.fastf1.dev/), [matplotlib](https://matplotlib.org/), [numpy](https://numpy.org/), [pandas](https://pandas.pydata.org/), and [plotly](https://plotly.com/python/) (optional).

## Features

- Retrieves race data via FastF1
- Supports historic “best N results” points systems (1950–present)
- Saves progression charts as PNG images
- Modular structure, making it easy to extend
- Error handling

## Installation

```
git clone https://github.com/karacabingol/f1-standings-visualiser
cd f1-standings-visualiser
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

To use the application, run the script as follows:

```
python main.py -y YEAR [-n TOP_N]
```

**Arguments**
    - "-y" / "--year": **(Required)** Year, i.e. the Formula 1 season
    - "-n" / "--top_n": Number of top competitors to plot in the graphs (default: 10)

***e.g.*** 

```
# without optional arguments
python main.py -y 2008

#with optional arguments
python main.py -y 2008 -n 6
```

Note: The constructors' championship began to be awarded starting from the 1958 season. Any season between 1950 and 1957 will create one PNG file, showing the drivers' championship progression.

## Challenges

Implementing the various points systems was a much bigger challenge than I expected. Only a fraction of each driver's and team's results counted towards the championships in many seasons, e.g. in 1960, only the 6 best results out of the 10 rounds counted towards the standings. Implementing this required some creative thinking. In such cases, the results are sorted after each round, and only the best (n) values are taken and summed to calculate the total points up to that point.

Some seasons had even more complicated points systems, dividing the season into two halves and taking the best (n) results out of each of those halves. For instance, the 1970 season had the best 6 results out of the first 7 races, followed by the best 5 results out of the last 6 races count. These points systems must have caused a lot of confusion for the viewers when working out the championship permutations back in the day!

## Future Improvements

Functionality for interactive plots can be added. I have added the framework to the code for this using plotly, however, it is commented out.