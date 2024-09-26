# Networking components
- Forward proxy - Mediate between client device and the internet. Enforce cooporate access control.
- Reverse Proxy - Internet and web server. Offloading SSL.
- Load balancer - distribute traffic across we bservers, L4 or L7
- API Gateway
  - Security policy
  - Rate limiting
  - Auth
  - Authz
- Load balancing benefits
  - Scalabilities
  - HA
  - Performance
  - 
- Global load balancer
- Local load balancer
- Load balancer between each tier
  - Between web server - no single server is overwelemed
  - Between application server - no application server is overwelmed
  - Between database server - for read only replica
## Load balancing alg
    - Round Robin
    - Weighted round robin
    - Least Connection
- Dyanmic
  - Least Response time
  - Hash based algorithm
  - Lease Loaded
- Sticky session
  - Store session in cookie. Source
# Load Balancer Types
- DNS load balancer - distribute traffic at the DNS level
- L4 load balancer
- L7 load balancer
# Load balance type
- Hardware load balancer
- NGINX
- Layer 4 and Layer 7 load balancer
- 