from timeit import Timer
popzero = Timer("x.pop(0)",
                       "from __main__ import x")
popend = Timer("x.pop()",
                      "from __main__ import x")

x = list(range(2000000))
print "time taken for poping from first position =%10.7f"%(popzero.timeit(number=1000))


#output
#4.8213560581207275

x = list(range(2000000))
print "time taken for poping from last position  =%10.7f"%(popend.timeit(number=1000))
#output
#0.0003161430358886719
