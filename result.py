from db.subject import get_subjects


def save_result(fname, sname, matric_no, subject, score):
    with open(f'data/{subject.lower()}.txt', 'a') as f:
        f.write(f'{fname} {sname} {matric_no} {score}\n')
    

def get_results(subject):
    results = []
    with open(f'data/{subject.lower()}.txt', 'r') as f:
        for line in f:
            result = line.strip().split(" ")
            results.append(result)
    return results


def result_exist(subject, matric_no):
    with open(f'data/{subject.lower()}.txt', 'r') as f:
        content = f.read()
        if matric_no in content:
            return True
        else:
            return False


def get_mean(subject):
    results = get_results(subject)
    total = 0
    for result in results:
        total += int(result[-1])
    return total / len(results)

def get_lowest(subject):
    results = get_results(subject)
    min = None
    min_result = []
    for result in results:
        if min == None:
            min = result[-1]
            min_result = result
        elif min > result[-1]:
            min = result[-1]
            min_result = result
    return min_result

def get_highest(subject):
    results = get_results(subject)
    max = None
    max_result = []
    for result in results:
        if max == None:
            max = result[-1]
            max_result = result
        elif max < result[-1]:
            max = result[-1]
            max_result = result
    return max_result

def get_above_count(subject, min):
    results = get_results(subject)
    # count = 0
    above = []
    for result in results:
        if min < int(result[-1]):
            # count += 1
            above.append(result)
    return above