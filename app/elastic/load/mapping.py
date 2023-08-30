from app.elastic.connect import connect_elasticsearch


def create_geo_mapping():
    """Create the geo mapping."""
    mapping = {
        "mappings": {
            "properties": {
                "pin": {
                    "properties": {
                        "location": {
                            "type": "geo_point"
                        }
                    }
                }
            }
        }
    }
    es = connect_elasticsearch()
    es.indices.create(index="michelin_restaurants", body=mapping)


if __name__ == "__main__":
    create_geo_mapping()
