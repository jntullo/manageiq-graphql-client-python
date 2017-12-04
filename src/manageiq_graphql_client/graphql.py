from graphqlclient import GraphQLClient

class ManageiqGraphQLClient(object):
    client = GraphQLClient('http://localhost:3000/graphql')
    @classmethod
    def query(cls, query):
        return cls.client.execute(query)



