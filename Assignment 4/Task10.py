for i in range(2):
    str1 = input("Enter any string: ")
    
    for i in str1:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            print("Accepted!")
            break;
        else:
            print("Not Accepted!")
            break;