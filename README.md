# Mochi Mochi Web

Versión web ligera para **Mochi Mochi**, hecha con HTML, CSS y JavaScript puro.

## Funciones

- Menú dinámico por categorías.
- Carrito con cantidades y total estimado.
- Pedido listo para enviar por WhatsApp.
- Modo claro/oscuro.
- Diseño responsive para celular.
- Imágenes remotas bonitas para prototipo rápido.

## Cómo editar rápido

1. Abre `app.js`.
2. Cambia `BUSINESS.whatsappNumber` por el número real en formato internacional, sin `+`.
3. Edita el arreglo `menu` para cambiar productos, precios, categorías e imágenes.
4. Abre `index.html` en el navegador.

## Cómo subirlo a GitHub Pages

Puedes dejar esta carpeta en el repo y activar GitHub Pages desde:

`Settings > Pages > Deploy from branch > main > /mochi-mochi-web`

Si GitHub no permite elegir una subcarpeta normal, mueve estos archivos a la raíz del repo o usa una rama `gh-pages`.

## Nota mía

Dejé el proyecto sin frameworks para que sea más fácil de mantener, correr y enseñar. Si después quiero algo más pro, se puede migrar a React/Vite sin perder la idea del diseño.
