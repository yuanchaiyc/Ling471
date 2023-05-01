from pathlib import Path

p = Path('c:/users')
print(p)
p /= 'matt'
print(p)

ff = list(p.glob('*'))
print(ff)

all_files = [x for x in p.glob('*') if x.is_file()]
print(all_files)

docx = [x for x in p.glob('*.docx')]
print(docx)
pdf = [x for x in p.glob('*.pdf')]
print(pdf)

py = [x for x in p.glob('*.py')]
print(py)

jpg = [x for x in p.glob('*.jpg')]
print(jpg)
