import logging_config as log
import os


def ensure_file_exists(
        file_path: str, file_name: str, create: bool = False) -> bool:
    
    full_path = os.path.join(file_path, file_name)
    log.logging.info(f"Validating file {full_path} exists")
    if not os.path.exists(full_path):
        if create:
            log.logging.info(
                f"Creating requested file {file_name} in {file_path}")
            with open(full_path, 'w') as f:
                pass
            return False
        return False
    log.logging.info(f"File {full_path} already exists")
    return True