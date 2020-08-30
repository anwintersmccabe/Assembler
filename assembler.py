def assembler():
    
    '''Prompts user for a file containing assembly instructions,
    then translates those instructions into their equivalent machine
    code and puts translated instructions in a user-named out_file'''
    
    #retrieve file, read it, then put the instructions in the file into a list
    try:       
        file_name= input('Name of input file: ')
        in_file = open(file_name, 'r')   
        out_file = open(input('Name of output file: '),"w")
        out_file.write("v2.0 raw\n")   
        text = in_file.read()
        lines =text.split()
    
        #make all instructions lower case
        for instruction in range(len(lines)):
            lines[instruction] = lines[instruction].lower()
        
        #look for instructions, and write corresponding opcode hex values to
            #out_file
        for instruction in range(len(lines)):
            if lines[instruction] == 'input':
                out_file.write("4 ")
            elif lines[instruction] == 'output':
                out_file.write("7 ")
            elif lines[instruction] == 'jmp':
                out_file.write("a ")
                instruction+=1
                out_file.write(lines[instruction])
                out_file.write(" ")
            elif lines[instruction] == 'load':
                out_file.write("e ")
                instruction+=1
                out_file.write(lines[instruction])
                out_file.write(" ")
            elif lines[instruction] == 'inc':
                out_file.write("14 ")
            elif lines[instruction] == 'mov':
                out_file.write("17 ")
            elif lines[instruction] == 'add':
                out_file.write("1a ")
            elif lines[instruction] == 'halt':
                out_file.write("1d ")
            else:
                print("Syntax error", instruction)
    except FileNotFoundError:
        print("File not found, please rerun program using a valid filename")


def main():
    ''' Wrapper function, tester function '''
        
    assembler()

if __name__ == "__main__":
    main()