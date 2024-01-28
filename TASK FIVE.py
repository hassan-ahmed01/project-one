#TASK FIVE 
def read_file_lines(file_path):
    lines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

#we can use any path we want 
file_path = 'example.txt' 
# Replace with the path to your file
result_lines = read_file_lines(file_path)
print(result_lines)


#storage/emulated/0/document/Pydriod3/
