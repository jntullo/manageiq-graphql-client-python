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
from manageiq_graphql_client.graphql import ManageiqGraphQLClient
ManageiqGraphQLClient.query('{ vms { name } }')
```
