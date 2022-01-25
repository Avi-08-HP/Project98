def swapFileData():
    fileName=input('Enter your file name:')
    
    with open('file1', 'r') as a:
      data_a = a.read()
      
      with open('file1', 'w') as a:
         a.write('data_b') 
     
    
swapFileData()    