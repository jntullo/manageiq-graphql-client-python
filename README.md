# manageiq-graphql-client-python
Python ManageIQ GraphQLclient 

### Installation
Install it locally, run the following command from this directory: 
```
pip install -e .
```

### Execute a sample query
Open up the console
```python
python
```

And execute the following sample command:
```python
from manageiq_graphql.client import ManageIQGraphQLClient
ManageIQGraphQLClient.query('{ vms { name } }')
```

### Execute a named query
To execute a named query, pass in a hash with the `documentName` such as: 
```python
from manageiq_graphql.client import ManageIQGraphQLClient
ManageIQGraphQLClient.query({ 'documentName': 'vms_with_names' })
```
