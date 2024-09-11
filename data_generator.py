import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import random

try:
    # Define the scope of the application
    scope = ["https://www.googleapis.com/auth/spreadsheets"]

    # Load the credentials from the JSON file
    creds = Credentials.from_service_account_file('credentials.json', scopes=scope)

    # Authorize and create a client
    client = gspread.authorize(creds)

    # Access the Google Sheet
    sheet_id = "1SAIhGo8gvjn7bpClqqUlJ0VEjtgl27qgFIuMGprqn5g"
    sheet = client.open_by_key(sheet_id).sheet1

    def generate_flood_data():
        # Date: Generate any day and month for this year and 2023
        current_year = datetime.now().year
        year = random.choice([2023, current_year])
        month = random.randint(1, 12)
        day = random.randint(1, 28)  # To avoid invalid days for some months
        date = f"{day:02d}-{month:02d}-{year}"

        # Location: List of Indian state capitals with their corresponding latitudes and longitudes
        capitals = {
            'Delhi': (28.7041, 77.1025),
            'Mumbai': (19.0760, 72.8777),
            'Bengaluru': (12.9716, 77.5946),
            'Chennai': (13.0827, 80.2707),
            'Kolkata': (22.5726, 88.3639),
            'Hyderabad': (17.3850, 78.4867),
            'Jaipur': (26.9124, 75.7873),
            'Lucknow': (26.8467, 80.9462),
            'Bhopal': (23.2599, 77.4126),
            'Guwahati': (26.1445, 91.7362),
            'Patna': (25.5941, 85.1376),
            'Thiruvananthapuram': (8.5241, 76.9366)
            # Add more as needed
        }

        location, (lat, lon) = random.choice(list(capitals.items()))

        # Rainfall (mm) between 50-900
        rainfall = random.uniform(50, 900)

        # Flood Impact either High, Medium, Low
        impact = random.choice(['High', 'Medium', 'Low'])

        # Casualties: between 10-2000
        casualties = random.randint(10, 2000)

        # People Displaced: between 100-20000
        people_displaced = random.randint(100, 20000)

        # Property Damage (INR) between 10000-1000000
        property_damage = random.randint(10000, 1000000)

        # Storing everything in a list in the requested order
        flood_data = [
            date, location, lat, lon, round(rainfall, 2), impact,
            casualties, people_displaced, property_damage
        ]
        sheet.append_row(flood_data)
        print(f"Data Genrated: {flood_data}")

    # Example usage:



    if __name__ == "__main__":
        generate_flood_data()
except Exception as e:
    print(f"An error occurred: {e}")
