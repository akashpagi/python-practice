
import first as f
import second as se
#s=f.Myschool()
#s.show()
c=se.Mycollege()
c.disp()

print('--------------------------------------')

from first import Myclass,Myschool
from second import Mycollege 
#c1=Myclass()
#c1.name()
se1=Mycollege()
se1.disp()


print('--------------------------------------')

from first import Myschool as Ms , Myclass as Mc
from second import Mycollege as Myc
se2=Myc()
se2.disp()
c2=Mc()
c2.name()
