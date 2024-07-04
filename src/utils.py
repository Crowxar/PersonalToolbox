from pathlib import Path
import crowdebug as cdb


def asset_path(image:str) -> Path:
    ASSETS_PATH = Path(__file__).resolve().parent / "Assets"
    cdb.log.info(f"Returning {ASSETS_PATH/image}")
    return ASSETS_PATH/ image