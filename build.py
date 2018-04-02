import  os  
if __name__ == '__main__':  
    from PyInstaller.__main__ import run  
    opts=['ctmTranslate.py','ctmui.py','-F','-w','--icon=icon.ico']  
    run(opts)  