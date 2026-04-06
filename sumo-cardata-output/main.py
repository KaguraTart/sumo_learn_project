# -*- coding: utf-8 -*-
# @auther:	KaguraTart
# @time:	2021/10/31 14:50:27
# @version:	python3.8
# @institution:Tongji university

import pandas as pd
import os, sys

# SUMO path — set the SUMO_HOME environment variable to avoid editing this file.
# Example (Linux/Mac): export SUMO_HOME="/usr/share/sumo"
# Example (Windows):   set SUMO_HOME=C:\Program Files\Eclipse\Sumo
sumo_path = os.environ.get("SUMO_HOME", "F:\\software two\\sumo-1.8.0")
project_path = "sumo-cardata-output"
cfg_path = os.path.join("sumo-cardata-output", "sumo_photo.sumo.cfg")

sys.path.append(sumo_path)
sys.path.append(os.path.join(sumo_path, "tools"))
sys.path.append(os.path.join(sumo_path, "tools", "xml"))
import traci

import output_car_data2 as ocd2
import output_car_data as ocd

# Set gui = True to open the SUMO GUI, False to run headless
gui = True
if gui:
    sumoBinary = os.path.join(sumo_path, "bin", "sumo-gui")
else:
    sumoBinary = os.path.join(sumo_path, "bin", "sumo")

sumoCmd = [
    sumoBinary, "-c", cfg_path,
    "--tripinfo-output", os.path.join(project_path, "tripinfo2_TEST.xml"),
    "--duration-log.statistics",
]

simulation_time = 1200


def traci_control_env_update(step_time):
    traci.start(sumoCmd)
    frames = []
    try:
        for step in range(step_time):
            traci.simulationStep(step + 1)
            frames.append(ocd2.output_car_data2(step, project_path))
    finally:
        traci.close(wait=True)
    return pd.concat(frames, axis=0, ignore_index=True)


if __name__ == "__main__":
    N_STATES = 60

    print("------------------------------------------------")
    a = traci_control_env_update(N_STATES)
    output_dir = os.path.join(project_path, "output_data")
    os.makedirs(output_dir, exist_ok=True)
    a.to_csv(os.path.join(output_dir, "Aoutput-1.csv"))
    print("--------------------END----------------------------")
