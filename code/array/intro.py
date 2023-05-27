# def minimumTime(time, totalTrips):
#
#
#     time.sort()
#
#     possible_max_time = min(time)*totalTrips
#
#     binary_search_start = 0
#     binary_search_end = possible_max_time
#     binary_search_mid = int((binary_search_start+binary_search_end)/2)
#     while(binary_search_start<binary_search_end):
#         current_time = binary_search_mid
#         no_of_trips = [current_time//time_taken_by_bus for time_taken_by_bus in time]
#
#         if(sum(no_of_trips)>totalTrips):
#             binary_search_end=binary_search_mid
#         elif sum(no_of_trips)<totalTrips:
#             binary_search_start=binary_search_mid
#         else:
#             return current_time
#         binary_search_mid=int((binary_search_start+binary_search_end)/2)
#         # print(binary_search_mid,sum(no_of_trips))
#     # no_of_trips = [current_time // time_taken_by_bus for time_taken_by_bus in time]
#     # while sum(no_of_trips)>totalTrips:
#     #     current_time-=1
#     #     no_of_trips = [current_time // time_taken_by_bus for time_taken_by_bus in time]
#     # return current_time
#
#
#
#     # current_time = min(time)
#     # no_of_trips = [0, 0, 0]
#     # while sum(no_of_trips) < totalTrips:
#     #     print("inisde while")
#     #     current_time += current_time
#     #     no_of_trips = [current_time // time_taken_by_bus for time_taken_by_bus in time]
#     #
#     # return current_time
#
#
# print(minimumTime([1,2,3],5))
# dummy=[2422//x for x in [24,67,55,92,66,19,70,49,27,33,5,68,58,62,38,69,38,7,99,15,2,97,38,93,99,29,72,94,87,47,99,28,8,37,52,36,10,1,86,65,73,93,74,94,84,49,25,76,55,94,71,7,36,82,62,44,49,82,96,60,75,67,67,72,94,82,44,15,42,95,86,35,66,15,73,91,16,40,36]]
# print(sum(dummy))