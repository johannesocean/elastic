import os
from elasticsearch import Elasticsearch


def connect_elasticsearch() -> Elasticsearch:
    es = Elasticsearch(os.getenv("URL_ELASTIC"))
    if es.ping():
        print('Elastic Connected')
    else:
        print('Elastic Not Connected')
    return es


if __name__ == '__main__':
    es = connect_elasticsearch()
