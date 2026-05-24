import customtkinter as ctk
import json
import os
import copy
from datetime import datetime
from tkinter import messagebox

# ============================================================
# BANDERILLAS MONT'S - SISTEMA V4
# Inventario + recetas editables + ventas + costos + ganancias
# ============================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

APP_TITLE = "Banderillas Mont's - Sistema V4.1 Optimizado"
DATA_DIR = "data"

os.makedirs(DATA_DIR, exist_ok=True)

FILES = {
    "items": os.path.join(DATA_DIR, "items.json"),
    "products": os.path.join(DATA_DIR, "products.json"),
    "recipes": os.path.join(DATA_DIR, "recipes.json"),
    "sales": os.path.join(DATA_DIR, "sales.json"),
}

CATEGORIES = {
    "ingredientes": "🥫 Ingredientes Auto",
    "insumos": "🧂 Insumos Auto",
    "desechables": "🥡 Desechables",
    "manuales": "🌶️ Manuales",
}

AUTOMATIC_CATEGORIES = ["ingredientes", "insumos", "desechables"]


# ============================================================
# DATOS DEFAULT
# qty = cantidad actual
# cost = costo por unidad usada en receta
# ============================================================

DEFAULT_ITEMS = {
    "ingredientes": {
        "Queso Mozarella": {"qty": 10.0, "cost": 0.0},
        "Salchicha para banderilla": {"qty": 50.0, "cost": 0.0},
        "Harina": {"qty": 10.0, "cost": 0.0},
        "Levadura": {"qty": 1.0, "cost": 0.0},
        "Sal": {"qty": 2.0, "cost": 0.0},
        "Agua": {"qty": 20.0, "cost": 0.0},
        "Huevo": {"qty": 30.0, "cost": 0.0},
        "Palo Brocheta": {"qty": 100.0, "cost": 0.0},
        "Maicena": {"qty": 2.0, "cost": 0.0},

        "Alga Nori": {"qty": 50.0, "cost": 0.0},
        "Arroz para sushi": {"qty": 8.0, "cost": 0.0},
        "Queso Crema": {"qty": 6.0, "cost": 0.0},
        "Aguacate": {"qty": 20.0, "cost": 0.0},
        "Pepino": {"qty": 15.0, "cost": 0.0},
        "Tocino": {"qty": 20.0, "cost": 0.0},
        "Surimi": {"qty": 60.0, "cost": 0.0},
        "Ajonjolí": {"qty": 1.5, "cost": 0.0},
        "Camarones Empanizados": {"qty": 40.0, "cost": 0.0},
        "Plátano Macho": {"qty": 15.0, "cost": 0.0},
        "Mango": {"qty": 15.0, "cost": 0.0},
        "Queso Manchego": {"qty": 5.0, "cost": 0.0},
        "Pollo Empanizado": {"qty": 20.0, "cost": 0.0},
        "Palillos comida": {"qty": 100.0, "cost": 0.0},

        "Leche condensada": {"qty": 12.0, "cost": 0.0},
        "Leche evaporada": {"qty": 12.0, "cost": 0.0},
        "Limones": {"qty": 50.0, "cost": 0.0},
        "Galletas": {"qty": 20.0, "cost": 0.0},
        "Uvas": {"qty": 15.0, "cost": 0.0},

        "Fresa": {"qty": 20.0, "cost": 0.0},
        "Galletas Oreo": {"qty": 10.0, "cost": 0.0},
        "Durazno": {"qty": 15.0, "cost": 0.0},
        "Harina de Arroz G": {"qty": 5.0, "cost": 0.0},
        "Azúcar": {"qty": 10.0, "cost": 0.0},
        "Leche": {"qty": 15.0, "cost": 0.0},
        "Colorante": {"qty": 3.0, "cost": 0.0},
        "Mantequilla": {"qty": 6.0, "cost": 0.0},
        "Crema para batir": {"qty": 10.0, "cost": 0.0},

        "Pastel": {"qty": 5.0, "cost": 0.0},
        "Chocolate Blanco": {"qty": 8.0, "cost": 0.0},
        "Grajea": {"qty": 3.0, "cost": 0.0},
        "Palitos cake pop": {"qty": 100.0, "cost": 0.0},

        "Harina Hot K": {"qty": 8.0, "cost": 0.0},
        "Plátano": {"qty": 20.0, "cost": 0.0},

        "Refresco de Limón": {"qty": 20.0, "cost": 0.0},
        "Agua Mineral": {"qty": 20.0, "cost": 0.0},
        "Perlas explosivas": {"qty": 10.0, "cost": 0.0},

        "Pan de Sal": {"qty": 30.0, "cost": 0.0},
        "Salsa de Tomate": {"qty": 8.0, "cost": 0.0},
        "Queso Manchego Rallado": {"qty": 6.0, "cost": 0.0},
        "Peperoni": {"qty": 10.0, "cost": 0.0},

        "Papa para papas fritas": {"qty": 20.0, "cost": 0.0},
    },

    "insumos": {
        "Vasos de cristal": {"qty": 50.0, "cost": 0.0},
        "Tapa de vaso cristal": {"qty": 50.0, "cost": 0.0},
    },

    "desechables": {
        "Domo Hot Dog": {"qty": 100.0, "cost": 0.0},
        "Domo Hamburguesa": {"qty": 50.0, "cost": 0.0},
        "Palillos desechables": {"qty": 200.0, "cost": 0.0},
        "Bolsas CP": {"qty": 200.0, "cost": 0.0},
        "Vasos de 16 oz": {"qty": 100.0, "cost": 0.0},
        "Tapa vaso 16 oz con popote": {"qty": 100.0, "cost": 0.0},
        "Popotes de tapioca": {"qty": 100.0, "cost": 0.0},
        "Domo para mochis": {"qty": 50.0, "cost": 0.0},
        "Papel Absorbente": {"qty": 10.0, "cost": 0.0},
        "Vasito para aderezo": {"qty": 100.0, "cost": 0.0},
        "Tapa para vasito de aderezo": {"qty": 100.0, "cost": 0.0},
    },

    "manuales": {
        "Aceite": {"qty": 10.0, "cost": 0.0},
        "Catsup": {"qty": 5.0, "cost": 0.0},
        "Salsa Valentina": {"qty": 5.0, "cost": 0.0},
        "Queso Amarillo": {"qty": 5.0, "cost": 0.0},
        "Mostaza": {"qty": 5.0, "cost": 0.0},
        "Salsa Anguila": {"qty": 3.0, "cost": 0.0},
        "Salsa de soya": {"qty": 3.0, "cost": 0.0},
        "Mirin": {"qty": 2.0, "cost": 0.0},
        "Nutella": {"qty": 4.0, "cost": 0.0},
        "Crema": {"qty": 5.0, "cost": 0.0},
        "Lechera": {"qty": 5.0, "cost": 0.0},
        "Mermelada de fresa": {"qty": 5.0, "cost": 0.0},
        "Jarabe de Sabor": {"qty": 8.0, "cost": 0.0},
        "Hielo": {"qty": 30.0, "cost": 0.0},

        "Cheetos Flaming Hot": {"qty": 5.0, "cost": 0.0},
        "Maruchan": {"qty": 10.0, "cost": 0.0},
        "Panko": {"qty": 5.0, "cost": 0.0},
        "Doritos Nacho": {"qty": 5.0, "cost": 0.0},
        "Papa para topping": {"qty": 20.0, "cost": 0.0},
    },
}

