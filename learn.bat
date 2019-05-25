@echo off

:: set variables below

::number var with /A
set /A myVar=5

::string var
set myVar2= hello

:: this is an empty string
set a=
::check if string is empty
if [%a%]==[] (echo Is empty)

echo %date%
echo %time%



::concat / interpolation
SET x=Hello 
SET y=World 
SET /A z=50 
SET q=%x% and %y% %z%
echo %q%



::remove string is from below string
set str=Batch scripts is easy. It is really easy. 
echo %str% 
::remove all is
set str=%str:is=% 
echo %str%
::remove spaces
set str=%str:=% 
echo %str%
::replace string easy with hard
set str=%str:easy=hard% 
echo %str%


::Arrays
set a[0]=1
echo %a[0]%

::or
set list = 1 2 3 4 

(for %%a in (%list%) do ( 
   echo %%a 
))

::iterate
set topic[0] = comments 
set topic[1] = variables 
set topic[2] = Arrays 
set topic[3] = Decision making 
set topic[4] = Time and date 
set topic[5] = Operators 

for /l %%n in (0,1,5) do ( 
   echo !topic[%%n]! 
)


set Arr[0] = 1 
set Arr[1] = 2 
set Arr[2] = 3 
set Arr[3] = 4 
set "x = 0" 
:SymLoop 

if defined Arr[%x%] ( 
   call echo %%Arr[%x%]%% 
   set /a "x+=1"
   GOTO :SymLoop 
)
echo "The length of the array is" %x%




::obj
set obj[0].Name = Joe 
set obj[0].ID = 1 
set obj[1].Name = Mark 
set obj[1].ID = 2 


::if statements
if %a%==5 goto :label1
if %a%==10 goto :labe2

:label1
echo "The value of a is 5"
EXIT /B 0 

:label2
echo "The value of a is 10"
EXIT /B 0



::functions
:myfunction
echo this is the function running
EXIT /B 0

call :myfunction

::function with parameters
CALL :Display 5 , 10
EXIT /B %ERRORLEVEL%

:Display
echo The value of parameter 1 is %~1
echo The value of parameter 2 is %~2
EXIT /B 0




if %a%==15 (echo "The value of variable a is 15") else (echo "Unknown value") 
if 2 EQU 2  (echo "The value of variable a is 15") else (echo "Unknown value") 
if 2 LSS 3 will give true (echo "The value of variable a is 15") else (echo "Unknown value") 
if 2 LEQ 3 will give true (echo "The value of variable a is 15") else (echo "Unknown value") 
if 2 GTR 3 will give true (echo "The value of variable a is 15") else (echo "Unknown value") 
if 2 GEQ 3 will give true (echo "The value of variable a is 15") else (echo "Unknown value") 

if defined str3 (echo "Variable str3 is defined") else (echo "Variable str3 is not defined")
if exist C:\test3.txt (echo "File exists") else (echo "File does not exist")








rem make text file and input data into it
echo.>"C:\lists.txt"
echo.>"C:\lists2.txt"

@echo Writing this text to lists.txt> lists.txt

rem discard output by posting to nul
dir "C:\Program Files" > nul

rem write running tasks to list2.txt
tasklist > C:\lists2.txt 

echo Done
pause