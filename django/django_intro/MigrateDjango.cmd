@echo off
@REM set these to your locations
set virt_loc=C:\Users\dennst\git-repo\python_stack\my_environments
set django_loc=C:\Users\dennst\git-repo\python_stack\django\django_intro

if '%1' == '' echo Project name can't be blank!&& goto :HELP
if '%2' == '' echo App name can't be blank!&& goto :HELP

if '%django_loc%' == '' echo Need to set django_loc!&& goto :eof
if not exist %django_loc% echo "%django_loc%" django_loc is not a valid location!&& goto :eof

if '%virt_loc%' == '' echo Need to set virt_loc for my_environments!&& goto :eof
if not exist %virt_loc% echo "%virt_loc%" django_loc is not a valid location!&& goto :eof
cd /d %virt_loc%
call djangoPy3Env\Scripts\activate
cd /d %django_loc%

rem C:\Program Files (x86)\GnuWin32


:HELP
    echo Need to supply the proj name and app name.
    