import re
import shutil



    
def phone_num(text):
    """
    Function filters phone numbers from text in xxx-yyy-zzzz format 
    Arguments : text 
    retuns : list of phone_numbers 
    """
    phone_pattern = r"[0-9-+x.()]{7,}"   
    phone_numbers = []

    numbers=re.findall(phone_pattern, text)

    for number in numbers:
        edited_number =number.replace(".","").replace("(","").replace(")","").replace("-","")
        if len(edited_number) == 10:
            edited_number =edited_number[:3] + "-" + edited_number[3:6] + "-" + edited_number[6:]
        phone_numbers.append(edited_number)
        
    phone_numbers = list(set(phone_numbers))
    phone_numbers.sort()
    return phone_numbers
    

def email(text):
    email_pattern = r"\w+@\S+"
    emails= re.findall(email_pattern, text)
    emails_ = list(set(emails))
    emails_.sort()
    return emails_

def write_file(text,path):
    result = ""
    for element in text:
        result += element + "\n"
    with open (path, 'w') as f :
        f.write(result)    

def main_fun():
    path ='./assets/potential-contacts.txt'
    with open(path,'r') as file:
        content = file.read()

    phone_numbers_list = phone_num(content)
    emails_list = email(content)
    write_file(phone_numbers_list , 'assets/phone_numbers.txt')
    write_file(emails_list , 'assets/emails.txt')

if __name__ == '__main__':
    main_fun()