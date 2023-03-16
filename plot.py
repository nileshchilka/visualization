import plotly.graph_objects as go
import pandas as pd

from read_data import moor_anchor_dfv2, imo_to_teu
from constants import colors_list, colors_teu, colors_dur

apmt_c = "#ff6441"
non_apmt_c = "royalblue"
total_c = "limegreen"

def vessel_dis_per():
    
    plot_df = pd.read_csv("data/Vessel_Distribution_Percentage.csv",header=[0],index_col=[0])

    fig = go.Figure(
        layout=go.Layout(
            height=500,
            title="Vessel Distribution (by TEU)  Percentage across terminals", barmode="relative",
            yaxis_showticklabels=True, yaxis_showgrid=False,
            yaxis_range=[0, plot_df.groupby(axis=1, level=0).sum().max().max() * 1.8],
            font=dict(size=10), legend_orientation="v", legend_x=1, legend_y=1,
            margin=dict(t=25)
        )
    )

    for j, col in enumerate(plot_df.columns):
        fig.add_bar(
            x=plot_df.index, y=plot_df[col], width=0.4, name=col,
            marker_line=dict(width=1, color="#333"), marker_color= colors_list[j],
            hovertemplate='%{y:.1f}%'
        )
    fig.update_layout(xaxis_title="Terminals", yaxis_title="Percentage", width=1000)
    
    return fig

def vessel_distribution_count():

    plot_df = pd.read_csv("data/Vessel_Distribution_Count.csv",header=[0],index_col=[0])

    fig = go.Figure(
        layout=go.Layout(
            height=500,
            title="Vessel Distribution (by TEU)  Count across terminals", barmode="relative",
            yaxis_showticklabels=True, yaxis_showgrid=False,
            yaxis_range=[0, plot_df.groupby(axis=1, level=0).sum().max().max() * 2.5],
            font=dict(size=10), legend_orientation="v", legend_x=1, legend_y=1,
            margin=dict(t=25)
        )
    )

    for j, col in enumerate(plot_df.columns):
        fig.add_bar(
            x=plot_df.index, y=plot_df[col], width=0.4, name=col,
            marker_line=dict(width=1, color="#333"), marker_color= colors_list[j],
        )
    fig.update_layout(xaxis_title="Terminals", yaxis_title="Count", width=1000)
    
    return fig

def per_of_vessels_based_on_teu():
    plot_df = pd.read_csv("data/Percentage_of_vessels_based_on_TEU.csv",header=[0,1],index_col=[0])*100

    # Create a figure with the right layout
    fig = go.Figure(
        layout=go.Layout(
            title="Percentage of vessels based on TEU\n APMT vs Non APMT",
            height=450, width=1000, barmode="relative",
            yaxis_showticklabels=True, yaxis_showgrid=False,
            yaxis_range=[0, plot_df.groupby(axis=1, level=0).sum().max().max() * 1.1],
            # Secondary y-axis overlayed on the primary one and not visible
            yaxis2=go.layout.YAxis(visible=False, matches="y", overlaying="y", anchor="x", ),
            font=dict(size=10), legend_orientation="v",
            # hovermode="x", # dict(b=0,t=10,l=0,r=10)
            margin=dict(t=25)
        )
    )

    for i, t in enumerate(colors_teu):
        for j, col in enumerate(plot_df[t].columns):
            if (plot_df[t][col] == 0).all():
                continue
            if t == "Non APMT":
                fig.add_bar(
                    x=plot_df.index, y=plot_df[t][col],
                    # Set the right yaxis depending on the selected product (from enumerate)
                    yaxis=f"y{i + 1}",
                    # Offset the bar trace, offset needs to match the width
                    # The values here are in milliseconds, 1billion ms is ~1/3 month
                    offsetgroup=str(i), offset=(i - 1) * 0.3, width=0.3, legendgroup=t,
                    legendgrouptitle_text=t, name=col, marker_pattern_shape="/", marker_color=colors_teu[t][col],
                    marker_line=dict(width=2, color="#333"),
                    hovertemplate='%{y:.1f}%'
                )
            else:
                fig.add_bar(
                    x=plot_df.index, y=plot_df[t][col],
                    # Set the right yaxis depending on the selected product (from enumerate)
                    yaxis=f"y{i + 1}",
                    # Offset the bar trace, offset needs to match the width
                    # The values here are in milliseconds, 1billion ms is ~1/3 month
                    offsetgroup=str(i), offset=(i - 1) * 0.3, width=0.3, legendgroup=t,
                    legendgrouptitle_text=t, name=col, marker_color=colors_teu[t][col],
                    marker_line=dict(width=2, color="#333"),
                    hovertemplate='%{y:.1f}%'
                )
    fig.update_layout(xaxis_title="Months", yaxis_title="Percentage", width=1000)
    
    return fig

def shipping_line_analysis():
    
    plot_df = pd.read_csv("data/Shipping_Line_Analysis.csv",header=[0],index_col=[0])

    fig = go.Figure(
        layout=go.Layout(
            title="Shipping Line Analysis", barmode="group",
            yaxis_showticklabels=True, yaxis_showgrid=False,
            yaxis_range=[0, plot_df.groupby(axis=1, level=0).sum().max().max() * 1.2],
            font=dict(size=10), legend_orientation="h", legend_x=0, legend_y=1,
            margin=dict(t=25)
        )
    )

    colors = {"APMT": apmt_c, "Non APMT": non_apmt_c}

    for j, col in enumerate(plot_df.columns):
        fig.add_bar(
            x=plot_df.index, y=plot_df[col], width=0.4, name=col,
            marker_line=dict(width=1, color="#333"), marker_color=colors[col],
            hovertemplate='%{y:.1f}%'
        )
    fig.update_layout(xaxis_title="Shipping Lines", yaxis_title="Percentage", width=1000)

    return fig

