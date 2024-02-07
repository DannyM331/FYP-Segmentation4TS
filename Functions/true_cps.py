def read_true_change_points(filename, dataset_name):
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if parts[0] == dataset_name:
                return [int(cp) for cp in parts[1:]]
    return []