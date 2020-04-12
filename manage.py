import sys
import utils

print("This is argv:", sys.argv)
command = sys.argv[1]

if command == "build":
    utils.main()
    print("Build was specified")
elif command == "new":
    filename = (sys.argv[2] if len(sys.argv) > 2 else "default") + '.html'
    utils.create_file(filename, 'content/')
    print("New page was specified")
else:
    print("Please specify ’build’ or ’new’")
