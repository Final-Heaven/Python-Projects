

import os
import re


Path1 = 'C:\\ScriptAssignment\\'


x = os.listdir(Path1)
FullDirectory = ' '.join(x)
print(FullDirectory)
print("")


TextFiles = re.findall("Hello.{2}txt", FullDirectory)
print(TextFiles)


for x in TextFiles:
    print(x + " was last modified: " + str(os.path.getmtime(os.path.join(Path1, x))))








