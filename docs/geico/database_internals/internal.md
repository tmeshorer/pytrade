

Shared model
----------
- Shared model - database
- What happen with a process does not recieve response
  - Fully synch communication. 
- What is the nature of the crash - failure model
  - Temp faulure
  - Ommit message
- Fault tolorance - property that describe the system realibility, continue to operate under failure. 
  - Network is not perfect - retry / reconnect.
  - Bandwidth is not finaite.
  - Processing take time. Processing not start as soon as the msg arrive - pending queue.
  - Qeueue capacitiy is not infitie. Need to apply backpressure.
  - Msgs are sitting in the queue. 
## Network partition
- when two systems cannot communicate.


# Distibuted system Abstraction
## Links
- Send a msg from sender A to Recipient B
  - Not yet deleivered
  - Lost
  - Deleivered.
- Fair loss - if both sender and recievers are correct.
- Solve with ack from the B. 
- Msg can arrive in different order, or more than once. 
- Twe general problem - cannot reach concensus. 
- Failures:
  - message loss
  - network parition
  - deduplication
% Leader election
  - Distribured lock - let you select app, only one instance read.
  - Only one write the status back.
  - 
  - Avoid comm overhead, processes elect leader.
  - Cannot gurntee safety. since we can have split brain.
  - Election occur at start time. or when the leader crushed.
  - Distibuted locking. 
  - Leader - avoid sync state between remote participants, reduce the number of exchanged messages. 
  - We can have each replica has its own leader.
# Replication and consistency
  - Want to make the system fault tolorent. we must remove single point of failure
  - Usually done by redudency.
  - Multple copies of the data
  - Data replicated - multiple copy of the data, but might be expensive to update
  - Also geo replication between data centers.
  - Care about
    - Write
    - Replica update
    - Read.
  - Want high availaiblity.
# CAP
- Avaibility - measure the ability of system to service response for every request.
- CP - consistent and parition
- AP - avaialbity but eventual consistency

# Shared memory
- Distibuted system storing data, inter node communication is abstracted.
- Since unit of stroage : register

# CRDT
- Confilct free replicated datatype
- Perclude the existance of conflicts
- Grow only counter, each server holds a counter vector from all the other nodes, each server update its own.

# Database partitioning 
- Storing all data in a single node is unrealistic. 
- Parititition the data into ranges allow replicas to manage range. Client are routed to the ranges.
- The parition scheme is call sharding.
- Some node use hash of the key to find a node.
- Consistent hashing  - hasfunction(x) -> ring, change in the ring affect only immdeita nieghbor.


# Consencus
- Agreamnt
- Validaty
- Termination
- Usefull for putting events in order

- Abstraction over concenus:
  - config store
  - queue
  - locking
  - 