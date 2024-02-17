import socket
from common_ports import ports_and_services
  
def get_open_ports(target, port_range, verbose = False):
  open_ports = []
  #check for open ports in the given range
  for port in range(port_range[0], port_range[1] + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    #chack for the vaidity of the target
    try:
      #check if the port is open, connect_ex returns 0 if it's successfull
      result = s.connect_ex((target, port))
      if result == 0:
        open_ports.append(port)
        #if it catches exception the target is invalid
    except socket.error:
      if target[0].isalpha():
        return "Error: Invalid hostname"
      return "Error: Invalid IP address"
    s.close()
  #check for the outpout format
  if not verbose:
    return open_ports
  else:
    url = ''
    ip = ''
    output = "Open ports for "
    if target[0].isalpha():
      url = target
      #takes the ip from the url
      ip = socket.gethostbyname(target)        
    else:
      ip = target
      #check if there is a valid url from the already checked ip
      try:
        url = socket.gethostbyaddr(target)[0]
      except socket.error:
        url = ""
    #create the output string
    if url:
      output += url + " (" + ip + ")"
    else:
      output += ip 
    output += "\nPORT     SERVICE"
    for port in open_ports:
      output += "\n" + str(port).ljust(9) + ports_and_services[port]
    return output