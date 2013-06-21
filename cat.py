cat = ["a","b","c","d", "e"]
dog = [5,6,7,8]
# value = "cat"
# index=3

#cat.insert(index,value)
#cat.remove(3)
#print cat

# cat[-1:3:-1]  

# print cat

#cat=[0:len(cat)+1]=[len(cat)-1:-1:-1]

#cat=[0:-1:1]=[(len(cat)-1):-1:-1]
#print cat

temp=" "

# forward_counter = 0 
# backward_counter = 1

# for element in cat:
# 	element=temp
# 	cat[len(cat)-backward_counter] = cat[forward_counter]
# 	temp=cat[len(cat)-forward_counter]
# 	forward_counter += 1
# 	backward_counter += 1
# print cat

counter1=1
counter2=2
counter3=0
counter4=1

for element in cat:
	element=temp
	[len(cat)-counter1:len(cat)-2] = [counter3:counter4]
	temp=[len(cat)-counter1:len(cat)-2]
	counter1+=1
	counter2+=1
	counter3+=1
	counter4+=1


#cat[len(cat):-1:-1]=[4]
# counter = 0
# for element in cat:
# #	cat[len(cat)-1:-1:-1]
# 	cat[::-1]
# 	counter += 1
# print cat[(counter-1)]	

# new_list = []
# for element in range(len(cat)-1,-1,-1):
# 	new_list += cat[element]
# cat=new_list
# print cat 



#cat[len(cat)-1:-1,-1]



 

# temp = ""

#new_list = []

# print "NEW LIST: %r" % new_list

# for element in cat:
# 	element = temp
# 	new_list += temp
# print cat.extend(new_list)
# # value = 3

# while element is not cat[-1]:
# 	element = temp
# 	cat += temp
# print cat

# counter=0
# print "Value: %r " % value

# for element in cat:
#     print "COUNTER: %r" % counter
#     print "ELEMENT: %r" % element
#     if element == value:
#        del cat[counter]
#     counter += 1
#cat.append(dog)
#print "append should list 1-9!!!!"
#print cat

#cat.extend(dog)
#print "extend does the same thing??"
#print cat

#dog.insert(4,9)

#for element in print
#x dog
#for element in cat:
#	print element