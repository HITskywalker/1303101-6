@echo  off
cd c:\mysite
python.exe manage.py makemigrations smp
pause
python.exe manage.py migrate
pause