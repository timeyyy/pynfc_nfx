from cffi import FFI
ffi = FFI()
#~ import ctypes
#~ test = ctypes.CDLL('./test.o')
ffi = FFI()
ffi.cdef("""
void ass();

""")
C = ffi.verify("""#include "test.c"
""")


#~ print (C.ass())
