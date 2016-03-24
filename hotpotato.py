from queuedefine import *
def hotpotato(namelist,num):
	potatoqueue=Queue()
	for name in namelist:
		potatoqueue.enqueue(name)

	while potatoqueue.size() > 1 :
		for i in range(num):
			potatoqueue.enqueue(potatoqueue.dequeue())

		potatoqueue.dequeue()
	return potatoqueue.dequeue()


print(hotpotato(["Bill","David","Susan","Jane","Kent","Brad"],7))