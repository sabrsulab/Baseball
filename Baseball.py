#***************************************************************
#
#  Developer:         <Brandon>
#
#  Program #:         <Program 11>
#
#  File Name:         <Program11.py>
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Course Synonym:    <90696>
#
#  Due Date:          <July 27, 2019>
#
#  Instructor:        Sajjad Mohsin 
#
#  Chapter:           <Chapter #5, 6, 7, 8, 9>
#
#  Description:
#     <An explanation of what the program is designed to do>
#
#***************************************************************



#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program; runs other functions
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def main():
    developerInfo()#
    returnfrom = createDicts()
    showResults(returnfrom[0], returnfrom[1])
    # End of the main function
    
#***************************************************************
#
#  Function:     createDicts
# 
#  Description:  Creates two dictionaries.
#
#  Parameters:   None
#
#  Returns:      year_dict, count_dict
#
#**************************************************************    
def createDicts():
    
    # Open the file for reading
    input_file = open('Program11.txt', 'r')
    
    # Local dictionary variables
    year_dict = {}
    year = 1903
    index = 0
    count_dict = {}
    lineRead = input_file.readlines()
    #print(lineRead)#list validated
    #print(len(lineRead))
    while index < len(lineRead):
        lineRead[index] = lineRead[index].rstrip('\n')
        dataTable = lineRead[index]
        if year == 1904 or year == 1994:
            year += 1
        else:
            year_dict[year] = dataTable
            count = count_dict.get(dataTable, 0)
            if count > 0:
                count_dict[dataTable] = count + 1
            else:
                count_dict[dataTable] = 1
            year += 1
            index += 1
                

    input_file.close()
    return year_dict, count_dict
#***************************************************************
#
#  Function:     showResults
# 
#  Description:  Requests user input and displays output as requested
#
#  Parameters:   year_dict, count_dict
#
#  Returns:      Nothing 
#
#**************************************************************    
def showResults(year_dict, count_dict):
    year = 1
    while year != 0:    
    # Receive user input
        year = int(input('Enter a year in the range 1903-2018 (or 0 to exit): '))
        # Print results
        if year == 0:
            print('Thanks for playing.')
        elif year == 1904 or year == 1994:
            print("The world series wasn't played in the year", year)
        elif year < 1903 or year > 2018:
            print('The data for the year', year, \
                  'is not included in our database.')
        else:
            winner = year_dict[year]
            wins = count_dict[winner]
            print('The team that won the world series in ', \
                  year, ' is the ', winner, '.', sep='')
            print('They have won the world series', wins, 'times.')
        
    # End of showResults

#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def developerInfo():
    print('Name:     <Brandon>')
    print('Course:   Programming Fundamentals I')
    print('Program:  Eleven')
    print()
    # End of the developerInfo function

# Call the main function.
main()
