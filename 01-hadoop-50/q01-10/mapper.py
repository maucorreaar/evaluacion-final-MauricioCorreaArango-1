import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":

    ##
    ## itera sobre cada linea de codigo recibida
    ## a traves del flujo de entrada
    ##
    cadena =''
    for line in sys.stdin:

        ##
        ## genera las tuplas palabra \tabulador 1
        ## ya que es un conteo de palabras
        ##

        pos = 0
        for word in list(line.split(',')):
            pos +=1
            ##
            ## escribe al flujo estandar de salida
            ##

            if (pos == 3):
                cadena ="{}\t1\n".format(word)
                pos = 0
                break
        sys.stdout.write(cadena)
