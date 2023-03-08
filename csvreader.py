import csv
import os

# Set the path of the folder containing CSV files
folder_path = 'C:/Users/Administrator/Desktop/CodewithMv/CsvColumnReaderModified/ExampleDataset'

# Set the output file name and path
output_file_path = 'C:/Users/Administrator/Desktop/CodewithMv/CsvColumnReaderModified/output.csv'

# Create a set for each column to store unique data
pos_set = set()
name_set = set()
age_set = set()

# Create a dictionary for each column to store the count of each data item
pos_dict = {}
name_dict = {}
age_dict = {}

# Loop through each CSV file in the folder
for file in os.listdir(folder_path):
    if file.endswith('.csv'):
        file_path = os.path.join(folder_path, file)
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Add each data item to its respective set
                pos_set.add(row['pos'])
                name_set.add(row['name'])
                age_set.add(row['age'])

                # Update the count of each data item in its respective dictionary
                pos_dict[row['pos']] = pos_dict.get(row['pos'], 0) + 1
                name_dict[row['name']] = name_dict.get(row['name'], 0) + 1
                age_dict[row['age']] = age_dict.get(row['age'], 0) + 1

# Create the output CSV file
with open(output_file_path, 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    # Write the header row
    writer.writerow(['pos', 'pos_count', 'name', 'name_count', 'age', 'age_count'])

    # Loop through each unique data item in each column
    for pos in pos_set:
        for name in name_set:
            for age in age_set:
                # Check if the data item exists in each column
                if pos in pos_dict and name in name_dict and age in age_dict:
                    # Write the data item and its count in the output CSV file
                    writer.writerow([pos, pos_dict[pos], name, name_dict[name], age, age_dict[age]])
