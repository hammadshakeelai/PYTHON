#Assignment 
# O(n) time complexity
# O(n) memory complexity
# 1.	Consider you are a junior developer in IMSCIENCES [ERP]. You are given a task to create a program for [counting students' marks]. The program should ask for the [number of students in a class]. Then, it should assign random marks to each student: from 5 to 30 for the mid-term and from 5 to 50 for the final term. Next, the program should calculate the total marks of each student and[ display their final marks.]
# Furthermore, group the students based on their total marks as follows:
# o	Group 1: Marks from 5 to 10
# o	Group 2: Marks from 11 to 20
# o	Group 3: Marks from 21 to 30
# o	… and so on, until:
# o	Group 8: Marks from 71 to 80
# Finally, print the number of asterisks (*) equal to the number of students in each group, with each group printed on a separate line. If a group has no students, print an empty line for that group.
# Output Example:
# If Group 1 has 5 students, Group 2 has 3 students, and Group 3 has 8 students, the output should be:
#####################################################################
#####################################################################
#####################################################################
import random
# from timeit import Timer 
num_of_std  = int( input( "Enter number of students:  " ) )
method = 2
method = int( input( "Enter method number:  " ) )
printt=1
if method == 1 :
        # Timer.timeit()
        std_num_list = [ ]

        for _ in range( num_of_std ):
        
                std_num_mids = random.randint( 5 , 30 )
                std_num_finals = random.randint(5 , 50 )
                
                std_total = std_num_finals + std_num_mids
                # print(f"Total Marks: {std_total}")
                std_num_list.insert( _ , std_total )
        
        nums_5_10 = []
        nums_11_20 = []
        nums_21_30 = []
        nums_31_40 = []
        nums_41_50 = []
        nums_51_60 = []
        nums_61_70 = []
        nums_71_80 = []


        for num in std_num_list:
                if num > 40 :
                        if num > 60 : 
                                if num > 70 :                
                                        nums_71_80.append(num)                
                                else:
                                        nums_61_70.append(num)     
                        else:
                                if num > 50 :
                                        nums_51_60.append(num)
                                else:
                                        nums_41_50.append(num)
                else:    
                        if num > 20 :
                                if num > 30:   
                                        nums_31_40.append(num)  
                                else:
                                        nums_21_30.append(num)
                        else:
                                if num > 10 :
                                        nums_11_20.append(num)
                                else:
                                        nums_5_10.append(num)
        if printt == 1:
                #asteric ka mazak
                print(' o	Group 1: Marks from 5 to 10\n',len(nums_5_10)*"*")
                # print(nums_5_10)
                print(' o	Group 2: Marks from 11 to 20\n',len(nums_11_20)*"*")
                # print(nums_11_20)
                print(' o	Group 3: Marks from 21 to 30\n',len(nums_21_30)*"*")
                # print(nums_21_30)
                print(' o	Group 4: Marks from 31 to 40\n',len(nums_31_40)*"*")
                # print(nums_31_40)
                print(' o	Group 5: Marks from 41 to 50\n',len(nums_41_50)*"*")
                # print(nums_41_50)
                print(' o	Group 6: Marks from 51 to 60\n',len(nums_51_60)*"*")
                # print(nums_51_60)
                print(' o	Group 7: Marks from 61 to 70\n',len(nums_61_70)*"*")
                # print(nums_61_70)
                print(' o	Group 8: Marks from 71 to 80\n',len(nums_71_80)*"*")
                # print(nums_71_80)
        else:
                
                print( len( nums_5_10) * "*")
                print( len( nums_11_20) * "*")
                print( len( nums_21_30) * "*")
                print( len( nums_31_40) * "*")
                print( len( nums_41_50) * "*")
                print( len( nums_51_60) * "*")
                print( len( nums_61_70) * "*")
                print( len( nums_71_80) * "*")

