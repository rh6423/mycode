#!/usr/bin/env python3
# need shutil and os to interact with files
import shutil
import os

# always start in mycode subdirectory of homedir
os.chdir('/home/student/mycode')

# copy a file
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')

# copy a directory tree
shutil.copytree('5g_research', '5g_research_backup')

