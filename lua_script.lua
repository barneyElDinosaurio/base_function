print("first lua")
-- comment
-- end
print(type('hello'))
print(type(10))
print(type(10.0))
print(type(print))
print(type(type))
print(type(true))
print(type(nil))
print(type(type(X)))

--calc len
name='lua script'
print('len of name')
print(#name)

t={'taobao','jd'}
print(t)
print('frist elem of t')
print(t[1])
print(t['taobao'])

a = {}
a["key"] = "value"
key = 10
a[key] = 22
a[key] = a[key] + 11
print('a key ')
print(a[1])
print(a['key'])
for k, v in pairs(a) do
    print(k .. " : " .. v)
end

function factorial(n)
  if n==0 then
    return 1
  else 
	return n * factorial(n-1)
  end
end

print('function')
print(factorial(5))
f=factorial
print(f(5))


-- loop
cycle=10
while(cycle>0)
do
print('current cycle')
print(cycle)
cycle=cycle-1
end

animal='dog'
if animail=='dog' then
print('wo wo wo')
else
print('person')
end

function max(n1,n2)
if n1>n2 then
return n1
else
return n2
end
end
print(max(10,11))

myprint = function(content)
print('this is my print ::: ',content)
end

myprint('KING')
