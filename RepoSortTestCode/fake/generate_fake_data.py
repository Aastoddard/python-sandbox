import random
import time
from faker import Faker

fake = Faker()

def generate_fake_data(n=10, jitter_range=1000):
   # Get current time and the time 2 years ago in Unix timestamp (seconds)
    current_time = time.time()
    two_years_ago = current_time - (2 * 365 * 24 * 60 * 60)  # Approx. 2 years in seconds
    
    data = []
    for _ in range(n):
        # Generate a random timestamp between current time and 2 years ago
        timestamp = random.randint(int(two_years_ago), int(current_time)) * 1000  # Convert to milliseconds
        
        # Add some jitter
        jitter = random.randint(-jitter_range, jitter_range)
        timestamp_with_jitter = timestamp + jitter
        
        record = {
            "repo": fake.bothify(text="repo-??????????"),  # Generates a repo name with 12+ characters
            "branch": fake.bothify(text="branch-####"),  # Generates a branch name with 7+ characters
            "build_number": random.randint(1, 2000),  # Random build number within range
            "timestamp": timestamp_with_jitter  # Timestamp with jitter applied
        }
        data.append(record)
    return data