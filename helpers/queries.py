from boto3.dynamodb.conditions import Attr
from datetime import datetime
from decimal import Decimal
from config.dynamodb import dynamodb


def query_with_index():
    """
        This query returns all documents on dynamodb
    :return: query response
    """
    query_response = dynamodb.Table('openaq_ana').scan(IndexName="location-date-index")
    return query_response


def query_current_air_quality_by_city():
    """
        This query returns all documents on dynamodb during the last 3 hours of the current date.
        It measures current air quality by city in Belgium (to be seen on the map).
    :return: query response
    """
    date_today = str(datetime.date(datetime.today()))  # 2022-09-18
    # AirMax defines the current air quality in a city as the average of the measurements over the last 3 hours
    current_hour = Decimal(3)  # Decimal(datetime.today().hour)
    current_hour_minus_three = Decimal(current_hour - 3)

    query_response = dynamodb.Table('openaq_ana').scan(FilterExpression=Attr("date").eq(date_today) &
                                                                        Attr("hour").between(high_value=current_hour,
                                                                                             low_value=current_hour_minus_three),
                                                       IndexName="location-date-index")
    return query_response

