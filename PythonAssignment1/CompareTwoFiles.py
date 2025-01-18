def compare_two_files(file1, file2):
    file1 = open(file1, 'r')
    file2 = open(file2, 'r')
    if file1.readlines() == file2.readlines():
        return print("Identical files")
    else:
        return print("Not Identical files")

compare_two_files("file1.txt", "file2.txt")
