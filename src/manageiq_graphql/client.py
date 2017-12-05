from graphqlclient import GraphQLClient

class ManageIQGraphQLClient(object):
  client = GraphQLClient('http://localhost:3000/graphql')

  @classmethod
  def query(cls, query):
    return cls.client.execute(query)
