import os
import re

tex_files = [f for f in os.listdir('.') if f.endswith('.tex') and os.path.isfile(f)]

def process_text(content):
    parts = re.split(r'(\\begin\{lstlisting\}.*?\\end\{lstlisting\})', content, flags=re.DOTALL)
    
    for i in range(0, len(parts), 2):
        text = parts[i]
        
        # 1. Normalize already italicized words to lowercase
        text = re.sub(r'\\textit\{Frontend\}', r'\\textit{frontend}', text)
        text = re.sub(r'\\textit\{Backend\}', r'\\textit{backend}', text)
        
        # 2. Find bare 'Frontend' or 'frontend' (not preceded by \textit{)
        text = re.sub(r'(?<!\\textit\{)\b[Ff]rontend\b(?![\w}])', r'\\textit{frontend}', text)
        text = re.sub(r'(?<!\\textit\{)\b[Bb]ackend\b(?![\w}])', r'\\textit{backend}', text)
        
        parts[i] = text
        
    return ''.join(parts)

for file in tex_files:
    with open(file, 'r', encoding='utf-8') as f:
        original = f.read()
    
    updated = process_text(original)
    
    if original != updated:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f'Fixed {file}')
