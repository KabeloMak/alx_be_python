from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the datetime as 'YYYY-MM-DD HH:MM:SS'
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current date and time: {formatted_date}")
    
    return current_date  # Optional: returning it for reuse if needed


def calculate_future_date(days_to_add):
    # Get the current date (date only, no time)
    current_date = datetime.now().date()
    
    # Add the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    
    return future_date


def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Ask user for number of days to add
    try:
        days_input = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()