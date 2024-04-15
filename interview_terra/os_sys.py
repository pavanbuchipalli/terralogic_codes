import os
# cmd = 'date'
# cmd= 'notepad'
# notepade =os.system(cmd)
cwd = os.getcwd()
print(cwd)
parent_dir='C:\Windows'
dir = 'pavan'
os.mkdir(os.path.join(parent_dir,dir))
