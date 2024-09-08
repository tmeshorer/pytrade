# Overview
- Method ro regular access to resource based on roles of indevidual users
- Four objects: Role / ClusterRole / RoleBinding / ClusterRoleBinding
- Operation : create/list/get/update/delete/watch

## Role
- List of verbs allowed for specific resouace.
- Specify permission in a namespace
## ClusterRole
- Grants permissions cluster wide.
- Cluster scoped resources
## RoleBinding
- Grant permission on a role to a user within a namespace
## ClusterRoleBinding
- Same as RoleBinding but for all namespaces.

# How
## Create Role
```yaml
apiVersion:
  rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: my-namespace
  name: pod-reader
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "watch", "list"]
    apiVersion: rbac.
```

## Create RoleBinding
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: my-namespace
subjects:
  - kind: User
    name: my-user
    apiGroup: rbac.authorization.k8s.io
roleRef:
    kind: Role
    name: pod-reader
    apiGroup: rbac.authorization.k8s.io

```