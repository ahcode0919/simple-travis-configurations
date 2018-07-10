import compileall
import os
import sys

# Get path of this file's directory
directory = os.path.dirname(os.path.realpath(__file__))

# Check that files are compileable
success = compileall.compile_dir(dir=directory, maxlevels=20, force=True)

# Return appropriate exit code
sys.exit(0) if success else sys.exit(1)
