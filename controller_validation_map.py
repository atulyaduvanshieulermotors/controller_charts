controller_validation = [
    {
        "name": "AC Speed of Compressor",
        "can_id": "248",
        "can_id_start_bit": 0,
        "can_id_end_bit": 1,
        "roundabout": 0,
        "multiplier": 1, 
        "index": 61,  #dumb here
        "lower_limit": 0, #dumb here
        "upper_limit": 250, #dumb here
        "range": True, #dumb here
    },
    {
        "name": "Compressor Run Current",
        "can_id": "248",
        "can_id_start_bit": 6,
        "can_id_end_bit": 6,
        "roundabout": 0,
        "multiplier": 0.1, 
        "index": 61,  #dumb here
        "lower_limit": 0, #dumb here
        "upper_limit": 250, #dumb here
        "range": True, #dumb here
    },
    {
        "name": "Compressor Run Voltage",
        "can_id": "248",
        "can_id_start_bit": 7,
        "can_id_end_bit": 7,
        "roundabout": 0,
        "multiplier": 4, 
        "index": 61,  #dumb here
        "lower_limit": 0, #dumb here
        "upper_limit": 250, #dumb here
        "range": True, #dumb here
    },
]
