class DashboardController {
    constructor() {

    }
}

function asideHover() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        entry.target.dataset.active = entry.isIntersecting ? "true" : "false";
      });
    });
  
    const asideOptions = document.querySelectorAll('.aside-link');
    asideOptions.forEach((asideOption) => {
      observer.observe(asideOption);
    });
}
  
asideHover()