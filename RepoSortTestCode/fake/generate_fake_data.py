import random
import time
import string
from faker import Faker
from datetime import datetime, timedelta

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

def generate_fake_repos_return(num_repos=5):
    """Generate fake data based on the JSON schema with a variable array size."""
    
    def random_repo_name():
        """Generate a random repo name between 5 and 12 characters."""
        length = random.randint(5, 12)
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    fake_data = {
        "repos": [{"repoNames": random_repo_name()} for _ in range(num_repos)]
    }
    
    return fake_data

def generate_fake_branches_return(num_branches=5):
    """Generate fake data based on the JSON schema with a weighted boolean probability for buildable."""
    
    def random_branch_name():
        """Generate a random branch name between 5 and 12 characters."""
        length = random.randint(5, 12)
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    fake_data = {
        "branches": [{"branchName": random_branch_name()} for _ in range(num_branches)],
        "buildable": random.choices([True, False], weights=[0.7, 0.3])[0]  # 80% True, 20% False
    }
    
    return fake_data

def generate_fake_last_build_return():
    """Generate a last build number (>50 and <2500) and a timestamp (Unix time in milliseconds)."""
    
    last_build_number = random.randint(51, 2499)  # Ensure it's >50 and <2500

    # Generate a random timestamp within the last 2 years
    now = datetime.now()
    past_two_years = now - timedelta(days=2*365)  # Approximate 2 years
    random_timestamp = past_two_years + timedelta(seconds=random.randint(0, int((now - past_two_years).total_seconds())))

    # Convert timestamp to Unix time in milliseconds
    timestamp_unix_ms = int(random_timestamp.timestamp() * 1000)

    return {
        "lastBuildNumber": last_build_number,
        "timestamp": timestamp_unix_ms  # Unix time in milliseconds
    }

def generate_fake_build_data(num_objects):
    """Generate fake build data with sequential build numbers and decreasing timestamps with jitter."""
    
    now = datetime.now()
    past_two_years = now - timedelta(days=2*365)  # Approximate 2 years

    # List to store generated build data
    build_data = []

    # Generate the first timestamp randomly between now and the past two years
    prev_timestamp = random.randint(int(past_two_years.timestamp() * 1000), int(now.timestamp() * 1000))

    for build_number in range(1, num_objects + 1):

        # Make sure the adjusted timestamp is still smaller than the previous one
        if adjusted_timestamp >= prev_timestamp:
            jitter = random.randint(-90, 90)
            adjusted_timestamp = prev_timestamp - (2700 + jitter) * 1000  # Fallback to the strict 45-minute rule if jitter breaks it

        prev_timestamp = adjusted_timestamp  # Update the previous timestamp for the next iteration

        # Add the generated build data to the list
        build_data.append({
            "build_number": build_number,
            "timestamp": adjusted_timestamp
        })

    return build_data