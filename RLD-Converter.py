from nrgpy.convert_rld import local
import glob
import sys, os
import shutil

outputDir = "csv_output/"

# Uses NRGPy to convert the files to *.txt files
def convert(dirIn, dirOut):
    converter = local(rld_dir= dirIn, out_dir=dirOut)
    converter.convert()
    #The files it outputs aren't useable (in Excel for example), so we go through
    #all files in the new output directory 
    replace(dirOut)

#HORRIBLE
def replace(dirOut):
    # List of all files in the directory, that end on *.txt
    files = glob.glob(dirOut + '*.txt')
    # We make a directory for the cleaned files
    os.mkdir(dirOut + outputDir)
    
    for file in files:
        # The next part won't be necessary for SQ, it's just that Excel only
        # recognises ',' as a decimal separator
        read_file = open(file, 'r')
        data = read_file.read()
        read_file.close()
        data = data.replace('.', ',')
        write_file = open(file, 'w')
        write_file.write(data)
        write_file.close()

        #This part gets rid of the header (containing info about all the sensors)
        #First we get the file name, so we can reuse it later on
        head, tail = os.path.split(file)
        #We create a new file in the directory we created earlier
        new_file = open(dirOut + outputDir + tail, 'wb')
        # We write to that file the last 146 lines(the actual data)
        new_file.write(removeLines(file))
        new_file.close()
        

def removeLines(file):
    total_lines_wanted = 146
    f = open(file, 'rb')
    BLOCK_SIZE = 1024
    f.seek(0, 2)
    block_end_byte = f.tell()
    lines_to_go = total_lines_wanted
    block_number = -1
    blocks = []
    while lines_to_go > 0 and block_end_byte > 0:
        if (block_end_byte - BLOCK_SIZE > 0):
            f.seek(block_number*BLOCK_SIZE, 2)
            blocks.append(f.read(BLOCK_SIZE))
        else:
            f.seek(0,0)
            blocks.append(f.read(block_end_byte))
        lines_found = blocks[-1].count(b'\n')
        lines_to_go -= lines_found
        block_end_byte -= BLOCK_SIZE
        block_number -= 1
    all_read_text = b''.join(reversed(blocks))
    # + 1 to get rid of the Leading Data tag that would interfere with importing in Excel
    return b'\n'.join(all_read_text.splitlines()[-total_lines_wanted+1:])
        
        
        

input_dir = input("Enter the directory of the NRG files: ")
#input_dir = r"C:\Users\jvi\Desktop\Wind Data\LU_Mellerdall_NRGLogger\Data Example"
convert(input_dir, input_dir + '/output/')
input = input("Enter to exit")
