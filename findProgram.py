import winreg

program_to_found = 'Software\\GPL Ghostscript'

try:
    h_key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, program_to_found)
    try:
        gs_version = winreg.EnumKey(h_key, 0)
        h_subkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, program_to_found + '\\' + gs_version)
        gs_dll = (winreg.EnumValue(h_subkey, 0))[1]
        print("Ghostscript %s is installed in: %s" % (gs_version, gs_dll.replace('gsdll32.dll', '')))
    except OSError:
        print("Ghostscript insn't correctly installed!! ")
except PermissionError:
    print("Ghostsript not found!! ")