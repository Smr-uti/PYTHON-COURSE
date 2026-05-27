msg= " Hello World"
msg1=" Hello India"
fobj=open("text3.txt", "a")
fobj.write(msg)
fobj.close()
fobj2=open("text3.txt", "a")
fobj2.write(msg1)
fobj2.close()
