line = "-----------------------------------------"
courses = ["History", "Math", "Physics", "CompSci"]

print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1])
# print(courses[4])
print(courses[0:2])
print(courses[:2])
print(courses[2:])
print(line)
#################
courses.append("Art")
print(courses)
courses.insert(0, "Art")
print(courses)
print(line)
#################
courses_2 = ["Art", "Education"]
courses.insert(0, courses_2)
print(courses)
print(courses[0])
#################
courses.extend(courses_2)
print(courses)
print(line)
print(line)
##################
courses = ["History", "Math", "Physics", "CompSci"]
print(courses)
courses.remove("Math")
print(courses)
courses = ["History", "Math", "Physics", "CompSci"]
popped = courses.pop(2)
print(popped)
print(courses)
print(line)
#######################
courses = ["History", "Math", "Physics", "CompSci"]
print(courses)
courses.reverse()
courses.sort()

nums = [1, 5, 4, 3]
nums.sort()
print(nums.sort())
print(courses)
print(nums)

nums.sort(reverse=True)
print(nums)
print(line)
################################
courses = ["History", "Math", "Physics", "CompSci"]
sorted_courses = sorted(courses)
print(courses)
print(sorted_courses)
print(line)
################################
courses = ["History", "Math", "Physics", "CompSci"]
nums = [1, 5, 4, 3]
print(min(nums))
print(sum(nums))
print(courses.index("CompSci"))
print("Math" in courses)
################################
print(line)

for item in courses:
    print(item)

for index, item in enumerate(courses):
    print(index, item)

for index, item in enumerate(courses, start=1):
    print(index, item)

##################################
print(line)
course_str = " - ".join(courses)
print(course_str)

new_list = course_str.split(" - ")
print(new_list)
#################################
print(line)
print(line)
list_1 = ["History", "Math", "Physics", "CompSci"]
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = "Art"
print(list_1)
print(list_2)
#######################################
print(line)
print(line)

# tuple () is immutable - ie will not change

tuple_1 = ("History", "Math", "Physics", "CompSci")
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
# tuple_1[0] = "Art"

#######################################
print(line)
print(line)

# call set {} used to remove duplicates or do a membership test

cs_course = {"History", "Math", "Physics", "CompSci"}
print(cs_course)
cs_course = {"History", "Math", "Physics", "CompSci", "Math"}
print(cs_course)
print("Math" in cs_course)
cs_course = {"History", "Math", "Physics", "CompSci"}
art_course = {"History", "Math", "Art", "Design"}
print(cs_course.intersection(art_course))
print(cs_course.difference(art_course))
print(cs_course.union(art_course))
#################################
empty_list = []
empty_list2 = list()  # use of built-in list class with no values
empty_tuple = ()
empty_tupple = tuple()  # use built-in tuple class with no values
empty_set = {}  # this will create an empty dictionary instead !! gotcha
print(empty_set)
empty_set = set()  # use of built-in set class with no values
