from fake import generate_fake_data
from process_data import binary_search
from datetime import datetime
import time
import json

def main():
    fake_data = generate_fake_data.generate_fake_data(30000, 10000)
    sorted_data = sorted(fake_data, key=lambda x: x['timestamp'], reverse=True)
    
    newest_timestamp = sorted_data[0]['timestamp']
    oldest_timestamp = sorted_data[-1]['timestamp']

    newest_date = datetime.fromtimestamp(newest_timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S PST')
    oldest_date = datetime.fromtimestamp(oldest_timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S PST')

    print(f"newest timestamp: {newest_date}")
    print(f"oldest timestamp: {oldest_date}")

    current_time = time.time()
    one_year_ago = current_time - (365 * 24 * 60 * 60)  # 1 year ago in seconds
    target_timestamp = int(one_year_ago * 1000)  # Convert to milliseconds

    # Find the closest timestamp
    index, closest_record = binary_search.find_closest_timestamp(sorted_data, target_timestamp)

    # Print the result
    print(f"The closest timestamp is at index {index} with the record:")
    print(f"Repo: {closest_record['repo']}")
    print(f"Branch: {closest_record['branch']}")
    print(f"Build Number: {closest_record['build_number']}")
    print(f"Timestamp: {datetime.fromtimestamp(closest_record['timestamp'] / 1000).strftime('%Y-%m-%d %H:%M:%S PST')}")

    output_file = "output.txt"

    # Open the file in write mode
    with open(output_file, 'w') as file:
        # Print the result for the closest timestamp
        file.write(f"The closest timestamp is at index {index} with the record:\n")
        file.write(f"Repo: {closest_record['repo']}\n")
        file.write(f"Branch: {closest_record['branch']}\n")
        file.write(f"Build Number: {closest_record['build_number']}\n")
        file.write(f"Timestamp: {datetime.fromtimestamp(closest_record['timestamp'] / 1000).strftime('%Y-%m-%d %H:%M:%S PST')}\n")

        # Now, iterate through the list until we reach the closest index and print to file
        file.write("\nIterating through the list until the closest index:\n")
        for i in range(index + 1):  # Include the closest index itself
            timestamp = sorted_data[i]['timestamp']
            formatted_timestamp = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S PST')
            file.write(f"Index {i}: {formatted_timestamp}\n")

if __name__ == "__main__":
    main()