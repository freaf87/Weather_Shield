# Cleanup eagle auto generated files
import os, glob

currentdir = os.path.realpath(__file__)
deleteditems = []

for file in glob.glob("*.s#*"):
    os.remove(file)
    deleteditems.append(file)

for file in glob.glob("*.b#*"):
    os.remove(file)
    deleteditems.append(file)

if os.path.isdir('lib'):
    os.chdir("lib")
    for file in glob.glob("*.l#*"):
        os.remove(file)
        deleteditems.append(file)

if deleteditems:
    print("Deleted files:")
    for item in deleteditems:
        print(item)
else:
    print("Nothing to be done !!")