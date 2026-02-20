# app/utils/file_handler.py
import os
import re

def save_html_report(html_content: str, version: str, output_dir: str = "static/reports") -> str:
    """
    Limpa, formata e salva o HTML em disco.
    Retorna o caminho relativo do arquivo salvo.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    if isinstance(html_content, str):
        clean_html = html_content.strip().strip('"').strip("'")
        clean_html = clean_html.replace("\\n", "\n").replace('\\"', '"')
    else:
        clean_html = str(html_content)

    safe_version = re.sub(r'[^a-zA-Z0-9_.-]', '', version)
    filename = f"release_notes_{safe_version}.html"
    file_path = os.path.join(output_dir, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(clean_html)
    
    return file_path