
#FUNCTIONS
from sort_and_compare import sort, compare  #for sorting terminal input

from binary_to_decimal import decimal_con, decimal_fun, binary_fun  #converts binary into decimal and reverse

from ip_class import ipclass_fun #ip adress class

from errors import default_errors, err #error messages and errors

from nim_text import nim_banner_fun, nim_help, help_ipclass, help_binaryintodecimal, help_decimalintobinary #text-based messages 

from nim_ai import nim_ai_fun #ai for helping


#MODULES
from colorama import Fore

from termcolor import colored

import os 

import sys

import os







#Welcome Page

nim_banner_fun()
print("")

                                                                ##COMMANDS## 
                                                                

                            
#Default command before every command                                                                       
nim = "nim"


#Help command
help = "help"

#Other help commands
help_other = ["--b", "--d", "--c"]

#Options

options = ["b", "d", "c", "ai"]

#Exit
exit_command = "exit"


#Clear command
clear_command = "clear"







                                                            ##TERMINAL##



while 1:

    terminal_w = input(colored("nim $ ", 'red', attrs=['bold']))


    sort_input = (sort(terminal_w))
    input_error, clear_difference = (compare(terminal_w))
    decimal_input = decimal_con(sort_input,options)
    binary_number, count_bits = binary_fun(decimal_input)

                                                            ##ERROR MESSAGES##



    bad_usage, not_found, not_binary_number, enter_option, unexpected = default_errors(terminal_w) #default errors
    error, error_message = err(sort_input,options)
    


                                                        ##TEMINAL STATEMENTS##

    if not terminal_w.strip():  # check if input is empty or whitespace
        continue  # start a new iteration of the loop without executing the code below

    if len(sort_input) >= 1 and nim in sort_input[0] and input_error == "" :


        #help 

        if len(sort_input) == 2 and sort_input[1] == help and input_error == "":

            nim_help()
            
        #other help functions    
        elif len(sort_input) == 3 and sort_input[1] == help and input_error == "":
            
            if sort_input[2] == help_other[0]:
                
                help_decimalintobinary()
                
            elif sort_input[2] == help_other[1]:
                
                help_binaryintodecimal()
                
                
            elif sort_input[2] == help_other[2]:
                
                help_ipclass()
            


        #convert to binary
        elif input_error == "" and len(sort_input) == 3:
            
            if options[0] == sort_input[1]:




                if error in "2":

                    print(error_message) 


                else:

                    print(Fore.WHITE + 'Your binary number:', colored(binary_number, 'green', attrs=['bold']))
                    print((Fore.WHITE + 'And has:'),(colored(' '.join(count_bits),'green', attrs=['bold'])+ ' ' + colored('bits', 'green', attrs=['bold']))) 


            #convert to decimal 

            elif options[1] == sort_input[1]:



                if error == "3":

                    print(error_message)
                    
                else:


                    print((Fore.WHITE + 'Your decimal number:'),(colored(decimal_fun(decimal_input), 'green', attrs=['bold'])))


            #ip class

            elif options[2] == sort_input[1]:


                if error == "1":

                    print(error_message)

                else:


                    print((Fore.WHITE + 'Your IP is class'), (colored(ipclass_fun(terminal_w),'green', attrs=['bold'])))


            #bad usage error

            elif input_error == "2":

                print(f"unexpected + '{clear_difference}'")

            else:

                print(bad_usage)
                
        #NIM AI

        elif len(sort_input) == 2 and options[3] == sort_input[1]:
                
            nim_ai_fun()

                    

        
        #enter option 
        elif input_error == "" and len(sort_input) == 1:
            
            print(enter_option)
        
        else:
            
            print(bad_usage)
        
    #clear    
    
    elif len(sort_input) >= 1 and sort_input[0] == clear_command and input_error == "":
            
            clear = os.system('clear')


    #exit

    elif len(sort_input) >= 1 and sort_input[0] == exit_command and input_error == "":
        
        sys.exit()
 
 
    #not found command error

    else:

        print(not_found)

    print(sort(terminal_w))


