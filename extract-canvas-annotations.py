# Extract annotations from pdf with Canvas annotations.
# 1. Download annotaded pdf from Canvas.
# 2. Generate new pdf with annotations on sep. page after each page.
#     - In Adobe: Do print to pdf after click on Summrize Comments at bottom of print dialogue.
#     - In Adobe: Copy all (CtlA CtlC) of generated pdf file contents to Notepad (CtlV) - save as ANSI-file!
# 3. Run this script on that ANSI-file.
#
# NB: Uses that all project files has page banner starting with "MdU/FLA402" - see note in source code!
#
# History:
# 2024-10-25/GF: Introduced 0.1/0 
#

import sys

# total arguments
n = len(sys.argv)

C_THIS_VERSION = "Extract Canvas Annotations v.0.1/0 of 2024-10-25/GF"

print()
print(C_THIS_VERSION)

argCount = len(sys.argv)
if argCount == 1:
    print("Missing file name!");
    ansiFileName = input("ANSI File name: ")

if argCount == 2:
    ansiFileName = sys.argv[1]

if argCount > 2:
    print("Too many arguments - aborts!");
    exit(1)


print("Using file '" + ansiFileName + "'")
isInsideAnnotation = 0
lineNr = 0;
with open(ansiFileName ) as f:
    while True:
        line = f.readline()
        #print("*** lineNr = ", lineNr, '"' + line.strip() + '"') 
        if not line:
            break
        lineNr = lineNr + 1
        if (isInsideAnnotation == 1):
            if ("MdU/FLA402" in line): 		# Needs hands-on edit when used for different project
                isInsideAnnotation = 0
        if ("Page: " in line):
            print()
            isInsideAnnotation = 1
        if (isInsideAnnotation == 1):
           print(line.strip()) 

print("\nLine Count = ", lineNr)
print("\nEnd of execution of " + C_THIS_VERSION)
print()