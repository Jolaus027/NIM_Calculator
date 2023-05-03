
#SORT                                                               

def sort(terminal_w):
    sort_input = []
    element = ""
    count = 0

    b = ""
    c = ""

    sort_command = False
    sort_content = False
    word_command = False


    for i in terminal_w:
        
        count += 1   
        
        if i == "m" and b == "i" and c == "n":
            
            sort_input.append("nim")
            
            
        elif i == "-" and b == " " and c == "m":
            
            sort_command = True
            
            
        elif sort_command == True:
            
            if i.isalpha() and sort_command == True:
                
                element += i

            else:
                
                sort_command = False
                sort_input.append(element)
                element = ""
                
                
        elif len(sort_input) == 2:
            
            if not i.isalpha() and b == " " and c == sort_input[1][-1] and c.isalpha:
                sort_content = True


        if sort_content == True:
            
            if i == " ":
                
                sort_content = False
                sort_input.append(element)
                element = ""

            else:  

                element += i


        elif i in ["c","e"] and word_command == False and sort_command == False:
            
            word_command = True
            element += i


        elif word_command == True:
            
            if i.isalpha():
                element += i

            else:
                
                sort_input.append(element)
                element = ""
                word_command = False


        if len(terminal_w) == count:
            sort_input.append(element)
            break

        c = b
        b = i

    sort_input = [x for x in sort_input if x != '']

    return sort_input






#COMPARE
def compare(terminal_w):
    sort_input = sort(terminal_w)
    right_input = ""
    difference = ""
    clear_difference = ""

    input_error = ""

    if len(sort_input) >= 3:
        
        right_input += sort_input[0] + " -" + sort_input[1] + " " + sort_input [2]
        

    elif len(sort_input) == 2:
        
        right_input += sort_input[0] + " -" + sort_input[1]

    elif len(sort_input) == 1:
        
        right_input += sort_input[0]


    difference = terminal_w.replace(right_input, "")
    

    for g in difference:
        
        
        if g == " " or g =="":
            
            None
            
            
        else:
            
            input_error = "2"
            break

    for m in difference:

        if m != " " or g != "":

            clear_difference += m
        
        else:

            None
        
    return input_error, difference
        
