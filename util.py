import requests


def starluxPriceRequest(dates):
    output_str = ''
    headers = {'jx-lang': 'zh-TW'}
    seat_names = ['限量', '超值']
    departure = "TPE"
    arrival = "NRT"
    for date in dates:
        output_str += 'date:' + date[0] + '~' + date[1] + '\n'
        my_data = {"itineraries":
                   [{"departure": departure, "arrival": arrival, "departureDate": date[0]},
                    {"departure": arrival, "arrival": departure, "departureDate": date[1]}],
                   "travelers": {"adt": 2, "chd": 0, "inf": 0}, "cabin": "eco"}
        output_str += departure + "<->" + arrival + '\n'
        # 將資料加入 POST 請求中
        r = requests.post(
            'https://ecapi.starlux-airlines.com/searchFlight/v2/flights/search', json=my_data, headers=headers)

        json_data = r.json()
        #print('r', json_data)

        airOffers = json_data['data']["flights"][0]["airOffers"]
        for airoffer in airOffers:
            output_str += seat_names[0] + '剩餘座位:' + str(airoffer['quota']) + \
                ' 價格:' + str(airoffer['price']['total']['amount']) + '\n'
        return output_str