def percentage_of_vessels_not_anchored_before_serving():

    order = [2,6,7,1,5,4,3]
    len_data = []
    imo_data = []
    for lt, mon in zip(moor_anchor_dfv2["apmt_port_calls_anchor_data"].to_list(), list(moor_anchor_dfv2.index)):
        for imo_dur in lt[1:-1].split(", "):
            imo = int(imo_dur[2:-1].split("': ")[0])
            dur = round(float(imo_dur[2:-1].split("': ")[1]), 2)
            imo_data.append([imo, dur, mon])
        len_data.append(len(imo_data))

    imo_dur_mon_df = pd.DataFrame(imo_data)
    imo_dur_mon_df.columns = ["imo", "dur", "Month"]

    apmt_anchor_data = imo_dur_mon_df.merge(imo_to_teu, on="imo", how="left")

    len_data = []
    imo_data = []
    for lt, mon in zip(moor_anchor_dfv2["apmt_port_calls_moor_data"].to_list(), list(moor_anchor_dfv2.index)):
        for imo_dur in lt[1:-1].split(", "):
            imo = int(imo_dur[2:-1].split("': ")[0])
            dur = round(float(imo_dur[2:-1].split("': ")[1]), 2)
            imo_data.append([imo, dur, mon])
        len_data.append(len(imo_data))

    imo_dur_mon_df = pd.DataFrame(imo_data)
    imo_dur_mon_df.columns = ["imo", "dur", "Month"]

    apmt_moor_data = imo_dur_mon_df.merge(imo_to_teu, on="imo", how="left")

    plot_df = (apmt_moor_data.groupby('vesteu')['Month'].value_counts().unstack('vesteu').fillna(0) -
               apmt_anchor_data.groupby('vesteu')['Month'].value_counts().unstack('vesteu').fillna(0))
    plot_df["order"] = order
    plot_df = plot_df.sort_values("order").iloc[:, :-1]


    apmt_plot_df = (((plot_df.T / moor_anchor_dfv2["apmt_port_calls"]).T) * 100)
    apmt_plot_df = apmt_plot_df[['0-250', '250-1000', '1000-4000', '4000-8000', '8000-12000', '12000-16000', '16000-30000']]

    len_data = []
    imo_data = []
    for lt, mon in zip(moor_anchor_dfv2["non_apmt_port_calls_anchor_data"].to_list(), list(moor_anchor_dfv2.index)):
        for imo_dur in lt[1:-1].split(", "):
            imo = int(imo_dur[2:-1].split("': ")[0])
            dur = round(float(imo_dur[2:-1].split("': ")[1]), 2)
            imo_data.append([imo, dur, mon])
        len_data.append(len(imo_data))

    imo_dur_mon_df = pd.DataFrame(imo_data)
    imo_dur_mon_df.columns = ["imo", "dur", "Month"]

    non_apmt_anchor_data = imo_dur_mon_df.merge(imo_to_teu, on="imo", how="left")

    len_data = []
    imo_data = []
    for lt, mon in zip(moor_anchor_dfv2["non_apmt_port_calls_moor_data"].to_list(), list(moor_anchor_dfv2.index)):
        for imo_dur in lt[1:-1].split(", "):
            imo = int(imo_dur[2:-1].split("': ")[0])
            dur = round(float(imo_dur[2:-1].split("': ")[1]), 2)
            imo_data.append([imo, dur, mon])
        len_data.append(len(imo_data))

    imo_dur_mon_df = pd.DataFrame(imo_data)
    imo_dur_mon_df.columns = ["imo", "dur", "Month"]

    non_apmt_moor_data = imo_dur_mon_df.merge(imo_to_teu, on="imo", how="left")

    plot_df = (non_apmt_moor_data.groupby('vesteu')['Month'].value_counts().unstack('vesteu').fillna(0) -
               non_apmt_anchor_data.groupby('vesteu')['Month'].value_counts().unstack('vesteu').fillna(0))

    plot_df["order"] = order
    plot_df = plot_df.sort_values("order").iloc[:, :-1]

    non_apmt_plot_df = ((plot_df.T / moor_anchor_dfv2["non_apmt_port_calls"]).T) * 100
    non_apmt_plot_df = non_apmt_plot_df[
        ['0-250', '250-1000', '1000-4000', '4000-8000', '8000-12000', '12000-16000', '16000-30000']]

    plot_df = pd.concat([apmt_plot_df, non_apmt_plot_df], axis=1, keys=["APMT", "Non APMT"])

    # Create a figure with the right layout
    fig = go.Figure(
        layout=go.Layout(
            title="Percentage of vessels not anchored before serving\n APMT vs Non APMT",
            height=500, width=900, barmode="relative",
            yaxis_showticklabels=True, yaxis_showgrid=False,
            yaxis_range=[0, plot_df.groupby(axis=1, level=0).sum().max().max() * 1.1],
            # Secondary y-axis overlayed on the primary one and not visible
            yaxis2=go.layout.YAxis(visible=False, matches="y", overlaying="y", anchor="x", ),
            font=dict(size=10), legend_orientation="v",
            margin=dict(t=25)
        )
    )

    # Add the traces
    for i, t in enumerate(colors_teu):
        for j, col in enumerate(plot_df[t].columns):
            if (plot_df[t][col] == 0).all():
                continue
            if t == "Non APMT":
                fig.add_bar(
                    x=plot_df.index, y=plot_df[t][col],
                    # Set the right yaxis depending on the selected product (from enumerate)
                    yaxis=f"y{i + 1}",
                    # Offset the bar trace, offset needs to match the width
                    # The values here are in milliseconds, 1billion ms is ~1/3 month
                    offsetgroup=str(i), offset=(i - 1) * 0.3, width=0.3, legendgroup=t,
                    legendgrouptitle_text=t, name=col, marker_pattern_shape="/", marker_color=colors_teu[t][col],
                    marker_line=dict(width=2, color="#333"),
                    hovertemplate='%{y:.1f}%'
                )
            else:
                fig.add_bar(
                    x=plot_df.index, y=plot_df[t][col],
                    # Set the right yaxis depending on the selected product (from enumerate)
                    yaxis=f"y{i + 1}",
                    # Offset the bar trace, offset needs to match the width
                    # The values here are in milliseconds, 1billion ms is ~1/3 month
                    offsetgroup=str(i), offset=(i - 1) * 0.3, width=0.3, legendgroup=t,
                    legendgrouptitle_text=t, name=col, marker_color=colors_teu[t][col],
                    marker_line=dict(width=2, color="#333"),
                    hovertemplate='%{y:.1f}%'
                )
    fig.update_layout(xaxis_title="Months", yaxis_title="Percentage", width=1000)

    return fig

