import pandas as pd
import matplotlib.pyplot as plt

# Create weekly temperature data
data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Temperature (C)': [22, 24, 23, 26, 28, 27, 25]
}
df = pd.DataFrame(data)

print("Weekly Temperature Data (Pandas DataFrame):")
print(df)

# Visualization
plt.plot(df['Day'], df['Temperature (C)'], marker='o', color='red')
plt.title('Weekly Temperature Analysis')
plt.xlabel('Day of the Week')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()