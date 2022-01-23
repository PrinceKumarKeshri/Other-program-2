from pathlib import Path
import os
print(Path.home())

get_path = str(Path.home())
spli = get_path.split('\\')
path = '/'.join(spli)
print(path)
#new_path = path + '\Desktop\may'
#os.chdir(path)
#os.mkdir(new_path)
# Binary Method

#import os
#print(os.path.expanduser('~'))
