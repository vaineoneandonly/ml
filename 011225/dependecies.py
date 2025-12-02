from deps import *

import batch1, batch2

if __name__ == "__main__":
    #module
    m = getattr(sys.modules[__name__], sys.argv[1], None)
    
    #function of module
    f = getattr(m, sys.argv[2], None)
    f()