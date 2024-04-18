# HRV_Analysis Project

## Overview

`HRV_Analysis` is a tool developed to calculate Heart Rate Variability (HRV) from raw ECG data. The goal is to use HRV metrics as indicators to potentially identify risk factors for diabetes.

## Features

- ECG data loading from text files.
- R-peak detection in ECG data.
- Calculation of RR intervals.
- HRV metrics computation, including RMSSD, SDNN, and pNN50.
- Support for different ECG data formats (standard ECG, Apple Watch, ECO).
- Dynamic file path handling for flexible data analysis.

## Installation

1. Clone the project repository.

```
git@github.com:YitzhakMizrahi/HRV_Analysis.git
```

2. Create the virtual Environment

```
python -m venv venv
```

3. Activate the virtual environment

```
.\venv\Scripts\activate # Windows
source venv/bin/activate # Unix/Mac
```

4. Install required dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the program specifying the type of analysis and the path to the data file:

```
python main.py <type> [file_path]
```

### Types

- `standard`: Standard ECG data analysis.
- `apple_watch`: Analysis based on Apple Watch data.
- `eco`: Analysis of ECO device data.

Ensure you have a valid ECG data file in the `data/` directory for standard and eco analyses.

## Project Structure

```
HRV_Analysis/
├── analysis_module/
│ ├── init.py
│ ├── full_dataset.py
│ ├── segment_analysis.py
│ └── remaining_data.py
├── data_processing/
│ ├── init.py
│ └── process_segments.py
├── device_handlers/
│ ├── init.py
│ ├── apple_watch_handler.py
│ └── eco_handler.py
├── hrv/
│ ├── init.py
│ ├── reader.py
│ ├── analysis.py
│ └── metrics.py
├── data/
│ └── sample_ecg.txt
├── tests/
│ ├── init.py
│ └── test_hrv.py
├── requirements.txt
└── main.py
```

## Next Steps

- Integrate machine learning to predict diabetes risk based on HRV and other factors.
- Improve data handling for continuous and long-term monitoring.

## Potential Issues

- Data quality: Ensure ECG data is clean and accurately reflects heart activity.
- Algorithm accuracy: R-peak detection and HRV calculations must be precise and validated.

## License

This project is currently unlicensed and all rights are reserved by the author. A formal license will be added in the future as the project evolves.
