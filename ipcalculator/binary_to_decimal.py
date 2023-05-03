
#Filter only numbers from terminal
def decimal_con(sort_input,options):
        
    decimal_input = []


    if len(sort_input) == 3:

        if sort_input[1] == options[0] or sort_input[1] == options[1]:

            for char in sort_input[2]:

                if char.isdigit():

                    decimal_input.append(char)

    return decimal_input



#Convert into decimal
def decimal_fun(decimal_input):
        
        decimal_output = []
        number = len(decimal_input)
        decimal_final = 0

        for b in decimal_input:

            number = number - 1

            if b == '1':

                decimal_output.append(2**number)

            else:

                decimal_output.append(0)

        for element in decimal_output:

            decimal_final += element

        return decimal_final 



#Convert into binary
def binary_fun(decimal_input):
        
        binary_input = int()
        binary_bits = int()

        if not decimal_input:
            
            None

        else:
            
            binary_bits = ()
            binary_input = int("".join(decimal_input))
            binary_input = (bin(binary_input))
            binary_input = binary_input.replace("0b", "")
            binary_bits = len(binary_input)
            binary_bits = str(binary_bits).split()



        return binary_input, binary_bits

