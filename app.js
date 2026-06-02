const BUSINESS = {
  name: "Mochi Mochi",
  // Nota mía: este número va en formato internacional y sin el signo +.
  // Ejemplo México: 525512345678
  whatsappNumber: "525586793522",
  currency: "MXN"
};

const STORAGE_KEYS = {
  sales: "mochi_mochi_sales_v2"
};

const products = [
  {
    id: "banderilla-coreana",
    name: "Banderilla coreana",
    category: "Banderillas",
    price: 35,
    description: "Banderilla doradita con queso, salchicha o combinada. La cobertura se elige al momento.",
    image: "https://images.unsplash.com/photo-1614088685112-5a9e1e6b8d9a?auto=format&fit=crop&w=900&q=80",
    optionLabel: "Cobertura",
    options: ["Natural", "Cheetos Flaming Hot", "Maruchan", "Panko", "Doritos Nacho", "Papa"],
    tags: ["Coreana", "Queso", "Salchicha"],
    ingredients: ["Queso mozzarella", "Salchichas", "Harina", "Levadura", "Sal", "Agua", "Huevo", "Palo brocheta", "Maicena"],
    flavors: ["Cheetos Flaming Hot", "Maruchan", "Panko", "Doritos Nacho", "Papa"]
  },
  {
    id: "sushi-roll",
    name: "Sushi roll",
    category: "Sushis",
    price: 90,
    description: "Roll preparado con base de arroz para sushi, alga nori y rellenos a elegir.",
    image: "https://images.unsplash.com/photo-1579584425555-c3ce17fd4351?auto=format&fit=crop&w=900&q=80",
    optionLabel: "Variante",
    options: ["California", "Plátano macho", "Mango", "Pollo empanizado", "Camarón empanizado", "Tocino", "Surimi"],
    tags: ["Roll", "Frío", "Empanizado"],
    ingredients: ["Alga nori", "Arroz para sushi", "Queso crema", "Aguacate", "Pepino", "Tocino", "Surimi", "Ajonjolí", "Camarones empanizados", "Plátano macho", "Mango", "Queso manchego", "Pollo empanizado", "Palillos"],
    flavors: ["California", "Plátano macho", "Mango", "Pollo empanizado", "Camarón empanizado", "Tocino", "Surimi"]
  },
  {
    id: "pay-limon",
    name: "Pay de limón",
    category: "Postres",
    price: 25,
    description: "Postre frío, cremosito y fresco con base de galleta y limón.",
    image: "https://images.unsplash.com/photo-1519915028121-7d3463d20b13?auto=format&fit=crop&w=900&q=80",
    optionLabel: "Presentación",
    options: ["Individual", "Con uvas"],
    tags: ["Frío", "Cremoso"],
    ingredients: ["Leche condensada", "Leche evaporada", "Limones", "Galletas", "Uvas"],
    flavors: ["Limón"]
  },
  {
    id: "mochi",
    name: "Mochi",
    category: "Mochis",
    price: 35,
    description: "Mochi suave con relleno cremoso. Puedes elegir el sabor principal.",
    image: "https://images.unsplash.com/photo-1563805042-7684c019e1cb?auto=format&fit=crop&w=900&q=80",
    optionLabel: "Sabor",
    options: ["Mango", "Fresa", "Galletas Oreo", "Durazno"],
    tags: ["Suave", "Dulce", "Relleno"],
    ingredients: ["Harina de arroz glutinoso", "Maicena", "Azúcar", "Leche", "Colorante", "Mantequilla", "Crema para batir", "Queso crema"],
    flavors: ["Mango", "Fresa", "Galletas Oreo", "Durazno"]
  },
  {
    id: "waffles",
    name: "Waffles",
    category: "Hot cakes y waffles",
    price: 45,
    description: "Waffles calientitos para combinar con fruta o toppings dulces.",
    image: "https://images.unsplash.com/photo-1562376552-0d160a2f238d?auto=format&fit=crop&w=900&q=80",
    optionLabel: "Topping",
    options: ["Natural", "Fresa", "Plátano", "Fresa y plátano"],
    tags: ["Dulce", "Calientito"],
    ingredients: ["Harina hot cakes", "Huevo", "Leche", "Mantequilla", "Fresa", "Plátano"],
    flavors: ["Fresa", "Plátano"]
  },
  {
    id: "platanos-arabes",
    name: "Plátanos árabes",
    category: "Hot cakes y waffles",
    price: 35,
    description: "Plátano preparado como antojito dulce, sencillo y muy vendible.",
    image: "https://images.unsplash.com/photo-1528825871115-3581a5387919?auto=format&fit=crop&w=900&q=80",
    optionLabel: "Presentación",
    options: ["Natural", "Con fresa", "Con extra crema"],
    tags: ["Dulce", "Fruta"],
    ingredients: ["Plátano macho", "Fresa", "Plátano", "Mantequilla"],
    flavors: ["Natural", "Fresa"]
  },
  {
    id: "hot-cakes",
    name: "Hot cakes",
    category: "Hot cakes y waffles",
    price: 45,
    description: "Hot cakes suaves, perfectos para desayuno, postre o combo dulce.",
    image: "https://images.unsplash.com/photo-1528207776546-365bb710ee93?auto=format&fit=crop&w=900&q=80",
    optionLabel: "Topping",
    options: ["Natural", "Fresa", "Plátano", "Fresa y plátano"],
    tags: ["Desayuno", "Dulce"],
    ingredients: ["Harina hot cakes", "Huevo", "Leche", "Mantequilla", "Fresa", "Plátano"],
    flavors: ["Fresa", "Plátano"]
  },
  {
    id: "soda-italiana",
    name: "Soda italiana",
    category: "Bebidas",
    price: 35,
    description: "Bebida fresca con jarabe de sabor, hielo y opción de perlas explosivas.",
    image: "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?auto=format&fit=crop&w=900&q=80",
    optionLabel: "Base",
    options: ["Con agua mineral", "Con refresco de limón", "Con perlas explosivas", "Sin perlas"],
    tags: ["Fría", "Refrescante"],
    ingredients: ["Jarabe de sabor", "Hielo", "Refresco de limón", "Agua mineral", "Perlas explosivas"],
    flavors: ["Jarabe de sabor", "Perlas explosivas"]
  },
  {
    id: "molle-pizza",
    name: "Molle pizza",
    category: "Salado",
    price: 40,
    description: "Pan de sal con salsa de tomate, queso manchego rallado y pepperoni.",
    image: "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=900&q=80",
    optionLabel: "Extra",
    options: ["Normal", "Extra queso", "Extra pepperoni"],
    tags: ["Queso", "Pepperoni"],
    ingredients: ["Pan de sal", "Salsa de tomate", "Queso manchego rallado", "Pepperoni"],
    flavors: ["Queso", "Pepperoni"]
  },
  {
    id: "papas-fritas",
    name: "Orden de papas fritas",
    category: "Salado",
    price: 50,
    description: "Orden de papas fritas con sal, ideal para acompañar banderillas o molle pizzas.",
    image: "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=900&q=80",
    optionLabel: "Presentación",
    options: ["Normal", "Con extra sal", "Sin sal"],
    tags: ["Papas", "Acompañamiento"],
    ingredients: ["Papa", "Sal"],
    flavors: ["Natural"]
  }
];

