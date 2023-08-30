from app.elastic.connect import connect_elasticsearch
from app.elastic.query.models import Search


def searcher(query_model: Search = None, query_json: dict = None) -> dict:
    es = connect_elasticsearch()
    result = None
    if query_model:
        result = es.search(**query_model.dict(exclude_none=True))
    elif query_json:
        result = es.search(**query_json)
    return result


if __name__ == '__main__':
    query_data = {"match_all": {}}
    # query_data = {'match': {'city': 'Göteborg'}}
    # query_data = {
    #     'bool': {
    #         'must': [
    #             {'match': {'city': 'Göteborg'}},
    #             {'match': {'cuisine': 'Modern cuisine'}}
    #         ]
    #     }
    # }
    # query_data = {
    #     'bool': {
    #         'filter': {
    #             'geo_distance': {
    #                 'distance': '300km',
    #                 'pin.location': {
    #                     'lat': 58.5,
    #                     'lon': 15.1
    #                 }
    #             }
    #         }
    #     }
    # }
    search_model = Search(
        index="michelin_restaurants",
        query=query_data
    )
    print(search_model.dict(exclude_none=True))
    res = searcher(search_model)
    print(res)
