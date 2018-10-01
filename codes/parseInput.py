import sys
import os

# Output directory where we are to save our scored files
out_dir = None

# Will be filled with infile names
in_file_list = []

def parseArgs():
    global out_dir
    global in_file_list
    
    argCount = len(sys.argv)

    # first arg is always name of script. Must be even number of args
    if argCount % 2 != 1:
        print("Must pass even number of flags, ie (-i <infile>) -o <output>")
        sys.exit(1)

    seenOutputFlag = False
    flagIsInput = True
    
    readingFlag = True
    for arg in sys.argv[1:]:
        readingFlagCopy = readingFlag
        readingFlag = not readingFlag
        if readingFlagCopy:
            if arg != "-i" and arg != "-o":
                print("unrecognized flag %s" % (arg))
                sys.exit(1)

            if arg == "-o":
                if seenOutputFlag:
                    print("Repeated -o flag not allowed")
                    sys.exit(1)

                flagIsInput = False
                seenOutputFlag = True
            else:
                flagIsInput = True
        else:
            if arg[0] == "-":
                print("Incorrect usage, %s cannot be an argument to a flag" % arg)
                sys.exit(1)
            if flagIsInput:
                in_base = os.path.basename(arg)
                allowed_input_names = ["profession.test", "nationality.test"]
                if in_base not in allowed_input_names:
                    print("Input file must be one of: %s" % (" ".join(s for s in allowed_input_names)))
                    sys.exit(1)
                in_file_list.append(arg)
            else:
                out_dir = arg


    if out_dir is None or len(in_file_list) == 0:
        print("both -o and -i are required. Exiting")
        sys.exit(1)

# Ranking script must accept
# Calls ranking script
def runRanker(in_file_path, out_dir_path):
    out_dir_path = out_dir_path + os.sep

    in_base = os.path.basename(in_file_path)
    out_filename = out_dir_path + in_base
    
    is_nationality = (in_base == "nationality.test")

    # TODO: handle read write errosr
    # Namely, if one infile is not readable, need to continue on to call score() on other infiles
    with open(in_file_path, 'r') as in_handle:
        with open(out_filename, 'w+') as out_handle:
            score(in_handle, out_handle, is_nationality)

if __name__ == "__main__":
    parseArgs()
    for i in in_file_list:
        runRanker(i, out_dir)


