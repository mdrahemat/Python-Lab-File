import statistics

def perform_basic_analysis(data):
    print("--- Simple Data Analysis ---")
    print(f"Dataset: {data}\n")
    
    # 1. Basic properties
    count = len(data)
    total_sum = sum(data)
    min_value = min(data)
    max_value = max(data)
    
    # 2. Statistical calculations using the statistics module
    mean_value = statistics.mean(data)
    median_value = statistics.median(data)
    
    try:
        mode_value = statistics.mode(data)
    except statistics.StatisticsError:
        mode_value = "No unique mode"

    # 3. Displaying the results
    print(f"Total Data Points: {count}")
    print(f"Sum of Data:       {total_sum}")
    print(f"Minimum Value:     {min_value}")
    print(f"Maximum Value:     {max_value}")
    print("-" * 30)
    print(f"Mean (Average):    {mean_value:.2f}")
    print(f"Median:            {median_value}")
    print(f"Mode:              {mode_value}")

if __name__ == "__main__":
    # Sample dataset (e.g., student test scores)
    scores = [82, 90, 75, 82, 95, 88, 79, 100, 82, 91]
    
    perform_basic_analysis(scores)