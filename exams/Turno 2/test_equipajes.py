import pytest
from solucion import Equipaje,EquipajeComun,EquipajeEspecial
def test_comun():
 x=EquipajeComun(1,"Ana","Cordoba",10,5000); assert isinstance(x,Equipaje); assert x.importe()==pytest.approx(5000)
def test_especial():
 x=EquipajeEspecial(2,"Juan","Mendoza",10,5000); assert isinstance(x,Equipaje); assert x.importe()==pytest.approx(20000)
