# 🩻 Proyecto de Radiología e Imagen


## 📚 Descripción del Proyecto

Este proyecto está dedicado a la creación de una **plataforma avanzada** para la gestión y visualización de estudios de radiología e imagen médica. Nuestra misión es mejorar la precisión y eficiencia en el diagnóstico médico, proporcionando herramientas intuitivas y potentes para profesionales de la salud y pacientes.


## 🎯 Objetivos del Proyecto

### Objetivo General
Desarrollar una **plataforma integral** que optimice la gestión y visualización de imágenes médicas, potenciando la precisión diagnóstica.

### Objetivos Específicos
- **Automatizar** el almacenamiento y recuperación de estudios de imagen médica.
- **Facilitar** la colaboración entre profesionales de la salud mediante herramientas de anotación.
- **Optimizar** la visualización de imágenes con herramientas avanzadas.
- **Mejorar** la accesibilidad a los estudios para los pacientes desde cualquier lugar.

---

## 👥 Colaboradores

- **📄 Alexis Gomez Gaona** - *Documentador*
- **💻 Armando Carrasco Vargas** - *Front End*
- **🖥️ Juan Manuel Cruz Ortiz** - *Back End*
- **📝 Janeth Ahuacatitla Amixtlan** - *Documentación*

---

## 🚀 Instalación y Uso

### Requisitos Previos
- Node.js (o la tecnología utilizada en tu proyecto)
- Git

---
### Estructuras de las Tablas

 Tabla "tbc_estudios"
 
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Tipo = Column(String(50), nullable=False)
    Nivel_Urgencia = Column(String(50), nullable=False)
    #Solicitud_ID = Column(Integer, ForeignKey("tbd_solicitudes.ID"), nullable=False)
    #Consumibles_ID = Column(Integer, ForeignKey("tbc_consumibles.id"), nullable=True)
    Estatus = Column(String(50), nullable=False)
    Total_Costo = Column(DECIMAL(10, 2), nullable=False)
    Dirigido_A = Column(String(100), nullable=True)
    Observaciones = Column(Text, nullable=True)
    Fecha_Registro = Column(DateTime, nullable=False)
    Fecha_Actualizacion = Column(DateTime, nullable=True)
    
  Tabla "tbd_resultados_estudios"
  
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Paciente_ID = Column(Integer, ForeignKey("tbb_pacientes.Persona_ID"), nullable=False)
    Personal_Medico_ID = Column(Integer, ForeignKey("tbb_personal_medico.Persona_ID"), nullable=False)
    Estudio_ID = Column(Integer, ForeignKey("tbc_estudios.ID"), nullable=False)
    Folio = Column(String(50), nullable=False, unique=True)
    Resultados = Column(Text, nullable=False)
    Observaciones = Column(Text, nullable=False)
    Estatus = Column(Enum(
        'Pendiente',
        'En Proceso',
        'Completado',
        'Aprobado',
        'Rechazado'
    ), nullable=True)
    Fecha_Registro = Column(DateTime, nullable=False, default=func.now())
    Fecha_Actualizacion = Column(DateTime, nullable=True, onupdate=func.now())

---
### API endpoints
   ESTUDIOS

--> Este endpoint devuelve una lista de estudios, Llama a la función get_estudios en la capa CRUD para obtener la lista de estudios desde la base de datos y la devuelve.
      
      @estudios.get("/estudios/", response_model=List[schemas.estudios.Estudios], tags=["Estudios"], dependencies=[Depends(Portador())])
      def read_estudios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
          db_estudios = crud.estudios.get_estudios(db=db, skip=skip, limit=limit)
          return db_estudios


--> Este endpoint devuelve los detalles de un estudio específico según su ID, llama a la función get_estudio en la capa CRUD. Si el estudio no existe, lanza una excepción 404 Not Found.
      
       @estudios.get("/estudio/{id}", response_model=schemas.estudios.Estudios, tags=["Estudios"], dependencies=[Depends(Portador())])
       def read_estudio(id: int, db: Session = Depends(get_db)):
           db_estudio = crud.estudios.get_estudio(db=db, id=id)
           if db_estudio is None:
               raise HTTPException(status_code=404, detail="Estudio no encontrado")
    return db_estudio


--> Este endpoint crea un nuevo estudio en la base de datos, llama a la función create_estudio en la capa CRUD y guarda el nuevo estudio en la base de datos.
       
       @estudios.post("/estudio/", response_model=schemas.estudios.Estudios, tags=["Estudios"])
       def create_estudio(estudio: schemas.estudios.EstudiosCreate, db: Session = Depends(get_db)):
           # Asumiendo que no hay un método para verificar duplicados de 'Estudio'
           return crud.estudios.create_estudio(db=db, estudio=estudio)


--> Este endpoint actualiza los datos de un estudio existente, llama a la función update_estudio en la capa CRUD. Si el estudio no existe, lanza una excepción 404 Not Found.
     
     @estudios.put("/estudio/{id}", response_model=schemas.estudios.Estudios, tags=["Estudios"], dependencies=[Depends(Portador())])
     def update_estudio(id: int, estudio: schemas.estudios.EstudiosUpdate, db: Session = Depends(get_db)):
         db_estudio = crud.estudios.update_estudio(db=db, id=id, estudio=estudio)
         if db_estudio is None:
             raise HTTPException(status_code=404, detail="Estudio no existe, no actualizado")
         return db_estudio


--> Este endpoint elimina un estudio específico de la base de datos.
       
       @estudios.delete("/estudio/{id}", response_model=schemas.estudios.Estudios, tags=["Estudios"], dependencies=[Depends(Portador())])
       def delete_estudio(id: int, db: Session = Depends(get_db)):
           db_estudio = crud.estudios.delete_estudio(db=db, id=id)
           if db_estudio is None:
               raise HTTPException(status_code=404, detail="Estudio no existe, no se pudo eliminar")
           return db_estudio



### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu_usuario/tu_proyecto.git

# Navegar al directorio del proyecto
cd tu_proyecto

# Instalar dependencias
npm install


