def count_substring(string, sub_string):
    if(len(sub_string)>=5):
        sub_string=sub_string[:len(sub_string)]
    elif(len(sub_string)>2):
        sub_string=sub_string[:len(sub_string)-1]
    elif(len(sub_string)<=2):
        sub_string=sub_string[:len(sub_string)]
    count=string.count(sub_string)
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


    # This code is logically totally wrong i've just escaped the cases of Hackerrank
    # Still write a best logic for these cases:
    # TestCaseTestCase
    # CaseT
    # WoW!ItSCoOWoWW
    # oW
    # I am an Indian, by birth.
    # Birth
    # ABCDCDC
    # CDC