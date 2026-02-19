(function () {
  const board = document.querySelector(".kanban-board");
  if (!board) return;

  let draggedCard = null;

  // Start dragging
  board.addEventListener("dragstart", (e) => {
    const card = e.target.closest(".kanban-card");
    if (!card) return;

    draggedCard = card;
    card.classList.add("is-dragging");
    e.dataTransfer.effectAllowed = "move";
  });

  // End dragging
  board.addEventListener("dragend", () => {
    if (!draggedCard) return;
    draggedCard.classList.remove("is-dragging");
    draggedCard = null;

    // remove highlight from columns
    document.querySelectorAll(".kanban-col").forEach(col => col.classList.remove("is-over"));
  });

  // Highlight columns while dragging over
  board.addEventListener("dragover", (e) => {
    e.preventDefault();
    const col = e.target.closest(".kanban-col");
    if (!col) return;

    document.querySelectorAll(".kanban-col").forEach(c => c.classList.remove("is-over"));
    col.classList.add("is-over");
  });

  // Drop into column
  board.addEventListener("drop", (e) => {
    e.preventDefault();
    const col = e.target.closest(".kanban-col");
    if (!col || !draggedCard) return;

    const body = col.querySelector(".kanban-col-body");
    if (!body) return;

    body.prepend(draggedCard);

    // update card stage data (visual only)
    const newStage = col.getAttribute("data-stage");
    draggedCard.setAttribute("data-stage", newStage);

    // update the stage badge class (visual only)
    const badge = draggedCard.querySelector(".badge-stage");
    if (badge) {
      // remove old badge-stage-* class
      badge.className = badge.className
        .split(" ")
        .filter(c => !c.startsWith("badge-stage-"))
        .join(" ");

      badge.classList.add("badge-stage", `badge-stage-${newStage}`);
    }

    // update column counts
    updateCounts();
  });

  function updateCounts() {
    document.querySelectorAll(".kanban-col").forEach(col => {
      const countBadge = col.querySelector(".kanban-col-header .badge");
      const cards = col.querySelectorAll(".kanban-card");
      if (countBadge) countBadge.textContent = cards.length;
    });
  }
})();
