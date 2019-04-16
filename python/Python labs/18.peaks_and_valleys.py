# 18.peaks_and_valleys.py

data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]

def peaks(data):
    peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i+1] and data[i] > data[i-1]:
            peaks.append(i)
    return peaks


def valleys(data):
    valleys = []
    for i in range(1, len(data)-1):
        if data[i] < data[i+1] and data[i] < data[i-1]:
            valleys.append(i)
    return valleys


def peaks_and_valleys(data):
    return sorted(peaks(data) + valleys(data))


def graph(data):
    # count = 9
    for i in range(len(data)):
        print('*', end = '')


#data = the values in list form (base of X)
#data[i] = the amount

# print(peaks(data))
# print(valleys(data))
# print(peaks_and_valleys(data))
print(graph(data))
