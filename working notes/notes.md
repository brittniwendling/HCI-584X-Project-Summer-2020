STEPS TO START VERSION 1: 
1. Figure out the "holder of your data" 
    You can start with a simple nested something (as I sketched out above) but should eventually migrate to some sort of class
2. Code functions/methods to "fill the data" 
    Write some simple set/get functions for each part of your master data structure, e.g. set_qset_name() and get_qset_name() 
3. After that is done you should be able to write a simple script to simulate filling the data with what will eventually come from the GUI
    To fake the input, just hardcode if for now:
    D = <empty master data structure>
    qset_name = "biology"  # could be input() or come from GUI
    		set_qset_name(qset_name, D)
4. Next  re-write this to use a class with methods instead of your functions so you'll have a questions set data class (which could contain a list of qsets) with a lot of get/set methods
5. Figure out how to save and load the data (attributes) of your class into a file
6. Start with making a TkInter GUI version of one of your 2 apps (which either creates or consumes the file)
    Don't get fancy, just do something simple even if it's ugly and silly to work with (like my multiple choice input hack)
7.Do the other GUI app

Done with version 1
