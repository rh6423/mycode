#!/usr/bin/env python3

# import utils for file interaction
import shutil
import os

# start in subdir of home directory
os.chdir('/home/student/mycode')

# move a file
shutil.move('raynor.obj', 'ceph_storage/')

xname = input('What is the new name for kerrigan.obj?')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

