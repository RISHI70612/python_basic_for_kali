#STRING
#print string
print("hello world")
print('hello,world')
print("this string is "+"awesome!") # we can also concatenate
print ('\n') #new line
print ('test that new line ')

#MATH 
print ('\n') #new line
print (50+50) #add
print (50-50) #subtract
print (50*50) #multiply
print (50/50) #divide
print (50+50-50*50/50) #PEMDAS
print (50**5) #exponentials
print (50%6) #remainder
print (50//6) #division withour remainder


#VARIABLES AND METHODS
print ('\n') #new line

quote = "Hacking is the basic need of human " 
print (quote)
print (quote.upper())#uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #counts characters

name = "rishi" #string
age = 22 #Int

print (int(age))
print(int(30.1))
print("My name is " +name +" and I am " + str(age) +" years old .")

age += 1
print(age)

#FUNCTIONS
print ('\n') #new line

def who_am_i():  # this is a function without parameters
    name = "jen"  # local variable
    age = 20
    print("My name is " + name + " and my age is " + str(age) + " years old.")

who_am_i()  # Call the function by adding parentheses at the end

def add_one_hundred(num):  # function containing one parameter
    print(num + 100)

add_one_hundred(900)  # Call the function with an argument (e.g., 900)

def add(x,y): #function containing two parameters
  print(x+y)
  
add(6,9)
 
def multiply(x,y) :
 return x*y
print (multiply(6,9))  

#CONDITIONAL STATEMENT - if/else
def drink(money):
     if money >= 2:
          return " you got yourself a drinK"
     else : 
          return "fuck off, loser" 

print("\n")    
 
def nl():
    print('\n')      
          
print(drink(3))
print(drink(1))              

nl() 
def alcohol(age, money):
    if (age >= 21) and (money >= 5):
        return "you are getting a drink"
    elif (age >= 21) and (money < 5):
        return "come back with more money"
    elif (age < 21) and (money >= 5):
        return "go to study kiddo"
    else:
        return "you are so poor and young kiddo"

print(alcohol(20, 3))

nl()
#LIST - have brackets []

movie = ['avengers' , 'lort', 'justice league' , 'hobbit' ] 
print (movie[0]) #return first item from the list 
print (movie[1:3]) #return the first index number given right untill the last index but doesnot include the last number 
print(movie[1:])
print(movie[:1])

print(len(movie)) #count the numbers of item in the lists 

movie.append('Harry potter') #add to the end of the lists 
print(movie)

movie.insert(2,'hustle')
print(movie)

movie.pop() #removes the last item 
print(movie)

movie.pop(0) #removes the first item
print(movie)

grades = [["jenn",85], ["rupak", 84], ["god", 95]]
god_grade = grades[2][1]
print (god_grade)
grades[0][1] =89
print(grades)

nl()

#TUPLES - donot change , ()
grades = ('a', 'b', 'c', 'd')
print (grades)
print (grades[2])
nl()

#for loops - start to finish of an itrate
person = ['rupak', 'jessica', 'ankit', 'jenny']
for x in person : 
   print (x)
   
#while loops - execute untill it is true  
i =1

while i<10:
    print(i)
    i += 1 
    
nl()

#ADVANCE STRINGS 
# ADVANCE STRING
my_name = "god"
print(my_name[0])  # first letter
print(my_name[-1])  # last letter

sentence = "this is a sentence"
print(sentence[:4])
print(sentence.split())  # delimiter - default is a space

too_much_space = "     hi     "
print(too_much_space.strip())


print ('A' in 'Apple')
print ('a' in 'Apple')

letter= "A"
word="Apple"
print(letter.lower() in word.lower()) #improved


movie = "endgame" 
print(f'my favourite movie is {movie} ')


#DICTIONARIES
person = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York',
    'email': 'john.doe@example.com'
}

print(person)

#adding elements in a dictionary 

# Create an empty dictionary
student = {}

# Add elements to the dictionary
student['name'] = 'John Doe'
student['age'] = 25
student['grade'] = 'A'

print(student)


student = {'name': 'John Doe', 'age': 25, 'grade': 'A'}

# Deleting 'grade' from the dictionary
del student['grade']

print(student)

grades = {'Math': 90, 'Science': 85, 'History': 78, 'English': 92}

# Removing 'History' from the dictionary and getting its value
history_grade = grades.pop('History')

print(grades)       # Output: {'Math': 90, 'Science': 85, 'English': 92}
print(history_grade)  # Output: 78

student = {'name': 'John Doe', 'age': 25}

# Clear the dictionary (remove all elements)
student.clear()

print(student)  # Output: {}
