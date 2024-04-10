def load_ecg_data(file_path):
    """
    Load ECG data from a specified file path.

    :param file_path: Path to the file containing ECG data.
    :return: List of floating-point numbers representing ECG data points.
    :raises FileNotFoundError: If the file does not exist.
    :raises ValueError: If there is an issue converting the data to floats.
    """
    try:
        with open(file_path, "r") as file:
            data = file.read().split(",")
        return [float(point) for point in data]
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found.")
    except ValueError as e:
        raise ValueError(f"Error processing ECG data in {file_path}: {e}")
