import sys

if __name__ == '__main__':

    ground_truth = [1, 1, 0, 1, 0, 0, 1, 1, 0, 1]
    # system_output = [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    # system_output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    system_output = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # system_output = [1, 1, 0, 1, 0, 0, 1, 1, 0, 1]

    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for x, y in zip(ground_truth, system_output):
        if y == 1 and x == 1:
            tp += 1
        elif y == 1 and x == 0:
            fn += 1
        elif y == 0 and x == 1:
            fp += 1
        elif y == 0 and x == 0:
            tn += 1

    acc = (tp + tn) / len(ground_truth)
    print(f'accuracy:\t{acc}')
    # or
    # acc = (tp + tn) / (tp + fp + tn + fn)
    print('Positive metrics')
    recall = tp / (tp + fn)
    print(f'recall:\t{recall}')

    precision = tp / (tp + fp)
    print(f'precision:\t{precision}')

    print('Negative metrics')
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for x, y in zip(ground_truth, system_output):
        if y == 1 and x == 1:
            tn += 1
        elif y == 1 and x == 0:
            fp += 1
        elif y == 0 and x == 1:
            fn += 1
        elif y == 0 and x == 0:
            tp += 1


    recall = tp / (tp + fn)
    print(f'recall:\t{recall}')

    precision = tp / (tp + fp)
    print(f'precision:\t{precision}')