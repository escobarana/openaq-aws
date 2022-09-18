import csv


def save_csv(query_res):
    """
        This function calculates the current air quality by city, being the air quality defined as the average of the
        measurements over the last 3 hours. It creates a csv file with these results.
    :param query_res: result from the query against the Dynamo Database hosted in AWS
    """
    values = []
    with open('data_openaq.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["location", "city", "lat", "lng", "avg_val", "count_measurements"])
        current_loc = query_res[0]['location']
        lat = query_res[0]['latitude']
        lon = query_res[0]['longitude']
        city = query_res[0]['city']

        for message in query_res:
            message_loc = message['location']
            lat = message['latitude']
            lon = message['longitude']
            city = message['city']
            if current_loc == message_loc:
                values.append(float(message['value']))
            else:
                values.append(float(message['value']))
                avg = sum(values) / len(values)
                writer.writerow([current_loc, city, lat, lon, avg, len(values)])
                current_loc = message_loc
                lat = message['latitude']
                lon = message['longitude']
                city = message['city']
                values = []  # Empty array for new iteration

        # Write last city
        avg = sum(values) / len(values)
        writer.writerow([current_loc, city, lat, lon, avg, len(values)])
