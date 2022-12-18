# Fontuscator
A way to use fonts to obfuscate text. See the demo below for an example. 

## Demo
https://doctoreww.github.io/Fontuscator/

## Blog Posts

About this Program
https://medium.com/@doctoreww/7a6cd978c7a5?source=friends_link&sk=685eff2b6a94b22f3f6e39fb6dba787e

Orignal Idea
https://medium.com/@doctoreww/beating-plagiarism-checkers-for-science-step-by-step-1e477795e261?sk=f75b782679b205aaa16d72311c4296dc

## Usage

Not super robust atm. Will make a command line utility soon.
If you still want to try it...
Edit the letters array to add or remove valid chars. 
To generate a font, call the makeFont function and pass in an existing font (ie. Times New Roman) 
To make the CSS file call makeCSS and pass in the filename
To print the SPAN HTML tags, call the makeHTMLSPAN function passing in the values to write and the values to see as a user. 

## Issues
The sizes of the letters is not copied correctly. Need to do more research into fontforge about how to fix the letter sizing. 