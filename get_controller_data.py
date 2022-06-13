from typing import Dict

from matplotlib import pyplot as plt    

from controller_validation_map import controller_validation

from testing_module.can_data_logging_and_parsing import extract_can_id_data, log_can_data




def desired_decimal_number(data, roundabout, multiplier):
    '''
        This function will reverse the string and convert hex format into decimal format.
    '''
    
    hex_string = "".join(reversed([data[idx : idx + 2] for idx in range(0, len(data), 2)]))

    return (int(hex_string, 16)-roundabout) * multiplier


def get_values():

    print("Logging Data....")

    log_can_data()
    
    print("Reading and Plotting....")
    can_ids, can_data = extract_can_id_data()


    ac_comp_speed = []
    ac_comp_current = []
    ac_comp_voltage = []
    for idx, can_id in enumerate(can_ids):
        for mapp in controller_validation:
            if mapp["can_id"] == can_id:
                
                start_bit = mapp["can_id_start_bit"]*2
                end_bit = (mapp["can_id_end_bit"]+1)*2
                data_point_value = desired_decimal_number( can_data[idx][start_bit : end_bit], mapp["roundabout"], mapp["multiplier"] )
                
                if can_id == "248" and mapp["can_id_start_bit"] == 0 and mapp["can_id_end_bit"] == 1:

                    ac_comp_speed.append(data_point_value)
                
                if can_id == "248" and mapp["can_id_start_bit"] == 6 and mapp["can_id_end_bit"] == 6:

                    ac_comp_current.append(data_point_value)
                
                if can_id == "248" and mapp["can_id_start_bit"] == 7 and mapp["can_id_end_bit"] == 7:

                    ac_comp_voltage.append(data_point_value)

    return [ac_comp_speed, ac_comp_current, ac_comp_voltage]