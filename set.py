from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH_2 = Path.joinpath(ROOT_PATH, "tests")
OPEN_CSV = Path.joinpath(DATA_PATH_2, "item.csv")
print(OPEN_CSV)
