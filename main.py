import csv
import koreanize-matplotlib

# File path to the CSV file
file_path = 'your_file_path_here.csv'

# Read the file line by line and count the number of columns
column_counts = []
with open(file_path, 'r', encoding='cp949') as file:
    reader = csv.reader(file)
    for line in reader:
        column_counts.append(len(line))

# Print the first 20 column counts to understand the structure
print(column_counts[:20])
