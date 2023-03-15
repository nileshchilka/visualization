import pandas as pd

imo_to_teu = pd.read_csv("data/imo_to_teu.csv")

moor_anchor_df_070809v2 = pd.read_csv("data/mooring_anchor_070809v2.csv")
moor_anchor_df_070809v2.columns = ["index","July","August","September"]
moor_anchor_df_101112v2 = pd.read_csv("data/mooring_anchor_101112v2.csv")
moor_anchor_df_101112v2.columns = ["index","October","November","December"]
moor_anchor_df_01v2 = pd.read_csv("data/mooring_anchor_01v2.csv")
moor_anchor_df_01v2.columns = ["index","January"]
moor_anchor_df_01v2["order"] = [3,2,0,1,5,4]
moor_anchor_df_01v2 = moor_anchor_df_01v2.sort_values("order").reset_index(drop=True)
moor_anchor_dfv2 = pd.concat([moor_anchor_df_070809v2,moor_anchor_df_101112v2[["October","November","December"]],moor_anchor_df_01v2[["January"]]],axis=1)
moor_anchor_dfv2 = moor_anchor_dfv2.T
moor_anchor_dfv2.columns = moor_anchor_dfv2.iloc[0].values
moor_anchor_dfv2 = moor_anchor_dfv2.iloc[1:]
moor_anchor_dfv2["len of target_apmt_port_calls_df"] = moor_anchor_dfv2["len of target_apmt_port_calls_df"].astype(int)
moor_anchor_dfv2["len of target_non_apmt_port_calls_df"] = moor_anchor_dfv2["len of target_non_apmt_port_calls_df"].astype(int)
moor_anchor_dfv2["len of target_port_calls_df"] = moor_anchor_dfv2["len of target_apmt_port_calls_df"] + moor_anchor_dfv2["len of target_non_apmt_port_calls_df"]

len_data = []
for lt in moor_anchor_dfv2["apmt_port_calls_anchor_data"].to_list():
    imo_data = []
    for imo_dur in lt[1:-1].split(", "):
        imo = int(imo_dur[2:-1].split("': ")[0])
        dur = round(float(imo_dur[2:-1].split("': ")[1]),2)
        imo_data.append([imo,dur])
    len_data.append(len(imo_data))
    
moor_anchor_dfv2["apmt_anchor_count"] = len_data

len_data = []
for lt in moor_anchor_dfv2["apmt_port_calls_moor_data"].to_list():
    imo_data = []
    for imo_dur in lt[1:-1].split(", "):
        imo = int(imo_dur[2:-1].split("': ")[0])
        dur = round(float(imo_dur[2:-1].split("': ")[1]),2)
        imo_data.append([imo,dur])
    len_data.append(len(imo_data))
    
moor_anchor_dfv2["apmt_port_calls"] = len_data
moor_anchor_dfv2["apmt_instantly_served"] = moor_anchor_dfv2["apmt_port_calls"] - moor_anchor_dfv2["apmt_anchor_count"]
moor_anchor_dfv2["apmt_instantly_served_per"] = (moor_anchor_dfv2["apmt_instantly_served"] / moor_anchor_dfv2["apmt_port_calls"]) * 100
moor_anchor_dfv2["apmt_anchor_count_per"] = (moor_anchor_dfv2["apmt_anchor_count"] / moor_anchor_dfv2["apmt_port_calls"]) * 100

len_data = []
for lt in moor_anchor_dfv2["non_apmt_port_calls_anchor_data"].to_list():
    imo_data = []
    for imo_dur in lt[1:-1].split(", "):
        imo = int(imo_dur[2:-1].split("': ")[0])
        dur = round(float(imo_dur[2:-1].split("': ")[1]),2)
        imo_data.append([imo,dur])
    len_data.append(len(imo_data))
    
moor_anchor_dfv2["non_apmt_anchor_count"] = len_data

len_data = []
for lt in moor_anchor_dfv2["non_apmt_port_calls_moor_data"].to_list():
    imo_data = []
    for imo_dur in lt[1:-1].split(", "):
        imo = int(imo_dur[2:-1].split("': ")[0])
        dur = round(float(imo_dur[2:-1].split("': ")[1]),2)
        imo_data.append([imo,dur])
    len_data.append(len(imo_data))
    
moor_anchor_dfv2["non_apmt_port_calls"] = len_data
moor_anchor_dfv2["non_apmt_instantly_served"] = moor_anchor_dfv2["non_apmt_port_calls"] - moor_anchor_dfv2["non_apmt_anchor_count"]
moor_anchor_dfv2["non_apmt_instantly_served_per"] = (moor_anchor_dfv2["non_apmt_instantly_served"] / moor_anchor_dfv2["non_apmt_port_calls"]) * 100
moor_anchor_dfv2["non_apmt_anchor_count_per"] = (moor_anchor_dfv2["non_apmt_anchor_count"] / moor_anchor_dfv2["non_apmt_port_calls"]) * 100

moor_anchor_dfv2["port_calls"] = moor_anchor_dfv2["apmt_port_calls"] + moor_anchor_dfv2["non_apmt_port_calls"]
moor_anchor_dfv2["total_anchor_count"] = moor_anchor_dfv2["non_apmt_anchor_count"] + moor_anchor_dfv2["apmt_anchor_count"]
moor_anchor_dfv2["total_instantly_served"] = moor_anchor_dfv2["non_apmt_instantly_served"] + moor_anchor_dfv2["apmt_instantly_served"]
moor_anchor_dfv2["total_anchor_count_per"] = (moor_anchor_dfv2["total_anchor_count"] / moor_anchor_dfv2["len of target_port_calls_df"]) * 100
moor_anchor_dfv2["total_instantly_served_per"] = (moor_anchor_dfv2["total_instantly_served"] / moor_anchor_dfv2["port_calls"]) * 100


