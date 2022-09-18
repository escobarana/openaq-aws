import streamlit as st
import pandas as pd
from config.dynamodb import dynamodb
import numpy as np
import pydeck as pdk
from boto3.dynamodb.conditions import Attr
from datetime import datetime


def draw_map(res):
    """
        This function draws a map using the library streamlit and pydeck
    :param res: result data of the query against dynamodb on AWS
    """
    coords = []
    lats = []
    longs = []
    for i in res['Items']:
        lat_lon = []
        lat_lon.append(float(i["latitude"]))
        lats.append(float(i["latitude"]))
        lat_lon.append(float(i["longitude"]))
        longs.append(float(i["longitude"]))
        coords.append(lat_lon)

    df = pd.DataFrame(
        coords,
        columns=['lat', 'lon'])

    layer = pdk.Layer(
        'ScatterplotLayer',
        data=df,
        get_position='[lon, lat]',
        auto_highlight=True,
        get_radius=1000,  # Radius is given in meters
        get_color='[180, 0, 200, 140]'  # Set an RGBA value for fill
    )

    view_state = pdk.ViewState(
        latitude=np.average(lats),
        longitude=np.average(longs),
        zoom=7,
        pitch=40.5,
        bearing=-27.36
    )

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=view_state,
        layers=[layer]
    ))

    # st.map(data=data, zoom=7)


def query_test():
    """
        This query returns all documents on dynamodb
    :return: query response
    """
    query_response = dynamodb.Table('openaq_ana').scan()
    return query_response


def query_current_air_quality_by_city():
    """
        This query returns all documents on dynamodb during the last 3 hours of the current date.
        It measures current air quality by city in Belgium (to be seen on the map).
    :return: query response
    """
    date_today = str(datetime.date(datetime.today()))
    # AirMax defines the current air quality in a city as the average of the measurements over the last 3 hours
    current_hour = datetime.today().hour
    current_hour_minus_three = current_hour + 2

    query_response = dynamodb.Table('openaq_ana').scan(FilterExpression=Attr("date").eq(date_today) &
                                                                        Attr("hour").between(current_hour_minus_three,
                                                                                             current_hour))
    return query_response


if __name__ == '__main__':
    response = query_test()
    draw_map(res=response)
