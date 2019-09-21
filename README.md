# Implant-Optimization

From analyses-selfc.py file, change the filepath of assembled design in step format 

Start abaqus software with this python code

import subprocess
    subprocess.call(['C:\SIMULIA\Abaqus\Commands\\abq6131.bat cae noGUI=C:\Users\scadscad\Desktop\\filesfornewpc\implantanalyses\\analyses-selfc.py'], shell=True)
    
After abaqus analysis, use this python code to take results 


import subprocess
    subprocess.call(['C:\SIMULIA\Abaqus\Commands\\abq6131.bat cae noGUI=C:\Users\scadscad\Desktop\\filesfornewpc\implantanalyses\\createrpt4.py'], shell=True)


For the whole optimization process, unpack filesfornewpc.zip and change filepaths 
