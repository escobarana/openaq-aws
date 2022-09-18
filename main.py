from helpers.queries import query_current_air_quality_by_city
from helpers.save_to_csv import save_csv
from helpers.draw_map import draw_map

if __name__ == '__main__':
    response = query_current_air_quality_by_city()
    save_csv(response['Items'])
    draw_map()
