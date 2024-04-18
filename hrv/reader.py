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


def load_eco_data(file_path, channel_index=3):
    """
    Load ECO data from a specified file path and extract ECG data based on the channel index.

    Parameters:
        file_path (str): Path to the file containing ECO data.
        channel_index (int): Index of the ECG channel in the repeated sequence.

    Returns:
        list: List of ECG data points extracted from the file.
    """
    try:
        with open(file_path, "r") as file:
            data = file.read().split(",")
        # Extract every fourth value starting from the index specified by channel_index
        ecg_data = [int(data[i]) for i in range(channel_index, len(data), 4)]
        return ecg_data
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found.")
    except ValueError as e:
        raise ValueError(f"Error processing ECO data in {file_path}: {e}")
