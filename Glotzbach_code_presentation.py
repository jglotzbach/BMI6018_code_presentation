#Jason Glotzbach code used in code presentation

#Quiz: Advanced Functions and Logic (Question 5)
#It is possible to write any recursive function with a while loop. (True/False)

#Answer: TRUE


#example code: Jason Glotzbach inner list problem using recursion

def innerloop_plus1(lst):
    for element in lst:
            if isinstance(element, list):
                return innerloop_plus1(element)
    output_list = [x + 1 for x in lst]
    print(output_list)

# example solution:
innerloop_plus1([1,[2,3,[4,[7,9,[22,99],8,2],5],6,7,8],9])


#example code: Jason Glotzbach module 5 assignment inner list using while loop

def innerloop_plus1(lst):
    while any(isinstance(element, list) for element in lst):
        for element in lst:
            if isinstance(element, list):
                lst = element
                break
    output_list = [x + 1 for x in lst]
    print(output_list)

# example solution:
innerloop_plus1([1,[2,3,[4,[7,9,2],5],6,7,8],9])



#answer to Debugging Assignment, Question 1a:

def wrong_add_function(arg1,arg2):
   arg1_index=0
   while arg1_index < len(arg1):
      arg_2_sum = 0
      print('arg1 is currently' ,arg1)
      print('arg_2_sum is currently' ,arg_2_sum) 
      for arg2_elements in arg2:
         arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
      print('arg_2_sum is now' ,arg_2_sum)
      print('arg1 is now' ,arg1) 
      print('arg1_index is now' ,arg1_index)
      print('we are making an error in the loop') 
      print(f"The correct answer for arg1 index {arg1_index} is supposed to be {arg1[arg1_index]} plus {arg2[arg1_index]}")
      arg1[arg1_index]=arg_2_sum 
      arg1_index+=1
   return arg1
   print(arg1) 

arg1 = [1,2,3]
arg2 = [1,1,1]

wrong_add_function(arg1, arg2)