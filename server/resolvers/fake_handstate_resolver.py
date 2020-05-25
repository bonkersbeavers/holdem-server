from ariadne import gql, QueryType, make_executable_schema, SubscriptionType

helloQuery = QueryType()


@helloQuery.field("hello")
def resolve_hello(_, info):
    return "hi there sexy"