DEFAULT_PRODUCTS = {
    "Banderilla Natural": {"price": 35.0, "sold": 0},
    "Banderilla Cheetos Flaming Hot": {"price": 35.0, "sold": 0},
    "Banderilla Maruchan": {"price": 35.0, "sold": 0},
    "Banderilla Panko": {"price": 35.0, "sold": 0},
    "Banderilla Doritos Nacho": {"price": 35.0, "sold": 0},
    "Banderilla Papa": {"price": 35.0, "sold": 0},

    "Sushi California Roll": {"price": 90.0, "sold": 0},
    "Sushi Empanizado Roll": {"price": 110.0, "sold": 0},
    "Sushi Mango Roll": {"price": 100.0, "sold": 0},
    "Sushi Banana Roll": {"price": 100.0, "sold": 0},
    "Sushi Tocino Roll": {"price": 100.0, "sold": 0},

    "Pay de Limón": {"price": 20.0, "sold": 0},
    "Mochi Mango": {"price": 0.0, "sold": 0},
    "Mochi Fresa": {"price": 0.0, "sold": 0},
    "Mochi Oreo": {"price": 0.0, "sold": 0},
    "Mochi Durazno": {"price": 0.0, "sold": 0},
    "Cake Pop": {"price": 0.0, "sold": 0},
    "Waffle Fresa": {"price": 25.0, "sold": 0},
    "Waffle Plátano": {"price": 25.0, "sold": 0},
    "Plátano Árabe Fresa": {"price": 35.0, "sold": 0},
    "Plátano Árabe Plátano": {"price": 35.0, "sold": 0},
    "Hot Cake Fresa": {"price": 0.0, "sold": 0},
    "Hot Cake Plátano": {"price": 0.0, "sold": 0},
    "Soda Italiana": {"price": 0.0, "sold": 0},
    "Molle Pizza": {"price": 0.0, "sold": 0},
    "Papas Fritas": {"price": 50.0, "sold": 0},
}


def empty_recipe():
    return {
        "ingredientes": {},
        "insumos": {},
        "desechables": {},
        "manuales": [],
        "banderilla": False,
    }


BASE_BANDERILLA_RECIPE = {
    "ingredientes": {
        "Harina": 0.08,
        "Levadura": 0.01,
        "Sal": 0.01,
        "Agua": 0.10,
        "Huevo": 0.20,
        "Palo Brocheta": 1.0,
        "Maicena": 0.02,
    },
    "insumos": {},
    "desechables": {
        "Domo Hot Dog": 1.0,
        "Vasito para aderezo": 1.0,
        "Tapa para vasito de aderezo": 1.0,
    },
    "manuales": [],
    "banderilla": True,
}


def recipe_copy(recipe):
    return copy.deepcopy(recipe)


DEFAULT_RECIPES = {
    "Banderilla Natural": recipe_copy(BASE_BANDERILLA_RECIPE),
    "Banderilla Cheetos Flaming Hot": {
        **recipe_copy(BASE_BANDERILLA_RECIPE),
        "manuales": ["Cheetos Flaming Hot"],
    },
    "Banderilla Maruchan": {
        **recipe_copy(BASE_BANDERILLA_RECIPE),
        "manuales": ["Maruchan"],
    },
    "Banderilla Panko": {
        **recipe_copy(BASE_BANDERILLA_RECIPE),
        "manuales": ["Panko"],
    },
    "Banderilla Doritos Nacho": {
        **recipe_copy(BASE_BANDERILLA_RECIPE),
        "manuales": ["Doritos Nacho"],
    },
    "Banderilla Papa": {
        **recipe_copy(BASE_BANDERILLA_RECIPE),
        "manuales": ["Papa para topping"],
    },

    "Sushi California Roll": {
        "ingredientes": {
            "Alga Nori": 1.0,
            "Arroz para sushi": 0.25,
            "Queso Crema": 0.08,
            "Aguacate": 0.05,
            "Pepino": 0.05,
            "Ajonjolí": 0.01,
            "Palillos comida": 1.0,
            "Surimi": 3.0,
        },
        "insumos": {},
        "desechables": {"Palillos desechables": 1.0},
        "manuales": ["Salsa Anguila", "Salsa de soya"],
        "banderilla": False,
    },

    "Soda Italiana": {
        "ingredientes": {
            "Refresco de Limón": 0.20,
            "Agua Mineral": 0.20,
            "Perlas explosivas": 0.03,
        },
        "insumos": {},
        "desechables": {
            "Vasos de 16 oz": 1.0,
            "Tapa vaso 16 oz con popote": 1.0,
            "Popotes de tapioca": 1.0,
        },
        "manuales": ["Jarabe de Sabor", "Hielo"],
        "banderilla": False,
    },

    "Papas Fritas": {
        "ingredientes": {
            "Papa para papas fritas": 0.30,
            "Sal": 0.01,
        },
        "insumos": {},
        "desechables": {},
        "manuales": ["Aceite"],
        "banderilla": False,
    },
}