def percentage_of_vessels_anchored_before_serving():


    len_data = []
    imo_data = []
    for lt,mon in zip(moor_anchor_dfv2["apmt_port_calls_anchor_data"].to_list(),list(moor_anchor_dfv2.index)):
        for imo_dur in lt[1:-1].split(", "):
            imo = int(imo_dur[2:-1].split("': ")[0])
            dur = round(float(imo_dur[2:-1].split("': ")[1]),2)
            imo_data.append([imo,dur,mon])
        len_data.append(len(imo_data))

    imo_dur_mon_df = pd.DataFrame(imo_data)
    imo_dur_mon_df.columns = ["imo","dur","Month"]

    apmt_anchor_data = imo_dur_mon_df.merge(imo_to_teu,on="imo",how="left")

    len_data = []
    imo_data = []
    for lt,mon in zip(moor_anchor_dfv2["apmt_port_calls_moor_data"].to_list(),list(moor_anchor_dfv2.index)):
        for imo_dur in lt[1:-1].split(", "):
            imo = int(imo_dur[2:-1].split("': ")[0])
            dur = round(float(imo_dur[2:-1].split("': ")[1]),2)
            imo_data.append([imo,dur,mon])
        len_data.append(len(imo_data))

    imo_dur_mon_df = pd.DataFrame(imo_data)
    imo_dur_mon_df.columns = ["imo","dur","Month"]

    apmt_moor_data = imo_dur_mon_df.merge(imo_to_teu,on="imo",how="left")

    plot_df = apmt_anchor_data.groupby('vesteu')['Month'].value_counts().unstack('vesteu').fillna(0)
    plot_df["order"] = [2,6,7,1,5,4,3]
    plot_df = plot_df.sort_values("order").iloc[:,:-1]
    
    plot_df = plot_df.T
    plot_df["order"] = [1,3,6,7,2,4,5]
    plot_df = plot_df.sort_values("order").iloc[:,:-1]
    plot_df = plot_df.T

    apmt_plot_df = (((plot_df.T / moor_anchor_dfv2["apmt_port_calls"]).T)*100)

    len_data = []
    imo_data = []
    for lt,mon in zip(moor_anchor_dfv2["non_apmt_port_calls_anchor_data"].to_list(),list(moor_anchor_dfv2.index)):
        for imo_dur in lt[1:-1].split(", "):
            imo = int(imo_dur[2:-1].split("': ")[0])
            dur = round(float(imo_dur[2:-1].split("': ")[1]),2)
            imo_data.append([imo,dur,mon])
        len_data.append(len(imo_data))

    imo_dur_mon_df = pd.DataFrame(imo_data)
    imo_dur_mon_df.columns = ["imo","dur","Month"]

    non_apmt_anchor_data = imo_dur_mon_df.merge(imo_to_teu,on="imo",how="left")

    len_data = []
    imo_data = []
    for lt,mon in zip(moor_anchor_dfv2["non_apmt_port_calls_moor_data"].to_list(),list(moor_anchor_dfv2.index)):
        for imo_dur in lt[1:-1].split(", "):
            imo = int(imo_dur[2:-1].split("': ")[0])
            dur = round(float(imo_dur[2:-1].split("': ")[1]),2)
            imo_data.append([imo,dur,mon])
        len_data.append(len(imo_data))

    imo_dur_mon_df = pd.DataFrame(imo_data)
    imo_dur_mon_df.columns = ["imo","dur","Month"]

    non_apmt_moor_data = imo_dur_mon_df.merge(imo_to_teu,on="imo",how="left")

    plot_df = non_apmt_anchor_data.groupby('vesteu')['Month'].value_counts().unstack('vesteu').fillna(0)
    plot_df["order"] = [2,6,7,1,5,4,3]
    plot_df = plot_df.sort_values("order").iloc[:,:-1]
    
    plot_df = plot_df.T
    plot_df["order"] = [1,3,6,7,2,4,5]
    plot_df = plot_df.sort_values("order").iloc[:,:-1]
    plot_df = plot_df.T

    non_apmt_plot_df = (((plot_df.T / moor_anchor_dfv2["non_apmt_port_calls"]).T)*100)

    plot_df = pd.concat([apmt_plot_df, non_apmt_plot_df], axis=1, keys=["APMT", "Non APMT"])

    # Create a figure with the right layout
    fig = go.Figure(
        layout=go.Layout(
            title="Percentage of vessels not anchored before serving\n APMT vs Non APMT",
            height=500, width=900, barmode="relative",
            yaxis_showticklabels=True, yaxis_showgrid=False,
            yaxis_range=[0, plot_df.groupby(axis=1, level=0).sum().max().max() * 1.1],
            # Secondary y-axis overlayed on the primary one and not visible
            yaxis2=go.layout.YAxis(visible=False, matches="y", overlaying="y", anchor="x", ),
            font=dict(size=10), legend_orientation="v",
            margin=dict(t=25)
        )
    )

    # Add the traces
    for i, t in enumerate(colors_teu):
        for j, col in enumerate(plot_df[t].columns):
            if (plot_df[t][col] == 0).all():
                continue
            if t == "Non APMT":
                fig.add_bar(
                    x=plot_df.index, y=plot_df[t][col],
                    # Set the right yaxis depending on the selected product (from enumerate)
                    yaxis=f"y{i + 1}",
                    # Offset the bar trace, offset needs to match the width
                    # The values here are in milliseconds, 1billion ms is ~1/3 month
                    offsetgroup=str(i), offset=(i - 1) * 0.3, width=0.3, legendgroup=t,
                    legendgrouptitle_text=t, name=col, marker_pattern_shape="/", marker_color=colors_teu[t][col],
                    marker_line=dict(width=2, color="#333"),
                    hovertemplate='%{y:.1f}%'
                )
            else:
                fig.add_bar(
                    x=plot_df.index, y=plot_df[t][col],
                    # Set the right yaxis depending on the selected product (from enumerate)
                    yaxis=f"y{i + 1}",
                    # Offset the bar trace, offset needs to match the width
                    # The values here are in milliseconds, 1billion ms is ~1/3 month
                    offsetgroup=str(i), offset=(i - 1) * 0.3, width=0.3, legendgroup=t,
                    legendgrouptitle_text=t, name=col, marker_color=colors_teu[t][col],
                    marker_line=dict(width=2, color="#333"),
                    hovertemplate='%{y:.1f}%'
                )
    fig.update_layout(xaxis_title="Months", yaxis_title="Percentage", width=1000)

    return fig

