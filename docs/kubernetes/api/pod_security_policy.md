# Overview
- Set of conditions/rules on Pod must follow in order to be accepted to the cluster
- a policy can define:
  - Type of volume
  - Read only filesystem
  - Host Port
- Need to enable pod security policy admission controller
- When a PSP is active, every pod must have one policy
- Only one PSP for a pod can be applied

## Policy Order
- Chose non mutable policies first
- Chose the one with name

## Yaml
Define a policy

```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
name: my-psp
spec:
  privileged: false
  seLinux:
    rule: RunAsAny
  supplementalGroups:
    rule: RunAsAny
  runAsUser:
    rule: RunAsAny
  fsGroup:
    rule: RunAsAny
  volumes:
    - '*'
```