const state = {
  activeCategory: "Todo",
  search: "",
  cart: new Map(),
  sales: loadSales()
};

const money = new Intl.NumberFormat("es-MX", {
  style: "currency",
  currency: BUSINESS.currency,
  maximumFractionDigits: 0
});

const $ = (selector) => document.querySelector(selector);
const $$ = (selector) => document.querySelectorAll(selector);

const categoriesContainer = $("[data-categories]");
const menuGrid = $("[data-menu-grid]");
const ingredientsGrid = $("[data-ingredients-grid]");
const cartItems = $("[data-cart-items]");
const cartTotal = $("[data-cart-total]");
const orderNote = $("[data-order-note]");
const whatsappOrder = $("[data-whatsapp-order]");
const searchInput = $("[data-search]");
const salesTable = $("[data-sales-table]");
const quickProduct = $("[data-quick-product]");

function getCategories() {
  return ["Todo", ...new Set(products.map((item) => item.category))];
}

function getDefaultOption(product) {
  return product.options?.[0] ?? "Normal";
}

function getCartKey(productId, option) {
  return `${productId}::${option}`;
}

function loadSales() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEYS.sales)) || [];
  } catch (error) {
    return [];
  }
}

function saveSales() {
  localStorage.setItem(STORAGE_KEYS.sales, JSON.stringify(state.sales));
}

