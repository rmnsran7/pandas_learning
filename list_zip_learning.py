import csv
import os

def merge_csv_files(input_files, output_file):
    csv_files = []
    readers = []

    try:
        # Open all input CSV files
        for file in input_files:
            if os.path.isfile(file):
                csv_files.append(open(file, 'r'))
                readers.append(csv.reader(csv_files[-1]))
            else:
                raise FileNotFoundError(f"File '{file}' not found.")

        # Create a writer for the output file
        output_file_obj = open(output_file, 'w', newline='')
        output_writer = csv.writer(output_file_obj)

        try:
            # Iterate over rows in the CSV files
            for reader in readers:
                # Merge corresponding columns from each row
                for line in reader:
                    output_writer.writerow(line)
        finally:
            # Close the output file
            output_file_obj.close()

    finally:
        # Close all input files
        for file in csv_files:
            file.close()



csv_file = "datasets/choclate protfolio project - 11.csv"
output_file = "datasets/merged_file.csv"
merge_csv_files([csv_file, csv_file, csv_file, csv_file, csv_file, csv_file], output_file)