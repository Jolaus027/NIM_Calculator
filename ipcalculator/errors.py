
import re

 
#Filter terminal input and save ip address 

#Default errors
def default_errors(terminal_w):


    bad_usage = ("Error: bad usage")

    not_found = ("Command '" + terminal_w + "' not found\nTry 'nim -help' for more information")
    
    not_binary_number = ("Your number is not in binary!\nBinary numbers are '0' and '1'")
    
    enter_option = ("Please enter the option")

    unexpected = ("Unexpected character ")

    return bad_usage, not_found, not_binary_number, enter_option, unexpected





#Errors for decimal to binary function
def errors_decimal_to_binary_fun(sort_input,options):

    error_decimal_to_binary = ""

    if len(sort_input) == 3 and sort_input[1] == options[0]:

        for i in sort_input[2]:
            if i.isdigit():

                None

            else:

                error_decimal_to_binary = "1"
                break




    return error_decimal_to_binary



#Errors for binary to decimal function
def errors_binary_to_decimal_fun(sort_input,options):

    error_binary_to_decimal = ""

    if len(sort_input) == 3 and sort_input[1] == options[1]:

        for i in sort_input[2]:

            if i.isdigit():

                if i != "0" and i != "1":

                    error_binary_to_decimal = "2"

                    break

                else:

                    None

            else:

                error_binary_to_decimal = "1"
                break

    return error_binary_to_decimal




#Errors for ip class function
def errors_ip_fun(sort_input,options):

    error_ip_class = ""
    first_byte = ""



    ipv4_binary_pattern = r'^(([01]{8})\.){3}([01]{8})$'
    ipv4_binary_pattern_classd = r'^(([01]\d\d|2[0-2]\d|23[0-2])\.){3}([01]\d\d|2[0-2]\d|23[0-2])$'
    ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'


    if len(sort_input) == 3 and sort_input[1] == options[2]:
            

        if re.match(ipv4_pattern, sort_input[2]):
            
            for i in sort_input[2]:

                if i != ".":
                    
                    first_byte += i
                    
                else:
                    
                    break   

            first_byte = int(first_byte)
        
            if first_byte > 223:
                
                error_ip_class = "6"

    
        elif re.match(ipv4_binary_pattern, sort_input[2]):


            if re.match(ipv4_binary_pattern_classd, sort_input[2]):
            
                error_ip_class = "6"

            else:

                None

                        
        elif "/" in sort_input[2]:

            error_ip_class = "3"

        elif sort_input[2].count(".") < 3:

                error_ip_class = "1"
                        
        elif sort_input[2].count(".") > 3:

                error_ip_class = "2"

        else:
                
            error_ip_class = "4"


    return error_ip_class






#Function for printing error messages and passing them to main.py
def err(sort_input,options):

    error_ip_class = errors_ip_fun(sort_input,options)
    error_decimal_to_binary = errors_decimal_to_binary_fun(sort_input,options)
    error_binary_to_decimal = errors_binary_to_decimal_fun(sort_input,options)
    error_message = ""


    if error_ip_class == "1":

        error = "1"
        error_message = ("Error: you probably did not put enough '.' to define octets of your ip, , try 'nim -help --c'")

    elif error_ip_class == "2":

        error = "1"
        error_message = ("Error: you probably put more '.' to define octets of ip than it's needed, try 'nim -help --c'")
    
    elif error_ip_class == "3":
        error = "1"
        error_message = ("Error: you can't use '/' with 'nim -c' command, try 'nim -help --c'")


    elif error_ip_class == "4":

        error = "1"
        error_message = ("Error: invalid IPv4 address, , try 'nim -help --c'")

    elif error_ip_class == "5":

        error = "1"
        error_message = ("Error: unexpexted character after IP address")
        
    elif error_ip_class == "6":

        error = "1"        
        error_message = ("Error: function works only with classes A,B and C, this is probably class D adress, which is used for multicast, try 'nim -help --c'")



    elif error_decimal_to_binary == "1":
        error = "2"
        error_message = ("Error: bad input number, try 'nim -help --b'")

    elif error_binary_to_decimal == "1":

        error = "3"
        error_message = ("Error: bad input number, try 'nim -help --d'")

    elif error_binary_to_decimal == "2":

        error = "3"
        error_message = ("Error: this is not binary number, binary number has only '0' and '1', try 'nim -help --d'")

    else:

            error = "0"


    return error, error_message


