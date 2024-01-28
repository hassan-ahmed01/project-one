#TASK SEVEN 
def create_alphabet_file(lines_per_group):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    with open('alphabet_file.txt', 'w') as file:
        for i in range(0, len(alphabet), lines_per_group):
            file.write(alphabet[i:i+lines_per_group] + '\n')
print("created")

lines_per_group = 5
create_alphabet_file(lines_per_group)