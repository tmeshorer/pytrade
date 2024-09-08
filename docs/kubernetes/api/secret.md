# Overview  
Save sensative information

# Create
- From key and value
- From env file
- From file

# How to
## From key value
```commandline
kubectl create secret generic my-secret —-from-literal=password=‘my-awesome-password’
```

## From file
```commandline
kubectl create secret generic my-secret —-from-file=password.txt -n my-namespace
```

## Decode secret
```commandline
kubectl get secret my-ca-secret -o=go-template='{{index .data "ca.crt" | base64decode}}'
```

