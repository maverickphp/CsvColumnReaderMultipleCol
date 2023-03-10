# CsvColumnReader

<h3>CSV Column Data Extractor</h3>
The CSV Column Data Extractor is a Python program that reads multiple CSV files from a folder, copies data from a column named "pos", and pastes it in a new CSV file without spaces. This program can be used to extract data from a specific column of multiple CSV files and combine them into a single CSV file.

<h4>Requirements</h4>
- Python 3.x
- csv module (comes with Python)

<h4>Installation</h4>

1. Clone the repository or download the ZIP file and extract its contents to a folder on your computer
2. Make sure you have Python 3.x installed on your computer. You can download it from the official website: https://www.python.org/downloads/
3. No additional installation is required for this program

<h4>How to use</h4>

1. Put all the CSV files you want to extract data from in a folder.
2. Open the csvreader.py file in a text editor or VSCode.
3. Modify the folder_path and output_file_path variables in the program to match the folder containing your CSV files and the path and name of the output file you want to create.
4. Run the program by typing python csvreader.py in your terminal or command prompt.
5. The program will extract data from the "NameOfColumn" column of all the CSV files in the folder and combine them into a single CSV file without spaces in the column names.

<h4>Example</h4>
Suppose you have a folder called csv_files containing the following CSV files:

```sh
csv_files/
    file1.csv
    file2.csv
    file3.csv
```

Each CSV file has the following columns:

```sh
id, name, pos, salary
```

To extract data from the "NameOfColumn" column of each CSV file and combine them into a single CSV file called output.csv without spaces in the column names, you would:

1. Open the csv_column_data_extractor.py file in a text editor.
2. Change the folder_path variable to "/path/to/csv_files" (replace with the actual path to the csv_files folder on your computer).
3. Change the output_file_path variable to "/path/to/output.csv" (replace with the actual path and name of the output file you want to create on your computer).
4. Save the changes to the csvreader.py file.
5. Open a terminal or command prompt and navigate to the folder containing the csvreader.py file.
6. Type python csvreader.py and press Enter.
7. Wait for the program to finish running. The output CSV file will be created in the location you specified.


<b><h3>License</h3></b>
This program is licensed under the MIT License. See the LICENSE file for details.


<b><h3>NOTE:</h3></b>
If you have any issue you can open a thread in issues.
Thanks!
