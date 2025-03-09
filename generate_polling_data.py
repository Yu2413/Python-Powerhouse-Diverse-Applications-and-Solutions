import csv
import random
from datetime import datetime, timedelta

# Function to generate random polling data
def generate_polling_data(start_date, end_date, parties):
    data = []
    current_date = start_date
    while current_date <= end_date:
        for party in parties:
            average = round(random.uniform(20, 50), 2)  # Random average between 20% and 50%
            data.append([current_date.strftime('%Y-%m-%d'), party, average])
        current_date += timedelta(days=1)
    return data

# Define the political parties
parties = ['Party A', 'Party B', 'Party C', 'Party D']

# Define the date range for the polling data
start_date = datetime(2023, 10, 1)
end_date = datetime(2023, 10, 10)

# Generate the polling data
polling_data = generate_polling_data(start_date, end_date, parties)

# Write the data to a CSV file
csv_filename = 'political_polling_averages.csv'
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Party', 'Average Polling Percentage'])
    writer.writerows(polling_data)

print(f"Polling data has been written to {csv_filename}")