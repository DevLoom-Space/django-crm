(function () {
  const btn = document.getElementById("sidebarToggle");
  const sidebar = document.getElementById("sidebar");
  const overlay = document.getElementById("sidebarOverlay");

  if (!btn || !sidebar) return;

  function openSidebar() {
    sidebar.classList.add("show");
    if (overlay) overlay.classList.add("show");
  }

  function closeSidebar() {
    sidebar.classList.remove("show");
    if (overlay) overlay.classList.remove("show");
  }

  btn.addEventListener("click", () => {
    const isOpen = sidebar.classList.contains("show");
    if (isOpen) closeSidebar();
    else openSidebar();
  });

  if (overlay) {
    overlay.addEventListener("click", closeSidebar);
  }

  // Close sidebar when resizing to large screens (prevents stuck overlay)
  window.addEventListener("resize", () => {
    if (window.innerWidth >= 992) closeSidebar();
  });
})();
