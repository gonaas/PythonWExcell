'''''
    #xlsx libreria
    archivo = xlsxwriter.Workbook("zinkeetabla.xlsx")
    hoja = archivo.add_worksheet()
    
    for n in range(0, len(VectorNombre)):
        hoja.write(0,n,VectorNombre[n])
    
    for row in range(1, len(registros)):
        for col in range(0,len(VectorNombre)):
            hoja.write(row,col,MCampos[row][col])
            
    archivo.close()
'''