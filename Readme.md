# Banderillas Mont's - Sistema de Inventario y Ventas

Sistema de escritorio desarrollado en Python para administrar inventario, recetas, ventas, costos y ganancias de un pequeño negocio de comida.

Este proyecto fue creado como una herramienta personalizada para **Banderillas Mont's**, con el objetivo de controlar ingredientes, insumos, desechables y productos vendidos de una forma más organizada.

## Características

- Interfaz gráfica de escritorio usando CustomTkinter.
- Inventario separado por categorías:
  - Ingredientes automáticos
  - Insumos automáticos
  - Desechables
  - Manuales / variables
- Registro de productos y precios de venta.
- Sistema de recetas editables.
- Descuento automático de ingredientes, insumos y desechables al registrar una venta.
- Control especial para banderillas:
  - Salchicha
  - Queso
  - Combinada
- Control de domos, vasitos de aderezo y tapas.
- Cálculo estimado de:
  - Precio de venta
  - Costo del producto
  - Ganancia estimada
- Historial de ventas.
- Dashboard con resumen de ingresos, costos y ganancias.
- Almacenamiento local usando archivos JSON.
- Búsqueda en diferentes secciones del sistema.

## Tecnologías utilizadas

- Python
- CustomTkinter
- JSON
- Tkinter
- PyInstaller

## Objetivo del proyecto

El objetivo principal fue crear un sistema sencillo pero funcional para un negocio real, permitiendo registrar ventas y controlar automáticamente el inventario.

También fue desarrollado como proyecto de práctica para mejorar habilidades en:

- Programación en Python
- Interfaces gráficas
- Manejo de archivos JSON
- Lógica de negocio
- Organización de datos
- Automatización de procesos

## Estructura de datos

El sistema guarda la información localmente dentro de la carpeta `data/`.

Ejemplo:

```text
data/
├── items.json
├── products.json
├── recipes.json
└── sales.json