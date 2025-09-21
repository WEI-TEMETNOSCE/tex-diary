Please modify the system with the following design:
1) all the posts are in a posts folder. 
   
2) every time, when I call diary today <optionalname>, it creates a latex file Year-month-day<optionalname>.tex under the Year folder (create it if empty). It will also the tex file for me to start edit. 
 
3) Inside each daily diary tex file, the user will add tages in the beginning in the line containing <TAGs>, the Year is automatically a default tag, the user could add its own tag, such as rectified flow, sampling, etc. Note that the Year is treated as a default tag. 

4) when i call diary <tag1> <tag2> ..., it will find all the diary files that contain at least one of tag1 tag2 ....  and combine them into a combined latex and combined into a pdf under a folder whose name is the combination of the tags. use entity resolution, such as ignoring capital vs. small letters. The way it combine the files is similar to create_anthopy.sh. but in fact, we will rename  create_anthopy to something like compile_topics <tag>...

5) please tell me how to implement the tag system in general. i want to keep it minimum and simple, and do not want to introduce too much installations. do you think it should build a mapping between files and tags somewhere? the problem is the user can modify the tags any time though...

