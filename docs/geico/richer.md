# REST
- /v1/song-management/users/{user-id}/playlists/{playlistid}
- Collections resource
- Item resource.
```yaml
GET /airports/LAX Get LAX info
GET /airports   List
DELETE /airports/LAX
```

## Collection
- If very large add skip and top


## Cloud
- Region / AZ (Own power / Own networking)
- Each AZ has Racks
- On Racks there are batch of PC
- On PC there are VM

# Micro services
- 3 Micro sevices - Inventory
- Order service
- Each service, multiple VM
- Split servivices
  - Scale this services indepedencty from one another
  - Tumbniel is needed only if we upload photo.
  - Different tech stacks
  - Reuse
# Chubby
  - Lock service
  - Chose small file to permit elected 
  - Event notification
## Design
- Client lib and server
- Chjubby cell - small set of servers - replicas.
- Cell has 5 replicas.
- Replicas use consensus to elect a master
- Master have a lease that is priodicy renewed.
- Each replica has copy of a simple database, but only master read or write.
- Replicas only update thier copy based on messages from the consuses protocol.
- Client find master by sending DNS request
- If replica get the request return the master address
- Each request are ackknowledge when the master reached majority of replicas.
- If replica is down, the master replace it, update the list of cell members (which kept among members)
- Replica obtain the current state from NFS as well as master log.
- Use file schemas
- Locks are advisory
- Client has caches. Master invalidate the cache.
- 