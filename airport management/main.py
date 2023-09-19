from TravelAgent import TravelAgent


def main():
    travel_agent = TravelAgent("Go Jaan")
    trip_info1 = travel_agent.set_trip_one_city_one_way(
        "DAC", "PRA", "05/07/2056")
    # print("Aircraft: ", trip_info1.aircraft)
    # print("Price: ", trip_info1.cost)

    trip_cities = ["DUB", "LHR", "DAC", "SYD", "JFK", "ORD"]
    trip_info2 = travel_agent.set_trip_multi_city_flexible_route(
        trip_cities, "05/11/2056")
    print("price", trip_info2[1])
    for trip in trip_info2[0]:
        print(trip)


if __name__ == "__main__":
    main()
