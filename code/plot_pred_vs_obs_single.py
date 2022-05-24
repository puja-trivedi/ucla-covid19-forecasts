import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import os

if not os.path.exists("pred_vs_obs_plots_singleStart"):
    os.mkdir("pred_vs_obs_plots_singleStart")

hist = pd.read_csv('./historical_data/Texas_2021-11-26_2022-05-07_histData.csv',sep=',')
pred = pd.read_csv('./pred_results_state/Single_pred_state_0.7_Texas_END_DATE_2022-01-19_PRED_START_DATE_2022-01-26.csv',sep=',')


# PLOT NUMBER OF CASES 
fig = go.Figure()
fig.add_trace(go.Scatter(
                  x=hist['date'],
                    y=hist['daily_cases'],
                    name="Observed"
                    ))

fig.add_trace(go.Scatter(
                x=pred['Date'],
                    y=pred['pre_confirm_daily'],
                    name="Predicted"
                    ))

# fig.add_trace(go.Scatter(
#                 x=pred_04['Date'],
#                     y=pred_04['pre_confirm'],
#                     name="Predicted (DR: 0.4)"
#                     ))

# fig.add_trace(go.Scatter(
#                 x=pred_01['Date'],
#                     y=pred_01['pre_confirm'],
#                     name="Predicted (DR: 0.1)"
#                     ))

# fig.add_trace(go.Scatter(
#                 x=pred_001['Date'],
#                     y=pred_001['pre_confirm'],
#                     name="Predicted (DR: 0.01)"
#                     ))

# fig.add_trace(go.Scatter(
#                 x=pred_0001['Date'],
#                     y=pred_0001['pre_confirm'],
#                     name="Predicted (DR: 0.001)"
#                     ))
fig.update_layout(
    title="(Single Start) Observed vs Predicted:<br>Daily Number of COVID-19 Cases (Omicron) (Texas)",
    xaxis_title="Date",
    yaxis_title="Total Number of Covid Cases",
    legend_title="Legend",
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="Black"
    )
)
fig.show()
fig.write_image("pred_vs_obs_plots_singleStart/single_texas_2021-11-26_2022-05-07_cases_daily_2022-05-18.png")

###############################################################################

# PLOT NUMBER OF DEATHS 
fig_death = go.Figure()
fig_death.add_trace(go.Scatter(
                  x=hist['date'],
                    y=hist['daily_deaths'],
                    name="Observed"
                    ))
fig_death.add_trace(go.Scatter(
                x=pred['Date'],
                    y=pred['pre_fata_daily'],
                    name="Predicted"
                    ))


# fig_death.add_trace(go.Scatter(
#                 x=pred_04['Date'],
#                     y=pred_04['pre_fata'],
#                     name="Predicted (DR: 0.4)"
#                     ))

# fig_death.add_trace(go.Scatter(
#                 x=pred_01['Date'],
#                     y=pred_01['pre_fata'],
#                     name="Predicted (DR: 0.1)"
#                     ))

# fig_death.add_trace(go.Scatter(
#                 x=pred_001['Date'],
#                     y=pred_001['pre_fata'],
#                     name="Predicted (DR: 0.01)"
#                     ))

# fig_death.add_trace(go.Scatter(
#                 x=pred_0001['Date'],
#                     y=pred_0001['pre_fata'],
#                     name="Predicted (DR: 0.001)"
#                     ))

fig_death.update_layout(
    title="(Single Start)Observed vs Predicted:<br>Daily Number of COVID-19 Deaths (Omicron) (Texas)",
    xaxis_title="Date",
    yaxis_title="Total Number of Covid Deaths",
    legend_title="Legend",
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="Black"
    )
)
fig_death.show()
fig_death.write_image("pred_vs_obs_plots_singleStart/single_texas_2021-11-26_2022-05-07_deaths_daily_2022-05-18.png")

###############################################################################

# PLOT RATIO OF INC.DEATHS/INC.CASES
fig_ratio = go.Figure()
fig_ratio.add_trace(go.Scatter(
                  x=hist['date'],
                    y=hist['ratio_dth_case'],
                    name="Observed"
                    ))

fig_ratio.add_trace(go.Scatter(
                x=pred['Date'],
                    y=pred['pre_fata_daily']/pred['pre_confirm_daily'],
                    name="Predicted"
                    ))


fig_ratio.update_layout(
    title="(Single Start) Ratio of Inc.Deaths/Inc.Cases (Omicron) (Texas)",
    xaxis_title="Date",
    yaxis_title="inc.deaths/inc.cases",
    legend_title="Legend",
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="Black"
    )
)
fig_ratio.show()
fig_ratio.write_image("pred_vs_obs_plots_singleStart/single_texas_2021-11-26_2022-05-07_ratio_daily_2022-05-18.png")

