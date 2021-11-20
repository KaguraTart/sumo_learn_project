# -*- coding: utf-8 -*-
# @auther:	KaguraTart
# @time:	2021/10/31 14:50:27
# @version:	python3.8
# @institution:Tongji university

from typing import Counter
import  traci
import  numpy as np
import  pandas as pd
import os

def output_car_data2(step,project_path):

    position_data = pd.DataFrame(columns=['car_num','x_position','y_position','x_acce(m^2/s)','y_acce(m^2/s)','length(m)','speed(m/s)','LateralSpeed(m/s)','accelaration(m^2/s)','angel(du)','roadID','LaneID','Lane_index','lane_position'],dtype=float)

    #获取车辆ID
    all_vehicle_id = traci.vehicle.getIDList()
    # print(type(all_vehicle_id))
    n = 0
    #获取车辆位置
    for i in all_vehicle_id:
        all_vehicle_position = traci.vehicle.getPosition(i)
        all_vehicle_accelatatioin = traci.vehicle.getAcceleration(i)
        get_vehicle_length = traci.vehicle.getLength(i)
        get_speed = traci.vehicle.getSpeed(i)
        get_lateral_speed = traci.vehicle.getLateralSpeed(i)
        # get_max_speedlat = traci.vehicle.getMaxSpeedLat(i)
        get_roadID = traci.vehicle.getRoadID(i)
        get_laneID = traci.vehicle.getLaneID(i)
        get_angle = traci.vehicle.getAngle(i)
        get_lane_index = traci.vehicle.getLaneIndex(i)
        get_lane_position = traci.vehicle.getLanePosition(i)
        #计算加速度
        if n == 0:
            x_acce = 0
            y_acce = 0
        else:
            x_acce = get_speed - traci.vehicle.getSpeed(all_vehicle_id[n-1])
            y_acce = get_lateral_speed - traci.vehicle.getLateralSpeed(all_vehicle_id[n-1])
        
        # print(i)
        # print(all_vehicle_id[n])
        
        position_data.loc[n] = [all_vehicle_id[n],all_vehicle_position[0],all_vehicle_position[1],x_acce,y_acce,get_vehicle_length,get_speed,get_lateral_speed,all_vehicle_accelatatioin,get_angle,get_roadID,get_laneID,get_lane_index,get_lane_position]
        n +=1
    # print(position_data)
    try:
        position_data.to_csv(project_path+"/output_data/for"+str(step)+"seconds"+".csv")
    except:
        os.makedirs(project_path+"/output_data") 
        position_data.to_csv(project_path+"/output_data"+"/for"+str(step)+"seconds"+".csv")