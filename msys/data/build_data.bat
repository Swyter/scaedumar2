@echo off && title compiling scaedumar 2 data --
set PATH="C:\Python24","C:\Python25";"C:\Python26";"C:\Python27";%PATH%
set PYTHONPATH=%cd%\..;
:start
cls
python  -B -OO  flora_kinds.py
python  -B -OO  ground_specs.py
python  -B -OO  skyboxes.py
echo.
echo ______________________________
echo.
echo Script processing has ended.
echo Press any key to recompile. . .
pause>nul && goto :start