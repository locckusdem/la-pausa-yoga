# 🧘‍♀️ La Pausa - Sistema de Inscripciones de Yoga

Una aplicación web desarrollada en Flask para gestionar inscripciones a clases de yoga en **La Pausa**, ubicada en Cabrera 54, Banfield.

## 📍 Sobre La Pausa

**La Pausa** es tu espacio de tranquilidad y bienestar en el corazón de Banfield. Ofrecemos clases de yoga para todos los niveles en un ambiente cálido y acogedor.

**Dirección**: Cabrera 54, Banfield, Buenos Aires

## ✨ Características

### Funcionalidades Principales:
- **Inscripción de alumnos** con validación de datos
- **Información de ubicación** (Cabrera 54, Banfield)
- **Gestión de horarios** con diferentes tipos de clases
- **Panel de administración** para ver y gestionar inscripciones
- **Galería de fotos** del estudio (cuando se agreguen las imágenes)
- **Logo personalizado** de La Pausa
- **Validación de email** y verificación de duplicados
- **Control de cupos** (máximo 10 personas por clase)
- **Interfaz moderna y responsiva**

### Páginas disponibles:
- `/` - Página principal con formulario de inscripción
- `/horarios` - Horarios y tipos de clases disponibles
- `/admin` - Panel de administración
- `/success` - Página de confirmación de inscripción

## � Personalización con Imágenes

Para agregar el logo y fotos de La Pausa, consulta el archivo `IMAGENES.md` que contiene instrucciones detalladas sobre:
- Cómo agregar el logo de La Pausa
- Dónde colocar las fotos del estudio
- Especificaciones técnicas de las imágenes

## �🚀 Instalación y Ejecución

### Requisitos:
- Python 3.7+
- Flask

### Pasos para ejecutar:

1. **Clonar o descargar el proyecto**
   ```bash
   cd yoga_app
   ```

2. **Crear entorno virtual**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # venv\Scripts\activate   # En Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install flask
   # o usar: pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

5. **Abrir en el navegador**
   ```
   http://127.0.0.1:5000
   ```

## 📊 Base de Datos

La aplicación utiliza SQLite con la siguiente estructura:

```sql
CREATE TABLE inscripciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    dia TEXT NOT NULL,
    hora TEXT NOT NULL,
    fecha_inscripcion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🎨 Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Base de datos**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Estilos**: CSS personalizado con gradientes y efectos modernos

## 📱 Características del Diseño

- **Diseño responsivo** que se adapta a móviles y tablets
- **Gradientes modernos** y efectos visuales atractivos
- **Interfaz intuitiva** y fácil de usar
- **Validación en tiempo real** de formularios
- **Mensajes flash** para feedback del usuario

## 🔧 Funcionalidades Técnicas

### Validaciones:
- ✅ Formato de email válido
- ✅ Campos obligatorios
- ✅ Verificación de duplicados
- ✅ Control de cupos por clase

### Seguridad:
- ✅ Sanitización de datos de entrada
- ✅ Manejo de errores de base de datos
- ✅ Validación server-side

## 📋 Horarios Disponibles

### Lunes a Viernes:
- **07:00** - Yoga Matutino (Despertar energético)
- **09:00** - Yoga Suave (Para principiantes)
- **11:00** - Hatha Yoga (Posturas tradicionales)
- **17:00** - Yoga Dinámico (Flujo energético)
- **19:00** - Yoga Relajante (Reducción de estrés)

### Fines de Semana:
- **09:00** - Yoga Familiar (Para toda la familia)
- **11:00** - Yoga Restaurativo (Relajación profunda)
- **20:30** - Yoga Nocturno (Preparación para el descanso)

## 🛠️ Mejoras Futuras

- [ ] Autenticación de usuarios
- [ ] Sistema de pagos
- [ ] Reservas con fechas específicas
- [ ] Notificaciones por email
- [ ] API REST
- [ ] Exportación de datos a Excel/PDF
- [ ] Dashboard con estadísticas

## 📞 Soporte

Para soporte técnico o dudas sobre la aplicación, contacta al administrador del sistema.

---

**¡Namaste desde La Pausa! 🙏**  
*Tu espacio de tranquilidad en Banfield*
