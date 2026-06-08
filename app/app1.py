import os
import pathlib
import runpy

ROOT = pathlib.Path(__file__).resolve().parent
os.chdir(ROOT)
runpy.run_path(str(ROOT / "app.py"), run_name="__main__")
