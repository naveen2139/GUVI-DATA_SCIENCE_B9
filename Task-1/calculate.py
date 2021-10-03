def calculate_total(sample_list):
    return sum(sample_list)


def calculate_average(sample_list):
    return sum(sample_list) / len(sample_list)


def calculate_grade(total):
    if total >= 80:
        return 'A'
    elif total >= 60:
        return 'B'
    elif total >= 40:
        return 'C'
    else:
        return 'F'
