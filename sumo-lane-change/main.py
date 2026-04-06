# -*- coding: utf-8 -*-
# @auther:	KaguraTart
# @time:	2021/10/31 14:50:27
# @version:	python3.8
# @institution:Tongji university

import os, sys

# SUMO path — set the SUMO_HOME environment variable to avoid editing this file.
# Example (Linux/Mac): export SUMO_HOME="/usr/share/sumo"
# Example (Windows):   set SUMO_HOME=C:\Program Files\Eclipse\Sumo
sumo_path = os.environ.get("SUMO_HOME", "F:\\software two\\sumo-1.10.0")
project_path = "sumo-lane-change"
cfg_path = os.path.join("sumo-lane-change", "sumo_simu.sumo.cfg")

sys.path.append(sumo_path)
sys.path.append(os.path.join(sumo_path, "tools"))
sys.path.append(os.path.join(sumo_path, "tools", "xml"))
import traci

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


def traci_control_env_update():
    """Run the lane-change simulation until interrupted (Ctrl+C) or SUMO closes."""
    traci.start(sumoCmd)
    step = 0.0
    try:
        while True:
            traci.simulationStep(step)
            step += 0.05
    except KeyboardInterrupt:
        print("\nSimulation interrupted by user.")
    finally:
        traci.close(wait=True)


if __name__ == "__main__":
    print("------------------------------------------------")
    print("Running lane-change simulation. Press Ctrl+C to stop.")
    traci_control_env_update()
    print("--------------------END----------------------------")
