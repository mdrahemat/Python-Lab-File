import pandas as pd
import matplotlib.pyplot as plt

def main():
    # 1. Create the Weekly Temperature Data
    data = {
        'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'Temperature_C': [22.5, 24.0, 23.5, 26.0, 28.5, 27.0, 25.0]
    }
    
    # Load data into a Pandas DataFrame
    df = pd.DataFrame(data)
    
    # 2. Data Analysis
    print("--- Weekly Temperature Data ---")
    print(df)
    print("\n--- Temperature Analysis ---")
    
    avg_temp = df['Temperature_C'].mean()
    max_temp = df['Temperature_C'].max()
    min_temp = df['Temperature_C'].min()
    
    # Find the days with the highest and lowest temperatures
    hottest_day = df.loc[df['Temperature_C'].idxmax(), 'Day']
    coldest_day = df.loc[df['Temperature_C'].idxmin(), 'Day']
    
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print(f"Highest Temperature: {max_temp}°C (on {hottest_day})")
    print(f"Lowest Temperature:  {min_temp}°C (on {coldest_day})")

    # 3. Data Visualization
    # Create a line chart
    plt.figure(figsize=(10, 5))
    plt.plot(df['Day'], df['Temperature_C'], marker='o', color='tomato', linestyle='-', linewidth=2, markersize=8)
    
    # Add title and labels
    plt.title('Weekly Temperature Analysis', fontsize=14, pad=15)
    plt.xlabel('Day of the Week', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    
    # Add grid lines for better readability
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Display the chart
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()