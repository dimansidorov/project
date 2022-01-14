import shutil as s
import os

r_dir = os.path.join(os.path.dirname(__file__), 'my_project')
d_dir = os.path.join(os.path.dirname(__file__), 'my_project', 'templates')

if not os.path.exists(d_dir):  # если папки нет - создаем
    os.makedirs(d_dir)

for root, dirs, files in os.walk('.'):
    if d_dir in dirs:
        for dr in dirs:
            if os.path.exists(os.path.join(d_dir, dr)):
                os.makedirs(os.path.join(d_dir, dr))
        for file in files:
            scr_file = os.path.join(root, file)
            d_file = os.path.join(d_dir, os.path.basename(root))
            if os.path.dirname(scr_file) == d_file:
                s.copy(scr_file, d_file)
