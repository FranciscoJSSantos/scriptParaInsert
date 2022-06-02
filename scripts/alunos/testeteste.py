string1 = 'null'
file1 = open("archives/matricula.txt", "r")



readfile = file1.read()

if string1 in readfile: 
    print('String', string1 , 'Found') 
else: 
    print('String', string1 , 'Not Found') 
    
file1.close() 