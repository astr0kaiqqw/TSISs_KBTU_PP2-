from datetime import datetime

def remove_microseconds():
    now = datetime.now()
    print("Original datetime:", now)
    
    # Remove microseconds
    no_microseconds = now.replace(microsecond=0)
    print("Datetime without microseconds:", no_microseconds)

def date_difference_in_seconds(date1, date2):
    delta = date2 - date1
    return delta.total_seconds()

if __name__ == "__main__":
    remove_microseconds()
    
    # Example usage
    date1 = datetime(2023, 1, 1, 12, 0, 0)
    date2 = datetime(2023, 1, 2, 12, 0, 0)
    print("Difference in seconds:", date_difference_in_seconds(date1, date2))
