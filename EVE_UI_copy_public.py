# Importing the modules
import os
import shutil

src_dir = os.getcwd() 
print(src_dir)



master_user="core_user_###.dat"
master_char="core_char_###.dat"

second_user="core_user_###.dat"
second_char="core_char_###.dat"

third_user="core_user_###.dat"
third_char="core_char_###.dat"

fourth_user="core_user_###.dat"
fourth_char="core_char_###.dat"

#second
print("second")
if os.path.exists(src_dir + "\\" + second_char):
    os.remove(src_dir + "\\" + second_char)
shutil.copy2(src_dir + "\\" + master_char, src_dir + "\\" + second_char)

if os.path.exists(src_dir + "\\" + second_user):
    os.remove(src_dir + "\\" + second_user)
shutil.copy2(src_dir + "\\" + master_user, src_dir + "\\" + second_user)

#third
print("third")
if os.path.exists(src_dir + "\\" + third_char):
    os.remove(src_dir + "\\" + third_char)
shutil.copy2(src_dir + "\\" + master_char, src_dir + "\\" + third_char)

if os.path.exists(src_dir + "\\" + third_user):
    os.remove(src_dir + "\\" + third_user)
shutil.copy2(src_dir + "\\" + master_user, src_dir + "\\" + third_user)

#fourth
print("fourth")
if os.path.exists(src_dir + "\\" + fourth_char):
    os.remove(src_dir + "\\" + fourth_char)
shutil.copy2(src_dir + "\\" + master_char, src_dir + "\\" + fourth_char)

if os.path.exists(src_dir + "\\" + fourth_user):
    os.remove(src_dir + "\\" + fourth_user)
shutil.copy2(src_dir + "\\" + master_user, src_dir + "\\" + fourth_user)