def percentage_of_vessels_which_took_longer_time_at_mooring():

    non_apmt_full_lt = []
    for lt in moor_anchor_dfv2["non_apmt_port_calls_moor_data"].apply(lambda x: preprocess(x)).to_list():
        non_apmt_full_lt.append([round(float(dur), 2) for dur in lt])

    apmt_full_lt = []
    for lt in moor_anchor_dfv2["apmt_port_calls_moor_data"].apply(lambda x: preprocess(x)).to_list():
        apmt_full_lt.append([round(float(dur), 2) for dur in lt])

    full_lt = [j for i in apmt_full_lt for j in i] + [j for i in non_apmt_full_lt for j in i]
    full_lt_ser = pd.Series(full_lt)

    Q1 = full_lt_ser.quantile(0.25)
    Q3 = full_lt_ser.quantile(0.75)
    IQR = Q3 - Q1
    # print(Q3 + 1.5 * IQR)
    Data = {"July": {}, "August": {}, "September": {}, "October": {}, "November": {}, "December": {}, "January": {}}
    for i, mon in zip(range(len(apmt_full_lt)), Data):
        full_lt_i = apmt_full_lt[i] + non_apmt_full_lt[i]
        full_lt_i_ser = pd.Series(full_lt_i)
        apmt_full_lt_ser = pd.Series(apmt_full_lt[i])
        non_apmt_full_lt_ser = pd.Series(non_apmt_full_lt[i])
        Data[mon]["Total"] = len(full_lt_i_ser[full_lt_i_ser > (Q3 + 1.5 * IQR)]) / len(full_lt_i_ser) * 100
        Data[mon]["APMT"] = len(apmt_full_lt_ser[apmt_full_lt_ser > (Q3 + 1.5 * IQR)]) / len(apmt_full_lt_ser) * 100
        Data[mon]["Non APMT"] = len(non_apmt_full_lt_ser[non_apmt_full_lt_ser > (Q3 + 1.5 * IQR)]) / len(
            non_apmt_full_lt_ser) * 100

    plot_df = pd.DataFrame(Data).T[["APMT", "Non APMT"]]

    fig = go.Figure(
        layout=go.Layout(
            title="Percentage of vessels which took longer time at Mooring", barmode="group",
            yaxis_showticklabels=True, yaxis_showgrid=False,
            yaxis_range=[0, plot_df.groupby(axis=1, level=0).sum().max().max() * 1.1],
            font=dict(size=10), legend_orientation="h", legend_x=0, legend_y=1,
            margin=dict(t=25)
        )
    )

    colors = {"APMT": apmt_c, "Non APMT": non_apmt_c}

    for j, col in enumerate(plot_df.columns):
        fig.add_bar(
            x=plot_df.index, y=plot_df[col], width=0.4, name=col,
            marker_line=dict(width=1, color="#333"), marker_color=colors[col],
            hovertemplate='%{y:.1f}%'
        )
    fig.add_scatter(x=pd.DataFrame(Data).T["Total"].index, y=pd.DataFrame(Data).T["Total"].values, name="Average",
                    marker_color=total_c, hovertemplate='%{y:.1f}%')
    fig.update_layout(xaxis_title="Months", yaxis_title="Percentage", width=1000)

    return fig

