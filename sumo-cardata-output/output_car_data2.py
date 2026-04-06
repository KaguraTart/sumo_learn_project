# -*- coding: utf-8 -*-
# @auther:	KaguraTart
# @time:	2021/10/31 14:50:27
# @version:	python3.8
# @institution:Tongji university

import traci
import pandas as pd


def output_car_data2(step, project_path):
    """Collect vehicle state data for the current simulation step.

    Args:
        step: Current simulation step number (recorded as simu_time column).
        project_path: Unused; kept for API compatibility with output_car_data.py.

    Returns:
        pd.DataFrame with one row per active vehicle.
    """
    columns = [
        "simu_time", "car_num", "x_position", "y_position",
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

        rows.append([
            step, vehicle_id, position[0], position[1],
            length, speed, lateral_speed,
            acceleration, angle,
            road_id, lane_id, lane_index, lane_position,
        ])

    return pd.DataFrame(rows, columns=columns)
