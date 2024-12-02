f = open("./day02/input.txt", "r")

reports = list(map(lambda line: list(map(int, line.split())), f.readlines()))

def is_safe(report_data: list[int]):
    if len(report_data) == 1:
        return True
        
    movement_direction = "increasing" if report_data[0] < report_data[1] else "decreasing"

    for i in range(len(report_data) - 1):
        if report_data[i] == report_data[i + 1]:
            return False
        
        new_movement_direction = "increasing" if report_data[i] < report_data[i + 1] else "decreasing"
        if new_movement_direction != movement_direction:
            return False
        
        if not (1 <= abs(report_data[i] - report_data[i + 1]) <= 3):
            return False

    return True


# I should do this in a more efficient way, brute forcing aint the way to go but
# After the suffering, perhaps i will circle back to this sometime in the future
def is_any_safe(report_data: list[int]):
    for i in range(len(report_data)):
        if is_safe(report_data[:i] + report_data[i + 1:]):
            return True
    return False

num_safe_reports = sum(map(is_any_safe, reports))
print(num_safe_reports)
