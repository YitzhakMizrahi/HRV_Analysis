# hrv/reader.py

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


def load_ppg_data(file_path):
    """
    Load PPG data from a specified file path and extract each channel.

    Parameters:
        file_path (str): Path to the file containing PPG data.

    Returns:
        dict: Dictionary containing lists of data points for each channel.
    """
    with open(file_path, "r") as file:
        data = file.read().split(",")
    # Assuming data is ordered as Red, IR, Green, ECG repeated
    return {
        "red": [float(data[i]) for i in range(0, len(data), 4)],
        "ir": [float(data[i]) for i in range(1, len(data), 4)],
        "green": [float(data[i]) for i in range(2, len(data), 4)],
        "ecg": [float(data[i]) for i in range(3, len(data), 4)],
    }
