# Una fecha es (Int, Int, Int) donde:
# el primer Int representa el día
# el segundo Int representa el mes
# el tercer Int representa el año
# (27, 9, 2021)
# (25, 5, 1810)

def bisiesto(anio : int) -> bool :
	return anio%400 == 0 or (anio%100 != 0 and anio%4 == 0) 

def totalDias(mes: int , anio: int) -> int :
	if mes == 2:
		return 29 if bisiesto(anio) else 28
	elif mes in [4,6,9,11]:
		return 30
	else:
		return 31

def diaSiguienteE(fecha: tuple) -> tuple:
	dia, mes, anio = fecha
	
	dia += 1
	if dia > totalDias(mes,anio):
		dia = 1
		if mes == 12:
			mes = 1
			anio += 1
		else:
			mes += 1
			
	return (dia,mes,anio)

def fechaEtoT(fechaE : tuple) -> tuple :
	meses = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
	
	dia, mes, anio = fechaE
	
	return (dia, meses[mes-1], anio)
	
def fechaTtoE(fechaT: tuple) -> tuple :
	meses = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
	
	dia, mes, anio = fechaT
	
	return (dia, meses.index(mes)+1, anio)
				
def diaSiguienteT(fecha: tuple) -> tuple:
	return fechaEtoT(diaSiguienteE(fechaTtoE(fecha)))

def test_bisiesto():
	assert bisiesto(2020) # (== True)
	assert bisiesto(2000)
	assert not bisiesto(1900)
	assert not bisiesto(2019)

def test_totalDias():
	assert (totalDias(2,2019) == 28)
	assert (totalDias(2,2020) == 29)
	assert (totalDias(3,2019) == 31)
	assert (totalDias(9,2020) == 30) 

def test_diaSiguienteE():
	assert (diaSiguienteE((28,2,2020)) == (29,2,2020))
	assert (diaSiguienteE((28,2,2019)) == (1,3,2019))
	assert (diaSiguienteE((31,12,2021)) == (1,1,2022))
	assert (diaSiguienteE((7,9,2022)) == (8,9,2022))	

def test_fechaEtoT():
	assert (fechaEtoT((1,7,2021)) == (1,"Jul",2021))
	assert (fechaEtoT((3,1,2022)) == (3,"Ene",2022))
	assert (fechaEtoT((30,12,2020)) == (30,"Dic",2020))

def test_fechaTtoE():
	assert (fechaTtoE((7,"Sep",2022)) == (7,9,2022))
	assert (fechaTtoE((25,"Ene",2021)) == (25,1,2021))
	assert (fechaTtoE((30,"Dic",2021)) == (30,12,2021))

def test_diaSiguienteT():
	assert (diaSiguienteT((28,"Feb",2020)) == (29,"Feb",2020))
	assert (diaSiguienteT((28,"Feb",2019)) == (1,"Mar",2019))
	assert (diaSiguienteT((31,"Dic",2021)) == (1,"Ene",2022))
	assert (diaSiguienteT((7,"Sep",2022)) == (8,"Sep",2022))

def avanzar_dias (fecha: tuple, n: int) -> None:
	for i in range(n):
		dia,mes,anio = fecha
		print(f"{dia}/{mes}/{anio}")
		fecha = diaSiguienteE(fecha)

