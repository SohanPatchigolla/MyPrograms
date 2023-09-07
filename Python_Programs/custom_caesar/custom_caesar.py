import sys

def custom_caesar():
    
    # user input
    keyuse = input("Use default key y/n?: ")
    
    # selection of key use and error handling
    if keyuse.upper() == 'Y'or keyuse.upper() == 'N':
        pass
    else:
        sys.exit("Error: try again, choose (y/n)")
        
    # select mode
    mode = input("Press 'E' to Encode/ 'D' to Decode: ")
    
    # mode input and error handling
    if mode.upper() == 'E':
        text = input("Enter plain text: ")
    elif mode.upper() == 'D':
        text = input("Enter cipher text: ")
    else:
        sys.exit("Error: try again, choose 'E' or 'D'")
     
    # keys 
    if keyuse == 'y' or keyuse == 'Y':
        # default key
        key = 'w*D}#hLkXs1WO|5{6VlFM=+Pe-3moqJ:,A<9]QbYGuNn[&? Zaz%HgrBf7)dt\i0vUySjI.8c/4\'xK_C2!>EpR("$;T@' 
    elif keyuse == 'n' or keyuse == 'N':
        # insert key
        key = input("Enter your key here: ")
    
    # algorithm
    l = len(key)
    values = key[l//2:l] + key[0:l//2]
    values = values[4:]+values[:4]
    
    # creating two dictionaries
    encrytDict = dict(zip(key, values))
    decryptDict = dict(zip(values, key))
    newText=''
    
    #encode and decode
    try:
        if mode.upper() == 'E':
            newText = ''.join([encrytDict[letter]
                                  for letter in text.lower()])
        elif mode.upper() == 'D':
            newText = ''.join([decryptDict[letter]
                                  for letter in text.lower()])
        else:
            print()
            print("Please try again, wrong choice entered")
    except KeyError as e:
        print('symbol not found', e)

    return newText

# output
print(custom_caesar())
