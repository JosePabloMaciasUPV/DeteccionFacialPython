import cv2
import os
import imutils

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')


#Extrae de una imagen los rostros , para ello recibe como primer parametro el directorio de la imagen a procesar y como 
#segundo parametro el directorio donde se almacenarán los rostros
def extraerDeImagen(nombreImagen,directorioAGuardar):
    #Lee la imagen
    image = cv2.imread(nombreImagen)
    imageAux = image.copy()
    #Aplica el color a escala de grices
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #Encuntra los rostros en la imagen a escala de grises usando el clasificador
    faces = faceClassif.detectMultiScale(gray, 1.1, 5)
    #inicializa la variable que se encargara de contar los rostros.
    count = 0

    #Ciclo que ayudará a almacenar cada rostro
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y),(x+w,y+h),(128,0,255),2)
        rostro = imageAux[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(directorioAGuardar+'/rostro_{}.jpg'.format(count),rostro)
        count = count + 1
        #Si se desea mostrar en ventanas visuales los rostros encontrados
        #cv2.imshow('rostro',rostro)
        #cv2.imshow('image',image)
        #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    #Se muestran por consola la cantidad de rostros extraídos.
    print('Se generaron: '+str(count)+' rostros.')



#Se extrae los rostros de un video MP4 , AVI, etc. Y los almacena los rostros en formato jpg en una carpeta proporcionada.
#El primer parametro es el directorio del video y el segundo parámetro es el directorio donde se almacenarán las imagenes con los rostros
def extraerDeVideo(nombreArchivo,directorioAGuardar):
    #Comprueba la existencia de la carpeta , si no existe la crea
    if not os.path.exists(directorioAGuardar):
        print('Carpeta creada: '+directorioAGuardar)
        os.makedirs(directorioAGuardar)
    #Guarda el video en la memoria ram    
    cap = cv2.VideoCapture(nombreArchivo)
    #Crea una variable para almacenar los costos
    count = 0
    #Obtiene un entero con el número de los frames del video.
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    #Ciclo for con cada uno de los frames del video
    for i in range(0,frame_count):
        #lee el siguiente frame
        frameFinal,frame = cap.read()
        frame = cv2.flip(frame,1)
        #el frame lo convierte a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #copia el frame
        auxFrame = frame.copy()
        #El clasificador genera los rostros
        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        #espera a que se presione la tecla ESC para terminar 
        k = cv2.waitKey(1)
        if k == 27:
            break


        #Ciclo por cada rostro encontrado
        for (x,y,w,h) in faces:
            #Se dibuja un rectangulo en el rostro encontrado
            cv2.rectangle(frame, (x,y),(x+w,y+h),(128,0,255),2)
            #Se suma uno al contador de rostros
            count=count+1
            #guarda el rostro en una variable
            rostro = auxFrame[y:y+h,x:x+w]
            #cambia el tamaño del rostro a un tamaño
            rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
            #se guarda el archivo en el directorio para ser guardado en formato jpg
            cv2.imwrite(directorioAGuardar+'/rostro_{}.jpg'.format(count),rostro)
        #Muestra la imagen en la ventana    
        cv2.imshow('frame',frame)
    #libera el video de la memoria RAM    
    cap.release()
    #Cierra las ventanas
    cv2.destroyAllWindows()
    #Muestra por consola la cantidad de rostros encontrados
    print('Se generaron: '+str(count)+' rostros.')


#Extrae los rostros de una carpeta que contiene multiples imagenes
#Para hacerlo necesita de dos parametros, el primero el directorio que contiene las imagenes 
# y el segundo el lugar donde se almacenarán las imagenes
def extraerDeDirectorio(directorioALeer,directorioAGuardar):
    #guarda las rutas de los archivos encontrados en el directorio que contiene las imagenes
    imagesPathList = os.listdir(directorioALeer)
    #Comprueba si el directorio donde se guardarán los rostros existe y si no lo crea
    if not os.path.exists(directorioAGuardar):
        print('Carpeta creada: '+directorioAGuardar)
        os.makedirs(directorioAGuardar)
    #Crea variable para contar los rostros    
    count = 0

    #Ciclo for por cada imagen en el directorio de las imagenes a procesar
    for imageName in imagesPathList:
        #lee la imagen
        image = cv2.imread(directorioALeer+'/'+imageName)
        #Hace una copia
        imageAux = image.copy()
        #Convierte la imagen a escala de grises
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #Detecta los rostros en la imagen y las almacena
        faces = faceClassif.detectMultiScale(gray, 1.1, 5)
        #Por cada rostro entonces
        for (x,y,w,h) in faces:
            #Se establece la ubicación de el rostro usando las coordenadas detectadas
            rostro = imageAux[y:y+h,x:x+w]
            #Se ajusta el tamaño de la imagen del rostro encontrado
            rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
            #Si se desea mostrar en ventanas los rostros encontrados
            #cv2.imshow('rostro',rostro)
            #cv2.waitKey(0)
            #Se guarda la imagen en el disco duro en el directorio establecido en el parametro
            cv2.imwrite(directorioAGuardar+'/rostro_{}.jpg'.format(count),rostro)
            #Se añade uno al contador de rostros
            count = count +1
    #Se muestra por consola los rostros encontrados         
    print('Se generaron: '+str(count)+' rostros.')    



     

#extraerDeImagen('/home/coder/Public/ACTIVIDAD ESPECIAL/Imagenes y Videos de pruba/IMG-20201204-WA0013.jpg','output')
extraerDeVideo('/home/coder/Public/ACTIVIDAD ESPECIAL/video_1.mp4','output')
#extraerDeDirectorio('/home/coder/Public/ACTIVIDAD ESPECIAL/Imagenes y Videos de pruba','output')