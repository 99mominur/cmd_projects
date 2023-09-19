import glob
import shutil
import os

source_path = "../source/*"
destination_path = "../destination/"

postfix = [1, 2, 3]

source_obj = glob.glob(source_path)

# print(source_obj)

object_path = source_obj[0]

shutil.copy(object_path, ".")

instance_file = object_path.split("/")[-1]
object_name = object_path.split("/")[-1].split(".")
prefix = object_name[0]
postfix2 = object_name[1]

# print(prefix, postfix)


# print(object_name1)

for item in postfix:
    fileName = prefix + "_" + str(item) + "." + postfix2
    print(fileName)
    shutil.copy(object_path, f"{destination_path}{fileName}")

os.remove(object_path)
os.remove(instance_file)
