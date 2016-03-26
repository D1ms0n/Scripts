import os

os.chdir('/data/work/virtualenvs/magaz/')
os.system('source bin/activate')
os.chdir('/data/work/virtualenvs/magaz/src/')
os.system('../bin/django-admin startproject "gooood"')
os.chdir("gooood")
os.system('python manage.py startapp "goodapp"')
os.chdir("goodapp")
os.system('mkdir -p templates/"gooood"')