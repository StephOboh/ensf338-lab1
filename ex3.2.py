import json
import timeit
import matplotlib.pyplot as plt
import numpy as np

# Function to modify the size value in each record
def modify_size(data, num_records):
    for record in data[:num_records]:
        record['size'] = 35

# Function to measure the average time to modify size for a given number of records
def measure_time(num_records):
    setup_code = f"from __main__ import modify_size, data; num_records={num_records}"

    total_time = timeit.timeit(stmt="modify_size(data, num_records)", setup=setup_code, number=100)
    average_time = total_time / 100
    
    return average_time

file_path = "/Users/stephenieoboh/Desktop/ENSF338/Lab1/large-file.json"

with open(file_path, 'r') as file:
    data = json.load(file)

num_records_list = [1000, 2000, 5000, 10000]

average_times = [measure_time(num_records) for num_records in num_records_list]

slope, intercept = np.polyfit(num_records_list, average_times, 1)

plt.scatter(num_records_list, average_times, label='Data')
plt.plot(num_records_list, [slope * x + intercept for x in num_records_list], 'r', label='Linear Fit')
plt.xlabel('Number of Records')
plt.ylabel('Average Processing Time (seconds)')
plt.title('Linear Regression Plot')
plt.legend()


plt.savefig('output.3.2.png')

print(f"The linear model is: t = {slope:.2e} * n + {intercept:.2e}")
plt.show()
