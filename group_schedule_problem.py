from datetime import datetime, timedelta


def find_common_availability(person1_schedule, person1_daily_act, person2_schedule, person2_daily_act, duration_of_meeting):
    # Combine the schedules of both persons
    combined_schedule = person1_schedule + person2_schedule

    # Sort the combined schedule by start time
    sorted_schedule = sorted(combined_schedule, key=lambda x: datetime.strptime(x[0], '%H:%M'))

    # Create a list to store unavailable time slots
    unavailable_times = []

    # Initialize variables for the loop
    earliest_start = max(datetime.strptime(person1_daily_act[0], '%H:%M'), datetime.strptime(person2_daily_act[0], '%H:%M'))
    latest_end = min(datetime.strptime(person1_daily_act[1], '%H:%M'), datetime.strptime(person2_daily_act[1], '%H:%M'))

    # Loop through the sorted schedule to find unavailable time slots
    for i in range(len(sorted_schedule) - 1):
        current_slot = sorted_schedule[i]
        next_slot = sorted_schedule[i + 1]

        current_slot_end = datetime.strptime(current_slot[1], '%H:%M')
        next_slot_start = datetime.strptime(next_slot[0], '%H:%M')

        if current_slot_end >= earliest_start and next_slot_start <= latest_end:
            if next_slot_start - current_slot_end >= timedelta(minutes=duration_of_meeting):
                # There is an available slot between the two schedules
                available_slot = [current_slot_end.strftime('%H:%M'), next_slot_start.strftime('%H:%M')]
                unavailable_times.append(available_slot)

    # Convert unavailable time slots to 24-hour military time format
    available_times = []
    for slot in unavailable_times:
        start_time = convert_to_military_time(slot[0])
        end_time = convert_to_military_time(slot[1])
        available_times.append([start_time, end_time])

    # Merge overlapping time slots
    available_times.sort()
    merged_times = []
    for start, end in available_times:
        if not merged_times or merged_times[-1][1] < start:
            merged_times.append([start, end])
        else:
            merged_times[-1][1] = max(merged_times[-1][1], end)

    # Return the available time slots
    return merged_times


def convert_to_military_time(time_str):
    time_obj = datetime.strptime(time_str, '%H:%M')
    return time_obj.strftime('%H:%M')


# Sample input
person1_Schedule =[ ['7:00', '8:30'], ['12:00', '13:00'], ['16:00', '18:00']]
person1_DailyAct = ['9:00', '19:00']
person2_Schedule = [['9:00', '10:30'], ['12:20', '14:30'], ['14:00', '15:00'], ['16:00', '17:00']]
person2_DailyAct = ['9:00', '18:30']
duration_of_meeting = 30

# Call the function and print the result
available_times = find_common_availability(person1_Schedule, person1_DailyAct, person2_Schedule, person2_DailyAct, duration_of_meeting)
print(available_times)

# Expected output
# [['10:30', '12:00'], ['15:00', '16:00'], ['18:00',['18:30']
