# Job 

## Overview
- Process that run to completion (Batch, Backup, Database migration)
- Run one or more pods and ensure that specifc number terminate
- Job can be lunched by a cron job.
- Job schedule format

# Restart Policy
## Never
If the pod failed, job controller will start a new Pod.
## On Failure
If the pod failed, the pod stay on a node but the container rerun
## Always
Can not be set, if the pod terminate with success, job will never rerun.



## Create a job
```commandline
kubectl create job my-job -—image=busybox
```

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

# Delete a job
```commandline
kubectl delete job my-job
```

# Delete a job only
```commandline
kubectl delete job my-job cascade=false
```

# Job Spec
## Parallel Job:

spec.parallelisim

## BacoffLimit
Number of retries before considering the job as failed.
```yaml
spec.backoffLimit
```
## activeDeadlineSeconds
- Once a job reached , all running pods will be killed.
- A job will not deploy another Pods when activeDeadline reached.
## completion
If >1 , job controller will spawn Pods until the number of complete pods
reach this number.

## Restart Policy
spec.template.spec.restartPolicy (Always, OnFailure , Never)

