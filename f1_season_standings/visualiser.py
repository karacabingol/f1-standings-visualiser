# import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np

TOP_N = 10  # Default number of top competitors to plot

def plot_championship_progression(races_list, standings_data, title, year, top_n=TOP_N,
                                figsize=(15, 8), rotation=45, colors=None):
    if not standings_data:
        print(f"No standings data available to plot.")
        return
    
    plt.figure(figsize=figsize)
    plt.style.use("tableau-colorblind10")

    colors = plt.cm.Set2(np.linspace(0, 1, top_n))
    # colors = sns.color_palette("husl", top_n)
    
    final_standings = standings_data[-1]
    top_competitors = sorted(final_standings.items(), key=lambda x: x[1], reverse=True)[:top_n]
    top_names = [x[0] for x in top_competitors]
    
    for idx, name in enumerate(top_names):
        points = [race_standing[name] if name in race_standing else 0 
                for race_standing in standings_data]
        plt.plot(races_list, points, marker='o', label=f"{name} ({final_standings[name]}pts)", 
                color=colors[idx], linewidth=2)
    
    plt.title(f"{title} - {year}", fontsize=16, pad=20)
    plt.xlabel('Races', fontsize=12)
    plt.ylabel('Points', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt



"""
def plot_championship_progression_plotly(races_list, standings_data, title, year, top_n = TOP_N) -> None:
    if not standings_data:
        print("No standings data to plot.")
        return
    
    final_standings = standings_data[-1]
    top_competitors = sorted(final_standings.items(), key=lambda x: x[1], reverse=True)[:top_n]
    top_names = [x[0] for x in top_competitors]
    
    fig = go.Figure()
    
    for name in top_names:
        points = [race_standing.get(name, 0) for race_standing in standings_data]
        fig.add_trace(go.Scatter(
            x=races_list,
            y=points,
            mode="lines+markers",
            name=f"{name} ({final_standings[name]} pts)"
        ))
    
    fig.update_layout(
        title=f"{title} - {year}",
        xaxis_title="Races",
        yaxis_title="Points",
        hovermode="x unified",
        template="plotly_dark"
    )
    
    fig.show()
"""

