
# fernando rodriguez lopez
#matricula: 236w0341
#grupo: 303A
#fecha: 2024-09-2024
import csv

datos = [
    ["236W0298", "Marlen", "Álvarez", "Cruz", "Ciudad 1", "Código Postal 1"],
    ["236W0301", "Adriana", "Arias", "Ronzon Cruz", "Ciudad 2", "Código Postal 2"],
    ["236W0312", "Hanna Itzel", "Castillo", "Galindo", "Ciudad 3", "Código Postal 3"],
    ["226W0909", "Humberto", "Cortes", "Cabrales", "Ciudad 4", "Código Postal 4"],
    ["236W0342", "Natasha Paulina", "Cruz", "Maldonado", "Ciudad 5", "Código Postal 5"],
    ["236W0341", "Osvaldo", "De La Cruz", "Paz", "Ciudad 6", "Código Postal 6"],
    ["236W0333", "Juan Francisco", "De Los Santos", "Perez", "Ciudad 7", "Código Postal 7"],
    ["236W0355", "Ingrid Itzel", "Estrada", "Valencia", "Ciudad 8", "Código Postal 8"],
    ["236W0315", "Brayan Iván", "Fuentes", "Arévalo", "Ciudad 9", "Código Postal 9"],
    ["236W0317", "Oscar Daniel", "Garza", "Guerra", "Ciudad 10", "Código Postal 10"],
    ["236W0334", "Fernando", "González", "Huerta", "Ciudad 11", "Código Postal 11"],
    ["236W0347", "Oscar Eduardo", "Gutiérrez", "Castillo", "Ciudad 12", "Código Postal 12"],
    ["236W0325", "Reyna Xóchitl", "Hernández", "Hernández", "Ciudad 13", "Código Postal 13"],
    ["236W0346", "Ángel Eduardo", "Hernández", "Vázquez", "Ciudad 14", "Código Postal 14"],
    ["226W1024", "Matías Aldair", "Herrera", "Mata", "Ciudad 15", "Código Postal 15"],
    ["236W0348", "Braulio Alberto", "Lozano", "Salazar", "Ciudad 16", "Código Postal 16"],
    ["236W1025", "Juan Pablo", "Morales", "Santiago", "Ciudad 17", "Código Postal 17"],
    ["236W0340", "Karla Yaretzi", "Murillo", "Mata", "Ciudad 18", "Código Postal 18"],
    ["236W0363", "Ángel David", "Onofre", "Cervantes", "Ciudad 19", "Código Postal 19"],
    ["236W0295", "Everth de Jesús", "Pazos", "Velásquez", "Ciudad 20", "Código Postal 20"],
    ["236W1034", "Alan Daniel", "Porfirio", "Hernández", "Ciudad 21", "Código Postal 21"],
    ["236W0344", "José Florencio", "Quintero", "Debernardi", "Ciudad 22", "Código Postal 22"],
    ["236W0411", "Marco Antonio", "Ramos", "Ramírez", "Ciudad 23", "Código Postal 23"],
    ["236W0341", "Fernando", "Rodríguez", "López", "Ciudad 24", "Código Postal 24"],
    ["236W0412", "Ángel Axel", "Rodríguez", "Pérez", "Ciudad 25", "Código Postal 25"],
    ["236W0399", "Alan Ariel", "Rojas", "Torales", "Ciudad 26", "Código Postal 26"],
    ["236W0336", "Karla Paris", "Sandoval", "Sibaja", "Ciudad 27", "Código Postal 27"],
    ["236W0334", "David Raúl", "Tobón", "Martínez", "Ciudad 28", "Código Postal 28"],
    ["236W0905", "Samantha", "Trujillo", "Tenchipe", "Ciudad 29", "Código Postal 29"],
    ["236W0332", "Edgar", "Valente", "Juárez", "Ciudad 30", "Código Postal 30"],
    ["226W0664", "Edwin Jassiel", "Vázquez", "Domínguez", "Ciudad 31", "Código Postal 31"]
]
with open("datos.csv",mode="w")as archivo_csv:

    escritor_csv = csv.writer (archivo_csv)
    escritor_csv.writerow(datos)
# Imprimir los datos

