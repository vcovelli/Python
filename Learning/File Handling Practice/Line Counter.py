# Line Counter
with open("test_file_path.txt", 'r') as file:
    lines = file.readlines()
    line_count = len(lines)
    print("Number of lines:", line_count)