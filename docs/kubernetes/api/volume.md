# 
- Attach volume to the container.
- Data remain.
- Data processed by it get deleted as well.
```yaml

  containers:
    - name: first
      volumeMounts:
        - mountPath: /opt
          volume: data-volume

volumes:
   - name: data-volume
     hostPath:
      path: /data
      type: Directory
```

- but cannot share across nodes.
- AWS:
- ```yaml
    volumes:
        -name: data-volume
        - aws
```

