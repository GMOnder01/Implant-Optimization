import os

def xlstoxlsx():

    import os

    if os.path.exists('C:\Users\scadscad\Desktop\\filesfornewpc\implantanalyses\Job-1.lck'):
        os.remove('C:\Users\scadscad\Desktop\\filesfornewpc\implantanalyses\Job-1.lck')

    if os.path.exists('C:\Users\scadscad\Desktop\\filesfornewpc\implant\Info\cortical.xlsx'):
        os.remove('C:\Users\scadscad\Desktop\\filesfornewpc\implant\Info\cortical.xlsx')

    if os.path.exists('C:\Users\scadscad\Desktop\\filesfornewpc\implant\Info\\trabecular.xlsx'):
        os.remove('C:\Users\scadscad\Desktop\\filesfornewpc\implant\Info\\trabecular.xlsx')

    if os.path.exists('C:\Users\scadscad\Desktop\\filesfornewpc\implant\Info\implant.xlsx'):
        os.remove('C:\Users\scadscad\Desktop\\filesfornewpc\implant\Info\implant.xlsx')

    import win32com.client as win32
    fname = "C:\Users\scadscad\Desktop\\filesfornewpc\implant\Info\cortical.xls"
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(fname)

    wb.SaveAs(fname+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
    wb.Close()                               #FileFormat = 56 is for .xls extension
    excel.Application.Quit()

    fname = "C:\Users\scadscad\Desktop\\filesfornewpc\implant\Info\\trabecular.xls"
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(fname)

    wb.SaveAs(fname+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
    wb.Close()                               #FileFormat = 56 is for .xls extension
    excel.Application.Quit()

    fname = "C:\Users\scadscad\Desktop\\filesfornewpc\implant\Info\implant.xls"
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(fname)

    wb.SaveAs(fname+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
    wb.Close()                               #FileFormat = 56 is for .xls extension
    excel.Application.Quit()

    #import shutil
    #shutil.copyfile("C:\Users\scadscad\Desktop\\filesfornewpc\implant\Info\cortical.xlsx", "D:\implant\Deneme\cortical.xlsx")

def optimization():

  import os
  os.startfile('C:/Users/scadscad/Desktop//filesfornewpc/implant/Optimize/Debug/Optimize.exe', )
  os.startfile('C:\Windows\system32\Taskmgr.exe', )

def solidworks():

    import  subprocess
    subprocess.call('C:\Users\scadscad\Desktop\macro.lnk', shell=True)

    os.remove('C:\Users\scadscad\Desktop\\filesfornewpc\implant\Info\cortical.xlsx')
    os.remove('C:\Users\scadscad\Desktop\\filesfornewpc\implant\Info\\trabecular.xlsx')
    os.remove('C:\Users\scadscad\Desktop\\filesfornewpc\implant\Info\implant.xlsx')

def lfmsg():

 import os
 while True:

    if os.path.exists('C:\Users\scadscad\Desktop\\filesfornewpc\implant\Deneme\msg3.txt'): # if msg.txt file exists, while loop breaks and python reads the subsequent line.
        os.remove('C:\Users\scadscad\Desktop\\filesfornewpc\implant\Deneme\msg3.txt') # removes the txt file
        break
    else:
        os.system("taskkill /f /t /im  SLDWORKS.exe")
        os.system("taskkill /f /t /im  EXCEL.exe")
        time.sleep(5)
        os.startfile('C:\Users\scadscad\Desktop\macro.lnk', )
        time.sleep(120)
        continue #if the msg.txt file does not exist, python waits until it recieves the msg.txt file    # call lmfg function which looks for the required finish msg file coming from the preceding analyses

def abaqus():

    import subprocess
    subprocess.call(['C:\SIMULIA\Abaqus\Commands\\abq6131.bat cae noGUI=C:\Users\scadscad\Desktop\\filesfornewpc\implantanalyses\\analyses-selfc.py'], shell=True)

def report():

    import subprocess
    subprocess.call(['C:\SIMULIA\Abaqus\Commands\\abq6131.bat cae noGUI=C:\Users\scadscad\Desktop\\filesfornewpc\implantanalyses\\createrpt4.py'], shell=True)

optimization()


while True:
    import os                                       ##
    import time
    import subprocess

    try:                                            ##
            os.environ.pop('PYTHONIOENCODING')      ## This codes inherits a problem while starting the Abaqus.
    except KeyError:                                ##
            pass                                    ##
    #import subprocess
    #lfmsg()            # Look for Message (lfmsg) function continuously looks for the msg.txt files in the predefined location.
    #subprocess.call(['C:\SIMULIA\Abaqus\Commands\\abq6131.bat cae noGUI=C:\Users\\acer\son.py'], shell=True) ## Call the abaqus command prompt and run the abaqus file
    #subprocess.call(['C:\SIMULIA\Abaqus\Commands\\abq6131.bat cae noGUI=C:\Users\\acer\createrpt2.py'], shell=True) ## Call the abaqus command prompt and run result retrieval file

    os.system("taskkill /f /t /im  EXCEL.exe")
    xlstoxlsx()
    #if os.path.exists('C:\Users\scadscad\Desktop\\filesfornewpc\implant\Deneme\msg3.txt'): # if msg.txt file exists, while loop breaks and python reads the subsequent line.
    #    os.remove('C:\Users\scadscad\Desktop\\filesfornewpc\implant\Deneme\msg3.txt') # removes the txt file
    time.sleep(5)
    os.startfile('C:\Users\scadscad\Desktop\macro.lnk', )  ## call solidworks macro shortcut (macro.lnk) with any path.
    time.sleep(120)
    lfmsg()
    abaqus()
    report()
    time.sleep(5)
    messageFile= open('C:\Users\scadscad\Desktop\\filesfornewpc\implant\Info\msg2.txt','w')
    messageFile.close()