function renderCategories() {
  categoriesContainer.innerHTML = getCategories()
    .map((category) => `
      <button
        class="category-button ${category === state.activeCategory ? "is-active" : ""}"
        type="button"
        data-category="${category}"
      >${category}</button>
    `)
    .join("");
}

function getFilteredProducts() {
  const normalizedSearch = state.search.trim().toLowerCase();

  return products.filter((item) => {
    const categoryMatch = state.activeCategory === "Todo" || item.category === state.activeCategory;
    const searchText = [
      item.name,
      item.category,
      item.description,
      item.options?.join(" "),
      item.ingredients?.join(" ")
    ].join(" ").toLowerCase();

    return categoryMatch && (!normalizedSearch || searchText.includes(normalizedSearch));
  });
}

function renderMenu() {
  const filtered = getFilteredProducts();

  if (filtered.length === 0) {
    menuGrid.innerHTML = `<p class="empty-cart">No encontré productos con esa búsqueda.</p>`;
    return;
  }

  menuGrid.innerHTML = filtered
    .map((item) => `
      <article class="menu-card reveal is-visible">
        <img class="menu-card__image" src="${item.image}" alt="${item.name}" loading="lazy" />
        <div class="menu-card__body">
          <div class="menu-card__top">
            <div>
              <h3>${item.name}</h3>
              <span>${item.category}</span>
            </div>
            <strong class="price">${money.format(item.price)}</strong>
          </div>
          <p>${item.description}</p>
          <div class="tags">${item.tags.map((tag) => `<span class="tag">${tag}</span>`).join("")}</div>
          <label class="menu-option-label">
            ${item.optionLabel}
            <select data-option-for="${item.id}">
              ${item.options.map((option) => `<option value="${option}">${option}</option>`).join("")}
            </select>
          </label>
          <button class="add-button" type="button" data-add="${item.id}">Agregar</button>
        </div>
      </article>
    `)
    .join("");
}

function renderIngredients() {
  ingredientsGrid.innerHTML = products
    .map((item) => `
      <article class="ingredients-card reveal is-visible">
        <h3>${item.name}</h3>
        <span class="tag">${item.category}</span>
        <div class="flavors">
          <strong>Sabores / variantes</strong>
          <ul>${item.flavors.map((flavor) => `<li>${flavor}</li>`).join("")}</ul>
        </div>
        <div class="flavors">
          <strong>Ingredientes</strong>
          <ul>${item.ingredients.map((ingredient) => `<li>${ingredient}</li>`).join("")}</ul>
        </div>
      </article>
    `)
    .join("");
}

function addToCart(productId, option) {
  const item = products.find((product) => product.id === productId);
  if (!item) return;

  const selectedOption = option || getDefaultOption(item);
  const key = getCartKey(productId, selectedOption);
  const current = state.cart.get(key) || { ...item, selectedOption, qty: 0, cartKey: key };

  current.qty += 1;
  state.cart.set(key, current);
  renderCart();
}

function updateQty(key, direction) {
  const current = state.cart.get(key);
  if (!current) return;

  current.qty += direction;
  if (current.qty <= 0) state.cart.delete(key);
  else state.cart.set(key, current);

  renderCart();
}

function getTotal() {
  return [...state.cart.values()].reduce((sum, item) => sum + item.price * item.qty, 0);
}

function renderCart() {
  if (state.cart.size === 0) {
    cartItems.innerHTML = `<p class="empty-cart">Tu carrito está vacío. Agrega algo rico del menú.</p>`;
  } else {
    cartItems.innerHTML = [...state.cart.values()]
      .map((item) => `
        <div class="cart-row">
          <div>
            <strong>${item.name}</strong>
            <small>${item.selectedOption}</small>
            <small>${item.qty} x ${money.format(item.price)}</small>
          </div>
          <div class="cart-row__actions">
            <button class="qty-button" type="button" data-qty="-1" data-key="${item.cartKey}">-</button>
            <strong>${item.qty}</strong>
            <button class="qty-button" type="button" data-qty="1" data-key="${item.cartKey}">+</button>
          </div>
        </div>
      `)
      .join("");
  }

  cartTotal.textContent = money.format(getTotal());
  whatsappOrder.href = buildWhatsAppLink();
}

