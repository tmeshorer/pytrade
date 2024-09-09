# Storage in docker

- how docker store data
  /var/lib/docker 
  - files stored under containers.
- how docker stored files
- images are layers arch. Each line in DockerFile is new layer.
- Since each layer only store the changes from prev layer. It affect the size. 
- Docker reuse the layer.
- Docker image layers. Layers are read only
- docker run - create new writable layer.
- Create a new file, create tmp.text in the container layer.
- Files are build using copy on write.
- If we delete the containers all the data get deleted.
## Docker volumes
```commandline
docker volume create data_volume
```
```commandline
docker run -v data_volume:/var/lib/mysql mysql
```

- called volume mounting. 
- Create folder under :
- /var/lib/docker/volumes/data_volume
- Mount the data inside the container
- What happen if we have another data.
- docker run -v /data/mysql:/var/lib (Bind mounting)
- Volume mount and Bind mount. 
- --mount
- docker run --mount type=bind,source=/data/mysql,target=
- Docker uses storage drivers to manage this.
- Ubuntu - AUFS. Different storage drivers.


## Storage Drivers
- Halp manage storage in containers.
- Volumes are handled by volume driver plugin
- Local volume driver.

# Container Storage Interface
- container runtime interface - follow CRI standard.
- CNI - container networking interface. 
- CSI - container storage interface.
  - GRPC API - CreateVolume / Delete Volume
  - RPC implemeneted by the storage driver.

## Volume Drivers