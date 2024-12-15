import pandas as pd

# Load the Excel file
data = pd.read_excel('AD9364.xlsx')

# Debug: Strip column names to avoid leading/trailing spaces
data.columns = data.columns.str.strip()

def get_bit_names(register_address, hex_value):
    # Convert the hex value to an 8-bit binary string
    binary_value = bin(int(hex_value, 16))[2:].zfill(8)  # Ensure 8 bits

    # Find the row matching the register address
    row = data.loc[data['Register Address'] == register_address]

    if row.empty:
        return f"Register address '{register_address}' not found."

    # Extract the register name
    register_name = row.iloc[0]['Name']

    # Extract bit names for D7-D0
    bit_names = [row.iloc[0][f'D{i}'] for i in range(7, -1, -1)]  # D7 to D0

    # Map binary bits to their names
    bit_status = {bit_names[i]: binary_value[i] for i in range(8)}

    # Format the output
    output = f"Register Name: {register_name}\n"
    output += "Bit Details:\n"
    for bit_name, bit_value in bit_status.items():
        output += f"  {bit_name}: {bit_value}\n"

    return output

# Input values
register_address = input("Enter register address : ")
hex_value = input("Enter hex value : ")

# Get and print the bit names
result = get_bit_names(register_address, hex_value)
print(result)
