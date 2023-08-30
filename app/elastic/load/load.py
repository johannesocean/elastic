from elasticsearch import Elasticsearch

from app.elastic.load.models import DocumentIndex
from app.elastic.connect import connect_elasticsearch
from app.elastic.handler.data_handler import get_json_format


def load_michelins(data_list: list[dict], _es: Elasticsearch):
    """Load the michelin restaurants example_data into elasticsearch."""
    for i, data_object in enumerate(data_list):
        doc = DocumentIndex(_id=str(i), document=data_object)
        resp = _es.index(**doc.dict())
        if resp.get("_shards", {}).get("failed"):
            print("Failed to load example_data!")
            print(resp)
    print("Load complete!")


def load_it():
    # create the elasticsearch connection
    es = connect_elasticsearch()

    # define the document example_data
    data = get_json_format()

    # load the example_data into elasticsearch
    load_michelins(data, es)


if __name__ == "__main__":
    # OBS! You need to set mappings first
    # (app.elastic.load.mapping.create_geo_mapping())
    load_it()

    # import pprint
    # es = connect_elasticsearch()
    # example_data = get_json_format()
    # doc = DocumentIndex(_id=str("5555"), document=example_data[0])
    # pprint.pprint(doc.dict())