def percentage_of_vessels_which_took_longer_time_at_anchor():

    non_apmt_full_lt = []
    for lt in moor_anchor_dfv2["non_apmt_port_calls_anchor_data"].apply(lambda x: preprocess(x)).to_list():
        non_apmt_full_lt.append([round(float(dur), 2) for dur in lt])

    apmt_full_lt = []
    for lt in moor_anchor_dfv2["apmt_port_calls_anchor_data"].apply(lambda x: preprocess(x)).to_list():
        apmt_full_lt.append([round(float(dur), 2) for dur in lt])

    full_lt = [j for i in apmt_full_lt for j in i] + [j for i in non_apmt_full_lt for j in i]
    full_lt_ser = pd.Series(full_lt)

    Q1 = full_lt_ser.quantile(0.25)
    Q3 = full_lt_ser.quantile(0.75)
    IQR = Q3 - Q1
    # print(Q3 + 1.5 * IQR)
    Data = {"July": {}, "August": {}, "September": {}, "October": {}, "November": {}, "December": {}, "January": {}}
    for i, mon in zip(range(len(apmt_full_lt)), Data):
        full_lt_i = apmt_full_lt[i] + non_apmt_full_lt[i]
        full_lt_i_ser = pd.Series(full_lt_i)
        apmt_full_lt_ser = pd.Series(apmt_full_lt[i])
        non_apmt_full_lt_ser = pd.Series(non_apmt_full_lt[i])
        Data[mon]["Total"] = len(full_lt_i_ser[full_lt_i_ser > (Q3 + 1.5 * IQR)]) / len(full_lt_i_ser) * 100
        Data[mon]["APMT"] = len(apmt_full_lt_ser[apmt_full_lt_ser > (Q3 + 1.5 * IQR)]) / len(apmt_full_lt_ser) * 100
        Data[mon]["Non APMT"] = len(non_apmt_full_lt_ser[non_apmt_full_lt_ser > (Q3 + 1.5 * IQR)]) / len(
            non_apmt_full_lt_ser) * 100

    plot_df = pd.DataFrame(Data).T[["APMT", "Non APMT"]]

    fig = go.Figure(
        layout=go.Layout(
            title="Percentage of vessels which took longer time at Anchor", barmode="group",
            yaxis_showticklabels=True, yaxis_showgrid=False,
            yaxis_range=[0, plot_df.groupby(axis=1, level=0).sum().max().max() * 1.1],
            font=dict(size=10), legend_orientation="h", legend_x=0, legend_y=1,
            margin=dict(t=25)
        )
    )

    colors = {"APMT": apmt_c, "Non APMT": non_apmt_c}

    for j, col in enumerate(plot_df.columns):
        fig.add_bar(
            x=plot_df.index, y=plot_df[col], width=0.4, name=col,
            marker_line=dict(width=1, color="#333"), marker_color=colors[col],
            hovertemplate='%{y:.1f}%'
        )
    fig.add_scatter(x=pd.DataFrame(Data).T["Total"].index, y=pd.DataFrame(Data).T["Total"].values, name="Average",
                    marker_color=total_c, hovertemplate='%{y:.1f}%')
    fig.update_layout(xaxis_title="Months", yaxis_title="Percentage", width=1000)

    return fig

def percentage_vessels_not_anchored_before_serving_line():
    fig = go.Figure(
        layout=go.Layout(
            title="Percentage of vessels which took longer time at Anchor",
            yaxis_showticklabels=True, yaxis_showgrid=False,
            font=dict(size=10), legend_orientation="h", legend_x=0, legend_y=1,
            margin=dict(t=25)
        )
    )

    fig.add_scatter(x=moor_anchor_dfv2["total_instantly_served_per"].index, y=moor_anchor_dfv2["total_instantly_served_per"].values, name="Average",
                    marker_color=total_c, hovertemplate='%{y:.1f}%')
    fig.add_scatter(x=moor_anchor_dfv2["apmt_instantly_served_per"].index,
                    y=moor_anchor_dfv2["apmt_instantly_served_per"].values, name="APMT",
                    marker_color=apmt_c, hovertemplate='%{y:.1f}%')
    fig.add_scatter(x=moor_anchor_dfv2["non_apmt_instantly_served_per"].index,
                    y=moor_anchor_dfv2["non_apmt_instantly_served_per"].values, name="Non APMT",
                    marker_color=non_apmt_c, hovertemplate='%{y:.1f}%')

    fig.update_layout(xaxis_title="Months", yaxis_title="Percentage", width=1000)
    
    return fig