##########################################################
##########################################################
##########################################################
elif method == 2 :
        Mark5_10=0
        Mark11_20=0
        Mark21_30=0
        Mark31_40=0
        Mark41_50=0
        Mark51_60=0
        Mark61_70=0
        Mark71_80=0
        for _ in range( num_of_std ):
        
                std_num_mids = random.randint( 5 , 30 )
                std_num_finals = random.randint(5 , 50 )
                
                std_total = std_num_finals + std_num_mids
                
                
                if std_total > 40 :
                        if std_total > 60 : 
                                if std_total > 70 :                
                                        Mark71_80 += 1
                                else:
                                        Mark61_70  += 1  
                        else:
                                if std_total > 50 :
                                        Mark51_60 += 1
                                else:
                                        Mark41_50 += 1
                else:    
                        if std_total > 20 :
                                if std_total > 30:   
                                        Mark31_40 += 1
                                else:
                                        Mark21_30 += 1
                        else:
                                if std_total > 10 :
                                        Mark11_20 += 1
                                else:
                                        Mark5_10 += 1
        if printt == 1:
                print(' o	Group 1: Marks from 5 to 10\n',(Mark5_10)*"*")
                print(' o	Group 2: Marks from 11 to 20\n',(Mark11_20)*"*")
                print(' o	Group 3: Marks from 21 to 30\n',(Mark21_30)*"*")
                print(' o	Group 4: Marks from 31 to 40\n',(Mark31_40)*"*")
                print(' o	Group 5: Marks from 41 to 50\n',(Mark41_50)*"*")
                print(' o	Group 6: Marks from 51 to 60\n',(Mark51_60)*"*")
                print(' o	Group 7: Marks from 61 to 70\n',(Mark61_70)*"*")
                print(' o	Group 8: Marks from 71 to 80\n',(Mark71_80)*"*")
        else:
                print((Mark5_10)*"*")
                print((Mark11_20)*"*")
                print((Mark21_30)*"*")
                print((Mark31_40)*"*")
                print((Mark41_50)*"*")
                print((Mark51_60)*"*")
                print((Mark61_70)*"*")
                print((Mark71_80)*"*")
##########################################################
##########################################################
##########################################################
elif method == 3 :
        my_dict = {
                'G8':0,
                'G7':0,
                'G6':0,
                'G5':0,
                'G4':0,
                'G3':0,
                'G2':0,
                'G1':0
                  }
        for _ in range( num_of_std ):
        
                std_num_mids = random.randint( 5 , 30 )
                std_num_finals = random.randint(5 , 50 )
                
                std_total = std_num_finals + std_num_mids
                
                
                if std_total > 40 :
                        if std_total > 60 : 
                                if std_total > 70 :                
                                        my_dict['G8'] += 1
                                else:
                                        my_dict['G7'] += 1  
                        else:
                                if std_total > 50 :
                                        my_dict['G6'] += 1
                                else:
                                        my_dict['G5'] += 1
                else:    
                        if std_total > 20 :
                                if std_total > 30:   
                                        my_dict['G4'] += 1
                                else:
                                        my_dict['G3'] += 1
                        else:
                                if std_total > 10 :
                                        my_dict['G2'] += 1
                                else:
                                        my_dict['G1'] += 1
        
        if printt == 1:                          
                print(' o	Group 1: Marks from 5 to 10\n',my_dict['G1']*"*")
                print(' o	Group 2: Marks from 11 to 20\n',my_dict['G2']*"*")
                print(' o	Group 3: Marks from 21 to 30\n',my_dict['G3']*"*")
                print(' o	Group 4: Marks from 31 to 40\n',my_dict['G4']*"*")
                print(' o	Group 5: Marks from 41 to 50\n',my_dict['G5']*"*")
                print(' o	Group 6: Marks from 51 to 60\n',my_dict['G6']*"*")
                print(' o	Group 7: Marks from 61 to 70\n',my_dict['G7']*"*")
                print(' o	Group 8: Marks from 71 to 80\n',my_dict['G8']*"*")
        else:        
                print(my_dict['G1']*"*")
                print(my_dict['G2']*"*")
                print(my_dict['G3']*"*")
                print(my_dict['G4']*"*")
                print(my_dict['G5']*"*")
                print(my_dict['G6']*"*")
                print(my_dict['G7']*"*")
                print(my_dict['G8']*"*")
        # print(my_dict)