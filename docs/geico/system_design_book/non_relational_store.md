# Over view
- novel data models.
- Prioritize scalability , fault tolorant , low latency access.
## Concepts
- Schema flexilility  - allow dynamic schema
- Data Model
  - Document Store - Json
  - Key Value store
  - Column Family Store - Store data in column families
  - Graph database
- Scalability - designed to scale
- HA
- Basicaly available.
## Key Value Database
- Key/Value as data model
- Primary Key - Uniqe
- Parition Key - used for data distribution
- API
  - GetItem
  - PutItem
  - UpdateItem
  - DeleteItem
- Leaderless replication
  - Can send key/value to any node
  - Save on quarom
- Consistent hashing
  - Ring
  - Each node assume position using an hash function
- High avaialbilty
  - Optimistic replication
  - Allow subset of replicat to ack
- Tradeoff
  - Limited query

## Open source key value database
- Dynamo
  - Simple key value model

# Document database
- Store documents. JSON
- DataModel
  - Collections
  - Document - fundemtal unit of data
  - Insert / Update / Delete
  - Replica set - groups of nodes that store multiple copies of the data.
  - Primary/Secondery node cluster - 
  - Heartbit

# Columnar databases
- Group columns into column families
- Keys
  - Parition key
  - Clustering key
- Offer eventual consistency / Strong consistency
- Architecture
  - Commit log
  - Memtable, sturuced hash table
  - SSTable - sorted by key
- Good for data warehousr
- Cassandra
  - CQL
  - Distributed architecture
  - Linear Scalability

# Graph databases
    - Present graph