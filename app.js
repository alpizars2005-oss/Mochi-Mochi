const BUSINESS = {
  name: "Mochi Mochi",
  // Nota mía: aquí va el número real del negocio, en formato internacional y sin +.
  // Ejemplo México: 525512345678
  whatsappNumber: "525586793522",
  currency: "MXN"
};

const menu = [
  {
    id: "mochi-fresa",
    name: "Mochi de fresa",
    category: "Mochis",
    price: 35,
    description: "Suavecito, relleno cremoso y con ese toque fresco que se antoja muchísimo.",
    image: "https://images.unsplash.com/photo-1563805042-7684c019e1cb?auto=format&fit=crop&w=900&q=80"
  },
  {
    id: "mochi-matcha",
    name: "Mochi matcha",
    category: "Mochis",
    price: 38,
    description: "Sabor elegante, no tan dulce, ideal para quien quiere algo diferente.",
    image: "https://images.unsplash.com/photo-1606791422814-b32c705e3e2f?auto=format&fit=crop&w=900&q=80"
  },
  {
    id: "mochi-mango",
    name: "Mochi mango",
    category: "Mochis",
    price: 38,
    description: "Dulce, frutal y con vibra de postre de fin de semana.",
    image: "https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?auto=format&fit=crop&w=900&q=80"
  },
  {
    id: "boba-taro",
    name: "Boba taro",
    category: "Bebidas",
    price: 55,
    description: "Cremosa, fría y muy bonita para foto. De esas que se venden solitas.",
    image: "https://images.unsplash.com/photo-1558857563-b371033873b8?auto=format&fit=crop&w=900&q=80"
  },
  {
    id: "boba-fresa",
    name: "Boba fresa cream",
    category: "Bebidas",
    price: 58,
    description: "Fresa con crema, tapioca y un acabado suave para algo más especial.",
    image: "https://images.unsplash.com/photo-1551024506-0bccd828d307?auto=format&fit=crop&w=900&q=80"
  },
  {
    id: "limonada-lychee",
    name: "Limonada lychee",
    category: "Bebidas",
    price: 45,
    description: "Refrescante, ligera y perfecta para acompañar algo dulce.",
    image: "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?auto=format&fit=crop&w=900&q=80"
  },
  {
    id: "taiyaki",
    name: "Taiyaki relleno",
    category: "Antojitos",
    price: 48,
    description: "Panecito calientito con relleno dulce. Sencillo, rico y diferente.",
    image: "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=900&q=80"
  },
  {
    id: "dorayaki",
    name: "Dorayaki mini",
    category: "Antojitos",
    price: 42,
    description: "Dos pancitos suaves con relleno dulce. Muy fácil de compartir.",
    image: "https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=900&q=80"
  },
  {
    id: "combo-kawaii",
    name: "Combo Kawaii",
    category: "Combos",
    price: 95,
    description: "2 mochis a elegir y una bebida chica. Buen combo para primera compra.",
    image: "https://images.unsplash.com/photo-1558326567-98ae2405596b?auto=format&fit=crop&w=900&q=80"
  },
  {
    id: "combo-date",
    name: "Combo date",
    category: "Combos",
    price: 165,
    description: "4 mochis, 2 bebidas y una nota bonita. Pensado para regalar.",
    image: "https://images.unsplash.com/photo-1514517604298-cf80e0fb7f1e?auto=format&fit=crop&w=900&q=80"
  }
];

const state = {
  activeCategory: "Todo",
  cart: new Map()
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
const cartItems = $("[data-cart-items]");
const cartTotal = $("[data-cart-total]");
const orderNote = $("[data-order-note]");
const whatsappOrder = $("[data-whatsapp-order]");

function getCategories() {
  return ["Todo", ...new Set(menu.map((item) => item.category))];
}

function renderCategories() {
  categoriesContainer.innerHTML = getCategories()
    .map(
      (category) => `
        <button
          class="category-button ${category === state.activeCategory ? "is-active" : ""}"
          type="button"
          data-category="${category}"
        >${category}</button>
      `
    )
    .join("");
}

function renderMenu() {
  const filtered = state.activeCategory === "Todo"
    ? menu
    : menu.filter((item) => item.category === state.activeCategory);

  menuGrid.innerHTML = filtered
    .map(
      (item) => `
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
            <button class="add-button" type="button" data-add="${item.id}">Agregar</button>
          </div>
        </article>
      `
    )
    .join("");
}

function addToCart(id) {
  const item = menu.find((product) => product.id === id);
  if (!item) return;

  const current = state.cart.get(id) || { ...item, qty: 0 };
  current.qty += 1;
  state.cart.set(id, current);
  renderCart();
}

function updateQty(id, direction) {
  const current = state.cart.get(id);
  if (!current) return;

  current.qty += direction;
  if (current.qty <= 0) state.cart.delete(id);
  else state.cart.set(id, current);

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
      .map(
        (item) => `
          <div class="cart-row">
            <div>
              <strong>${item.name}</strong>
              <small>${item.qty} x ${money.format(item.price)}</small>
            </div>
            <div class="cart-row__actions">
              <button class="qty-button" type="button" data-qty="-1" data-id="${item.id}">-</button>
              <strong>${item.qty}</strong>
              <button class="qty-button" type="button" data-qty="1" data-id="${item.id}">+</button>
            </div>
          </div>
        `
      )
      .join("");
  }

  cartTotal.textContent = money.format(getTotal());
  whatsappOrder.href = buildWhatsAppLink();
}

function buildWhatsAppLink() {
  const lines = [
    `Hola, quiero hacer un pedido en ${BUSINESS.name}:`,
    ""
  ];

  if (state.cart.size === 0) {
    lines.push("Todavía no agregué productos, pero quiero pedir información.");
  } else {
    [...state.cart.values()].forEach((item) => {
      lines.push(`- ${item.qty} x ${item.name} = ${money.format(item.qty * item.price)}`);
    });
    lines.push("", `Total estimado: ${money.format(getTotal())}`);
  }

  const note = orderNote.value.trim();
  if (note) lines.push("", `Nota: ${note}`);

  return `https://wa.me/${BUSINESS.whatsappNumber}?text=${encodeURIComponent(lines.join("\n"))}`;
}

function setupEvents() {
  categoriesContainer.addEventListener("click", (event) => {
    const button = event.target.closest("[data-category]");
    if (!button) return;
    state.activeCategory = button.dataset.category;
    renderCategories();
    renderMenu();
  });

  menuGrid.addEventListener("click", (event) => {
    const button = event.target.closest("[data-add]");
    if (button) addToCart(button.dataset.add);
  });

  cartItems.addEventListener("click", (event) => {
    const button = event.target.closest("[data-qty]");
    if (!button) return;
    updateQty(button.dataset.id, Number(button.dataset.qty));
  });

  $("[data-clear-cart]").addEventListener("click", () => {
    state.cart.clear();
    renderCart();
  });

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
    { threshold: 0.14 }
  );

  $$(".reveal").forEach((element) => observer.observe(element));
}

// Nota mía: dejé todo separado en funciones para que luego no sea un caos editarlo.
renderCategories();
renderMenu();
renderCart();
setupEvents();
setupReveal();
