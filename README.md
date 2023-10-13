# Encryption-and-Decryption-using-Python
Created a function in Python where a binary key (0 or 1) and a plaintext file in the directory are given. The function should perform XOR operation on the file with the key bit by bit and write the XORed result to a new file


## Execution steps Explained:

1) Get input of the file path from the user
2) Get input of the key from the user
3) Read the file as binary data
   Where 'r' in 'rb' stands for 'read', and the 'b' stands for 'binary'. So, 'rb' means that the file is opened in binary read mode. 
4) Converting the binary data to integers
5) Performing the XOR operation on each integer with the key
6) Converting the encrypted data back to binary
7) Writing the encrypted data to a new file
    Where 'w' in 'wb' stands for 'write', and the 'b' stands for 'binary'. So, 'wb' means that the file is opened in binary write mode.
8) Then theres and if-else statement which Print the corresponding message based on the key
9) and finally we Call the function.  