# Agregar receta vacía a productos que no tienen receta default
for product_name in DEFAULT_PRODUCTS:
    DEFAULT_RECIPES.setdefault(product_name, empty_recipe())


# ============================================================
# APP
# ============================================================

class MontsApp:
    def __init__(self, root):
        self.root = root

        self.items = self.load_or_default("items", DEFAULT_ITEMS)
        self.products = self.load_or_default("products", DEFAULT_PRODUCTS)
        self.recipes = self.load_or_default("recipes", DEFAULT_RECIPES)
        self.sales = self.load_or_default("sales", [])

        self.normalize_data()
        self.save_all()

        self.search_products = ctk.StringVar()
        self.search_items = {}
        self.search_sales = ctk.StringVar()
        self.search_history = ctk.StringVar()

        self.selected_recipe_product = ctk.StringVar()
        self.selected_recipe_category = ctk.StringVar(value="ingredientes")
        self.selected_recipe_item = ctk.StringVar()

        self.sale_status = None

        self.build_ui()

        # Render diferido: no dibujamos todas las tablas al abrir.
        # Esto acelera bastante el arranque del programa.
        self.refresh_current_tab()

    # ----------------------------
    # DATA
    # ----------------------------

    def load_or_default(self, key, default):
        path = FILES[key]
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return copy.deepcopy(default)
        return copy.deepcopy(default)

    def save_key(self, key):
        with open(FILES[key], "w", encoding="utf-8") as f:
            json.dump(getattr(self, key), f, indent=4, ensure_ascii=False)

    def save_all(self):
        self.save_key("items")
        self.save_key("products")
        self.save_key("recipes")
        self.save_key("sales")

    def normalize_data(self):
        # Completar categorías
        for cat, default_items in DEFAULT_ITEMS.items():
            self.items.setdefault(cat, {})
            for name, data in default_items.items():
                self.items[cat].setdefault(name, data)

        # Normalizar items viejos que pudieran venir como número
        for cat in self.items:
            for name in list(self.items[cat].keys()):
                value = self.items[cat][name]
                if isinstance(value, (int, float)):
                    self.items[cat][name] = {"qty": float(value), "cost": 0.0}
                else:
                    value.setdefault("qty", 0.0)
                    value.setdefault("cost", 0.0)

        # Completar productos
        for name, data in DEFAULT_PRODUCTS.items():
            self.products.setdefault(name, data)

        for name in list(self.products.keys()):
            value = self.products[name]
            if isinstance(value, (int, float)):
                self.products[name] = {"price": 0.0, "sold": int(value)}
            else:
                value.setdefault("price", 0.0)
                value.setdefault("sold", 0)

        # Completar recetas
        for name in self.products:
            self.recipes.setdefault(name, empty_recipe())

        for name in list(self.recipes.keys()):
            recipe = self.recipes[name]
            recipe.setdefault("ingredientes", {})
            recipe.setdefault("insumos", {})
            recipe.setdefault("desechables", {})
            recipe.setdefault("manuales", [])
            recipe.setdefault("banderilla", False)

    # ----------------------------
    # HELPERS
    # ----------------------------

    def fmt(self, n):
        try:
            n = float(n)
            if n.is_integer():
                return str(int(n))
            return str(round(n, 2))
        except Exception:
            return str(n)

    def money(self, n):
        try:
            return f"${float(n):.2f}"
        except Exception:
            return "$0.00"

    def matches(self, text, query):
        return query.strip().lower() in text.strip().lower()

    def clear(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def status_for_qty(self, qty):
        try:
            qty = float(qty)
        except Exception:
            qty = 0

        if qty == 0:
            return "❌ Agotado", "red"
        if qty <= 3:
            return "⚠️ Poco stock", "yellow"
        return "✅ Disponible", "lightgreen"

    def get_item_names(self, category):
        return list(self.items.get(category, {}).keys())

    def safe_float(self, value, default=None):
        try:
            return float(value)
        except Exception:
            return default

    # ----------------------------
    # UI
    # ----------------------------

    def build_ui(self):
        title = ctk.CTkLabel(
            self.root,
            text=APP_TITLE,
            font=("Arial", 32, "bold")
        )
        title.pack(pady=12)

        self.tabs = ctk.CTkTabview(self.root, width=1480, height=820, command=self.refresh_current_tab)
        self.tabs.pack(fill="both", expand=True, padx=18, pady=10)

        self.tab_dashboard = self.tabs.add("📊 Dashboard")
        self.tab_products = self.tabs.add("🍽️ Productos")
        self.tab_items = {}
        for cat, label in CATEGORIES.items():
            self.tab_items[cat] = self.tabs.add(label)
        self.tab_recipes = self.tabs.add("🔗 Recetas")
        self.tab_sales = self.tabs.add("💰 Ventas")
        self.tab_history = self.tabs.add("📋 Historial")

        self.build_dashboard_tab()
        self.build_products_tab()
        for cat in CATEGORIES:
            self.build_items_tab(cat)
        self.build_recipes_tab()
        self.build_sales_tab()
        self.build_history_tab()

    def make_search(self, parent, variable, placeholder, callback):
        frame = ctk.CTkFrame(parent)
        frame.pack(pady=8)

        ctk.CTkLabel(frame, text="🔎 Buscar:", font=("Arial", 14, "bold")).grid(row=0, column=0, padx=8, pady=8)

        entry = ctk.CTkEntry(
            frame,
            textvariable=variable,
            placeholder_text=placeholder,
            width=380
        )
        entry.grid(row=0, column=1, padx=8, pady=8)

        ctk.CTkButton(
            frame,
            text="Limpiar",
            width=80,
            command=lambda: variable.set("")
        ).grid(row=0, column=2, padx=8, pady=8)

        variable.trace_add("write", lambda *args: callback())

    def build_dashboard_tab(self):
        self.dashboard_frame = ctk.CTkScrollableFrame(self.tab_dashboard, width=1380, height=650)
        self.dashboard_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def build_products_tab(self):
        self.make_search(self.tab_products, self.search_products, "Buscar producto...", self.refresh_products)

        self.products_frame = ctk.CTkScrollableFrame(self.tab_products, width=1380, height=545)
        self.products_frame.pack(fill="both", expand=True, padx=20, pady=10)

        form = ctk.CTkFrame(self.tab_products)
        form.pack(pady=10)

        self.product_name_entry = ctk.CTkEntry(form, placeholder_text="Nuevo producto", width=260)
        self.product_name_entry.grid(row=0, column=0, padx=8, pady=8)

        self.product_price_entry = ctk.CTkEntry(form, placeholder_text="Precio venta", width=140)
        self.product_price_entry.grid(row=0, column=1, padx=8, pady=8)

        ctk.CTkButton(form, text="Agregar producto", command=self.add_product).grid(row=0, column=2, padx=8, pady=8)

    def build_items_tab(self, category):
        tab = self.tab_items[category]

        self.search_items[category] = ctk.StringVar()
        self.make_search(tab, self.search_items[category], f"Buscar en {CATEGORIES[category]}...", lambda c=category: self.refresh_items(c))

        frame = ctk.CTkScrollableFrame(tab, width=1380, height=535)
        frame.pack(fill="both", expand=True, padx=20, pady=10)
        setattr(self, f"{category}_frame", frame)

        form = ctk.CTkFrame(tab)
        form.pack(pady=10)

        name_entry = ctk.CTkEntry(form, placeholder_text="Nombre", width=260)
        name_entry.grid(row=0, column=0, padx=8, pady=8)

        qty_entry = ctk.CTkEntry(form, placeholder_text="Cantidad", width=130)
        qty_entry.grid(row=0, column=1, padx=8, pady=8)

        cost_entry = ctk.CTkEntry(form, placeholder_text="Costo unitario", width=140)
        cost_entry.grid(row=0, column=2, padx=8, pady=8)

        setattr(self, f"{category}_name_entry", name_entry)
        setattr(self, f"{category}_qty_entry", qty_entry)
        setattr(self, f"{category}_cost_entry", cost_entry)

        ctk.CTkButton(
            form,
            text="Agregar",
            command=lambda c=category: self.add_item(c)
        ).grid(row=0, column=3, padx=8, pady=8)

        if category == "manuales":
            ctk.CTkLabel(
                tab,
                text="Manual = salsas, toppings y cosas variables. NO se descuentan automáticamente; solo salen como aviso en la venta.",
                text_color="orange",
                font=("Arial", 14)
            ).pack(pady=5)

    def build_recipes_tab(self):
        top = ctk.CTkFrame(self.tab_recipes)
        top.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(top, text="Producto:", font=("Arial", 14, "bold")).grid(row=0, column=0, padx=8, pady=8)
        self.recipe_product_menu = ctk.CTkOptionMenu(
            top,
            values=list(self.products.keys()),
            variable=self.selected_recipe_product,
            command=lambda _: self.refresh_recipe_editor()
        )
        self.recipe_product_menu.grid(row=0, column=1, padx=8, pady=8)

        ctk.CTkLabel(top, text="Categoría:", font=("Arial", 14, "bold")).grid(row=0, column=2, padx=8, pady=8)
        self.recipe_category_menu = ctk.CTkOptionMenu(
            top,
            values=list(CATEGORIES.keys()),
            variable=self.selected_recipe_category,
            command=lambda _: self.update_recipe_item_menu()
        )
        self.recipe_category_menu.grid(row=0, column=3, padx=8, pady=8)

        ctk.CTkLabel(top, text="Item:", font=("Arial", 14, "bold")).grid(row=0, column=4, padx=8, pady=8)
        self.recipe_item_menu = ctk.CTkOptionMenu(
            top,
            values=["Sin items"],
            variable=self.selected_recipe_item
        )
        self.recipe_item_menu.grid(row=0, column=5, padx=8, pady=8)

        self.recipe_qty_entry = ctk.CTkEntry(top, placeholder_text="Cantidad", width=120)
        self.recipe_qty_entry.grid(row=0, column=6, padx=8, pady=8)

        ctk.CTkButton(top, text="Vincular descuento", command=self.add_recipe_link).grid(row=0, column=7, padx=8, pady=8)

        self.banderilla_var = ctk.BooleanVar(value=False)
        ctk.CTkCheckBox(
            top,
            text="Este producto es banderilla y debe preguntar relleno",
            variable=self.banderilla_var,
            command=self.update_recipe_banderilla_flag
        ).grid(row=1, column=0, columnspan=4, padx=8, pady=8, sticky="w")

        self.recipe_frame = ctk.CTkScrollableFrame(self.tab_recipes, width=1380, height=590)
        self.recipe_frame.pack(fill="both", expand=True, padx=20, pady=10)

    def build_sales_tab(self):
        ctk.CTkLabel(self.tab_sales, text="Registrar ventas", font=("Arial", 28, "bold")).pack(pady=10)

        self.make_search(self.tab_sales, self.search_sales, "Buscar producto para vender...", self.refresh_sales_buttons)

        self.sales_buttons_frame = ctk.CTkScrollableFrame(self.tab_sales, width=1380, height=500)
        self.sales_buttons_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.sale_status = ctk.CTkLabel(
            self.tab_sales,
            text="Aquí aparecerá el resultado de la venta.",
            font=("Arial", 16),
            wraplength=1200,
            justify="left"
        )
        self.sale_status.pack(pady=10)

    def build_history_tab(self):
        ctk.CTkLabel(self.tab_history, text="Historial de ventas", font=("Arial", 28, "bold")).pack(pady=10)
        self.make_search(self.tab_history, self.search_history, "Buscar en historial...", self.refresh_history)

        self.history_frame = ctk.CTkScrollableFrame(self.tab_history, width=1380, height=640)
        self.history_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # ----------------------------
    # REFRESH
    # ----------------------------

    def refresh_all(self):
        self.refresh_dashboard()
        self.refresh_products()
        for cat in CATEGORIES:
            self.refresh_items(cat)
        self.refresh_recipe_menus()
        self.refresh_recipe_editor()
        self.refresh_sales_buttons()
        self.refresh_history()

    def refresh_current_tab(self):
        """Actualiza solo la pestaña visible.

        Antes la app redibujaba todas las tablas después de casi cualquier cambio.
        Eso funciona, pero se vuelve lento cuando hay muchos datos. Ahora solo
        actualizamos lo que el usuario está viendo.
        """
        if not hasattr(self, "tabs"):
            return

        current = self.tabs.get()

        if current == "📊 Dashboard":
            self.refresh_dashboard()

        elif current == "🍽️ Productos":
            self.refresh_products()

        elif current == CATEGORIES["ingredientes"]:
            self.refresh_items("ingredientes")

        elif current == CATEGORIES["insumos"]:
            self.refresh_items("insumos")

        elif current == CATEGORIES["desechables"]:
            self.refresh_items("desechables")

        elif current == CATEGORIES["manuales"]:
            self.refresh_items("manuales")

        elif current == "🔗 Recetas":
            self.refresh_recipe_menus()
            self.refresh_recipe_editor()

        elif current == "💰 Ventas":
            self.refresh_sales_buttons()

        elif current == "📋 Historial":
            self.refresh_history()

    def refresh_dashboard(self):
        self.clear(self.dashboard_frame)

        total_sales = sum(float(s.get("price", 0)) for s in self.sales)
        total_cost = sum(float(s.get("cost", 0)) for s in self.sales)
        total_profit = total_sales - total_cost
        total_units = len(self.sales)

        cards = [
            ("Ventas registradas", str(total_units)),
            ("Ingresos", self.money(total_sales)),
            ("Costo estimado", self.money(total_cost)),
            ("Ganancia estimada", self.money(total_profit)),
        ]

        for i, (title, value) in enumerate(cards):
            card = ctk.CTkFrame(self.dashboard_frame, width=300, height=120)
            card.grid(row=0, column=i, padx=12, pady=12, sticky="nsew")

            ctk.CTkLabel(card, text=title, font=("Arial", 15, "bold")).pack(pady=(20, 5))
            ctk.CTkLabel(card, text=value, font=("Arial", 26, "bold")).pack(pady=5)

        ctk.CTkLabel(
            self.dashboard_frame,
            text="Stock bajo / agotado",
            font=("Arial", 22, "bold")
        ).grid(row=1, column=0, columnspan=4, pady=20, sticky="w")

        row = 2
        for cat, label in CATEGORIES.items():
            for name, data in self.items.get(cat, {}).items():
                qty = float(data.get("qty", 0))
                if qty <= 3:
                    status, color = self.status_for_qty(qty)
                    ctk.CTkLabel(
                        self.dashboard_frame,
                        text=f"{label} | {name}: {self.fmt(qty)} | {status}",
                        text_color=color,
                        font=("Arial", 15)
                    ).grid(row=row, column=0, columnspan=4, padx=12, pady=4, sticky="w")
                    row += 1

    def refresh_products(self):
        self.clear(self.products_frame)

        headers = ["Producto", "Precio", "Vendidos", "Ingresos", "Editar precio", "Editar vendidos", "Borrar"]
        for col, h in enumerate(headers):
            ctk.CTkLabel(self.products_frame, text=h, font=("Arial", 16, "bold")).grid(row=0, column=col, padx=12, pady=10)

        query = self.search_products.get()
        row = 1

        for name, data in self.products.items():
            if not self.matches(name, query):
                continue

            price = float(data.get("price", 0))
            sold = int(data.get("sold", 0))
            revenue = price * sold

            values = [name, self.money(price), sold, self.money(revenue)]
            for col, value in enumerate(values):
                ctk.CTkLabel(self.products_frame, text=str(value), font=("Arial", 14)).grid(row=row, column=col, padx=12, pady=7)

            ctk.CTkButton(
                self.products_frame,
                text="Precio",
                width=80,
                command=lambda n=name: self.edit_product_price(n)
            ).grid(row=row, column=4, padx=5)

            ctk.CTkButton(
                self.products_frame,
                text="Vendidos",
                width=80,
                command=lambda n=name: self.edit_product_sold(n)
            ).grid(row=row, column=5, padx=5)

            ctk.CTkButton(
                self.products_frame,
                text="🗑️",
                width=50,
                fg_color="red",
                command=lambda n=name: self.delete_product(n)
            ).grid(row=row, column=6, padx=5)

            row += 1

    def refresh_items(self, category):
        frame = getattr(self, f"{category}_frame")
        self.clear(frame)

        headers = ["Nombre", "Cantidad", "Costo unit.", "Valor inventario", "Estado", "+", "-", "Editar", "Borrar"]
        for col, h in enumerate(headers):
            ctk.CTkLabel(frame, text=h, font=("Arial", 16, "bold")).grid(row=0, column=col, padx=10, pady=10)

        query = self.search_items[category].get()
        row = 1

        for name, data in self.items[category].items():
            if not self.matches(name, query):
                continue

            qty = float(data.get("qty", 0))
            cost = float(data.get("cost", 0))
            value = qty * cost
            status, color = self.status_for_qty(qty)

            values = [name, self.fmt(qty), self.money(cost), self.money(value), status]
            for col, value_text in enumerate(values):
                text_color = color if col == 4 else "white"
                ctk.CTkLabel(frame, text=str(value_text), text_color=text_color, font=("Arial", 14)).grid(row=row, column=col, padx=10, pady=7)

            ctk.CTkButton(frame, text="+", width=40, fg_color="green", command=lambda c=category, n=name: self.item_add_qty(c, n, 1)).grid(row=row, column=5, padx=4)
            ctk.CTkButton(frame, text="-", width=40, fg_color="orange", command=lambda c=category, n=name: self.item_add_qty(c, n, -1)).grid(row=row, column=6, padx=4)
            ctk.CTkButton(frame, text="Editar", width=70, command=lambda c=category, n=name: self.edit_item(c, n)).grid(row=row, column=7, padx=4)
            ctk.CTkButton(frame, text="🗑️", width=50, fg_color="red", command=lambda c=category, n=name: self.delete_item(c, n)).grid(row=row, column=8, padx=4)

            row += 1

    def refresh_recipe_menus(self):
        products = list(self.products.keys())
        if not products:
            products = ["Sin productos"]

        self.recipe_product_menu.configure(values=products)

        if self.selected_recipe_product.get() not in products:
            self.selected_recipe_product.set(products[0])

        self.update_recipe_item_menu()

    def update_recipe_item_menu(self):
        category = self.selected_recipe_category.get()
        items = self.get_item_names(category)
        if not items:
            items = ["Sin items"]

        self.recipe_item_menu.configure(values=items)

        if self.selected_recipe_item.get() not in items:
            self.selected_recipe_item.set(items[0])

    def refresh_recipe_editor(self):
        self.clear(self.recipe_frame)

        product = self.selected_recipe_product.get()
        if product not in self.recipes:
            return

        recipe = self.recipes[product]
        self.banderilla_var.set(bool(recipe.get("banderilla", False)))

        ctk.CTkLabel(
            self.recipe_frame,
            text=f"Receta de: {product}",
            font=("Arial", 22, "bold")
        ).grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="w")

        row = 1

        for cat in ["ingredientes", "insumos", "desechables"]:
            ctk.CTkLabel(
                self.recipe_frame,
                text=CATEGORIES[cat],
                font=("Arial", 18, "bold"),
                text_color="lightgreen"
            ).grid(row=row, column=0, columnspan=5, padx=10, pady=10, sticky="w")
            row += 1

            ctk.CTkLabel(self.recipe_frame, text="Item", font=("Arial", 15, "bold")).grid(row=row, column=0, padx=10, pady=6)
            ctk.CTkLabel(self.recipe_frame, text="Cantidad", font=("Arial", 15, "bold")).grid(row=row, column=1, padx=10, pady=6)
            ctk.CTkLabel(self.recipe_frame, text="Costo", font=("Arial", 15, "bold")).grid(row=row, column=2, padx=10, pady=6)
            ctk.CTkLabel(self.recipe_frame, text="Acción", font=("Arial", 15, "bold")).grid(row=row, column=3, padx=10, pady=6)
            row += 1

            for item_name, qty in recipe.get(cat, {}).items():
                cost = self.get_recipe_line_cost(cat, item_name, qty)

                ctk.CTkLabel(self.recipe_frame, text=item_name, font=("Arial", 14)).grid(row=row, column=0, padx=10, pady=5)
                ctk.CTkLabel(self.recipe_frame, text=self.fmt(qty), font=("Arial", 14)).grid(row=row, column=1, padx=10, pady=5)
                ctk.CTkLabel(self.recipe_frame, text=self.money(cost), font=("Arial", 14)).grid(row=row, column=2, padx=10, pady=5)

                ctk.CTkButton(
                    self.recipe_frame,
                    text="Eliminar vínculo",
                    width=120,
                    fg_color="red",
                    command=lambda c=cat, i=item_name: self.delete_recipe_link(c, i)
                ).grid(row=row, column=3, padx=10, pady=5)

                row += 1

        ctk.CTkLabel(
            self.recipe_frame,
            text="🌶️ Manuales / variables",
            font=("Arial", 18, "bold"),
            text_color="orange"
        ).grid(row=row, column=0, columnspan=5, padx=10, pady=10, sticky="w")
        row += 1

        for manual in recipe.get("manuales", []):
            ctk.CTkLabel(self.recipe_frame, text=manual, font=("Arial", 14)).grid(row=row, column=0, padx=10, pady=5)
            ctk.CTkLabel(self.recipe_frame, text="Solo aviso; no descuenta", text_color="orange", font=("Arial", 14)).grid(row=row, column=1, padx=10, pady=5)
            ctk.CTkButton(
                self.recipe_frame,
                text="Eliminar aviso",
                width=120,
                fg_color="red",
                command=lambda m=manual: self.delete_manual_recipe_link(m)
            ).grid(row=row, column=3, padx=10, pady=5)
            row += 1

        estimated_cost = self.calculate_recipe_cost(recipe)
        product_price = float(self.products.get(product, {}).get("price", 0))
        profit = product_price - estimated_cost

        ctk.CTkLabel(
            self.recipe_frame,
            text=f"Costo estimado: {self.money(estimated_cost)} | Precio: {self.money(product_price)} | Ganancia estimada: {self.money(profit)}",
            font=("Arial", 18, "bold"),
            text_color="lightgreen" if profit >= 0 else "red"
        ).grid(row=row, column=0, columnspan=5, padx=10, pady=20, sticky="w")

    def refresh_sales_buttons(self):
        self.clear(self.sales_buttons_frame)

        query = self.search_sales.get()
        row = 0

        for name, data in self.products.items():
            if not self.matches(name, query):
                continue

            price = self.money(data.get("price", 0))

            button = ctk.CTkButton(
                self.sales_buttons_frame,
                text=f"{name}\n{price}",
                width=300,
                height=60,
                command=lambda n=name: self.start_sale(n)
            )
            button.grid(row=row // 3, column=row % 3, padx=12, pady=10)
            row += 1

    def refresh_history(self):
        self.clear(self.history_frame)

        headers = ["Fecha", "Producto", "Precio", "Costo", "Ganancia", "Detalle"]
        for col, h in enumerate(headers):
            ctk.CTkLabel(self.history_frame, text=h, font=("Arial", 15, "bold")).grid(row=0, column=col, padx=10, pady=10)

        query = self.search_history.get()
        row = 1

        for sale in reversed(self.sales[-150:]):
            searchable = f"{sale.get('date', '')} {sale.get('product', '')} {sale.get('detail', '')}"
            if not self.matches(searchable, query):
                continue

            profit = float(sale.get("profit", 0))
            color = "lightgreen" if profit >= 0 else "red"

            values = [
                sale.get("date", ""),
                sale.get("product", ""),
                self.money(sale.get("price", 0)),
                self.money(sale.get("cost", 0)),
                self.money(profit),
                sale.get("detail", ""),
            ]

            for col, value in enumerate(values):
                ctk.CTkLabel(
                    self.history_frame,
                    text=str(value),
                    font=("Arial", 13),
                    text_color=color if col == 4 else "white",
                    wraplength=360 if col == 5 else 200
                ).grid(row=row, column=col, padx=10, pady=6)

            row += 1

    # ----------------------------
    # PRODUCT ACTIONS
    # ----------------------------

    def add_product(self):
        name = self.product_name_entry.get().strip()
        price = self.safe_float(self.product_price_entry.get().strip(), 0.0)

        if not name:
            return

        self.products[name] = {"price": price, "sold": 0}
        self.recipes.setdefault(name, empty_recipe())
        self.save_key("products")
        self.save_key("recipes")

        self.product_name_entry.delete(0, "end")
        self.product_price_entry.delete(0, "end")

        self.refresh_products()
        self.refresh_recipe_menus()
        self.refresh_sales_buttons()
        self.refresh_dashboard()

    def edit_product_price(self, name):
        dialog = ctk.CTkInputDialog(text=f"Nuevo precio para '{name}'", title="Editar precio")
        value = dialog.get_input()
        if value is None:
            return

        price = self.safe_float(value, None)
        if price is None:
            return

        self.products[name]["price"] = max(0, price)
        self.save_key("products")
        self.refresh_products()
        self.refresh_recipe_editor()
        self.refresh_sales_buttons()
        self.refresh_dashboard()

    def edit_product_sold(self, name):
        dialog = ctk.CTkInputDialog(text=f"Cantidad vendida para '{name}'", title="Editar vendidos")
        value = dialog.get_input()
        if value is None:
            return

        sold = self.safe_float(value, None)
        if sold is None:
            return

        self.products[name]["sold"] = int(max(0, sold))
        self.save_key("products")
        self.refresh_products()
        self.refresh_dashboard()

    def delete_product(self, name):
        if not messagebox.askyesno("Confirmar", f"¿Borrar producto '{name}'?"):
            return

        self.products.pop(name, None)
        self.recipes.pop(name, None)
        self.save_key("products")
        self.save_key("recipes")

        self.refresh_products()
        self.refresh_recipe_menus()
        self.refresh_recipe_editor()
        self.refresh_sales_buttons()
        self.refresh_dashboard()

    # ----------------------------
    # ITEM ACTIONS
    # ----------------------------

    def add_item(self, category):
        name_entry = getattr(self, f"{category}_name_entry")
        qty_entry = getattr(self, f"{category}_qty_entry")
        cost_entry = getattr(self, f"{category}_cost_entry")

        name = name_entry.get().strip()
        qty = self.safe_float(qty_entry.get().strip(), None)
        cost = self.safe_float(cost_entry.get().strip(), 0.0)

        if not name or qty is None:
            return

        self.items[category][name] = {"qty": max(0, qty), "cost": max(0, cost)}
        self.save_key("items")

        name_entry.delete(0, "end")
        qty_entry.delete(0, "end")
        cost_entry.delete(0, "end")

        self.refresh_items(category)
        self.refresh_recipe_menus()
        self.refresh_recipe_editor()
        self.refresh_dashboard()

    def item_add_qty(self, category, name, delta):
        self.items[category][name]["qty"] = max(0, float(self.items[category][name].get("qty", 0)) + delta)
        self.save_key("items")
        self.refresh_items(category)
        self.refresh_dashboard()

    def edit_item(self, category, name):
        qty_dialog = ctk.CTkInputDialog(text=f"Nueva cantidad para '{name}'", title="Editar cantidad")
        qty_value = qty_dialog.get_input()
        if qty_value is None:
            return

        qty = self.safe_float(qty_value, None)
        if qty is None:
            return

        cost_dialog = ctk.CTkInputDialog(text=f"Costo unitario para '{name}'", title="Editar costo")
        cost_value = cost_dialog.get_input()
        if cost_value is None:
            return

        cost = self.safe_float(cost_value, None)
        if cost is None:
            return

        self.items[category][name]["qty"] = max(0, qty)
        self.items[category][name]["cost"] = max(0, cost)
        self.save_key("items")

        self.refresh_items(category)
        self.refresh_recipe_editor()
        self.refresh_dashboard()

    def delete_item(self, category, name):
        if not messagebox.askyesno("Confirmar", f"¿Borrar '{name}'?"):
            return

        self.items[category].pop(name, None)
        self.remove_item_from_all_recipes(category, name)

        self.save_key("items")
        self.save_key("recipes")

        self.refresh_items(category)
        self.refresh_recipe_menus()
        self.refresh_recipe_editor()
        self.refresh_dashboard()

    def remove_item_from_all_recipes(self, category, name):
        for recipe in self.recipes.values():
            if category == "manuales":
                if name in recipe.get("manuales", []):
                    recipe["manuales"].remove(name)
            else:
                recipe.get(category, {}).pop(name, None)

    # ----------------------------
    # RECIPE ACTIONS
    # ----------------------------

    def update_recipe_banderilla_flag(self):
        product = self.selected_recipe_product.get()
        if product not in self.recipes:
            return

        self.recipes[product]["banderilla"] = bool(self.banderilla_var.get())
        self.save_key("recipes")
        self.refresh_recipe_editor()

    def add_recipe_link(self):
        product = self.selected_recipe_product.get()
        category = self.selected_recipe_category.get()
        item = self.selected_recipe_item.get()

        if product not in self.recipes or item == "Sin items":
            return

        if category == "manuales":
            if item not in self.recipes[product]["manuales"]:
                self.recipes[product]["manuales"].append(item)
        else:
            qty = self.safe_float(self.recipe_qty_entry.get().strip(), None)
            if qty is None or qty <= 0:
                return
            self.recipes[product][category][item] = qty

        self.recipe_qty_entry.delete(0, "end")
        self.save_key("recipes")
        self.refresh_recipe_editor()

    def delete_recipe_link(self, category, item):
        product = self.selected_recipe_product.get()
        if product in self.recipes:
            self.recipes[product].get(category, {}).pop(item, None)
            self.save_key("recipes")
            self.refresh_recipe_editor()

    def delete_manual_recipe_link(self, item):
        product = self.selected_recipe_product.get()
        if product in self.recipes and item in self.recipes[product].get("manuales", []):
            self.recipes[product]["manuales"].remove(item)
            self.save_key("recipes")
            self.refresh_recipe_editor()

    # ----------------------------
    # COSTS
    # ----------------------------

    def get_recipe_line_cost(self, category, item_name, qty):
        if category not in self.items:
            return 0.0
        if item_name not in self.items[category]:
            return 0.0
        unit_cost = float(self.items[category][item_name].get("cost", 0))
        return float(qty) * unit_cost

    def calculate_recipe_cost(self, recipe):
        total = 0.0
        for category in AUTOMATIC_CATEGORIES:
            for item_name, qty in recipe.get(category, {}).items():
                total += self.get_recipe_line_cost(category, item_name, qty)
        return total

    def get_banderilla_fill_consumption(self, fill_type):
        if fill_type == "Salchicha":
            return {
                "Salchicha para banderilla": 1.0,
                "Queso Mozarella": 0.0,
            }
        if fill_type == "Queso":
            return {
                "Salchicha para banderilla": 0.0,
                "Queso Mozarella": 0.20,
            }
        return {
            "Salchicha para banderilla": 0.5,
            "Queso Mozarella": 0.10,
        }

    # ----------------------------
    # SALES
    # ----------------------------

    def start_sale(self, product_name):
        recipe = self.recipes.get(product_name, empty_recipe())

        if recipe.get("banderilla"):
            self.open_banderilla_sale_dialog(product_name)
        else:
            self.sell_product(product_name, detail="Venta normal")

    def open_banderilla_sale_dialog(self, product_name):
        dialog = ctk.CTkToplevel(self.root)
        dialog.title("Venta de banderilla")
        dialog.geometry("420x320")
        dialog.grab_set()

        ctk.CTkLabel(
            dialog,
            text=f"Vender: {product_name}",
            font=("Arial", 20, "bold")
        ).pack(pady=15)

        fill_var = ctk.StringVar(value="Combinada")

        ctk.CTkLabel(dialog, text="Tipo de relleno:", font=("Arial", 14, "bold")).pack(pady=5)

        ctk.CTkOptionMenu(
            dialog,
            values=["Salchicha", "Queso", "Combinada"],
            variable=fill_var
        ).pack(pady=8)

        sauce_cup_var = ctk.BooleanVar(value=True)

        ctk.CTkCheckBox(
            dialog,
            text="Descontar vasito de aderezo y tapa",
            variable=sauce_cup_var
        ).pack(pady=12)

        def confirm():
            self.sell_product(
                product_name,
                banderilla_fill=fill_var.get(),
                sauce_cup=bool(sauce_cup_var.get()),
                detail=f"Relleno: {fill_var.get()} | Vasito aderezo: {'Sí' if sauce_cup_var.get() else 'No'}"
            )
            dialog.destroy()

        ctk.CTkButton(dialog, text="Confirmar venta", height=42, command=confirm).pack(pady=15)

    def build_sale_recipe(self, product_name, banderilla_fill=None, sauce_cup=True):
        recipe = copy.deepcopy(self.recipes.get(product_name, empty_recipe()))

        if recipe.get("banderilla"):
            fill_consumption = self.get_banderilla_fill_consumption(banderilla_fill or "Combinada")
            for item, qty in fill_consumption.items():
                if qty > 0:
                    recipe["ingredientes"][item] = recipe["ingredientes"].get(item, 0) + qty

            if not sauce_cup:
                recipe["desechables"].pop("Vasito para aderezo", None)
                recipe["desechables"].pop("Tapa para vasito de aderezo", None)

        return recipe

    def validate_sale_stock(self, recipe):
        missing = []

        for category in AUTOMATIC_CATEGORIES:
            for item, needed in recipe.get(category, {}).items():
                current = float(self.items.get(category, {}).get(item, {}).get("qty", 0))
                if current < float(needed):
                    missing.append(f"{CATEGORIES[category]} | {item}: {self.fmt(current)} / {self.fmt(needed)}")

        return missing

    def deduct_recipe(self, recipe):
        for category in AUTOMATIC_CATEGORIES:
            for item, qty in recipe.get(category, {}).items():
                if item in self.items.get(category, {}):
                    current = float(self.items[category][item].get("qty", 0))
                    self.items[category][item]["qty"] = max(0, current - float(qty))

    def sell_product(self, product_name, banderilla_fill=None, sauce_cup=True, detail=""):
        if product_name not in self.products:
            return

        recipe = self.build_sale_recipe(product_name, banderilla_fill, sauce_cup)
        missing = self.validate_sale_stock(recipe)

        if missing:
            self.sale_status.configure(
                text="❌ No se pudo registrar la venta.\nFalta:\n" + "\n".join(missing),
                text_color="red"
            )
            return

        price = float(self.products[product_name].get("price", 0))
        cost = self.calculate_recipe_cost(recipe)
        profit = price - cost

        self.deduct_recipe(recipe)

        self.products[product_name]["sold"] = int(self.products[product_name].get("sold", 0)) + 1

        manuales = recipe.get("manuales", [])

        sale = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "product": product_name,
            "price": price,
            "cost": cost,
            "profit": profit,
            "detail": detail,
            "manuales": manuales,
            "recipe": recipe,
        }

        self.sales.append(sale)

        self.save_key("items")
        self.save_key("products")
        self.save_key("sales")

        # No redibujamos todas las pestañas. Solo actualizamos la vista actual.
        # Cuando el usuario entre a Dashboard/Historial/Inventario, se recalcula en ese momento.
        self.refresh_current_tab()

        message = f"✅ Venta registrada: {product_name}\nPrecio: {self.money(price)} | Costo: {self.money(cost)} | Ganancia: {self.money(profit)}"

        if detail:
            message += f"\n{detail}"

        if manuales:
            message += "\n⚠️ Revisar manualmente:\n- " + "\n- ".join(manuales)

        self.sale_status.configure(
            text=message,
            text_color="lightgreen" if profit >= 0 else "orange"
        )


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    root = ctk.CTk()
    root.title(APP_TITLE)
    root.geometry("1540x900")

    app = MontsApp(root)

    root.mainloop()
