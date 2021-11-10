import fileAnalysis
import WebAnalysis
import reader

url='https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj2qeKn24v0AhVPQhoKHQ4-B4YQFnoECAIQAQ&url=https://www.rojadirectatv.tv/&usg=AOvVaw2JeSqCMmyc6XqKWymY4fJ1'
VTapiKey='fc06e14f7e9409d28771c645456c958477fb78eda4d89034bc1bde729827f2af'
mailApiKey='AIzaSyAc2vZQS7QedPd0zfqRbd7MvSkT3FYgJ4o'


#Comprobar que hay correos recibidos no leidos
mailUnRead=reader.checkEmailUnRead()

#Comprobar que hay correos recibidos
mailStored=reader.checkEmailStored()

#Analisis direccion sender
senderCheck=True

#Analisis web
if url !='':
    resultadoWeb=WebAnalysis.runWeb(VTapiKey,url)
    if resultadoWeb == True:
        print("Pagina segura")
    else:
        output=resultadoWeb.split('&&')
        print(output)

#Analisis Archivo

