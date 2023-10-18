f = open("file_test.txt", 'r')
print(f.read())

f = open("file_test.txt", 'w')
f.write("\n The file has only this content...")
f.close()

f = open("file_test.txt", 'r')
print(f.read())

f = open("file_test.txt" , 'a')
f.write("\n This content can add end of the file")
f.close()

f = open("file_test.txt", 'r')
print(f.read())