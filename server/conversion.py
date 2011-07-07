#!/usr/bin/env python

#Will be a daemon for queuing song conversions. Listens on a TCP socket for song IDs, or uses some other IPC. Will take care of starting conversions efficiently (keeping a certain number running when on a multi-core machine, for instance). Will also update the status entry for the converted songs in the database.
