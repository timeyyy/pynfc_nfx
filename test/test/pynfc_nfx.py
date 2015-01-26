import ctypes

_polling = ctypes.CDLL('_polling.so')

def poll(): #run main from card polling, returns type of card 
	print('come')
	return _polling.myprint()
	#~ return _polling.my_mod(ctypes.c_int(5), ctypes.c_int(2))
	
poll()
print('e')
