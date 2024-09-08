#Overview
Default memory request & limit values for containers in a namespace

# Yaml

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: memory-limit-range
spec:
    limits:
    - default:
        memory: 512Mi
      defaultRequest:
        memory: 256Mi
      type: Container

```

# Scenario
- Pod has container without mem request and limit. System append the limit range.
- Pod has container with only memory limit

# Request/