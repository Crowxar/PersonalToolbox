from pathlib import Path
import crowdebug as cdb
import markdown
import os

def asset_path(image:str) -> Path:
    ASSETS_PATH = Path(__file__).resolve().parent / "Assets"
    cdb.log.info(f"Returning {ASSETS_PATH/image}")
    return ASSETS_PATH/ image


def create_HTML_file(file_path):
    html_file_path = os.path.splitext(file_path)[0] + '.html'
    write_file_content(html_file_path, markdown.markdown(read_file_content(file_path)))
    return html_file_path

def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
    return file_content

def write_file_content(file_path, content):
    with open(file_path, "w", encoding="utf-8") as output_file:
        output_file.write(content)