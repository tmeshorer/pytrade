# Sytem
- Set of interconnected components, that has expected behivor on its interface with the env.
- Large number of components, Large number of interconnections
- 
- 
- 
- load balancing
- consistent hashing
- R/W ratio
- Design for single server - DB schema / API / Business logic.
- Database layer - caching / read replicas
- Horizontal sharding - breaking single table across multiple database schema.
- Schema changes must be cordinateed across all shareds, postgress is not longer transaction.
- Wrote a db proxy.
- pg bouncer.

# System Concepts
- Comunication
    - Server communicate with each other 
    - Sync or async
- Consistency
  - All replicas to have the same view of data.
  - Any update immidely reflected on all replica nodes.
  - Each read has the most value of write.
  - Ensure consistency
    - Data replication.
    - Consenus protocol - all replicate agree on the update.
    - Conflict resolution
  - Techniqe to assure
    - Write ahead logging.
    - Locking
    - Data versioning
  - Spectrum model
    - Strong consistency - all replica have the same view
    - Monotonoc read
    - Eventual consistency
- Availibity
  - Precentage of time the system was up / total time.
  - Sequencal system vs parallel
  - Assuring:
    - Reduncency
    - Fault tolorant 
    - Load balancing
  - Fail over pattern
    - Active - Active / Active Passive
  - Replication Patterns
    - Multi leader replication
    - Single leader replication
- Realbility
  - Ability of system to perform its intended function without fail. 
  - MTBF
  - MTTR - Mean time to repair
- Scalability
  - Vertical scaling
  - Horizontal scaling
- Maintainability

## Fault Tolorance
- Require the system to recover from any failure. 
- Replication - replicate the service thus multiple replica server and multi copy of data.
  - Data served from replca store
- Checkpoint
  - Data is stored and backed up.
  - Sync Checkpointing
  - Async Checkpointing
# Falaclis of distributed computing
- Relaible networks
  - Network outage.
  - Zero latency
    - Bring client close to the data.
  - Infinite bandwidth
    - Quiing delays. bottleneck
  - Secure network
  - Fixed topology
  - Single admin

## Tradeoffs
- Capture latency trough prencile
- Performance vs scalbility
- Concistency vs avaialbility
- CAP Tehorem.

## System design process
- Idenfiy core requirments
- Minimize the number of compoenents.
- Make the system easy to use.


   