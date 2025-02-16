from datetime import datetime

def remove_microseconds():
    now = datetime.now()
    print("Original datetime:", now)
    
    # Remove microseconds
    no_microseconds = now.replace(microsecond=0)
    print("Datetime without microseconds:", no_microseconds)

if __name__ == "__main__":
    remove_microseconds()
