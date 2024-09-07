# Storage:
  - RAM - store temp data.
  - SRAM - fast and expensive RAM
  - DRAM - slower and cheaper than SRAM. DDR4 / DDR5.
  - GDDR6.
  - BIOS - handling over control
  - HDD - Stored data on magnetic disk
  - SSD - Naned based flash memory. 
  - NVME - Connect to PCIE. 
# DNS
  - Translate domain name (www.google.com) to IP address.
  - Root -> DNS resover (cloud flare 1.1.1.1)-> Cache. Found name server.
  - Autheritative name server.  Root -> TLD nameserver -> 
# Latency numbers
  - CPU register - sub nanosec. 
  - L1 / L2 cache - 10 ns . also branch mis prediction
  - L3 Cache (shared) 100 ns. Main memory access 
  - System call - hunders of nano second. MD5 hadh. 100-1000ns
  - 1-10 microsec - context switching thread. copy 64k
  - 10-100 microsec - ngnix http req. reading 100. Read 9kp SSD
  - 100 micro - 1 ms - SSD write page, inta zone 100 micro sec. Memcach/Reddit read data.
  - 1 - 10 ms - Inter zone (5 ms), HDD
  - 10 - 100ms - US East , West cost
  - 100 - 1000 ms - Bcrupt a password. TLS handshake (250 ms). Network round trip. Read 1GB from SSD.
# Rest API
  - API - Two computer to talk. 
  - REST API - Rep state transfer.
  - Loose set of rules.
  - Orgnizied resources into URI /api/v1/products [By nouns not verb]
  - GET /api/v1/products.
  - Request over HTTP
  - POST /products
  - POST - create new resource
  - GET - read data
  - PUT - update existing resource
  - DELETE - remove existing resource. 
  - Options body - encoding in json
  - Server return respoinse HTTP 1.1 200 OK (status code)
  - 200 - Successful
  - 400 - somthing was wrong
  - 500 - mistake at the server level. 
  - POST - not idempotent. 
  - Response is options - Formatted in json. 
  - REST should be stateless. Easy to scale.
  - Use pagenetion (limit and offset)
  - Versioning of an API is important. 
# Key Data Structure
  -  List - Essential - storing for storing. Task managmenet , store tasks. Social media application
  -  Array - Fixed size order collection of elements.
  -  Storing large dataset - Temp easy calc. Used in image processing.
  -  Stack - Last in / first out - undo and redo operation. Store each change. revert to prev state.
  -  Queue - FIFO, send user action in game. in chat store messages in the order
  -  Heaps - task scheduling, implement priority queues. Highest and lowest priorities. 
  -  Tree - data bases indexing. Decision trees. Used in database indexing. BTREE , B+TREE
  -  Hash tables - effienct data lookup . Cache system, compilers. Store index data.
  -  Symbol tables in compilers. 
  - Suffix tree - specialied searching trees in documents. 
  - Graphs - social network, recommendation enginer. Facebook - analzing netowkr
  - RTree- mapping apps. Store spatial data. 
# Cloud native
  - Need microservices . Small application. 
  - Break the functionality into smaller microservices. 
  - Communicate with well defined api. 
  - Containers - packaged in container. lightweight component.
  - Container orcestation manage large number of containers. 
  - Each microservice has its own db.
# Top 5 Redis Use cases
  - 