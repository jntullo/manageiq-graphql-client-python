from graphqlclient import GraphQLClient

class ManageIQGraphQLClient(object):
  client = GraphQLClient('http://localhost:3000/graphql')

  @classmethod
  def query(cls, query):
    if 'documentName' in query:
      query = open('queries/' + query['documentName'] + '.graphql', 'r').read()
    return cls.client.execute(query)
