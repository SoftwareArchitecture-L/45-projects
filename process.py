import os
for root, dirs, files in os.walk("E:\Architecture\Smell_Prediction/45-projects", topdown=False):
    for name in files:
        if name=="core_other.txt":
            print(os.path.join(root, name))