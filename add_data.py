while True :
 file = open("dictnory.txt", "r")
 data = file.read()
 print()
 name = input("Enter the tag : ")
 type = input("Enter the data type [file, string] : ")
 value = input("Enter the values : ")
 x = f",'''{name}''' : '''{type} {value}'''"
 data = data+"\n"+x
 print(data)
 file = open("dictnory.txt", "w")
 file.write(data)
 file.close()

