#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", "r") as data:
    guest_list = data.readlines()

with open("C:/Users/Admin/Documents/Python/code/day-24-Mail+Merge+Project/Mail Merge Project Start/Input/"
          "Letters/starting_letter.txt", "r") as data:
    message = data.read()

for name in guest_list:
    stripped_name = name.strip()
    personalised_message = message.replace("[name]", stripped_name)
    with open(f"./Output/ReadyToSend/letter_for{stripped_name}.txt", "w") as completed_letter:
        completed_letter.write(personalised_message)