def anchor_duration_distribution():

    non_apmt_full_lt = {}
    for lt, mon in zip(moor_anchor_dfv2["non_apmt_port_calls_anchor_data"].apply(lambda x: preprocess(x)).to_list(),
                       list(moor_anchor_dfv2.index)):
        non_apmt_full_lt[mon] = [round(float(dur), 2) for dur in lt]

    apmt_full_lt = {}
    for lt, mon in zip(moor_anchor_dfv2["apmt_port_calls_anchor_data"].apply(lambda x: preprocess(x)).to_list(),
                       list(moor_anchor_dfv2.index)):
        apmt_full_lt[mon] = [round(float(dur), 2) for dur in lt]

    apmt_plot_df = pd.DataFrame([apmt_full_lt]).T
    non_apmt_plot_df = pd.DataFrame([non_apmt_full_lt]).T

    apmt_plot_df["0-10"] = apmt_plot_df[0].apply(
        lambda x: (len(list(filter(lambda y: True if y < 10 else False, [float(val) for val in x]))) / len(x)) * 100)
    apmt_plot_df["10-20"] = apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 10 and y < 20 else False, [float(val) for val in x]))) / len(x)) * 100)
    apmt_plot_df["20-30"] = apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 20 and y < 30 else False, [float(val) for val in x]))) / len(x)) * 100)
    apmt_plot_df["30-40"] = apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 30 and y < 40 else False, [float(val) for val in x]))) / len(x)) * 100)
    apmt_plot_df["40-50"] = apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 40 and y < 50 else False, [float(val) for val in x]))) / len(x)) * 100)
    apmt_plot_df["50-60"] = apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 50 and y < 60 else False, [float(val) for val in x]))) / len(x)) * 100)
    apmt_plot_df["60-70"] = apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 60 and y < 70 else False, [float(val) for val in x]))) / len(x)) * 100)
    apmt_plot_df["70+"] = apmt_plot_df[0].apply(
        lambda x: (len(list(filter(lambda y: True if y >= 70 else False, [float(val) for val in x]))) / len(x)) * 100)

    non_apmt_plot_df["0-10"] = non_apmt_plot_df[0].apply(
        lambda x: (len(list(filter(lambda y: True if y < 10 else False, [float(val) for val in x]))) / len(x)) * 100)
    non_apmt_plot_df["10-20"] = non_apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 10 and y < 20 else False, [float(val) for val in x]))) / len(x)) * 100)
    non_apmt_plot_df["20-30"] = non_apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 20 and y < 30 else False, [float(val) for val in x]))) / len(x)) * 100)
    non_apmt_plot_df["30-40"] = non_apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 30 and y < 40 else False, [float(val) for val in x]))) / len(x)) * 100)
    non_apmt_plot_df["40-50"] = non_apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 40 and y < 50 else False, [float(val) for val in x]))) / len(x)) * 100)
    non_apmt_plot_df["50-60"] = non_apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 50 and y < 60 else False, [float(val) for val in x]))) / len(x)) * 100)
    non_apmt_plot_df["60-70"] = non_apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 60 and y < 70 else False, [float(val) for val in x]))) / len(x)) * 100)
    non_apmt_plot_df["70+"] = non_apmt_plot_df[0].apply(
        lambda x: (len(list(filter(lambda y: True if y >= 70 else False, [float(val) for val in x]))) / len(x)) * 100)

    plot_df = pd.concat([apmt_plot_df.drop(0, axis=1), non_apmt_plot_df.drop(0, axis=1)], axis=1,
                        keys=["APMT", "Non APMT"])

    # Create a figure with the right layout
    fig = go.Figure(
        layout=go.Layout(
            title="Anchor Duration Distribution (in hrs) \n APMT vs Non APMT",
            height=500, width=1000, barmode="relative",
            yaxis_showticklabels=True, yaxis_showgrid=False,
            yaxis_range=[0, plot_df.groupby(axis=1, level=0).sum().max().max() * 1.1],
            # Secondary y-axis overlayed on the primary one and not visible
            yaxis2=go.layout.YAxis(visible=False, matches="y", overlaying="y", anchor="x", ),
            font=dict(size=10), legend_orientation="v",
            margin=dict(t=25)
        )
    )

    for i, t in enumerate(colors_dur):
        for j, col in enumerate(plot_df[t].columns):
            if (plot_df[t][col] == 0).all():
                continue
            if t == "Non APMT":
                fig.add_bar(
                    x=plot_df.index, y=plot_df[t][col],
                    # Set the right yaxis depending on the selected product (from enumerate)
                    yaxis=f"y{i + 1}",
                    # Offset the bar trace, offset needs to match the width
                    # The values here are in milliseconds, 1billion ms is ~1/3 month
                    offsetgroup=str(i), offset=(i - 1) * 0.3, width=0.3, legendgroup=t,
                    legendgrouptitle_text=t, name=col, marker_pattern_shape="/", marker_color=colors_dur[t][col],
                    marker_line=dict(width=2, color="#333"),
                    hovertemplate='%{y:.1f}%'
                )
            else:
                fig.add_bar(
                    x=plot_df.index, y=plot_df[t][col],
                    # Set the right yaxis depending on the selected product (from enumerate)
                    yaxis=f"y{i + 1}",
                    # Offset the bar trace, offset needs to match the width
                    # The values here are in milliseconds, 1billion ms is ~1/3 month
                    offsetgroup=str(i), offset=(i - 1) * 0.3, width=0.3, legendgroup=t,
                    legendgrouptitle_text=t, name=col, marker_color=colors_dur[t][col],
                    marker_line=dict(width=2, color="#333"),
                    hovertemplate='%{y:.1f}%'
                )
    fig.update_layout(xaxis_title="Months", yaxis_title="Percentage", width=900)

    return fig

