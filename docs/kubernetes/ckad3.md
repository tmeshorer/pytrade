# Extend the kubernetes API

## Define the CRD
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: smoketests.stable.bmuschko.com   1
spec:
  group: stable.bmuschko.com             2
  versions:
    - name: v1                           3
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:                    4
            spec:
              type: object
              properties:
                service:
                  type: string
                path:
                  type: string
                timeout:
                  type: integer
                retries:
                  type: integer
  scope: Namespaced
  names:                                 5
    plural: smoketests
    singular: smoketest
    kind: SmokeTest
    shortNames:
    - st

```
Apply the CRD:
```yaml
 kubectl apply -f smoketest-resource.yaml
```
Instatiate the CRD kind smoketest
```yaml
apiVersion: stable.bmuschko.com/v1   1
kind: SmokeTest                      2
metadata:
  name: backend-smoke-test
spec:
  service: backend                   3
  path: /health                      3
  timeout: 600                       3
  retries: 3           
```
```commandline
kubectl get smoketest backend-smoke-test
```
2) Discovering CRDs
```commandline
kubectl api-resources --api-group=stable.bmuschko.com
```
```commandline
kubectl get crds
```

# Authentication, Authorization and Admission control
1) Request goes trough auth->authz->addmision control
2) Auth -validate the identity of the caller - bearer token
3) Authz - determines if the identity provided in the first stage can access verb.
4) Addmission control - check if request needs to be modified.

## Auth with kubectl
Kubeconfig defines the API server end points + credentials in the form of client certificates.
```yaml
apiVersion: v1
kind: Config
clusters:                   1
- cluster:
    certificate-authority: /Users/bmuschko/.minikube/ca.crt
    extensions:
    - extension:
        last-update: Mon, 09 Oct 2023 07:33:01 MDT
        provider: minikube.sigs.k8s.io
        version: v1.30.1
      name: cluster_info
    server: https://127.0.0.1:63709
  name: minikube
contexts:                   2
- context:
    cluster: minikube
    user: bmuschko
  name: bmuschko
```
Commands:

```commandline
kubectl config view
```

```commandline
 kubectl config current-context
```

Change context:
```commandline
 kubectl config use-context bmuschko
```

Add user:
```commandline
kubectl config set-credentials myuser \
  --client-key=myuser.key --client-certificate=myuser.crt \
  --embed-certs=true
```

## Autorization
Authorization check if the operation is permitted against the requested API resource.

### RBAC
Subject - The user or service account that wants to access a resource
Resource - The Kubernetes API resource type (e.g., a Deployment or node)
Verb - The operation that can be executed on the resource (e.g., creating a Pod or deleting a Service)

Role - Decrlare api resources and thier operation (e.g. list pods)
RoleBinding - Bind the role to the subjects. 

ServiceAccount

#### create a role
```commandline
 kubectl create role read-only --verb=list,get,watch \
  --resource=pods,deployments,services
```
With yaml
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: read-only
rules:
- apiGroups:
  - ""
  resources:
  - pods
  - services
  verbs:
  - list
  - get
  - watch
- apiGroups:      1
  - apps
  resources:
  - deployments
  verbs:
  - list
  - get
  - watch
```
List roles
```commandline
kubectl get roles
```
Render Role Details
```commandline
kubectl describe role read-only
```

#### Role Binding
Bind a role to a user
```commandline
kubectl create rolebinding read-only-binding --role=read-only --user=bmuschko
```
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-only-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: read-only
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: User
  name: bmuschko
```
```commandline
 kubectl describe rolebinding read-only-binding
```
```commandline
 kubectl auth can-i --list --as bmuschko
```

## Service Account
- Pods can use service account to auth to the api server
- Pod used the default service account
```commandline
kubectl get serviceaccounts
```
The default service account can request basic cluster information
Create service account:
```commandline
kubectl create serviceaccount cicd-bot
```
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: sa-api
  namespace: k97
```
Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: list-objects
  namespace: k97
spec:
  serviceAccountName: sa-api   1
  containers:
  - name: pods
    image: alpine/curl:3.14
```
Create the Role
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: list-pods-role
  namespace: k97
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["list"]
```
Create the role binding
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: serviceaccount-pod-rolebinding
  namespace: k97
subjects:
- kind: ServiceAccount
  name: sa-api
roleRef:
  kind: Role
  name: list-pods-role
  apiGroup: rbac.authorization.k8s.io
```

# Resource requirements, limits and quotas
- Workload consume certain amount of resources (CPU/Mem)
- Container level - min amount of resources, Max amount of resources.
- ResourceQuota - aggegrate at the name space level
- LimitRange - specific type.
- Each container define resource request, The scheduler assure that total resource fit
- Examples:
- requests.cpu = 500ml
- requests.memopty - 64Mi
- Example:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: rate-limiter
spec:
  containers:
  - name: business-app
    image: bmuschko/nodejs-business-app:1.0.0
    ports:
    - containerPort: 8080
    resources:
      requests:
        memory: "256Mi"
        cpu: "1"
  - name: ambassador
    image: bmuschko/nodejs-ambassador:1.0.0
    ports:
    - containerPort: 8081
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
```
