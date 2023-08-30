from app import BASE_PATH

import pandas as pd


def get_json_format():
    """Get the dataframe in json format."""
    df = pd.read_csv(
        BASE_PATH.joinpath("etc/example_data/2019-michelin-restaurants.txt"),
        sep=",",
        encoding="cp1252"
    )
    json_list = []
    for row in df.itertuples():
        json_list.append(
            {
                "name": row.name,
                "year": row.year,
                "pin": {
                    "location": {
                        "lat": row.lat,
                        "lon": row.lon
                    }
                },
                "city": row.city,
                "region": row.region,
                "zipCode": row.zipCode,
                "cuisine": row.cuisine,
                "price": row.price,
                "url": row.url,
                "star": row.star
            }
        )
    return json_list


if __name__ == "__main__":
    data = get_json_format()
    print(data)
