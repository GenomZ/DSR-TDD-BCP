from scipy import stats


def mean(data):
    return stats.tmean(data)


def median(data):
    return average(data)


def mode(data):
    return stats.mode(data).mode[0]
