#f = open('some_file.txt', 'r')
#file_data = f.read()
#f.close()
# Another syntax to open the file - the file obkect f is available only inside the "with" scope
#with open('some_file.txt', 'r') as f:
#    file_data = f.read()
#f.read(size in integer) - gives that many charcters
#f.readline() - reads each line at a time

#print(file_data)

#f = open('some_file.txt', 'w')
#f.write("Hello there!")
#f.close()

def create_cast_list(filename):
    cast_list = []
    with open(filename, 'r') as f:
        for line in f:
            line_in_file = line.strip()
            index = line_in_file.index(',')
            #name = line.split(",")[0]
            cast_list.append(line_in_file[:index])

    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    return cast_list

cast_list = create_cast_list('some_file.txt')
for actor in cast_list:
    print(actor)