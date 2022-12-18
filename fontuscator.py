import fontforge
import string
import shutil
import os

letters = string.ascii_lowercase + " " + string.ascii_uppercase #Get the letters we care about 

def makeFont(base_font, out_dir = 'fonts'):
    shutil.copyfile(base_font, "temp.ttf")
    f = fontforge.open(base_font)
    refrence = fontforge.open('temp.ttf') #Open a refrence font file (needs new name)
    for i in range(len(letters)):
        for letter in letters:
            refrence.selection.select(letters[(letters.index(letter) + i) % len(letters)])
            refrence.copy()
            f.selection.select(letter)
            f.paste()
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        f.generate(f'{out_dir}/{i}.woff')
    os.remove('temp.ttf') #remove temp file

def makeCSS(css_file_name):
    text_file = open((css_file_name), "w")
    for i in range(len(letters)):
        text_file.write("@font-face {font-family: \""+str(i)+"\";src: url(\"fonts/"+str(i)+".woff\") format('woff');}")
    text_file.close()

def makeHTMLSPAN(toWrite,toSee):
    toReturn = ""

    for i in range(min(len(toWrite),len(toSee))):
        if(letters.index(toWrite[i]) <= letters.index(toSee[i])):
            toReturn += "<span style=\"font-family: '"+ str(abs(letters.index(toWrite[i]) - letters.index(toSee[i]))) +"';\">"+ toWrite[i] +"</span>"
        else:
            toReturn += "<span style=\"font-family: '"+ str((letters.index(toSee[i]) - letters.index(toWrite[i]) + len(letters))) +"';\">"+ toWrite[i] +"</span>"
    return toReturn


makeFont('arial.ttf')
makeCSS("test.css")
print(makeHTMLSPAN("Thank you for liking this article it means alot", "would you like to buy some car insurance?"))