#######################################################
#    Ph 20 Homework 4 makefile
#
#
#
#
######################################################
ALL = 1 2 3 4 5 6 7 8 9 10 
H3 = ph20_hw3_git.py
RUN = python $(H3)
TEX = pdflatex -shell-escape -interaction=nonstopmode -file-line-error




#latex_output.pdf : test.png
#something to make the latex file
#makes latex document


all: python_script
	$(TEX) test.tex 

python_script : $(H3)
	$(RUN) $(ALL)
#runs the program to make plots, makes all the plos 


#remove all images
.PHONY : clean
clean: 
	rm -f *.png *.pdf 
