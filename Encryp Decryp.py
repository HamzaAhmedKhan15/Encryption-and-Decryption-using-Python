def encrypt_file():
    
    file_path = input("\nEnter the path to the file: ")     # Getting input of the file path from the user
    key = int(input("\nEnter the key (0 or 1): "))       # Getting input the key from the user

    with open(file_path, 'rb') as file:         # Read the file as binary data
        data = list(file.read())               
        
        #The 'r' in 'rb' stands for 'read', and the 'b' stands for 'binary'. 
        # So, 'rb' means that the file is opened in binary read mode

    data = [int(byte) for byte in data]       # Converting the binary data to integers
    
    encrypted_data = [byte ^ key for byte in data]     # Performing the XOR operation on each integer with the key
    
    encrypted_data = bytes(encrypted_data)         # Converting the encrypted data back to binary

    with open('encrypted_file.txt', 'wb') as file:             # Writing the encrypted data to a new file
        file.write(encrypted_data)
        
    if key == 1:
        print("\nYour file is Encrypted!\n")
    elif key == 0:                                       #    Print the corresponding message based on the key
        print("\nYour file is Decrypted!\n")
    else:
        print("\nInvalid key! Please enter 0 or 1 \n")

encrypt_file()          # Call the function
        
        
      
      
      
      
      
      
      
      
      
   