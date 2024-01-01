REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v "RESOLVE_SCRIPT_API" /d "C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting" 

REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v "RESOLVE_SCRIPT_LIB" /d "C:\Program Files\Blackmagic Design\DaVinci Resolve\fusionscript.dll" 

REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v "PYTHONPATH" /d "c:\Python310\;C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules\\" 

