from flask import Flask, request


app = Flask(__name__)


@app.route('/api/v1.0/get-time', methods=['POST'])
def create_task():
    if not request.json:
        return 'no json', 400
    intervals = request.json['data']
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    lesson_range = range(lesson[0], lesson[1]+1)
    pupil_ranges = make_ranges(pupil)
    tutor_ranges = make_ranges(tutor)
    intervals_list = []
    check_list = []
    check_list += lesson
    check_list += pupil
    check_list += tutor
    for timestump in check_list:
        if timestump in lesson_range:
            pupil_result = check_in_range(timestump, pupil_ranges)
            tutor_result = check_in_range(timestump, tutor_ranges)
            if pupil_result == True and tutor_result == True:
                intervals_list.append(timestump)
    intervals_list.sort()
    time = 0
    for i in range(1, len(intervals_list), 2):
        delta = intervals_list[i] - intervals_list[i-1]
        time += delta
    return str(time), 200


def check_in_range(timestump, ranges):
    for timedelta in ranges:
        if timestump in timedelta:
            return True      


def make_ranges(intervals):
    range_list = []
    for i in range(1, len(intervals), 2):
        range_list.append(range(intervals[i-1], intervals[i]+1))
    return range_list


if __name__ == '__main__':
    app.run(debug=True)