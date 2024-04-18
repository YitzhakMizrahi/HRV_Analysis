from hrv.reader import load_eco_data
from data_processing.process_segments import process_segments


def process_eco_data(file_path, file_name):
    """
    Process ECO data from a given file path.

    Parameters:
        file_path (str): Path to the ECO data file.
    """
    try:
        ecg_data = load_eco_data(file_path, channel_index=3)  # Corrected call
        if not ecg_data:
            print("Error: ECG data is empty.")
            return

        process_segments(ecg_data, 250, file_name)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    except Exception as e:
        print(f"Error processing ECO data: {e}")
        return
