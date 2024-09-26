- Read replicas
- Load balancer
- Cache
  - When to cache
  - Eviction policy

Fault tolorate 
- Use DHT
- Map from key segment to node in paxos.
- Duplicate the key to clock wize N. Replicate.

# SRE Book - disributed concensus


# SRE
- SLO - Service level objective. 
- Service - product defliverd over the internet. 
- 500 - Not service that user are paying for.
- Relaibility is the absense of errors. Need to work on relaibility all the time.
- Improve services
  - High availiblity
  - High performant.
  - SLI
    - Availbility - number successfull http per minute
    - Latency
    - Freshness
    - Durability
  - Error budget 1 - SLO
  - 