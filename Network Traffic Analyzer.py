def get_user_input():
    # Ask the user to enter network traffic data
    while True:
        try:
            traffic_data = int(input("Please enter the network traffic data (between 1 and 100): "))
            if 1 <= traffic_data <= 100:
                return traffic_data
            else:
                print("Invalid input. Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def analyze_traffic(traffic_data):
    # Check if the network traffic data indicates suspicious activity
    threshold_value = 80  # A threshold value for suspicious traffic
    if traffic_data > threshold_value:
        return True  # Suspicious activity detected
    else:
        return False  # No suspicious activity

def generate_alert():
    # Generate an alert if suspicious network traffic is detected
    print("Alert! Suspicious network traffic detected.")

# Main program
if __name__ == "__main__":
    # Get user input for network traffic data
    traffic_data = get_user_input()

    # Analyze the network traffic data
    if analyze_traffic(traffic_data):
        generate_alert()  # Generate an alert for suspicious traffic
    else:
        print("No suspicious activity detected.")
