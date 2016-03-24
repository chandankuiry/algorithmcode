def Towers(size,fromstack,tostack,sparestack):
	if size==1:
		print 'move disk form ',fromstack,'to',tostack
	else:
		Towers(size-1,fromstack ,sparestack,tostack)
		Towers(1,fromstack,tostack,sparestack)
		Towers(size-1,sparestack,tostack,fromstack)
Towers(15,'f','t','s')
