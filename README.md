# Mochi Mochi Web

Versión web ligera para **Mochi Mochi**, hecha con HTML, CSS y JavaScript puro.

## Origen del proyecto

Este proyecto está basado en la idea y estructura de mi app anterior de **Banderillas Mont's**, que originalmente estaba pensada como una aplicación de escritorio para administrar o presentar productos de un negocio de comida.

Para esta nueva versión decidí reimaginarla como una página web más moderna, visual y fácil de compartir. La idea fue conservar la lógica principal del proyecto anterior, pero adaptarla a una experiencia más práctica para clientes: ver el menú, agregar productos al carrito y preparar el pedido para enviarlo por WhatsApp.

También dejé el código organizado para que pueda servir como base en futuros negocios o catálogos, no solamente para Mochi Mochi.

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

Como los archivos principales están en la raíz del repo, puedes activar GitHub Pages desde:

`Settings > Pages > Deploy from branch > main > /root`

Después GitHub te dará un link público para abrir la página desde el navegador.

## Nota mía

Dejé el proyecto sin frameworks para que sea más fácil de mantener, correr y enseñar. Si después quiero algo más pro, se puede migrar a React/Vite sin perder la idea del diseño.
