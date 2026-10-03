
/* =====================================================
   SERENDIP PRIVATE JOURNEYS
   MAIN JAVASCRIPT
===================================================== */

document.addEventListener("DOMContentLoaded", function () {


    /* =================================================
       ELEMENTS
    ================================================= */

    const menuToggle =
        document.getElementById("menuToggle");

    const navbar =
        document.getElementById("navbar");

    const header =
        document.getElementById("header");

    const navLinks =
        document.querySelectorAll(
            ".navbar .nav-link"
        );

    const sections =
        document.querySelectorAll(
            "section[id]"
        );


    /* =================================================
       MOBILE NAVIGATION
    ================================================= */

    if (menuToggle && navbar) {

        menuToggle.addEventListener(
            "click",
            function () {

                navbar.classList.toggle("active");

                const isOpen =
                    navbar.classList.contains("active");


                menuToggle.setAttribute(
                    "aria-expanded",
                    isOpen
                );


                menuToggle.textContent =
                    isOpen ? "✕" : "☰";

            }
        );


        /* Close menu after clicking link */

        const allMenuLinks =
            navbar.querySelectorAll("a");


        allMenuLinks.forEach(
            function (link) {

                link.addEventListener(
                    "click",
                    function () {

                        navbar.classList.remove(
                            "active"
                        );


                        menuToggle.setAttribute(
                            "aria-expanded",
                            "false"
                        );


                        menuToggle.textContent =
                            "☰";

                    }
                );

            }
        );

    }

/* =================================================
   ACTIVE NAVIGATION
   ONLY ONE NAV LINK ACTIVE AT A TIME
================================================= */

function setActiveNav(activeLink) {

    // Remove active from ALL links first
    navLinks.forEach(function (link) {

        link.classList.remove("active");

        link.removeAttribute("aria-current");

    });


    // Add active ONLY to selected link
    if (activeLink) {

        activeLink.classList.add("active");

        activeLink.setAttribute(
            "aria-current",
            "page"
        );

    }

}


/* =================================================
   NAVIGATION CLICK
   ONLY CLICKED LINK BECOMES ACTIVE
================================================= */

navLinks.forEach(function (link) {

    link.addEventListener("click", function () {

        // Remove active from every link
        navLinks.forEach(function (navLink) {

            navLink.classList.remove("active");

            navLink.removeAttribute("aria-current");

        });


        // Add active ONLY to clicked link
        link.classList.add("active");

        link.setAttribute(
            "aria-current",
            "page"
        );

    });

});


/* =================================================
   DO NOT CHANGE ACTIVE NAVIGATION ON SCROLL
================================================= */

/*
   IMPORTANT:
   The old updateActiveNavigation() function has
   been removed.

   Scrolling will no longer change the selected
   navigation item.
*/


/* =================================================
   HEADER SCROLL EFFECT
================================================= */

if (header) {

    function updateHeader() {

        if (window.scrollY > 50) {

            header.classList.add("scrolled");

        } else {

            header.classList.remove("scrolled");

        }

    }


    window.addEventListener(
        "scroll",
        updateHeader
    );


    updateHeader();

}


    /* =================================================
       FINAL CTA ANIMATION
    ================================================= */

    const cta =
        document.getElementById(
            "finalCTA"
        );


    const background =
        document.querySelector(
            ".cta-bg"
        );


    const glowOne =
        document.querySelector(
            ".cta-glow-one"
        );


    const glowTwo =
        document.querySelector(
            ".cta-glow-two"
        );


    if (cta) {

        cta.addEventListener(
            "mousemove",
            function (event) {

                const rect =
                    cta.getBoundingClientRect();


                const x =
                    (event.clientX - rect.left) /
                    rect.width - 0.5;


                const y =
                    (event.clientY - rect.top) /
                    rect.height - 0.5;


                if (background) {

                    background.style.transform =
                        `scale(1.08)
                         translate(
                            ${x * -12}px,
                            ${y * -12}px
                         )`;

                }


                if (glowOne) {

                    glowOne.style.transform =
                        `translate(
                            ${x * 50}px,
                            ${y * 40}px
                         )`;

                }


                if (glowTwo) {

                    glowTwo.style.transform =
                        `translate(
                            ${x * -40}px,
                            ${y * -30}px
                         )`;

                }

            }
        );


        cta.addEventListener(
            "mouseleave",
            function () {

                if (background) {

                    background.style.transform =
                        "scale(1.05)";

                }


                if (glowOne) {

                    glowOne.style.transform =
                        "translate(0, 0)";

                }


                if (glowTwo) {

                    glowTwo.style.transform =
                        "translate(0, 0)";

                }

            }
        );

    }


    /* =================================================
       SCROLL REVEAL
    ================================================= */

    const revealElements =
        document.querySelectorAll(
            ".reveal"
        );


    if (
        revealElements.length > 0 &&
        "IntersectionObserver" in window
    ) {

        const revealObserver =
            new IntersectionObserver(
                function (entries) {

                    entries.forEach(
                        function (entry) {

                            if (
                                entry.isIntersecting
                            ) {

                                entry.target.classList.add(
                                    "visible"
                                );


                                revealObserver.unobserve(
                                    entry.target
                                );

                            }

                        }
                    );

                },
                {
                    threshold: 0.12
                }
            );


        revealElements.forEach(
            function (element) {

                revealObserver.observe(
                    element
                );

            }
        );

    }


    /* =================================================
       TRIP FORM
    ================================================= */

    const tripForm =
        document.getElementById(
            "tripForm"
        );


    const formMessage =
        document.getElementById(
            "formMessage"
        );


    if (tripForm) {

        tripForm.addEventListener(
            "submit",
            function (event) {

                event.preventDefault();


                const nameElement =
                    document.getElementById(
                        "name"
                    );


                const emailElement =
                    document.getElementById(
                        "email"
                    );


                const arrivalElement =
                    document.getElementById(
                        "arrival"
                    );


                const travelersElement =
                    document.getElementById(
                        "travelers"
                    );


                const messageElement =
                    document.getElementById(
                        "message"
                    );


                const name =
                    nameElement
                        ? nameElement.value.trim()
                        : "";


                const email =
                    emailElement
                        ? emailElement.value.trim()
                        : "";


                const arrival =
                    arrivalElement
                        ? arrivalElement.value
                        : "";


                const travelers =
                    travelersElement
                        ? travelersElement.value
                        : "";


                const message =
                    messageElement
                        ? messageElement.value.trim()
                        : "";


                const interestInputs =
                    document.querySelectorAll(
                        ".interest input:checked"
                    );


                const interests =
                    Array.from(
                        interestInputs
                    ).map(
                        function (input) {

                            return input.value;

                        }
                    );


                /* Validation */

                if (!name || !email) {

                    if (formMessage) {

                        formMessage.textContent =
                            "Please enter your name and email.";

                    }

                    return;

                }


                /* Success message */

                if (formMessage) {

                    formMessage.textContent =
                        "Thank you! Your trip request has been prepared. We'll contact you soon.";

                }


                console.log({

                    name,
                    email,
                    arrival,
                    travelers,
                    interests,
                    message

                });


                tripForm.reset();

            }
        );

    }


    /* =================================================
       CURRENT YEAR
    ================================================= */

    const yearElement =
        document.getElementById(
            "year"
        );


    if (yearElement) {

        yearElement.textContent =
            new Date().getFullYear();

    }


    /* =================================================
       WHATSAPP LINKS
    ================================================= */

    const whatsappLinks =
        document.querySelectorAll(
            'a[href*="wa.me"]'
        );


    whatsappLinks.forEach(
        function (link) {

            link.addEventListener(
                "click",
                function () {

                    console.log(
                        "Opening WhatsApp contact..."
                    );

                }
            );

        }
    );


    /* =================================================
       CURRENT PAGE NAVIGATION
    ================================================= */

    const currentPath =
        window.location.pathname;


    navLinks.forEach(
        function (link) {

            const href =
                link.getAttribute("href");


            if (
                href &&
                !href.startsWith("#") &&
                link.pathname === currentPath
            ) {

                link.classList.add(
                    "active"
                );

            }

        }
    );


    /* =================================================
       HIGHLIGHT VIDEO
       
       INLINE VIDEO
       NO MODAL
       ONE VIDEO AT A TIME
    ================================================= */

    window.toggleHighlightVideo =
        function (button) {

            const card =
                button.closest(
                    ".highlight-card"
                );


            if (!card) {
                return;
            }


            const preview =
                card.querySelector(
                    ".highlight-video-preview"
                );


            const video =
                card.querySelector(
                    ".highlight-video"
                );


            if (!preview || !video) {
                return;
            }


            const alreadyOpen =
                preview.classList.contains(
                    "active"
                );


            /* -----------------------------------------
               CLOSE ALL OTHER VIDEOS
            ----------------------------------------- */

            document
                .querySelectorAll(
                    ".highlight-video-preview.active"
                )
                .forEach(
                    function (activePreview) {

                        activePreview.classList.remove(
                            "active"
                        );


                        const activeVideo =
                            activePreview.querySelector(
                                ".highlight-video"
                            );


                        if (activeVideo) {

                            activeVideo.pause();

                            activeVideo.currentTime = 0;

                        }

                    }
                );


            /* Remove active arrows */

            document
                .querySelectorAll(
                    ".highlight-arrow.active"
                )
                .forEach(
                    function (activeButton) {

                        activeButton.classList.remove(
                            "active"
                        );

                    }
                );


            /* -----------------------------------------
               IF ALREADY OPEN
            ----------------------------------------- */

            if (alreadyOpen) {

                return;

            }


            /* -----------------------------------------
               OPEN CURRENT VIDEO
            ----------------------------------------- */

            preview.classList.add(
                "active"
            );


            button.classList.add(
                "active"
            );


            video.play().catch(
                function () {

                    /*
                     * Autoplay may be blocked
                     * by the browser.
                     * Video controls remain available.
                     */

                }
            );

        };


});
