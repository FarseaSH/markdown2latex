# ===================================================== #
# A simple Python scirpt to transform Markdown to Latex #
# From: https://www.yyshao.com                          #
# ===================================================== #


import re
import os

SOURCE_DIR = "src"
OUTPUT_DIR = "output"

REPLACE_PATTERNS = [
    r"^\s*\\hypertarget\{.*\}\{%\n",
    r"\\label\{.*\}\}",
    r"^\s*\\tightlist\n",
    r"^\\def\\labelenumi\{\\arabic\{enumi\}\.\}\n"
]

def main():
    # find all the markdown(md) files
    mdFilesList = []
    for path, subdirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.endswith('.md'):
                mdFilesList.append(os.path.join(path, file))

    currentDirPath = os.path.dirname(os.path.realpath(__file__))
    for mdFile in mdFilesList:
        md2Latex(mdFile, currentDirPath=currentDirPath)
        modifyLatexFile(mdFile)
    

def modifyLatexFile(filePath):
    filePath = os.path.splitext(filePath)[0].replace(SOURCE_DIR, OUTPUT_DIR) + ".tex"
    print(filePath)

    with open(filePath, 'r') as file:
        data = file.read() 

        for pattern in REPLACE_PATTERNS:
            data = re.sub(pattern, '', data, flags=re.MULTILINE)
        
        if os.path.split(filePath)[1] == "README.tex":
            data = re.sub("section", "chapter", data, flags=re.MULTILINE)

    with open(filePath, 'w') as file:
        file.write(data)   
            

def md2Latex(filePath, currentDirPath):
    outputPath = os.path.splitext(filePath)[0].replace(SOURCE_DIR, OUTPUT_DIR) + ".tex"
    outputPath = os.path.join(currentDirPath, outputPath)

    os.system(f"mkdir -p '{os.path.split(outputPath)[0]}'")
    CMD = f"pandoc -o '{outputPath}' --template='{os.path.join(currentDirPath, 'template.latex')}' '{os.path.join(currentDirPath, filePath)}'"
    
    os.system(CMD)


if __name__ == "__main__":
    main()
