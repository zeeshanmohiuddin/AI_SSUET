#*********Methods*********
# def my_print(num1,num2):
#     return num1*num2

# num = my_print(5,5)
# print(num)

#*********List********

# grades = [2,3,6,5,4]
# grades.append(25)
# print(sum(grades)/len(grades))


#******Tuples**********
# grades = (2,3,6,5,4) #can not add or append more variable in tuples it is fix
# print(sum(grades)/len(grades))

#*********Sets************
# grades = {2,3,6,5,4} #work as sets in math
# grades.add(55)
# print(sum(grades)/len(grades))

# set_1 = {1,2,3}
# set_2 = {4,5,6}
# print(set_1.union(set_2))

#***Exercise******

# my_list = [25,25,50]
# print(sum(my_list))

# my_tuple = (2)
# print(my_tuple)
# set_1 = {5,77,9,12,8,9,0}
# set_2 = {5,77,9,12}
# print(set_2.intersection(set_1))


#********loop**********

# num = [1,2,3,4,5,6,7,8,9]
# def evev_num_fun():
#     even_num = []
#     for a in num:
#         if a%2 == 0:
#             even_num.append(a)
#     return even_num

# print( evev_num_fun())

# def user_menu(choise):
#     loop_controller = True
    
#     while loop_controller == True:
#         if choise == 'a':
#             return "Add"
#         elif choise == 'q':
#             return "Quit"
# user_choise = input("Enter a to add q to quit: ")
# print(user_menu(user_choise))
    
#****************************


# def who_do_you_know():
#     know_people_list = []
#     loop_controller = True
    
#     while loop_controller == True:
#         known_people = input("Enter People you know: ")
#         know_people_list.append(known_people)
#         loop_stopper = input("Enter add for more people and q for quit: ")
#         if loop_stopper == "q":
#             loop_controller = False
            
#         else:
#             loop_controller = True
        
#     return know_people_list



# def ask_user():
#     your_name = input("Enter your name: ")
#     return your_name

# list_of_known_people = who_do_you_know()
# check_person = ask_user()
# if check_person in list_of_known_people:
#     print("You are in known people list")
# else:
#     print("You are not in list")



#**********************


# def who_do_you_know():
#     known_people = input("Enter Peoples you know seperate by , : ")
#     know_people_list = known_people.split(",")
#     return know_people_list



# def ask_user():
#     your_name = input("Enter your name: ")
#     return your_name

# list_of_known_people = who_do_you_know()
# check_person = ask_user()
# if check_person in list_of_known_people:
#     print("You are in known people list")
# else:
#     print("You are not in list")


#************ List Compresension **************

# range_list = [x * 3 for x in range(5)] 
# print(range_list)

# even_num = [x for x in range(10) if x % 2 == 0]
# print(even_num)

# people = ["Ali", " waqas", "HASAN"]
# format_people = [person.strip().lower() for person in people]
# print(format_people)


#*************** CLASSES AND OBJECTS ***********************

# class my_class:
#     def __init__(self,name):
#         self.name = name
#         self.num = (1,2,3)
#     def total(self):
#         return sum(self.num)

# person_1 = my_class("zee")
# person_2 = my_class("shan")
# print(person_1.name)
# print(person_2.name)



#******************************************

class student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []
    def avg_marks(self):
        return sum(self.marks)/len(self.marks)
    
    @staticmethod
    def go_to_school():
        # print("Im going to {}".format(self.school))
        print("im going to school")


zeeshan = student("Zeeshan","UIT")

# enter_marks = input("Enter marks: ")
# zeeshan.marks = enter_marks.split(',')

zeeshan.marks.append(56)
zeeshan.marks.append(12)
zeeshan.marks.append(45)
zeeshan.marks.append(67)
# print(zeeshan.marks)
# print(zeeshan.avg_marks())
# zeeshan.go_to_school()
student.go_to_school()

# *********************************

# class Store:
#     def __init__(self,name):
#         self.name = name
#         self.items = []
#     def add_item(self,name,price):
#         item = {
#             'name' : name,
#             'price' : price
#         }
#         self.items.append(item)
    
#     def stock_price(self):
#         return sum(item['price'] for item in self.items)

# store1 = Store('Store_one')
# print(store1.stock_price())

        