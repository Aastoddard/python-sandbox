
def find_closest_timestamp(data, target_timestamp):
    # First, sort the data by timestamp
    
    # Binary search to find the closest timestamp
    left, right = 0, len(data) - 1
    closest_index = -1
    closest_diff = float('inf')
    
    while left <= right:
        mid = (left + right) // 2
        diff = abs(data[mid]['timestamp'] - target_timestamp)
        
        if diff < closest_diff:
            closest_diff = diff
            closest_index = mid
        
        if data[mid]['timestamp'] < target_timestamp:
            left = mid + 1
        else:
            right = mid - 1
    
    return closest_index, data[closest_index]