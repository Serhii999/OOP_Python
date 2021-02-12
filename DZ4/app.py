from models import *
import traceback
from datetime import *

def main():
    Ksusha = Recruiter('Kseniya', 'ksusha@gmail.com', 30)

    Serhii = Programmer('Serhii', 'serhii@gmail.com', 40)
    Radislav = Programmer('Radislav', 'radislavchik@gmail.com', 45)
    Alexandr = Programmer('Alexandr', 'sanya@gmail.com', 45)
    Sasha = Programmer('Alexandr', 'sanya@gmail.com', 45)


    Dmitrii = Candidate('Dmitrii Vosruf', 'vosruf@gmail.com', '.Net, C#', 'Communication', 10)
    Ilya = Candidate('Khamza Ilya', 'khamza@gmail.com', 'FullStack', 'JS+html', 6)
    Artem = Candidate('Artem Pogorelov', 'pogorelov@gmail.com', 'FrontEnd', 'html+css', 7)

    NetJunior = Vacancy('.Net Junior', 'JS, C#, .Net', 6)
    Verstka = Vacancy('HTML+css Junior', 'html, css, js', 8)
    Dmitrii.work()
    Ilya.work()
    Artem.work()




try:
    main()

except ValueError as emailerror:
        logs = open('logs.py', 'a')
        error = traceback.format_exc().splitlines()
        logs.write('{} ValueError, {}, \n'.format(datetime.today(), emailerror))
        logs.close()
except UnableToWorkException as workerror:
    logs = open('logs.py', 'a')
    error = traceback.format_exc().splitlines()
    logs.write('{} UnableToWorkException, {}, \n'.format(datetime.today(), workerror))
    logs.close()

print(main())






