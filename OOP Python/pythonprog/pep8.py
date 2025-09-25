# Sample data containing both valid integer values and some non-integer entries
data_column = ['10', '20', 'abc', '30', 'NaN', '40']

# List to store the successfully converted integer values
cleaned_data = []

# Iterate through each value in the data_column list
for value in data_column:
    try:
        # Attempt to convert each value to an integer
        cleaned_data.append(int(value))
    except ValueError:
        # If conversion fails (e.g., for 'abc' or 'NaN'), handle the exception
        # and skip that value. Print an error message
        # with the problematic value.
        print(
            f"Encountered a non-integer value: {value}, skipping this entry.")
# The else block will execute after the for loop completes
# without an exception in try block
else:
    # If no errors occur during the iteration, this message is printed
    print("All valid values were successfully converted to integers.")

    # Display the list of cleaned integer values
    print("Cleaned Data:", cleaned_data)
