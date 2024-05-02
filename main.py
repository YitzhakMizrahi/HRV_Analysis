# main.py

import argparse
import sys
import os
from device_handlers import apple_watch_handler, eco_handler, ppg_handler
from data_processing.process_segments import process_segments
from hrv.reader import load_ecg_data


def main():
    parser = argparse.ArgumentParser(
        description="Process different types of ECG data with dynamic file paths."
    )
    parser.add_argument(
        "type",
        type=str,
        choices=["standard", "apple_watch", "eco", "ppg"],
        help="Type of analysis to perform: standard, apple_watch, eco, or ppg",
    )
    parser.add_argument(
        "file_path",
        type=str,
        nargs="?",
        help="Path to the data file. Required for standard, eco, and ppg types.",
    )

    args = parser.parse_args()

    if args.type in ["standard", "eco", "ppg"]:
        if not args.file_path:
            print(
                "Error: A file path must be specified for standard, eco, and ppg data types."
            )
            sys.exit(1)

        file_name = os.path.basename(args.file_path)

        try:
            if args.type == "standard":
                ecg_data = load_ecg_data(args.file_path)
                process_segments(ecg_data, 200, file_name)
            elif args.type == "eco":
                eco_handler.process_eco_data(args.file_path, file_name)
            elif args.type == "ppg":
                ppg_handler.process_ppg_data(
                    args.file_path, file_name
                )  # Use PPG handler
        except Exception as e:
            print(f"Error processing {args.type} data: {e}")
            sys.exit(1)

    elif args.type == "apple_watch":
        if args.file_path:
            print(
                "Warning: No file path needed for Apple Watch data. Ignoring file path argument."
            )
        try:
            apple_watch_handler.test_apple_watch_data()
        except Exception as e:
            print(f"Error processing Apple Watch data: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
