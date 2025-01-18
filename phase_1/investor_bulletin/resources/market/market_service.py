""" Market Service """

"""_summary_
this file to write any business logic for the Market
"""

import requests
from api.config import settings
from sqlalchemy import create_engine


def get_market_data():
    url = settings.rapid_api_url
    db_uri = settings.database_url

    try:
        engine = create_engine(
            db_uri
        )

        
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")


    querystring = {"symbol": "AAPL,MSFT,GOOG,AMZN,META"}

    headers = {
        "x-rapidapi-key": settings.x_rapid_api_key,
        "x-rapidapi-host": settings.x_rapid_api_host,
    }

    # response = requests.get(url, headers=headers, params=querystring)

    return {}#response.json()
