# Description
Create new Job Poridicaly based on schedule. Based on cron expression

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