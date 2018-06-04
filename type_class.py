def fn(self, name='world'):
	print('Hello, %s.' % name)

H = type('Hello',(object,),dict(play=fn))
print type(H)
h=H()
h.play()
