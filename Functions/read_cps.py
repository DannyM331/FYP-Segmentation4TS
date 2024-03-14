def read_number_of_change_points(desc_path):
    number_of_cps = {}
    with open(desc_path, 'r') as file:
        for line in file:
            parts = line.split()
            dataset_name = parts[0]  # Assuming the dataset name is the first entry in each line
            cps_count = len(parts) - 1  # Assuming the rest of the entries are change points
            number_of_cps[dataset_name] = cps_count
    return number_of_cps