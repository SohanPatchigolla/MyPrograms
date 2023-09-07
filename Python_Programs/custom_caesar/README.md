# Custom Implentation of Caeser Cipher in Python:
- I have imported sys library and created a function called custom_caesar()
- First, the programs asks user to input y/n to use default key or insert one.
- Then it checks for false input, here i have used sys.exit() and if else to implement.
- Next, it asks user to input 'E' for encryption/ 'D' for decryption.
- Again we check for errors in input using sys and if, elif, else.
- I created an algorithm (In which i interchange first and second half of string and pass though caesar cipher with shift value of 4) using string 'key' to generate string 'values'.
- For encryption/decryption i create variables and zip dictionaries of key,values/values,keys pairs.
- Finally, we match key for each value using try and except and store it in 'newText' empty string using join.
- The functions returns 'newText', and print custom_caesar() as output, outside the function. 
