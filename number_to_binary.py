##i am aware there is a built in function for this but im just doing this for fun :)

def num_to_binary(num, bits =6): #from left to right, minus off from num
    num_hold = int(num)
    bit_hold = int(bits)
    output = ""
    while len(output) != int(bits):
        bit_hold -= 1
        number = 2**bit_hold
        if number <= num_hold:
            num_hold -= number
            output += "1"
        else:
            output += "0"


    return output
#end

def binary_to_num(binary): #input must be string as numbers cannot start with 0...
    bit_hold = len(str(binary)) #from left to right, add to num
    binary_hold = list(str(binary))
    output = 0
    for a in binary_hold:
        bit_hold -= 1
        if a == "1":
            output += 2**bit_hold


    return output
#end
