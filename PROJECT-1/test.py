import numpy as np

test = 'Королев , (метро) , готова к переезду (город1б город2)'

def get_ready_to_move_flag(locations_data : str) -> bool:
    """Returns readiness of applicant to move to another city.

    Args:
        locations_data (str): String with applicant's locations like city of living, willingness to move
        and working trips.

    Returns:
        bool: True if applicant is ready to move, otherwise False
    """
    locations_data_list = locations_data.split(" , ")
    locations_data_list = [x for x in locations_data_list if not x.startswith("(")] #Delete unnecessary data like metro
    ready_to_move_data = locations_data_list[1]
    return ready_to_move_data.startswith("готов")
    
def get_ready_for_work_trips_flag(locations_data : str) -> bool:
    """Returns readiness of applicant for working trips.

    Args:
        locations_data (str): String with applicant's locations like city of living, willingness to move
        and working trips.

    Returns:
        bool: True if applicant is ready for working trips, otherwise False
    """
    locations_data_list = locations_data.split(" , ")
    locations_data_list = [x for x in locations_data_list if not x.startswith("(")] #Delete unnecessary data like metro
    if len(locations_data_list) == 2: #Means we lost work trip data while exporting
        return False
    else:
        return locations_data_list[2].startswith("готов")

print(get_ready_for_work_trips_flag(test))