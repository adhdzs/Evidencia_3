# =====================
# =   importaciones   =
# =====================
import os
import sys
import pandas as pd
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r'ui.ui', self)
        self.fnUI()


    def fnUI(self):
        self.btnRegistrar.clicked.connect(self.fnRegistrar)
        self.btnLimpiar.clicked.connect(self.fnLimpiar)
        self.btnGuardar.clicked.connect(self.fnGuardar)
        self.btnCargar.clicked.connect(self.fnCargar)
        self.btnConsulta.clicked.connect(self.fnBuscar)
        self.btnEliminar.clicked.connect(self.fnEliminar)
    

    # ===================
    # =   fnRegistrar   =
    # ===================
    def fnRegistrar(self):
        reg = self.tbwRegistros.rowCount()
        self.tbwRegistros.insertRow(reg)

        dato = QTableWidgetItem(self.txtMatricula.text())
        self.tbwRegistros.setItem(reg, 0, dato)

        dato = QTableWidgetItem(self.txtNombre.text())
        self.tbwRegistros.setItem(reg, 1, dato)
        
        dato = QTableWidgetItem(self.txtPaterno.text())
        self.tbwRegistros.setItem(reg, 2, dato)
        
        dato = QTableWidgetItem(self.txtMaterno.text())
        self.tbwRegistros.setItem(reg, 3, dato)
        
        dato = QTableWidgetItem(self.fechaNacimiento())
        self.tbwRegistros.setItem(reg, 4, dato)
       
        dato = QTableWidgetItem(self.sexo())
        self.tbwRegistros.setItem(reg, 5, dato)
       
        dato = QTableWidgetItem(str(self.spbEdad.value()))
        self.tbwRegistros.setItem(reg, 6, dato)


        dato = QTableWidgetItem(self.txtDireccion.text())
        self.tbwRegistros.setItem(reg, 7, dato)
        
        dato = QTableWidgetItem(self.txtMunicipio.text())
        self.tbwRegistros.setItem(reg, 8, dato)
        
        dato = QTableWidgetItem(self.cmbEstado.currentText())
        self.tbwRegistros.setItem(reg, 9, dato)
        
        dato = QTableWidgetItem(self.txtTelefono.text())
        self.tbwRegistros.setItem(reg, 10, dato)
        
        dato = QTableWidgetItem(self.txtEmail.text())
        self.tbwRegistros.setItem(reg, 11, dato)
        

        dato = QTableWidgetItem(self.cmbCarrera.currentText())
        self.tbwRegistros.setItem(reg, 12, dato)
        
        dato = QTableWidgetItem(self.beca())
        self.tbwRegistros.setItem(reg, 13, dato)
        
        dato = QTableWidgetItem(self.materias())
        self.tbwRegistros.setItem(reg, 14, dato)
        
        dato = QTableWidgetItem(self.tipoAlumno())
        self.tbwRegistros.setItem(reg, 15, dato)
        
        dato = QTableWidgetItem(str(self.spbSemestre.value()))
        self.tbwRegistros.setItem(reg, 16, dato)
        
        dato = QTableWidgetItem(self.idioma())
        self.tbwRegistros.setItem(reg, 17, dato)

        self.txtPrint.clear()
        self.txtPrint.append(self.nRegistro())
    


    # =================
    # =   fnLimpiar   =
    # =================
    def fnLimpiar(self):
        self.txtMatricula.clear()
        self.txtNombre.clear()
        self.txtPaterno.clear()
        self.txtMaterno.clear()
        self.dateNacimiento.setDate(QDate(2000,1,1))        
        self.rdbMasculino.setChecked(True)
        self.spbEdad.setValue(18)

        self.txtDireccion.clear()
        self.txtMunicipio.clear()
        self.cmbEstado.setCurrentIndex(-1)
        self.txtTelefono.clear()
        self.txtEmail.clear()

        self.cmbCarrera.setCurrentIndex(-1)
        self.rdbNA.setChecked(True)
        self.ckbContabilidad.setChecked(False)
        self.ckbEstadistica.setChecked(False)
        self.ckbProgramacion.setChecked(False)
        self.ckbBD.setChecked(False)
        self.ckbOperaciones.setChecked(False)
        self.rdbLocal.setChecked(True)
        self.spbSemestre.setValue(1)
        self.rdbAC.setChecked(True)
        self.txtPrint.clear()



    # =================
    # =   fnGuargar   =
    # =================
    def fnGuardar(self):
        # --> Validamos que existan registros en la tabla
        if self.tbwRegistros.rowCount() > 0:
            item = []
            # --> Recorremos cada una de las filas de la tabla
            for col in range(self.tbwRegistros.columnCount()):
                columna = []
                for fila in range(self.tbwRegistros.rowCount()):
                    columna.append(self.tbwRegistros.item(fila, col).text())

                # --> Generamos una lista con todos los datos encontrados en la tabla    
                item.append(columna)

            # --> Asignamos cada lista a una variable
            matricula    = item[0]
            nombre       = item[1]
            paterno      = item[2]
            materno      = item[3]
            f_nacimiento = item[4]
            sexo         = item[5]
            edad         = item[6]
            direccion    = item[7]
            municipio    = item[8]
            estado       = item[9]
            telefono     = item[10]
            email        = item[11]
            carrera      = item[12]
            beca         = item[13]
            materias     = item[14]
            t_alumno     = item[15]
            semestre     = item[16]
            idioma       = item[17]

            # --> Generamos un diccionario con la información contenida en listas
            data = {
                'matricula'    : matricula,
                'nombre'       : nombre,
                'paterno'      : paterno,
                'materno'      : materno,
                'f_nacimiento' : f_nacimiento,
                'sexo'         : sexo,
                'edad'         : edad,
                'direccion'    : direccion,
                'municipio'    : municipio,
                'estado'       : estado,
                'telefono'     : telefono,
                'email'        : email,
                'carrera'      : carrera,
                'beca'         : beca,
                'materias'     : materias,
                't_alumno'     : t_alumno,
                'semestre'     : semestre,
                'idioma'       : idioma
            }

            # --> Creamos un dataframe y agregamos los nombres de las columnas
            df = pd.DataFrame(data, columns = ['matricula', 'nombre', 'paterno', 'materno', 'f_nacimiento', 'sexo', 'edad', 'direccion', 'municipio', 'estado', 'telefono', 'email', 'carrera', 'beca', 'materias', 't_alumno', 'semestre', 'idioma'])

            # --> Validamos si existe algún archivo de datos
            if os.path.exists('data.csv'):
                # ** Generamos una base con la iformación existente
                df_b = pd.read_csv('data.csv', sep = '|', na_values = ['?'])

                # ** Validamos si los datos en la tabla ya existen en el archivo
                if df.size >= df_b.size:
                    df.to_csv('data.csv', index = None, sep = '|')
                else:
                    # ** Si la información que está en la tabla no existe en el archivo se agrega
                    df.to_csv('data.csv', index = None, sep = '|', header = None, mode = 'a')
                
            else:
                # ** En caso de no existir el archivo se crea uno nuevo
                df.to_csv('data.csv', index = None, sep = '|')

            self.txtPrint.clear()
            self.txtPrint.append('Información guardada correctamente')
        else:
            self.txtPrint.clear()
            self.txtPrint.append('No hay datos en tabla')

    # ================
    # =   fnCargar   =
    # ================
    def fnCargar(self):
        rows = self.tbwRegistros.rowCount()

        # --> Limpiamos la tabla de registros
        if rows != 0:
            for i in range(rows):
                self.tbwRegistros.removeRow(0)

        # --> Validamos que exista el archivo de datos
        if os.path.exists('data.csv'):
            df = pd.read_csv('data.csv', sep = '|', na_values = ['?'])
            
            # --> Extraemos lod datos y los asignamos a la tabla
            for data in range(len(df)):
                registro = self.tbwRegistros.rowCount()
                self.tbwRegistros.insertRow(registro)

                self.tbwRegistros.setItem(registro, 0, QTableWidgetItem(str(df['matricula'][data])))
                self.tbwRegistros.setItem(registro, 1, QTableWidgetItem(df['nombre'][data]))
                self.tbwRegistros.setItem(registro, 2, QTableWidgetItem(df['paterno'][data]))
                self.tbwRegistros.setItem(registro, 3, QTableWidgetItem(df['materno'][data]))
                self.tbwRegistros.setItem(registro, 4, QTableWidgetItem(df['f_nacimiento'][data]))
                self.tbwRegistros.setItem(registro, 5, QTableWidgetItem(df['sexo'][data]))
                self.tbwRegistros.setItem(registro, 6, QTableWidgetItem(str(df['edad'][data])))
                self.tbwRegistros.setItem(registro, 7, QTableWidgetItem(df['direccion'][data]))
                self.tbwRegistros.setItem(registro, 8, QTableWidgetItem(df['municipio'][data]))
                self.tbwRegistros.setItem(registro, 9, QTableWidgetItem(df['estado'][data]))
                self.tbwRegistros.setItem(registro, 10, QTableWidgetItem(str(df['telefono'][data])))
                self.tbwRegistros.setItem(registro, 11, QTableWidgetItem(df['email'][data]))
                self.tbwRegistros.setItem(registro, 12, QTableWidgetItem(df['carrera'][data]))
                self.tbwRegistros.setItem(registro, 13, QTableWidgetItem(df['beca'][data]))
                self.tbwRegistros.setItem(registro, 14, QTableWidgetItem(df['materias'][data]))
                self.tbwRegistros.setItem(registro, 15, QTableWidgetItem(df['t_alumno'][data]))
                self.tbwRegistros.setItem(registro, 16, QTableWidgetItem(str(df['semestre'][data])))
                self.tbwRegistros.setItem(registro, 17, QTableWidgetItem(df['idioma'][data]))
        else:
            # --> Se notifica que no hay data disponible
            self.txtPrint.clear()
            self.txtPrint.append('No hay datos disponibles')


    # ================
    # =   fnBuscar   =
    # ================
    def fnBuscar(self):
        # --> Validamos que exista la data
        if os.path.exists('data.csv'):
            df = pd.read_csv('data.csv', sep = '|', na_values = ['?'])

            # --> Obtenemos la matrícula del alumno que interesa obtener
            busqueda = self.txtMatricula.text()
            filtro = df.loc[:, 'matricula'] == int(busqueda)
            data = df.loc[filtro]
            
            if data.size > 0:
                # ** Preparamos informacion del alumno
                info = f'''
                --- RESULTADO DE BUSQUEDA ---
                Matrícula: {data.iloc[0]['matricula']}
                Nombre: {data.iloc[0]['paterno']}{data.iloc[0]['materno']}{data.iloc[0]['nombre']}
                Sexo: {data.iloc[0]['sexo']}     Fecha Nacimiento: {data.iloc[0]['f_nacimiento']} | {data.iloc[0]['edad']} años

                Dirección:
                {data.iloc[0]['direccion']}, {data.iloc[0]['municipio']}, {data.iloc[0]['estado']}
                Teléfono: {data.iloc[0]['telefono']}      E-mail: {data.iloc[0]['email']}

                Carrera: {data.iloc[0]['carrera']}
                Semestre actual: {data.iloc[0]['semestre']}
                Beca: {data.iloc[0]['beca']}
                Áreas favorita: {data.iloc[0]['materias']}
                Tipo de alumno: {data.iloc[0]['t_alumno']}
                Idioma inglés: {data.iloc[0]['idioma']}
                '''
            else:
                # ** Notificamos que no existe el alumno
                info = '\n\t--- Alumno no encontrado ---'

            # --> Mostramos informacion en pantalla
            self.txtPrint.clear()
            self.txtPrint.append(info)
        else:
            # --> Notificamos que no hay data
            msj = '\n\t--- No hay datos cargados ---'
            self.txtPrint.clear()
            self.txtPrint.append(msj)



    # ==================
    # =   fnEliminar   =
    # ==================
    def fnEliminar(self):
        # --> Validamos existencia de data
        if os.path.exists('data.csv'):
            data = pd.read_csv('data.csv', sep = '|', na_values = ['?'], index_col = 'matricula')

            # ** Obtenemos la fila y la matrícula del alumno seleccioando
            matricula = self.tbwRegistros.currentRow()
            alumno = self.tbwRegistros.item(matricula, 0).text()

            # ** Eliminamos la fila de la tabla y eliminamos el registro de la data
            self.tbwRegistros.removeRow(matricula)
            n_data = data.drop(int(alumno))
            print(n_data)
            
            n_data.to_csv('data.csv', index = 'matricula', sep = '|')
        else:
            self.txtPrint.clear()
            self.txtPrint.append('No hay data disponible')
        

    # =================
    # =   Funciones   =
    # =================
    # ===> Fecha de Nacimiento <===
    def fechaNacimiento(self):
        dia = self.dateNacimiento.date().day()
        mes = self.dateNacimiento.date().month()
        anio = self.dateNacimiento.date().year()
        fecha = f'{dia}/{mes}/{anio}'
        
        return fecha

    # ===> Radio Sexo <===
    def sexo(self):
        if self.rdbMasculino.isChecked():
            return self.rdbMasculino.text()
        elif self.rdbFemenino.isChecked():
            return self.rdbFemenino.text()
        else:
            return '---'
        
    # ===> Tipo de Beca <===
    def beca(self):
        if self.rdb100.isChecked():
            return self.rdb100.text()
        elif self.rdb80.isChecked():
            return self.rdb80.text()
        elif self.rdb50.isChecked():
            return self.rdb50.text()
        else:
            return '---'

    # ===> Materias seleccionadas <===
    def materias(self):
        seleccion = ''
        materias = [
            self.ckbContabilidad,
            self.ckbEstadistica,
            self.ckbProgramacion,
            self.ckbBD,
            self.ckbOperaciones
        ]
        
        for materia in materias:
            if materia.isChecked():
                seleccion += (materia.text() + ', ')
        
        return seleccion[0:-2]

    # ===> Alumno Local o Foráneo <===
    def tipoAlumno(self):
        if self.rdbLocal.isChecked():
            return self.rdbLocal.text()
        elif self.rdbForaneo.isChecked():
            return self.rdbForaneo.text()
        else:
            return 'No Especificado'

    # ===> Estado de idioma inglés <===
    def idioma(self):
        if self.rdbAC.isChecked():
            return self.rdbAC.text()
        else:
            return self.rdbNAC.text()
    


    # ====== Pantalla ======
    def nRegistro(self):

        info = f'''
        --- ALUMNO REGISTRADO ---
        Matrícula: {self.txtMatricula.text()}
        Nombre: {self.txtPaterno.text()} {self.txtMaterno.text()} {self.txtNombre.text()}
        Sexo: {self.sexo()}     Fecha Nacimiento: {self.fechaNacimiento()} | {self.spbEdad.value()} años

        Dirección:
        {self.txtDireccion.text()}, {self.txtMunicipio.text()}, {self.cmbEstado.currentText()}
        Teléfono: {self.txtTelefono.text()}      E-mail: {self.txtEmail.text()}

        Carrera: {self.cmbCarrera.currentText()}
        Semestre actual: {self.spbSemestre.value()}
        Beca: {self.beca()}
        Áreas favorita: {self.materias()}
        Tipo de alumno: {self.tipoAlumno()}
        Idioma inglés: {self.idioma()}
        '''
        return info




# ===> Inicio de aplicación <===
app = QApplication(sys.argv)
UIWindows = UI()
UIWindows.show()
sys.exit(app.exec_())