def mooring_duration_distribution():

    non_apmt_full_lt = {}
    for lt, mon in zip(moor_anchor_dfv2["non_apmt_port_calls_moor_data"].apply(lambda x: preprocess(x)).to_list(),
                       list(moor_anchor_dfv2.index)):
        non_apmt_full_lt[mon] = [round(float(dur), 2) for dur in lt]

    apmt_full_lt = {}
    for lt, mon in zip(moor_anchor_dfv2["apmt_port_calls_moor_data"].apply(lambda x: preprocess(x)).to_list(),
                       list(moor_anchor_dfv2.index)):
        apmt_full_lt[mon] = [round(float(dur), 2) for dur in lt]

    apmt_plot_df = pd.DataFrame([apmt_full_lt]).T
    non_apmt_plot_df = pd.DataFrame([non_apmt_full_lt]).T

    apmt_plot_df["0-10"] = apmt_plot_df[0].apply(
        lambda x: (len(list(filter(lambda y: True if y < 10 else False, [float(val) for val in x]))) / len(x)) * 100)
    apmt_plot_df["10-20"] = apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 10 and y < 20 else False, [float(val) for val in x]))) / len(x)) * 100)
    apmt_plot_df["20-30"] = apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 20 and y < 30 else False, [float(val) for val in x]))) / len(x)) * 100)
    apmt_plot_df["30-40"] = apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 30 and y < 40 else False, [float(val) for val in x]))) / len(x)) * 100)
    apmt_plot_df["40-50"] = apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 40 and y < 50 else False, [float(val) for val in x]))) / len(x)) * 100)
    apmt_plot_df["50-60"] = apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 50 and y < 60 else False, [float(val) for val in x]))) / len(x)) * 100)
    apmt_plot_df["60-70"] = apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 60 and y < 70 else False, [float(val) for val in x]))) / len(x)) * 100)
    apmt_plot_df["70+"] = apmt_plot_df[0].apply(
        lambda x: (len(list(filter(lambda y: True if y >= 70 else False, [float(val) for val in x]))) / len(x)) * 100)

    non_apmt_plot_df["0-10"] = non_apmt_plot_df[0].apply(
        lambda x: (len(list(filter(lambda y: True if y < 10 else False, [float(val) for val in x]))) / len(x)) * 100)
    non_apmt_plot_df["10-20"] = non_apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 10 and y < 20 else False, [float(val) for val in x]))) / len(x)) * 100)
    non_apmt_plot_df["20-30"] = non_apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 20 and y < 30 else False, [float(val) for val in x]))) / len(x)) * 100)
    non_apmt_plot_df["30-40"] = non_apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 30 and y < 40 else False, [float(val) for val in x]))) / len(x)) * 100)
    non_apmt_plot_df["40-50"] = non_apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 40 and y < 50 else False, [float(val) for val in x]))) / len(x)) * 100)
    non_apmt_plot_df["50-60"] = non_apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 50 and y < 60 else False, [float(val) for val in x]))) / len(x)) * 100)
    non_apmt_plot_df["60-70"] = non_apmt_plot_df[0].apply(lambda x: (len(list(
        filter(lambda y: True if y >= 60 and y < 70 else False, [float(val) for val in x]))) / len(x)) * 100)
    non_apmt_plot_df["70+"] = non_apmt_plot_df[0].apply(
        lambda x: (len(list(filter(lambda y: True if y >= 70 else False, [float(val) for val in x]))) / len(x)) * 100)

    plot_df = pd.concat([apmt_plot_df.drop(0, axis=1), non_apmt_plot_df.drop(0, axis=1)], axis=1,
                        keys=["APMT", "Non APMT"])

    # Create a figure with the right layout
    fig = go.Figure(
        layout=go.Layout(
            title="Mooring Duration Distribution (in hrs) \n APMT vs Non APMT",
            height=500, width=1000, barmode="relative",
            yaxis_showticklabels=True, yaxis_showgrid=False,
            yaxis_range=[0, plot_df.groupby(axis=1, level=0).sum().max().max() * 1.1],
            # Secondary y-axis overlayed on the primary one and not visible
            yaxis2=go.layout.YAxis(visible=False, matches="y", overlaying="y", anchor="x", ),
            font=dict(size=10), legend_orientation="v",
            margin=dict(t=25)
        )
    )

    for i, t in enumerate(colors_dur):
        for j, col in enumerate(plot_df[t].columns):
            if (plot_df[t][col] == 0).all():
                continue
            if t == "Non APMT":
                fig.add_bar(
                    x=plot_df.index, y=plot_df[t][col],
                    # Set the right yaxis depending on the selected product (from enumerate)
                    yaxis=f"y{i + 1}",
                    # Offset the bar trace, offset needs to match the width
                    # The values here are in milliseconds, 1billion ms is ~1/3 month
                    offsetgroup=str(i), offset=(i - 1) * 0.3, width=0.3, legendgroup=t,
                    legendgrouptitle_text=t, name=col, marker_pattern_shape="/", marker_color=colors_dur[t][col],
                    marker_line=dict(width=2, color="#333"), hovertemplate='%{y:.1f}%'
                )
            else:
                fig.add_bar(
                    x=plot_df.index, y=plot_df[t][col],
                    # Set the right yaxis depending on the selected product (from enumerate)
                    yaxis=f"y{i + 1}",
                    # Offset the bar trace, offset needs to match the width
                    # The values here are in milliseconds, 1billion ms is ~1/3 month
                    offsetgroup=str(i), offset=(i - 1) * 0.3, width=0.3, legendgroup=t,
                    legendgrouptitle_text=t, name=col, marker_color=colors_dur[t][col],
                    marker_line=dict(width=2, color="#333"),
                    hovertemplate='%{y:.1f}%'
                )
    fig.update_layout(xaxis_title="Months", yaxis_title="Percentage", width=900)

    return fig

