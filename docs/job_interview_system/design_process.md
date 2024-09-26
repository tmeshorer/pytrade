# Process
# Intial design 
2. Find entities (OO)
2. Decide use case
3. For each entity estimate size. If entity contain poiner to media estimate media size
4. Estimate number for each entity.
5. Estimate total size per entity, 
6. Estimate total system size
4. For transaction entity estimate transaction per day (e.g. message per day) -> message per second
5. Estimate number of servers.
6. Design API
7. Component design
   - Mobile app -> LB -> Spotify Web server -> Database
   - Each type of data per database (e.g. audio/video) / blob of data.
   - Metadata server
   - Add cache per popular data (in front of audio data)
   - Add CDN for media.
   - Think about partition of  metedata (RDBMS)
   - Need to work on media or batch job - message queue and workers.
8. Scalability
9. Availbility


# Alg
- Geo hash
- Quad tree
- Consistent hash
- Leakybucket
- Tokenbucket
- Bloomfilter
- HyperLogLog
- Count mean sketch 

# Scaling
- Keep web tier stateless
- Build redundency on every layer
- Cache data as much as you can
- Multiple data center
- Static data on CDN
- Scale your data tier by sharding
- Split tiers into individual service

# Pref estimation
## Power of two
- 10 - 1Kb
- 20 - 1MB
- 30 - 1GB
- 40 - 1TB
- 50   1PB

## Availiblity
- 99 - 14.4 min
- 99.9 - 1.44 min
- 99.99 - 8.64 sec

## Query per second
- Active users
- Dailty active users
- Transaction per user per day
- Transaction artifact size
- QPS = DUA * transaction_per_day / 24 hours / 3600 secs
- Pick QPS = 2 * QPS
- Size = DAU * transaciton_per_day * size 
- 5 year size = Size * 365 * 5

# Questions
- Mobile app / web app
- Most important features
- DAU ?

# Deep Dive
- Hash function design
- Chat system - how to reduce latency

# Time allocation for each step
- Step 1 - 10 min
- Step 2 - 15 min
- Step 3 - 10 min
- Step 4 - 5 min

# Rate limiter
- Bucket alg. 


