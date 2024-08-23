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

 Tabla = "tbc_estudios"
 
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


### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu_usuario/tu_proyecto.git

# Navegar al directorio del proyecto
cd tu_proyecto

# Instalar dependencias
npm install


