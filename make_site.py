import os
from pathlib import Path
from pelicanconf_static_paths import STATIC_PATHS

# Find all notebooks
p = Path('content')
notebooks = [f for f in p.glob('**/*.ipynb') if '-checkpoint' not in f.name]

# Convert notebooks to Markdown
for file in notebooks:
    os.system('jupyter nbconvert {} --to markdown'.format(file))
    file = str(file).replace('.ipynb', '.md')
    # Remove first line of file or content won't load
    with open(file, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(file, 'w') as fout:
        fout.writelines(data[1:])

# Find directories containing generated images
img_dirs = [
    str(d)[8:] for d in list(p.glob('**')) if d.name.endswith('_files') and '.ipynb_checkpoints' not in str(d)
]
STATIC_PATHS.extend(img_dirs)
for i in range(len(STATIC_PATHS) - 1):
    STATIC_PATHS[i] = "    '" + STATIC_PATHS[i] + "',\n"
STATIC_PATHS[-1] = "    '" + STATIC_PATHS[-1] + "'\n"

# Import base pelican config
with open('pelicanconf_base.py', 'r') as file:
    conf = file.read().splitlines(True)

conf.extend(['\n', 'STATIC_PATHS = [\n'])
for path in STATIC_PATHS:
    conf.append(path)
conf.extend([']\n', '\n'])

# Write pelican config with all static paths
with open('pelicanconf.py', 'w') as file:
    file.writelines(conf)

# # Compile site
generate_site = os.system('pelican content -o output -s pelicanconf.py')

# If no error:
if generate_site == 0:
    # Print action
    print('No errors found during site generation, deploying to Github Pages')
    
#     # Publish site to github
    os.system('ghp-import -m "Generate Pelican site" -b gh-pages output -c lewisdavi.es')
    os.system('git push origin gh-pages')
else:
    # Print error
    print('Error found during site generation, halting deployment')