function buildWhatsAppLink() {
  const lines = [`Hola, quiero hacer un pedido en ${BUSINESS.name}:`, ""];

  if (state.cart.size === 0) {
    lines.push("Todavía no agregué productos, pero quiero pedir información.");
  } else {
    [...state.cart.values()].forEach((item) => {
      lines.push(`- ${item.qty} x ${item.name} (${item.selectedOption}) = ${money.format(item.qty * item.price)}`);
    });
    lines.push("", `Total estimado: ${money.format(getTotal())}`);
  }

  const note = orderNote.value.trim();
  if (note) lines.push("", `Nota: ${note}`);

  return `https://wa.me/${BUSINESS.whatsappNumber}?text=${encodeURIComponent(lines.join("\n"))}`;
}

function makeSale(items, note = "") {
  const cleanItems = items.map((item) => ({
    productId: item.id,
    name: item.name,
    option: item.selectedOption || item.option || getDefaultOption(item),
    qty: Number(item.qty),
    unitPrice: Number(item.price),
    subtotal: Number(item.price) * Number(item.qty)
  }));

  return {
    id: crypto.randomUUID ? crypto.randomUUID() : String(Date.now()),
    createdAt: new Date().toISOString(),
    note,
    items: cleanItems,
    total: cleanItems.reduce((sum, item) => sum + item.subtotal, 0)
  };
}

function registerCartSale() {
  if (state.cart.size === 0) {
    alert("Primero agrega productos al carrito, mi bro.");
    return;
  }

  const sale = makeSale([...state.cart.values()], orderNote.value.trim());
  state.sales.unshift(sale);
  saveSales();
  state.cart.clear();
  orderNote.value = "";
  renderCart();
  renderSales();
  alert("Venta guardada correctamente.");
}

function registerQuickSale(event) {
  event.preventDefault();

  const product = products.find((item) => item.id === quickProduct.value);
  const qty = Number($("[data-quick-qty]").value || 1);
  const note = $("[data-quick-note]").value.trim();

  if (!product || qty <= 0) return;

  const sale = makeSale([{ ...product, selectedOption: getDefaultOption(product), qty }], note);
  state.sales.unshift(sale);
  saveSales();
  event.target.reset();
  $("[data-quick-qty]").value = 1;
  renderSales();
}

function saleItemsText(sale) {
  return sale.items.map((item) => `${item.qty} x ${item.name} (${item.option})`).join("; ");
}

function renderSales() {
  const salesCount = state.sales.length;
  const salesTotal = state.sales.reduce((sum, sale) => sum + sale.total, 0);
  const itemsTotal = state.sales.reduce((sum, sale) => sum + sale.items.reduce((itemSum, item) => itemSum + item.qty, 0), 0);

  $("[data-sales-count]").textContent = salesCount;
  $("[data-sales-total]").textContent = money.format(salesTotal);
  $("[data-sales-items]").textContent = itemsTotal;

  if (state.sales.length === 0) {
    salesTable.innerHTML = `<tr><td colspan="5">Todavía no hay ventas registradas.</td></tr>`;
    return;
  }

  salesTable.innerHTML = state.sales
    .map((sale) => `
      <tr>
        <td>${new Date(sale.createdAt).toLocaleString("es-MX")}</td>
        <td>${saleItemsText(sale)}</td>
        <td>${sale.note || "-"}</td>
        <td><strong>${money.format(sale.total)}</strong></td>
        <td><button class="delete-sale" type="button" data-delete-sale="${sale.id}">Borrar</button></td>
      </tr>
    `)
    .join("");
}

function deleteSale(id) {
  state.sales = state.sales.filter((sale) => sale.id !== id);
  saveSales();
  renderSales();
}

function clearSales() {
  const ok = confirm("¿Seguro que quieres borrar el historial de ventas?");
  if (!ok) return;
  state.sales = [];
  saveSales();
  renderSales();
}

