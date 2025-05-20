import os
import subprocess
from tqdm import tqdm
import argparse

def convert_with_libreoffice(input_path, output_path):
    """Конвертация через LibreOffice"""
    try:
        cmd = [
            'soffice',
            '--headless',
            '--convert-to', 'pdf',
            '--outdir', output_path,
            input_path
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False

def process_conversion(input_path, output_path):
   
    os.makedirs(output_path, exist_ok=True)
    docx_files = []
    for root, _, files in os.walk(input_path):
        for file in files:
            if file.endswith(".docx"):
                docx_files.append(os.path.join(root, file))
    for docx_file in tqdm(docx_files, desc="Конвертация"):
        try:
            relative_path = os.path.relpath(os.path.dirname(docx_file), input_path)
            target_dir = os.path.join(output_path, relative_path)
            os.makedirs(target_dir, exist_ok=True)
            
            if not convert_with_libreoffice(docx_file, target_dir):
                print(f"\nОшибка конвертации: {docx_file}")
                
        except Exception as e:
            print(f"\nКритическая ошибка: {docx_file} - {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DOCX to PDF Converter (LibreOffice)')
    parser.add_argument('input')
    parser.add_argument('-o', '--output', required=True)
    
    args = parser.parse_args()
    process_conversion(args.input, args.output)