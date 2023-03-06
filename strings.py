website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

a = " Hello World "
a = a.strip()
a = website.strip('h t p : /')
a = website.strip('h t p : / w . c o m ')
a = course.lower()
a = course.title()
a = website.count('a')
a = website.startswith('http')
a = website.find('.com',0,10)
a = course.rfind('Python')
a = course.center(122, '*')
a = course.rjust(122, '*')
a = course.replace(' ','')
a = 'hello world'
a = a.replace('world','there')
a = course.split(' ')
a = a[2]

print(a)


