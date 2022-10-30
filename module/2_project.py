
import first as f
s=f.Myschool()
s.show()
c=f.Myclass()
c.name()

print('--------------------------------------')

from first import Myclass,Myschool 
c_1=Myclass()
c_1.name()
s_1=Myschool()
s_1.show()


print('--------------------------------------')

from first import Myschool as Ms , Myclass as Mc
s_2=Ms()
s_2.show()
c_2=Mc()
c_2.name()
