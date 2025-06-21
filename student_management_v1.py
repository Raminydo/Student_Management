

"""
Student Management system v1

A simple terminal-based student management system

including actions:
    - add student
    - show all saved students
    - remove student (based on any option)
    - edit student (based on any option)
    - search student (based on any option)
    - exit

note:
    This project is just a simple version of a later final project.

Attention:
    After exiting the programm, all saved data will be lost.

"""



from os import system

student_list = []

while True:

    print("\n-----------------------------------")
    print('1. Add student')
    print('2. Show student')
    print('3. Remove student')
    print('4. Edit student')
    print('5. Search student')
    print('6. Exit')
    print("-----------------------------------\n")

    menu = input('Menu: ')
    system('cls')

    match menu:
        
        case '1':
            
            while True:
                system('cls')


                #region get firstname
                system('cls')

                while True:
                    firstname = input('Enter the firstname: ')
                    system('cls')

                    if firstname != '':
                        break

                    print('ERROR!')
                #endregion
                    

                #region get lastname
                system('cls')

                while True:
                    lastname = input('Enter the lastname: ')
                    system('cls')

                    if lastname != '':
                        break

                    print('ERROR!')
                #endregion
                    

                #region get age
                system('cls')

                while True:
                    age = int(input('Enter the age: '))
                    system('cls')

                    if age in range(1, 121):
                        age = str(age)
                        break

                    print('ERROR!')
                #endregion
                    

                #region get gender
                system('cls')

                while True:
                    gender = input('Enter the gender (male/female): ')
                    system('cls')

                    if gender == 'male' or gender == 'female':
                        break

                    print('ERROR!')
                #endregion
                    

                #region get national code
                system('cls')

                while True:
                    national_code = input('Enter the national code: ')
                    system('cls')

                    if national_code == '':
                        print('ERROR!')

                    for student in student_list:
                        if student[4] == national_code:
                            print('This national code already exists.')
                            break
                    
                    else:
                        break    
                #endregion
                    

                #region get student code
                system('cls')

                while True:
                    student_code = input('Enter the student code: ')
                    system('cls')

                    if student_code == '':
                        print('ERROR!')

                    for student in student_list:
                        if student[5] == student_code:
                            print('This student code already exists.')
                            break
                    
                    else:
                        break
                #endregion


                student = [firstname, lastname, age, gender, national_code, student_code]
                student_list.append(student)
                
                flag = True

                #region add again
                while True:
                    add_again = input('Do you want to add another student (yes/no)? ')
                    system('cls')

                    if add_again == 'yes':
                        break

                    elif add_again == 'no':
                        flag = False
                        break

                    else:
                        print('ERROR!')
                #endregion

                if flag == False:
                    break


        case '2':

            while True:

                check_all = input('Do you want to see all columns (yes/no)? ')
                system('cls')

                if check_all == 'yes':
                    show_column = ['ID', 'firstname', 'lastname', 'age', 'gender', 'national code', 'student code']
                    show_index = [0, 1, 2, 3, 4, 5]
                    break

                elif check_all == 'no':

                    column = ['firstname', 'lastname', 'age', 'gender', 'national code', 'student code']
                    show_column = ['ID']
                    show_index = []

                    for index in range(len(column)):
                        
                        print('Do you want to see column "', column[index], '" (yes/-)? ')

                        if input() == 'yes':
                            show_column.append(column[index])
                            show_index.append(index)

                        system('cls')
                    
                    break

                else:
                    print('ERROR!')        
                
            #region show result
            print(*show_column, sep='\t')
            print("____________________________________________________________________________________________\n")

            id_ = 1

            for student in student_list:

                print(id_, end='\t')

                for index in show_index:
                    print(student[index], end='\t\t')
                
                print()
                id_ += 1
            
            print("____________________________________________________________________________________________\n")
            #endregion


        case '3':
            
            while True:

                #region show list
                print(*['ID', 'Firstname', 'Lastname', 'Age', 'Gender', 'National Code', 'Student Code'], sep='\t')
                print("____________________________________________________________________________________________\n")

                id_ = 1

                for student in student_list:
                    print(id_, *student, sep='\t')
                    id_ += 1
                
                print("____________________________________________________________________________________________\n")
                #endregion

                
                print('How do you want to find the student you want to delete?')
                print('1. Firstname  2. Lastname  3. Age  4. Gender  5. National Code  6. Student Code  7. Exit')
                
                remove_column = input('\nWith column: ')
                system('cls')

                match remove_column:
                    case '1':
                        val = input('Firstname: ')
                        remove_index = 0

                    case '2':
                        val = input('Lastname: ')
                        remove_index = 1

                    case '3':
                        val = input('Age: ')
                        remove_index = 2

                    case '4':
                        val = input('Gender: ')
                        remove_index = 3

                    case '5':
                        val = input('National Code: ')
                        remove_index = 4

                    case '6':
                        val = input('Student Code: ')
                        remove_index = 5

                    case '7':
                        break

                    case _:
                        print('ERROR!')


                system('cls')
                check_exists = False

                for student in student_list:
                    if student[remove_index] == val:
                        check_exists = True

                        print(*student, sep='\t')

                        if input('\nDo you want to remove this student from the list (yes/-)? ') == 'yes':
                            system('cls')
                            student_list.remove(student)
                            print('Done.')

                        else:
                            system('cls')


                if not check_exists:
                    print('This student does not exist.')

                
                flag = True

                #region remove again
                while True:
                    remove_again = input('Do you want to remove another student (yes/no)? ')
                    system('cls')

                    if remove_again == 'yes':
                        break

                    elif remove_again == 'no':
                        flag = False
                        break

                    else:
                        print('ERROR!')
                #endregion
                        
                if flag == False:
                    break
                    
 
        case '4':
            while True:

                print('How do you want to find the student you want to edit?')
                print('1. Firstname  2. Lastname  3. Age  4. Gender  5. National Code  6. Student Code  7. Exit')
                
                edit_column = input('\nWith column: ')
                system('cls')

                match edit_column:
                    case '1':
                        val = input('Firstname: ')
                        edit_index = 0

                    case '2':
                        val = input('Lastname: ')
                        edit_index = 1

                    case '3':
                        val = input('Age: ')
                        edit_index = 2

                    case '4':
                        val = input('Gender: ')
                        edit_index = 3

                    case '5':
                        val = input('National Code: ')
                        edit_index = 4

                    case '6':
                        val = input('Student Code: ')
                        edit_index = 5

                    case '7':
                        break

                    case _:
                        print('ERROR!')

                system('cls')
                check_exists = False

                for student in student_list:
                    if student[edit_index] == val:

                        check_exists = True
                        system('cls')

                        print(*student, sep='\t')

                        if input('\nDo you want to edit this student (yes/-)? ') == 'yes':
                            system('cls')

                            print('What do you want to edit?')
                            print('1. Firstname  2. Lastname  3. Age  4. Gender  5. National Code  6. Student Code  7. Exit')

                            edit = input('\ncolumn: ')
                            system('cls')

                            match edit:
                                case '1':
                                    #region get new firstname
                                    system('cls')

                                    while True:
                                        new_firstname = input('Enter the new firstname: ')
                                        system('cls')

                                        if new_firstname != '':
                                            break

                                        print('ERROR!')
                                    #endregion
                                        
                                    student[0] = new_firstname
                                    print('Done.')
                                

                                case '2':
                                    #region get new lastname
                                    system('cls')

                                    while True:
                                        new_lastname = input('Enter the new lastname: ')
                                        system('cls')

                                        if new_lastname != '':
                                            break

                                        print('ERROR!')
                                    #endregion
                                        
                                    student[1] = new_lastname
                                    print('Done.')


                                case '3':
                                    #region get new age
                                    system('cls')

                                    while True:
                                        new_age = int(input('Enter the new age: '))
                                        system('cls')

                                        if new_age in range(1, 121):
                                            new_age = str(new_age)
                                            break

                                        print('ERROR!')
                                    #endregion

                                    student[2] = new_age  
                                    print('Done.')
                                      

                                case '4':
                                    #region get new gender
                                    system('cls')

                                    while True:
                                        new_gender = input('Enter the new gender (male/female): ')
                                        system('cls')

                                        if new_gender == 'male' or new_gender == 'female':
                                            break

                                        print('ERROR!')
                                    #endregion
                                        
                                    student[3] = new_gender
                                    print('Done.')


                                case '5':
                                    #region get new national code
                                    system('cls')

                                    while True:
                                        new_national_code = input('Enter the new national code: ')
                                        system('cls')

                                        if new_national_code == '':
                                            print('ERROR!')

                                        for student in student_list:
                                            if student[4] == new_national_code:
                                                print('This national code already exists.')
                                                break
                                        
                                        else:
                                            break    
                                    #endregion
                                        
                                    student[4] = new_national_code
                                    print('Done.')


                                case '6':
                                    #region get new student code
                                    system('cls')

                                    while True:
                                        new_student_code = input('Enter the new student code: ')
                                        system('cls')

                                        if new_student_code == '':
                                            print('ERROR!')

                                        for student in student_list:
                                            if student[5] == new_student_code:
                                                print('This student code already exists.')
                                                break
                                        
                                        else:
                                            break
                                    #endregion
                                        
                                    student[5] = new_student_code
                                    print('Done.')


                                case '7':
                                    break


                                case _:
                                    print('ERROR!')


                system('cls')
                if not check_exists:
                    print('This student does not exist.')

                flag = True

                #region edit again
                while True:
                    edit_again = input('Do you want to edit another student (yes/no)? ')
                    system('cls')

                    if edit_again == 'yes':
                        break

                    elif edit_again == 'no':
                        flag = False
                        break

                    else:
                        print('ERROR!')
                #endregion
                        
                if flag == False:
                    break


        case '5':
            
            while True:
                
                print('How do you want to search?')
                print('1. Firstname  2. Lastname  3. Age  4. Gender  5. National Code  6. Student Code  7. Exit')
                
                search_column = input('\nWith column: ')
                system('cls')

                match search_column:
                    case '1':
                        val = input('Firstname: ')
                        search_index = 0

                    case '2':
                        val = input('Lastname: ')
                        search_index = 1

                    case '3':
                        val = input('Age: ')
                        search_index = 2

                    case '4':
                        val = input('Gender: ')
                        search_index = 3

                    case '5':
                        val = input('National Code: ')
                        search_index = 4

                    case '6':
                        val = input('Student Code: ')
                        search_index = 5

                    case '7':
                        break

                    case _:
                        print('ERROR!')
                        

                system('cls')
                check_exists = False
                
                #region show result
                id_ = 1
                
                print(*['ID', 'firstname', 'lastname', 'age', 'gender', 'national code', 'student code'], sep='\t')
                print("____________________________________________________________________________________________\n")
                
                for student in student_list:
                    if student[search_index] == val:
                        check_exists = True
                        
                        print(id_, *student, sep='\t')

                        id_ += 1

                print("____________________________________________________________________________________________\n")
                #endregion

                flag = True

                #region search again
                while True:
                    search_again = input('Do you want to search again (yes/no)? ')
                    system('cls')

                    if search_again == 'yes':
                        break

                    elif search_again == 'no':
                        flag = False
                        break

                    else:
                        print('ERROR!')
                #endregion
                        
                if flag == False:
                    break


        case '6':
            break


        case _:
            print('ERROR!')

