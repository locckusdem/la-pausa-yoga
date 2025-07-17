# 📸 Guía para Agregar Fotos y Logo a La Pausa

## Archivos de imagen necesarios:

### Logo Principal:
- **Archivo**: `static/logo.png`
- **Tamaño recomendado**: 200x200 píxeles (o proporcional)
- **Formato**: PNG con fondo transparente preferible
- **Descripción**: Logo de "La Pausa" que aparecerá en la navegación

### Fotos del Estudio:
- **Archivo 1**: `static/studio1.jpg`
- **Archivo 2**: `static/studio2.jpg`
- **Tamaño recomendado**: 600x400 píxeles
- **Formato**: JPG o PNG
- **Descripción**: Fotos del interior del estudio, clases, ambiente, etc.

## 🔧 Cómo agregar las imágenes:

### Opción 1: Copiar archivos directamente
```bash
# Copia tus archivos a la carpeta static/
cp /ruta/a/tu/logo.png /home/locckus/yoga_app/static/
cp /ruta/a/tu/foto1.jpg /home/locckus/yoga_app/static/studio1.jpg
cp /ruta/a/tu/foto2.jpg /home/locckus/yoga_app/static/studio2.jpg
```

### Opción 2: Usar la interfaz de VS Code
1. Abre la carpeta `static` en el explorador de archivos
2. Arrastra y suelta tus imágenes
3. Renombra los archivos según los nombres requeridos

## 📁 Estructura final esperada:
```
yoga_app/
├── static/
│   ├── logo.png          ← Tu logo
│   ├── studio1.jpg       ← Foto del estudio 1
│   ├── studio2.jpg       ← Foto del estudio 2
│   └── style.css
├── templates/
└── app.py
```

## 🎨 Especificaciones técnicas:

### Logo:
- **Tamaño**: Se ajustará automáticamente a 50px de altura
- **Posición**: Aparece junto al nombre "La Pausa" en la navegación
- **Formato recomendado**: PNG con transparencia

### Fotos del estudio:
- **Tamaño**: Se redimensionarán automáticamente
- **Posición**: Aparecen en la página principal junto a la descripción
- **Formato**: JPG o PNG

## ✨ Notas importantes:

1. **Si no tienes las imágenes aún**: La aplicación funcionará perfectamente sin ellas. Las imágenes simplemente no se mostrarán.

2. **Nombres exactos**: Los archivos deben tener exactamente estos nombres:
   - `logo.png`
   - `studio1.jpg`
   - `studio2.jpg`

3. **Optimización**: Para mejor rendimiento, optimiza las imágenes antes de subirlas (puedes usar herramientas online como TinyPNG).

4. **Formatos alternativos**: Si tus imágenes están en otros formatos, puedes cambiar las extensiones en los templates HTML.

## 🚀 Después de agregar las imágenes:

1. Reinicia la aplicación Flask
2. Actualiza el navegador (Ctrl+F5)
3. ¡Disfruta tu aplicación personalizada!

---

**¿Necesitas ayuda?** Pregunta si tienes dudas sobre cómo agregar las imágenes.