function getSalesRows() {
  return state.sales.flatMap((sale) =>
    sale.items.map((item) => ({
      Fecha: new Date(sale.createdAt).toLocaleString("es-MX"),
      Producto: item.name,
      Variante: item.option,
      Cantidad: item.qty,
      "Precio unitario": item.unitPrice,
      Subtotal: item.subtotal,
      "Total venta": sale.total,
      Nota: sale.note || ""
    }))
  );
}

function exportSalesExcel() {
  const rows = getSalesRows();
  if (rows.length === 0) {
    alert("No hay ventas para exportar.");
    return;
  }

  if (!window.XLSX) {
    exportSalesCsv();
    alert("No cargó la librería de Excel, así que descargué CSV para abrirlo en Excel.");
    return;
  }

  const worksheet = XLSX.utils.json_to_sheet(rows);
  const workbook = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(workbook, worksheet, "Ventas");
  XLSX.writeFile(workbook, `ventas-mochi-mochi-${getDateStamp()}.xlsx`);
}

function exportSalesCsv() {
  const rows = getSalesRows();
  if (rows.length === 0) {
    alert("No hay ventas para exportar.");
    return;
  }

  const headers = Object.keys(rows[0]);
  const csv = [
    headers.join(","),
    ...rows.map((row) => headers.map((header) => `"${String(row[header]).replaceAll('"', '""')}"`).join(","))
  ].join("\n");

  const blob = new Blob(["\ufeff" + csv], { type: "text/csv;charset=utf-8;" });
  downloadBlob(blob, `ventas-mochi-mochi-${getDateStamp()}.csv`);
}

function downloadBlob(blob, filename) {
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
}

function getDateStamp() {
  return new Date().toISOString().slice(0, 10);
}

function renderQuickSaleOptions() {
  quickProduct.innerHTML = products
    .map((product) => `<option value="${product.id}">${product.name} - ${money.format(product.price)}</option>`)
    .join("");
}

function setupEvents() {
  categoriesContainer.addEventListener("click", (event) => {
    const button = event.target.closest("[data-category]");
    if (!button) return;
    state.activeCategory = button.dataset.category;
    renderCategories();
    renderMenu();
  });

  searchInput.addEventListener("input", (event) => {
    state.search = event.target.value;
    renderMenu();
  });

  menuGrid.addEventListener("click", (event) => {
    const button = event.target.closest("[data-add]");
    if (!button) return;
    const productId = button.dataset.add;
    const option = $(`[data-option-for="${productId}"]`)?.value;
    addToCart(productId, option);
  });

  cartItems.addEventListener("click", (event) => {
    const button = event.target.closest("[data-qty]");
    if (!button) return;
    updateQty(button.dataset.key, Number(button.dataset.qty));
  });

  salesTable.addEventListener("click", (event) => {
    const button = event.target.closest("[data-delete-sale]");
    if (!button) return;
    deleteSale(button.dataset.deleteSale);
  });

  $("[data-clear-cart]").addEventListener("click", () => {
    state.cart.clear();
    renderCart();
  });

  $("[data-register-cart-sale]").addEventListener("click", registerCartSale);
  $("[data-quick-sale-form]").addEventListener("submit", registerQuickSale);
  $("[data-export-sales]").addEventListener("click", exportSalesExcel);
  $("[data-export-csv]").addEventListener("click", exportSalesCsv);
  $("[data-clear-sales]").addEventListener("click", clearSales);

  orderNote.addEventListener("input", () => {
    whatsappOrder.href = buildWhatsAppLink();
  });

  $("[data-theme-toggle]").addEventListener("click", () => {
    const isDark = document.documentElement.dataset.theme === "dark";
    document.documentElement.dataset.theme = isDark ? "light" : "dark";
    $("[data-theme-toggle]").textContent = isDark ? "Modo noche" : "Modo día";
  });

  $("[data-nav-toggle]").addEventListener("click", () => {
    $("[data-nav-links]").classList.toggle("is-open");
  });
}

function setupReveal() {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) entry.target.classList.add("is-visible");
      });
    },
    { threshold: 0.12 }
  );

  $$(".reveal").forEach((element) => observer.observe(element));
}

// Nota mía: estos precios son base/editables. Cuando ya tenga precios finales, solo cambio el arreglo products.
$("[data-total-products]").textContent = products.length;
renderCategories();
renderMenu();
renderIngredients();
renderQuickSaleOptions();
renderCart();
renderSales();
setupEvents();
setupReveal();
