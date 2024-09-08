# Overview
- Control communication between pods in the cluster.
- Scoped by namespaces.
- Limited to IP address (no domain name)
- Must use CNI plugin that supports NP
- Use labels to detect pods and defines rules where traffic is allowed

# Yaml

- Pod selector (if empty, all the pods in the namespace)
```yaml
podSelector:
  matchLabels:
    role: my-role
```

Allow connections to all pods labeled `allow-role`

```yaml
ingress:
  - from:
      - podSelector:
          matchLabels:
            role: allow-role
    ports:
      - protocol: TCP
        port: 6379
```

Allow connections from our pods to communicate with pods with labels `allow-to-nodes`

```yaml
egress:
- to:
  - podSelector:
      matchLabels:
        role: allow-to-role
  ports:
    - protocol: TCP
      port: 5978
```

Deny all ingress traffic to our pods

```yaml
spec:
  podSelector: {}
  policyTypes:
    - Ingress
```

Allow all Egress traffic from our Pods:

```yaml
spec:
  podSelector: {}
  policyTypes:
    - Egress
  egress:
    - {}
```

# Can use several selectors

- podSelector
- namespaceSelector
- ipBlock

