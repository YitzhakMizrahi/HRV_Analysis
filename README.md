# HRV_Analysis Project

## Overview

`HRV_Analysis` is a tool developed to calculate Heart Rate Variability (HRV) from raw ECG data. The goal is to use HRV metrics as indicators to potentially identify risk factors for diabetes.

## Features

- ECG data loading from text files
- R-peak detection in ECG data
- Calculation of RR intervals
- HRV metrics computation, starting with RMSSD, SDNN, pNN50

## Installation

1. Clone the project repository.
2. Activate the virtual environment
```
.\venv\Scripts\activate
```
3. Install required dependencies:
```
pip install -r requirements.txt
```

## Usage

Run the program using:

```
python main.py
```

Ensure you have a valid ECG data file in the `data/` directory.

## Project Structure

```
HRV_Analysis/
├── data/
│ └── sample_ecg.txt
├── hrv/
│ ├── init.py
│ ├── reader.py
│ ├── analysis.py
│ └── metrics.py
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
