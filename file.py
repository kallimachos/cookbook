# gets input and writes it to a file

readme = raw_input("Enter some text: ")
doc = open('doc.xml', 'w')
doc.write(readme)
doc.close()
