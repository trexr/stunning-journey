import sys
import utils


print("This is argv:", sys.argv)
command = sys.argv[1]
print(command)
if command == "build":
    utils.main()
    print("Build was specified")
elif command == "new":
    print("New page was specified")
    filename = (sys.argv[2] or "default") + '.html'
    utils.create_file(sys.argv[2], 'content')
else:
    print("Please specify ’build’ or ’new’")
