list_64 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           '0','1','2','3','4','5','6','7','8','9',
           '+','/']

list_ASCII = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
              ' ','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',
              '0','1','2','3','4','5','6','7','8','9',
              ':',';','<','=','>','?',"@",
              'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
              '[',None,     #backslash giving problems... '\\' may work.?
              ']','^','_','`',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
              '{','|','}','~','\n']
#actuall ASCII dosent have \n at last index, i added that just to make this program better...

from number_to_binary import binary_to_num
from number_to_binary import num_to_binary

def encrypt_to_base64(text):
    text_hold = list(str(text))
    binary_string = ""
    output = ""
    padding = 0
    for i in range(0,len(text_hold)): #convert each letter to binary of length 8, concatinate in binary_string
        index_ASCII = list_ASCII.index(text_hold[i])
        binary_string += num_to_binary(index_ASCII,8)

    while (len(binary_string)%6)!= 0: #add 00 to complete 6 bit -> every 00 add 1 padding later
        binary_string += "00"
        padding += 1
    
    binary_list = list(binary_string)
    while len(binary_list) > 0: #minus away from binary list
        binary_6bit = ""
        for a in range(0,6):
            binary_6bit += binary_list[0]
            binary_list.pop(0)

        index_64 = binary_to_num(binary_6bit)
        output += list_64[index_64]


    for b in range(0,padding): #add padding
        output += "="
        
    return output
#end

def decrypt_from_base64(text):
    text_hold = list(str(text))
    padding = 0
    binary_string = ""
    output = ""
    while text_hold[len(text_hold)-1] == "=": #find num padding & remove it
        text_hold.pop()
        padding += 1

    for i in range(0,len(text_hold)): #change text to binary
        index_64 = list_64.index(text_hold[i])
        binary_string += num_to_binary(index_64,6)

    binary_list = list(binary_string)
    for a in range(0,padding*2): #for every padding remove 2 0s
        binary_list.pop()
    
    while len(binary_list) > 0: #minus away from binary list
        binary_8bit = ""
        for a in range(0,8):
            binary_8bit += binary_list[0]
            binary_list.pop(0)

        index_ASCII = binary_to_num(binary_8bit)
        output += list_ASCII[index_ASCII]


    return output
#end
