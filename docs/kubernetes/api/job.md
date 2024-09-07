# Job template
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: counter
spec:
  template:   
    spec:
      containers:
      - name: counter
        image: nginx:1.25.1
        command:
        - /bin/sh
        - -c
        - counter=0; while [ $counter -lt 3 ]; do counter=$((counter+1)); \
          echo "$counter"; sleep 3; done;
      restartPolicy: Never
```
# List Jobs
```yaml
kubectl get jobs
```

# Job Spec
## Parallel Job:
spec.parallelisim
## Number of retry a job attemept before successful completion
spec.backoffLimit
## Restart Policy
spec.template.spec.restartPolicy (Always, OnFailure , Never)

