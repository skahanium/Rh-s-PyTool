from pathlib import Path


def full_path():
    return str(Path(__file__).resolve().parent / "attachment" / "adcodes.csv")
