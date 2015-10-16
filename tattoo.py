from tattoo.application import TattooApplication

import sys

if __name__ == "__main__":
    app = TattooApplication()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
    
