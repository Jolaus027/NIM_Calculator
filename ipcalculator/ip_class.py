import re


def ipclass_fun(terminal_w):
        
        ipclass_input = []
        
        count = 1
        
        numbers = ['1','2','3','4','5','6','7','8','9','0','.','/']
        symbols = ['.', '/']
        
        ip_class = ""
        ip1 = ("")
        ip1_len = int()
        ip1_dec = ""

        for i in terminal_w:

            if i in numbers:
                
                ipclass_input.append(i)

            else:
                
                None

        for g in ipclass_input:

            if g not in symbols:
                
                ip1 += (g)
                count += 1

            if g in symbols:
                
                del ipclass_input[0:count]
                break 

        count == 1
        count2 = 1 
        
        ip1_dec = bin(int(ip1))
        ip1_dec = ip1_dec.replace("0b", "")
        ip1_len = len(ip1_dec)
        
        
        
        if re.match("^[01]+$", ip1) and len(ip1) > 3:
            
            for z in ip1:

                count2 += 1

                if z in "0" and count2 == 2:
                    
                    ip_class += "A address"
                    break

                if z in "0" and count2 == 3:
                    
                    ip_class += "B address"
                    break

                if z in "0" and count2 == 4:
                    
                    ip_class += "C address"
                    break
                
        else:
            
            if ip1_len < 8:
                
                ip1_dec = (8-ip1_len)*"0" + ip1_dec
                

            for p in ip1_dec:

                count2 += 1

                if p in "0" and count2 == 2:
                    
                    ip_class += "A address"
                    break

                if p in "0" and count2 == 3:
                    
                    ip_class += "B address"
                    break

                if p in "0" and count2 == 4:
                    
                    ip_class += "C address"
                    break


        if ip1 == "127":
            
            ip_class += "\nThis is loopback address"

        else:

            None

        return ip_class