/* 

UNIVERSIDAD DE LOS ANDES
GRUPO 27 - HEC

María Alejandra Pérez Valencia - 201823266
Santiago Ramírez Gerstner - 201914023
Jose Luis Tavera Ruiz - 201821999
 
 */

// Instalamos los Paquetes Necesarios */

ssc install reghdfe
ssc install ftools
ssc install byhist
net install scheme-modern, from("https://raw.githubusercontent.com/mdroste/stata-scheme-modern/master/")

// Limpiamos todo y definimos nuestro espacio de Trabajo

clear all
cd "/Users/josetavera/Documents/HEC_Datos/input/Corte"
import delimited "/Users/josetavera/Documents/HEC_Datos/input/Corte/cortetransversal.csv"

// Sorteamos por municipios y eliminamos entradas dobles que quedaron como consecuencia de pivotear los paneles

sort codmpio
duplicates list codmpio

// Dropeamos aquellas observaciones con 0 en la alfabetizacio

drop if alf_a1938 == 0 | alf_a1951 == 0 | alf_a1964 == 0 | alf_a1973 == 0

// Generamos Histogramos y Estadísticas Descriptivas de la Base Prepivoteo

label variable tvalor "Valor de Prestamos"
label variable tnumero "Número de Prestamos"

histogram  tvalor , by(depto) color(navy)  ytitle(Frecuencia) 

// Pivoteamos la base en long para tener un panel con los años 1938, 1951, 1964 y 1973

reshape long alf_a, i(codmpio) j(anio)

// Generamos una dummy posterior al periodo analizado

gen dummypost = 0
replace dummypost = 1 if anio == 1964 | anio == 1973

// Y una dummy del tratamiento multiplicado por la dummy posterior

gen vartrat = tratamiento*dummypost
gen tendencia = 1

replace tendencia = 2 if anio == 1951
replace tendencia = 3 if anio == 1964
replace tendencia = 4 if anio == 1973

// Generamos la variable categórica de departamento para usar como control

encode depto, generate(departamento)

// Hacemos la regresión por Efectos Fijos

asdoc reghdfe alf_a vartrat i.departamento#tendencia, a(codmpio anio) save(regresionprincipal.doc)

preserve

// Creamos la gráfica del Supuesto de Tendencias Paralelas

collapse alf_a, by(anio tratamiento)
xtset tratamiento anio

label define tratamientol 1 "Tratamiento" 0 "Control"
label values tratamiento tratamientol

xtline alf_a, i(tratamiento) t(anio) overlay xtitle(Año) ytitle(Alfabetización) tlabel(1938 1951 1964 1973) tline(1957) title(Supuesto de tendencias paralelas) 

restore

// Estadísticas descriptivas

label define tratamientol 1 "Tratamiento" 0 "Control"
label values tratamiento tratamientol
graph bar alf_a, over(tratamiento) title("Tasa de alfabetización promedio en" "grupos de tratamiento y control") ytitle("Tasa de alfabetización") 

//Para que los labels de la siguiente queden bien, toca hacer un clear all y volver a correr el código

label define tratamientol 1 "Caja Agraria abrió" 0 "Caja Agraria no abrió"
label values tratamiento tratamientol
graph bar, over(tratamiento) title("Proporción de municipios en los que abrió la caja agraria") ytitle("Proporción de la muestra (en %)") 

// Largo Plazo

clear all

cd "/Users/josetavera/Documents/HEC_Datos/input/Corte"

import excel "/Users/josetavera/Documents/HEC_Datos/output/Final/2018/alf2018.xlsx" , sheet("Merge1") firstrow

drop Column1

reg alf_A2018 tratamiento TValor distancia_mercado disbogota discapital altura gandina gcaribe gpacifica gamazonia, r

outreg2 using "largoplazo.doc"













