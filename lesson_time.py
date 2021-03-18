def appearance(intervals):
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    lesson_range = range(lesson[0], lesson[1]+1)
    pupil_ranges = make_ranges(pupil)
    tutor_ranges = make_ranges(tutor)
    intervals_list = []    
    for pupil_timestump in pupil:
        if pupil_timestump in lesson_range and not in intervals_list:
            pupil_result = check_in_range(pupil_timestump, pupil_ranges)
            tutor_result = check_in_range(pupil_timestump, tutor_ranges)
            if pupil_result == True and tutor_result == True:
                intervals_list.append(pupil_timestump)
    for tutor_timestump in tutor:
        if tutor_timestump in lesson_range and not in intervals_list:
            pupil_result = check_in_range(tutor_timestump, pupil_ranges)
            tutor_result = check_in_range(tutor_timestump, tutor_ranges)
            if pupil_result == True and tutor_result == True:
                intervals_list.append(tutor_timestump)
    intervals_list.sort()
    time = 0
    for i in range(1, len(intervals_list), 2):
        delta = intervals_list[i] - intervals_list[i-1]
        time += delta
    return time


def check_in_range(timestump, ranges):
    for timedelta in ranges:
        if timestump in timedelta:
            return True      


def make_ranges(intervals):
    range_list = []
    for i in range(1, len(intervals), 2):
        range_list.append(range(intervals[i-1], intervals[i]+1))
    return range_list


if __name__ == "__main__":
    timestumps = {
        'lesson': [1594663200, 1594666800], 
        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472], 
        'tutor': [1594663290, 1594663430, 1594663443, 1594666473] 
    }
    print(appearance(timestumps))
