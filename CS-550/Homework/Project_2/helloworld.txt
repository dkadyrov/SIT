*---------------------------------------------
* Program : Hello World
* Written by: Daniel Kadyrov
* Date: July 7th, 2019
* Description: CS550 Assignment 7, Hello World
*---------------------------------------------

START   ORG     $1000

        LEA     MESSAGE,A1 
        MOVE.B  #14,D0     
        TRAP    #15       

	MOVE.B	#9,D0
	TRAP	#15

MESSAGE DC.B    'HELLO WORLD',0


	END	START
