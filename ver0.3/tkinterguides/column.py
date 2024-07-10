hex_values = ["AA", "5C", "EA"] # Original Hex Values

def join_digits(hexvalue): # translate hex values into a group of 8, backfilling 0s 
    binary_number = bin(int(hexvalue, 16))[2:].zfill(8)
    return binary_number

def split_digits(binary_number, binary_lists):
 
    for i, bit in enumerate(binary_number):
        binary_lists[i].append(bit)
    
# Initialize a list of lists for each bit position (0 to 7)
binary_lists = [[] for _ in range(8)]

# Process each hex value
for value in hex_values:
    binary_number = join_digits(value)  # Get binary representation for the hex value
    split_digits(binary_number, binary_lists)  # Split and print binary representation

# Combine all lists into one long list
combined_list = []
for sublist in binary_lists:
    combined_list.extend(sublist)

str_list = [str(x) for x in combined_list]
result = ' '.join(''.join(str_list[i:i+6]) for i in range(0, len(str_list), 6))
print(result)