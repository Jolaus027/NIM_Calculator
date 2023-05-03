from colorama import Fore
from termcolor import colored
from pyfiglet import Figlet


def nim_banner_fun():

    #WELCOME PAGE
    nim_banner = Figlet(font='banner3-D')
    print(colored(nim_banner.renderText("NIM"), 'red', attrs=['bold']))
    print(colored("NIM - Network Manager", 'red', attrs=['bold']))
    print(Fore.RED + "Run 'nim -help' to see more options!")
    print(colored("-------------------------------------", 'red', attrs=['bold']))



def nim_help():

    #HELP BANNER
    nim_help = Figlet(font='banner3-D')
    print(colored(nim_help.renderText("HELP"), 'red', attrs=['bold']))


    #MESSAGE
    print(Fore.WHITE + "This is a bacic help page with the list of avalaible commands. To see all options for each command simply type 'nim -help --[name of the command(for example 'c')]'\n ")


    #USAGE
    print(colored("Usage of NIM commands\n---------------------\n", 'green', attrs=['bold']) + Fore.WHITE + "'nim' " + Fore.CYAN + "-command" + Fore.YELLOW + " ip adress/decimal_number/binary_number...")
    print(colored("Example: ", 'light_magenta', attrs=['bold']) + Fore.WHITE + "'nim -b 126'\n")

    #AI
    print(colored("NIM AI\n------\n", 'green', attrs=['bold']) + Fore.WHITE + "NIM AI is a ChatBot based on Davinci model. AI is trained" \
        " specifically for this tool.\nIt is here to help you if you don't understand any of the tools of NIM.\n")
    

    #DECIMAL INTO BINARY
    print(colored("DECIMAL INTO BINARY TOOL\n------------------------\n", 'red', attrs=['bold']) + Fore.WHITE + "This tool is for converting decimal numbers into binary numbers.")
    print(colored("Command: ", 'yellow', attrs=['bold']) + Fore.WHITE + "'-b'")
    print(colored("Example: ", 'magenta', attrs=['bold']) + Fore.WHITE + "'nim -b 154'\n")


    #BINARY INTO DECIMAL
    print(colored("BINARY INTO DECIMAL TOOL\n------------------------\n", 'red', attrs=['bold']) + Fore.WHITE + "This tool is for converting binary numbers into decimal numbers.")
    print(colored("Command: ", 'yellow', attrs=['bold']) + Fore.WHITE + "'-d'")
    print(colored("Example: ", 'magenta', attrs=['bold']) + Fore.WHITE + "'nim -d 0100101'\n")


    #IP CLASS
    print(colored("IP CLASS TOOL\n-------------\n", 'red', attrs=['bold']) + Fore.WHITE + "Determines what class is your ip adress.")
    print(colored("Command: ", 'yellow', attrs=['bold']) + Fore.WHITE + "'-c'")
    print(colored("Example: ", 'magenta', attrs=['bold']) + Fore.WHITE + "'nim -c 192.168.1.141'\n")



def help_decimalintobinary():

    print(colored("DECIMAL INTO BINARY TOOL\n------------------------\n", 'red', attrs=['bold']) + Fore.WHITE + "This tool is for converting decimal numbers into binary numbers.\n"\
          "You can learn how converting decimal numbers into binary numbers works here: " + Fore.BLUE + "https://www.youtube.com/watch?v=rsxT4FfRBaM")
    print(colored("Command: ", 'yellow', attrs=['bold']) + Fore.WHITE + "'-b'")
    print(colored("Example: ", 'magenta', attrs=['bold']) + Fore.WHITE + "'nim -b 154'\n")

def help_binaryintodecimal():
    print(colored("BINARY INTO DECIMAL TOOL\n------------------------\n", 'red', attrs=['bold']) + Fore.WHITE + "This tool is for converting binary numbers into decimal numbers."\
          "\nPlease enter only binary numbers with '0' and '1'.\n"\
            "You can learn how converting binary numbers into decimal numbers works here: " + Fore.BLUE + "https://www.youtube.com/watch?v=VLflTjd3lWA")
    print(colored("Command: ", 'yellow', attrs=['bold']) + Fore.WHITE + "'-d'")
    print(colored("Example: ", 'magenta', attrs=['bold']) + Fore.WHITE + "'nim -d 0100101'\n")


def help_ipclass():

    print(colored("IP CLASS TOOL\n-------------\n", 'red', attrs=['bold']) + Fore.WHITE + "Determines what class is your ip adress. You have to devide each byte of"\
          "\nip address with dot. Don't use class D addresses, because tool won't recognize them.\nA valid IP address must be in the form "\
          "of A.B.C.D, where A,B,C and D are numbers from 0-223.\nThe numbers cannot be 0 prefixed unless they are 0, so here is bad example '192.01.01.1'.\n"\
          "Tool doesn't make differences between local and public ip's.\n"\
            "You can find more info abou classful addressing here: " + Fore.BLUE + "https://www.boardinfinity.com/blog/classful-addressing")
    print(colored("You can also type ip address in binary notation!!!", 'white', attrs=['bold']))

    print(colored("Command: ", 'yellow', attrs=['bold']) + Fore.WHITE + "'-c'")
    print(colored("Example: ", 'magenta', attrs=['bold']) + Fore.WHITE + "'nim -c 192.168.1.141'")
    print(colored("Binary Example: ", 'magenta', attrs=['bold']) + Fore.WHITE + "'nim -c 11000000.10101000.00000001.10001101'\n")
















#"\n   --mask: gives you your subnet mask based on ip adress and number of your networking bits or your broadcast, for example: 'ip --mask 192.168.1.1/24'" \
#"\n   --broadcast: gives you your broadcast address based on ip adress and number of your networking bits or your subnet mask" \


