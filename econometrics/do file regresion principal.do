ssc install reghdfe
ssc install ftools

clear all

cd "C:\Users\santi\OneDrive - Universidad de los Andes\Documentos\Trabajos Economia Uniandes\2021-2 (sexto)\Historia económica de Colombia\Proyecto semestral\entrega final"

import delimited "C:\Users\santi\OneDrive - Universidad de los Andes\Documentos\Trabajos Economia Uniandes\2021-2 (sexto)\Historia económica de Colombia\Proyecto semestral\entrega final\cortetransversal.csv"

sort codmpio
duplicates list codmpio

drop if alf_a1938 == 0 | alf_a1951 == 0 | alf_a1964 == 0 | alf_a1973 == 0

reshape long alf_a, i(codmpio) j(anio)

gen dummypost = 0

replace dummypost = 1 if anio == 1964 | anio == 1973

gen vartrat = tratamiento*dummypost

gen tendencia = 1
replace tendencia = 2 if anio == 1951
replace tendencia = 3 if anio == 1964
replace tendencia = 4 if anio == 1973


encode depto, generate(departamento)


asdoc reghdfe alf_a vartrat i.departamento#tendencia, a(codmpio anio) save(regresionprincipal.doc)

preserve

collapse alf_a, by(anio tratamiento)
xtset tratamiento anio

label define tratamientol 1 "Tratamiento" 0 "Control"
label values tratamiento tratamientol

xtline alf_a, i(tratamiento) t(anio) overlay xtitle(Año) ytitle(Alfabetización) tlabel(1938 1951 1964 1973) tline(1957) title(Supuesto de tendencias paralelas) 

restore

*Estadísticas descriptivas













