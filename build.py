import  os
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['translateNamed.py','ctmTranslate.py','-F','-w','--icon=icon.ico']
    # opts=['translateNamed.py','ctmTranslate.py','-D','--icon=icon.ico']              #   调试打包
    run(opts)  
