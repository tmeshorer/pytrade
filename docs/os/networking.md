- Like a gift
- gift / package has an address. 
- gift box is hiding the item
- Place inside a box for shipping, protect the gift box.
- Carry the box, based on pallete, go to single location. 
- Encapsulation - put somthing in a box.
  - hide
  - protect , keep them from damage
  - group them

Addresses
----------
- Some information on the box itself.
- Put the person name on the gift box.
- Next address on the pallete. Take groping of items to a warehouse. 
- Each stage of jurney, different address.
- Address make sense withing the context
- Abstraction - abstract the item, address containing the person. Region is abstraction
- Multicast - more than one person in one.
- Unicase

# Network
 Application - Application (Segment)
 Host -> Host (Packet)
 Network -> Network (Frame)

# Headers
  pysical header / network header / Application header

# Addresses
- Application - Port/Socket
- Logical interface on host / interface address (packet)
- Pysical address - MAC address.

# Protocol
- All lang are protocol 
- Share grammer and dictionary 
- Communicate information.
- What symbol means
- Grammer, how I format the symbol.
- One protocol to transport thing - Transport protoocl
- Need to know the destenation - Routing protocl.
- Transport proptol (switch protocol)
- Routing protocol - give me direction. 

# IP v4
- 4 parts. Decimal format. 
- IP 6 - Use Nat- IPv6. 
- IP v6 - 128 bit. 

# Assiging address
- Local network - DHCP / DHCP server that the host talk to.
- Host discover packet. 


# Switching packets
- If not on the same segement
- Send the packet to the default router.
- Host A ARP for C address.
- C build a new frame

# Internet
- Access provider - last mile network
- Content provider - linode.
- Access connect to commercial buildings. Focus network as service for the business.
- Governece part of the internal - IANA-> assign IP address.
- Domain name system - DNS providers provide name
- Access provider -> Transit provider-> content provider.

# DNS
- DNS name things on the internal
- Org
- Computer
- Top level domain - .org/.com, 
- Example example.com
- Subdomain.
- www.example.com
- Networking stack build a dns query, call recursive
- Walk trough from right to left, until he get to IP.
- It also cache
- Recursive server -> ask root server . 13 addresses. TLD from .com.
- Root server for .com, 
- Recursive server, ask the autoretative server, ask example.com

# Networking tools
- ip
- ping
- tracerout
- nslookup
- 