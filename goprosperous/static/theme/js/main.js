document.addEventListener('DOMContentLoaded', function () {
  // Main sidebar toggling handler
  document.getElementById('toggle-sidebar').addEventListener('click', function () {
    document.getElementById('sidebar').classList.toggle('collapsed');
    document.getElementById('content').classList.toggle('collapsed');
    document.getElementById('navbar').classList.toggle('collapsed');
  });

  // Initiate all theme popovers
  const popoverElements = document.querySelectorAll('.button-triggers-theme-popover');
  popoverElements.forEach(element => {
    new bootstrap.Popover(element, {
      html: true,
    });
  });

  // Collapse handler for secondary sidebar
  const secondarySidebarCollapseTogglers = document.querySelectorAll('.secondary-sidebar-collapse-toggler');
  secondarySidebarCollapseTogglers.forEach(element => {
    element.addEventListener('click', () => {
      setTimeout(() => {
        const chevronElement = element.querySelector('.chevron-icon');

        if (element.classList.contains('collapsed')) {
          element.closest("div.secondary-sidebar-collapse-section").classList.remove("collapse-open");
          chevronElement.classList.remove("fa-chevron-up");
          chevronElement.classList.add("fa-chevron-down");
        }
        else {
          element.closest("div.secondary-sidebar-collapse-section").classList.add("collapse-open");
          chevronElement.classList.remove("fa-chevron-down");
          chevronElement.classList.add("fa-chevron-up");
        }
      }, 0);
    });
  });
});