def top_6_APMT_vs_Non_APMT_Terminals_on_port_stay():

    plot_df = pd.read_csv("data/Top_6_APMT_vs_Non_APMT_Terminals_on_Port_Stay.csv",header=[0,1],index_col=[0])
    apmt_plot_df = plot_df["APMT"][:-6]
    apmt = list(plot_df["APMT"][:-6].index)
    non_apmt_plot_df = plot_df["Non APMT"][6:]
    non_apmt = list(plot_df["Non APMT"][6:].index)

    non_apmt_plot_df.index = apmt
    plot_df = pd.concat([apmt_plot_df, non_apmt_plot_df], axis=1, keys=["APMT", "Non APMT"])

    # Create a figure with the right layout
    fig = go.Figure(
        layout=go.Layout(
            title="Top 6 APMT vs Non APMT Terminals on Port Stay",
            height=700, width=1000, barmode="relative",
            yaxis_showticklabels=True, yaxis_showgrid=False,
            yaxis_range=[0, plot_df.groupby(axis=1, level=0).sum().max().max() * 1.2],
            # Secondary y-axis overlayed on the primary one and not visible
            yaxis2=go.layout.YAxis(visible=False, matches="y", overlaying="y", anchor="x", ),
            font=dict(size=10), legend_orientation="v",
            margin=dict(t=25)
        )
    )


    for i, t in enumerate(colors_teu):
        for j, col in enumerate(plot_df[t].columns):
            if (plot_df[t][col] == 0).all():
                continue
            if t == "Non APMT":
                fig.add_bar(
                    x=[n + "<br> <br>" + a for a, n in zip(apmt, non_apmt)], y=plot_df[t][col],
                    # Set the right yaxis depending on the selected product (from enumerate)
                    yaxis=f"y{i + 1}",
                    # Offset the bar trace, offset needs to match the width
                    # The values here are in milliseconds, 1billion ms is ~1/3 month
                    offsetgroup=str(i), offset=(i - 1) * 0.3, width=0.3, legendgroup=t,
                    legendgrouptitle_text=t, name=col, marker_pattern_shape="/", marker_color=colors_teu[t][col],
                    marker_line=dict(width=2, color="#333"),
                    hovertemplate='%{y:.1f} hrs'
                )
            else:
                fig.add_bar(
                    x=[n + "<br> <br>" + a for a, n in zip(apmt, non_apmt)], y=plot_df[t][col],
                    # Set the right yaxis depending on the selected product (from enumerate)
                    yaxis=f"y{i + 1}",
                    # Offset the bar trace, offset needs to match the width
                    # The values here are in milliseconds, 1billion ms is ~1/3 month
                    offsetgroup=str(i), offset=(i - 1) * 0.3, width=0.3, legendgroup=t,
                    legendgrouptitle_text=t, name=col, marker_color=colors_teu[t][col],
                    marker_line=dict(width=2, color="#333"),
                    hovertemplate='%{y:.1f} hrs'
                )
    fig.update_layout(xaxis_title="Terminal", yaxis_title="Duration in hrs", width=900)
    fig.update_xaxes(tickangle=90)
    
    return fig

def top_6_APMT_vs_Non_APMT_Terminals_on_port_traffic():

    plot_df = pd.read_csv("data/Top_6_APMT_vs_Non_APMT_Terminals_on_Port_Traffic.csv",header=[0,1],index_col=[0])

    apmt_plot_df = plot_df["APMT"][:-6]
    apmt = list(plot_df["APMT"][:-6].index)
    non_apmt_plot_df = plot_df["Non APMT"][6:]
    non_apmt = list(plot_df["Non APMT"][6:].index)

    non_apmt_plot_df.index = apmt
    plot_df = pd.concat([apmt_plot_df, non_apmt_plot_df], axis=1, keys=["APMT", "Non APMT"])

    # Create a figure with the right layout
    fig = go.Figure(
        layout=go.Layout(
            title="Top 6 APMT vs Non APMT Terminals on Port Traffic",
            height=700, width=1000, barmode="relative",
            yaxis_showticklabels=True, yaxis_showgrid=False,
            yaxis2=go.layout.YAxis(visible=False, matches="y", overlaying="y", anchor="x", ),
            font=dict(size=10), legend_orientation="v",
            # hovermode="x", # dict(b=0,t=10,l=0,r=10)
            margin=dict(t=25)
        )
    )

    for i, t in enumerate(colors_teu):
        for j, col in enumerate(plot_df[t].columns):
            if (plot_df[t][col] == 0).all():
                continue
            if t == "Non APMT":
                fig.add_bar(
                    x=[n + "<br> <br>" + a for a, n in zip(apmt, non_apmt)], y=plot_df[t][col],
                    # Set the right yaxis depending on the selected product (from enumerate)
                    yaxis=f"y{i + 1}",
                    # Offset the bar trace, offset needs to match the width
                    # The values here are in milliseconds, 1billion ms is ~1/3 month
                    offsetgroup=str(i), offset=(i - 1) * 0.3, width=0.3, legendgroup=t,
                    legendgrouptitle_text=t, name=col, marker_pattern_shape="/", marker_color=colors_teu[t][col],
                    marker_line=dict(width=2, color="#333"),
                    hovertemplate='%{y:.1f}'
                )
            else:
                fig.add_bar(
                    x=[n + "<br> <br>" + a for a, n in zip(apmt, non_apmt)], y=plot_df[t][col],
                    # Set the right yaxis depending on the selected product (from enumerate)
                    yaxis=f"y{i + 1}",
                    # Offset the bar trace, offset needs to match the width
                    # The values here are in milliseconds, 1billion ms is ~1/3 month
                    offsetgroup=str(i), offset=(i - 1) * 0.3, width=0.3, legendgroup=t,
                    legendgrouptitle_text=t, name=col, marker_color=colors_teu[t][col],
                    marker_line=dict(width=2, color="#333"),
                    hovertemplate='%{y:.1f}'
                )
    fig.update_layout(xaxis_title="Terminal", yaxis_title="Count", width=900)
    fig.update_xaxes(tickangle=90)
    
    return fig


def preprocess(x):
    return [imo_dur.split(": ")[1] for imo_dur in x[2:-2].split("}, {")]


