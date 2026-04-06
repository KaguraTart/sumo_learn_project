# -*- coding: utf-8 -*-
# @auther:	KaguraTart
# @time:	2021/10/31 14:50:27
# @version:	python3.8
# @institution:Tongji university

import traci
import pandas as pd
import os


def output_car_data2(step, project_path):
    """Collect per-step vehicle state and save to CSV.

    Note: output_car_data2.py is the preferred version for aggregating data
    across steps. This file saves one CSV per step to disk.

    Args:
        step: Current simulation step number.
        project_path: Path to the project directory (used for output path).
    """
    columns = [
        "car_num", "x_position", "y_position",
        "x_acceleration(m/s^2)", "y_acceleration(m/s^2)",
        "length(m)", "speed(m/s)", "LateralSpeed(m/s)",
        "acceleration(m/s^2)", "angle(deg)",
        "roadID", "LaneID", "Lane_index", "lane_position",
    ]
    rows = []
    all_vehicle_id = traci.vehicle.getIDList()

    for vehicle_id in all_vehicle_id:
        position = traci.vehicle.getPosition(vehicle_id)
        acceleration = traci.vehicle.getAcceleration(vehicle_id)
        length = traci.vehicle.getLength(vehicle_id)
        speed = traci.vehicle.getSpeed(vehicle_id)
        lateral_speed = traci.vehicle.getLateralSpeed(vehicle_id)
        road_id = traci.vehicle.getRoadID(vehicle_id)
        lane_id = traci.vehicle.getLaneID(vehicle_id)
        angle = traci.vehicle.getAngle(vehicle_id)
        lane_index = traci.vehicle.getLaneIndex(vehicle_id)
        lane_position = traci.vehicle.getLanePosition(vehicle_id)

        # x_acceleration: SUMO longitudinal acceleration (m/s^2)
        # y_acceleration: lateral acceleration is not directly provided by SUMO
        x_acce = acceleration
        y_acce = 0.0

        rows.append([
            vehicle_id, position[0], position[1],
            x_acce, y_acce,
            length, speed, lateral_speed,
            acceleration, angle,
            road_id, lane_id, lane_index, lane_position,
        ])

    position_data = pd.DataFrame(rows, columns=columns)
    output_dir = os.path.join(project_path, "output_data")
    os.makedirs(output_dir, exist_ok=True)
    position_data.to_csv(os.path.join(output_dir, f"for{step}seconds.csv"))
