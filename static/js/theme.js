'use strict';
document.addEventListener('DOMContentLoaded', function () {
    /* =====================================================
        TESTIMONIALS SLIDER
    ===================================================== */
    var testimonialsSlider = new Swiper('.testimonials-slider', {
        slidesPerView: 1,
        spaceBetween: 10,
        breakpoints: {
            720: {
                slidesPerView: 2,
            },
            970: {
                slidesPerView: 3,
            },
            1170: {
                slidesPerView: 4,
            },
        },
        pagination: {
            el: '.swiper-pagination',
            dynamicBullets: true,
            clickable: true,
        },
    });

    /* =====================================================
        WORKS SLIDER
    ===================================================== */
    var worksSlider = new Swiper('.work-slider', {
        slidesPerView: 1,
        spaceBetween: 10,
        pagination: {
            el: '.swiper-pagination',
            dynamicBullets: true,
            clickable: true,
        },
    });

    /* =====================================================
        INITALIZE TOOLTIPS
    ===================================================== */
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    /* =====================================================
        PARALLAX
    ===================================================== */
    new universalParallax().init();

  
     /* =====================================================
       SCROLLING LINKS W/ OFFSET
    ===================================================== */

    document.querySelectorAll('.nav-item a[href^="#"]')
        .forEach(trigger => {
            trigger.onclick = function (e) {
                e.preventDefault();
                let hash = this.getAttribute('href');
                let target = document.querySelector(hash);
                let headerOffset = 90;
                let elementPosition = target.offsetTop;
                let offsetPosition = elementPosition - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: "smooth"
                });
            };
        });

    /* =====================================================
        TRIGGER COUNTERS WHEN REACHING THE TARGET SECTION
    ===================================================== */
    var waypoint = new Waypoint({
        element: document.getElementById('statistics'),
        handler: function (direction) {
            countup();
        },
        offset: '95%',
    });

    /* =====================================================
        BOOTSTRAP SCROLLSPY
    ===================================================== */
    var scrollSpy = new bootstrap.ScrollSpy(document.body, {
        target: '#navbar',
        offset: 100
    });

    /* =====================================================
        MIXITUP FILTER
    ===================================================== */
    var mixer = mixitup('#content');

    /* =====================================================
        REVEAL ANIMATION
    ===================================================== */
    var wow = new WOW({
        boxClass: 'wow',
        animateClass: 'animated',
        offset: 0,
        mobile: true,
        live: true,
        scrollContainer: null,
        resetAnimation: true,
    });
    wow.init();
});
