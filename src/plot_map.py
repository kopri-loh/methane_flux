from pathlib import Path

import pandas as pd
import numpy as np

# Set-up local (and temporary) sys.path for import
# All scripts for calculations and plots need this
from context import add_path


add_path(Path(".").resolve())

try:
    import lib.io
    import lib.proj

    from lib.conv import conv
except Exception:
    raise Exception("Issue with dynamic import")


def main():
    df_gps, df_li = lib.io.get_pq(2022, 7, 3)


if __name__ == "__main__":
    main()
