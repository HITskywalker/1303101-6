@echo  off
python.exe manage.py makemigrations smp
pause
python.exe manage.py migrate
pause