def load_ecg_data(file_path):
    """
    Load ECG data from a specified file path.

    :param file_path: Path to the file containing ECG data.
    :return: List of integers representing ECG data points.
    """
    with open(file_path, "r") as file:
        data = file.read().split(",")
    return [float(point) for point in data]
