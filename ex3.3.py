import json
import timeit
import matplotlib.pyplot as plt
import numpy as np

# Function to modify the size value in each record
def modify_size(data, num_records):
    for record in data[:num_records]:
        record['size'] = 35

# Function to measure the average time to modify size for a given number of records
def measure_time(num_records, repeats):
    setup_code = f"from __main__ import modify_size, data; num_records={num_records}"

    times = timeit.repeat(stmt="modify_size(data, num_records)", setup=setup_code, repeat=repeats, number=1)
    
    return times

#path for the file comtaining data 
file_path = "large-file.json"

with open(file_path, 'r') as file:
    data = json.load(file)

#repeats 100 times
num_records = 1000
repeats = 1000

# measuring time 
times = measure_time(num_records, repeats)

# Plotting histogram
plt.hist(times, bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title(f'Distribution of Processing Time for {num_records} Records (Repeats: {repeats})')
plt.savefig('output.3.3.png')
plt.show()