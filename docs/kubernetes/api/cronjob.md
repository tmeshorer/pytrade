# Description
Create new Job Periodically based on schedule. Based on cron expression

# Format
- Based on cron format.
- 

# Yaml
```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: current-date
spec:
  schedule: "* * * * *"   1
  jobTemplate:            2
    spec:
      template:
        spec:
          containers:
          - name: current-date
            image: nginx:1.25.1
            args:
            - /bin/sh
            - -c
            - 'echo "Current date: $(date)"'
          restartPolicy: OnFailure
```

## Create a cron job every 5 min
```commandline
kubectl create cronjob my-cj —-image=busybox  —-schedule="*/5 * * * *" -n my-namespace
```

## Change job schedule
```commandline
kubectl patch cronjob my-cronjob -p '{"spec":{"schedule": "0 */1 */1 * *"}}'
```

## Lunch a job from existing job
```commandline
kubectl create job —-from=cronjob/my-cronjob my-job -n my-namespace
```

