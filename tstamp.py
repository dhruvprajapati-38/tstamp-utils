from datetime import datetime

def print_timestamp():
    """
    Prints current date and time
    """
    now = datetime.now()
    print("Timestamp:", now.strftime("%d/%m/%Y %H:%M:%S"))
