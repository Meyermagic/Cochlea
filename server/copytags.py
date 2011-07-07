#!/usr/bin/env python2
import sys
import mutagen

source = mutagen.File(sys.argv[1], easy=True)
dest = mutagen.File(sys.argv[2], easy=True)
for key in source:
    try:
        dest[key] = source[key]
    except:
        pass
dest.save()
