# Mochi Mochi Web

Versión web de **Mochi Mochi** hecha con HTML, CSS y JavaScript puro.

## Origen del proyecto

Este proyecto nace tomando como base la app anterior de **Banderillas Mont's**. La idea original era tener una aplicación para presentar o administrar productos de un negocio de comida. En esta versión lo reorganicé como una página web más moderna, visual y fácil de compartir.

Ahora el proyecto funciona como menú digital, carrito de pedidos por WhatsApp y panel sencillo para registrar ventas.

## Productos incluidos

- Banderillas coreanas
- Sushis
- Pay de limón
- Mochis
- Waffles
- Plátanos árabes
- Hot cakes
- Sodas italianas
- Molle pizzas
- Orden de papas fritas

Se ignoraron los apartados de insumos desechables y cake pops.

## Funciones

- Menú dinámico por categorías.
- Búsqueda de productos.
- Sabores y variantes por producto.
- Ingredientes separados por producto.
- Carrito con cantidades y total estimado.
- Pedido listo para enviar por WhatsApp.
- Panel de ventas con historial.
- Registro de ventas desde carrito o venta rápida.
- Exportación a Excel usando SheetJS.
- Exportación alternativa a CSV.
- Modo claro/oscuro.
- Diseño responsive para celular.

## Cómo editar rápido

1. Abre `app.js`.
2. Cambia `BUSINESS.whatsappNumber` por el número real en formato internacional, sin `+`.
3. Edita el arreglo `products` para cambiar productos, precios, sabores, variantes, ingredientes e imágenes.
4. Abre `index.html` en el navegador.

## Ventas y Excel

Las ventas se guardan en `localStorage`, o sea, en el navegador donde se usa la página. No es una base de datos en la nube todavía.

Para descargar las ventas:

1. Ve a la sección **Ventas**.
2. Presiona **Exportar Excel**.
3. Se descarga un archivo `.xlsx`.

Si por alguna razón no carga la librería de Excel, puedes usar **Exportar CSV**, que también se abre en Excel.

## GitHub Pages

Como los archivos principales están en la raíz del repo, puedes activar GitHub Pages desde:

`Settings > Pages > Deploy from branch > main > /root`

## Nota mía

Dejé el proyecto sin frameworks para que sea fácil de entender, editar y enseñar. Si después quiero algo más pro, se puede migrar a React/Vite con backend para inventario, ventas en la nube y usuarios.
