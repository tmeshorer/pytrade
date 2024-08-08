# Colocation 

3. colocate data and code
   - L1 cache - 10 ns
   - DRAM     - 100 ns
2. Geo latency - latency between nodes 
3. CDN. typical deploy in one location
   - Far edge - close to end user.
4. Intranode latency 
   5. Network stack - orcastate the journey of packets.
   6. Network stack can introduce significant latency
   7. Numa vs non Numa node

## Replication
1. Have multiple copies of data to reduce latency and improve availability and scalability.
2. Latency imporove because you have copies close to the user.
3. Replication is like colocation which ensure multiple copies are in sync. 
4. Consistency models - trade off between consistency and latency
5. Price: multiple copies. For example, strong replication need 3 copies.
6. Replication also improve avaialibilty 
7. High availbility - operating a system with minimal downtime. 
8. HA defines as number of nines.
9. Scalbility - system handle increase utiliziation without comprising troughput or latency. 
10. Consistency model - consistency gureente - write visibile on all the replicas
11. Strong consistency - linearzability. 
12. Eventual consistency - gurntee that all replicas will eventually converge to the same state.
## Replication Strategies
1. Single leader replication - one node, the leader node, accept writes from the clients and 
   cordinates replication to the rest of the cluster. Require leader election.
2. Multi leader replication - multiple leader accept write.
3. Leaderless - amazon dynamo db.
4. Local first approche - CRDT. allow client to read and modify data localy
5. Async replication - faster response time. might lead to incosistences if the server failed. Eventual consistent.
6. Sync replication - primary wait for replication process to complete before ack the client.
7. State machine replication - Raft, Paxos, 1 failed node, require 3 node cluster. Assure that all nodes
   agree on the system current state. All nodes execute the system seq of changes.

# Partitioning
1. Colocation - put same thing at the same place.
2. Data is divided into similar subset, each accessible independetly. However need to support routing.
3. Divide logical data into smaller physical parts.
4. Can result in hot partition.
5. Joins are more complex.
6. key hash partition.
7. Key range partition.
8. Vertical partition -partition the columns. Used for OLAP.

## Request routing

1. Direct routing - the client knows which partition holds which key.
2. Proxy routing - client contact a proxy.
3. Forward routing - shards route to each other.

## Partition imbalance
1. Result from uneven distribution of data processing across partitions.
2. Hot partition - one parition is hot (e.g. zip code). Result when the values are unevenly distributed.
3. 

# Caching

1. Speed up data retrival by having temp copy of the data closer to where the data is accessed.
2. Need for example, database that does not change.
3. Also, might not be able to replicate.
4. Tradeoff freshnessfor reduced access latency. 
5. Cache storage can be main memory or disk. E.g. Redis.
6. Cache hit - cache has the copy of the value. 
7. Cache eviction - cache 10G, database 1T. 

## Caching Strategies
1. Cache aside caching - if there was a cache miss, the app read the value from backing store and store it in the cache.
   - Cache is just key/value store (e.g. redis)
   - Application is doing the cache management.
   - Need to handle cuncurrent cache access.
   - Can have significant tail latency becacuse the cache experaince
2. Read trough caching - the cache is active component when there is a cache miss.
3. 

