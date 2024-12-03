###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module data_exporter
###

## Function to export to CSV
def export_to_csv(data, filename, delimiter=",", include_index=False):
    """
    Export the DataFrame to a CSV file.

    Parameters:
        data (pd.DataFrame): The DataFrame to export.
        filename (str): Name of the output CSV file.
        delimiter (str): Delimiter for the CSV file (default: ',').
        include_index (bool): Whether to include the DataFrame index (default: False).

    Returns:
        None
    """
    try:
        data.to_csv(filename, sep=delimiter, index=include_index)
        print(f"Data successfully exported to {filename}")
    except Exception as e:
        print(f"Error exporting data to CSV: {e}")


import pandas as pd

def export_formatted(data, file_name="formatted_output.txt"):
    """
    Exports the dataframe to a formatted text file.

    Parameters:
    - dataframe: The pandas DataFrame to export.
    - file_name: The name of the output file (default is "formatted_output.txt").
    """
    with open(file_name, "w") as f:
        # Write the header
        f.write("Exported Data Summary\n")
        f.write("=" * 50 + "\n")
        
        # Write the column names and data types
        f.write("Column Details:\n")
        for col in data.columns:
            f.write(f"{col}: {data[col].dtype}\n")
        f.write("\n")
        
        # Write a brief summary of the data
        f.write("Data Summary (First 5 Rows):\n")
        f.write("=" * 50 + "\n")
        f.write(f"{data.head()}\n")
        
        # Write the entire dataframe to the file
        f.write("\nFull Data:\n")
        f.write("=" * 50 + "\n")
        f.write(data.to_string(index=False))

    print(f"Data exported to {file_name}")

# Example usage
# Assuming `simulated_data` is the DataFrame created by `simulate_data`
# export_formatted(simulated_data)
