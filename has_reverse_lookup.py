#!/usr/local/env python3

import socket

# Accepts a list of str, an int, or a str
# Returns whether the input has DNS reverse lookup records for each

def has_reverse_lookup(ip_addr):
    output_str = ''
    if type(ip_addr) == 'list':
        for x in ip_addr:
            rlookup = ''
            try:
                rlookup = socket.gethostbyaddr(x)
		out_str = str(x + " has a reverse lookup record of " + rlookup)
                output_str += out_str + ". \n"
            except Exception:
                out_str = str(x + " has no reverse lookup record")
                output_str += out_str + ". \n"
    elif type(id_addr) == 'int' || type(ip_addr) == 'str':
        rlookup = ''
	ip = str(ip_addr)
        try:
            rlookup = socket.gethostbyaddr(ip)
            output_str = ip + " has a reverse lookup record of " + rlookup
        except Exception:
            output_str = "No reverse lookup found for " + ip + "."
    else:
        return(str(ip_addr) + " is neither a list, an int, nor a str. Unable to process the request.")
    return output_str

