/**
 * Anthony Obinugwu Portfolio - Interactive Engine
 * Particles, Typewriter, SPA Navigation, Sticky Navbar & Utilities
 */

(function () {
  'use strict';

  // 1. Preloader
  window.addEventListener('load', function () {
    const preloader = document.getElementById('preloader');
    if (preloader) {
      setTimeout(function () {
        preloader.classList.add('loaded');
      }, 300);
    }
  });

  // 2. Sticky Navbar & Scroll-to-Top
  const navbar = document.querySelector('.navbar');
  const scrollTopBtn = document.getElementById('scroll-top-btn');

  window.addEventListener('scroll', function () {
    if (window.scrollY > 20) {
      if (navbar) navbar.classList.add('sticky');
    } else {
      if (navbar) navbar.classList.remove('sticky');
    }

    if (scrollTopBtn) {
      if (window.scrollY > 300) {
        scrollTopBtn.classList.add('visible');
      } else {
        scrollTopBtn.classList.remove('visible');
      }
    }
  });

  if (scrollTopBtn) {
    scrollTopBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // 3. Mobile Navigation Menu Toggle
  const navToggler = document.querySelector('.navbar-toggler');
  const navMenu = document.querySelector('.navbar-nav');

  if (navToggler && navMenu) {
    navToggler.addEventListener('click', function () {
      navMenu.classList.toggle('show');
    });

    // Close when clicking nav items
    const navLinks = navMenu.querySelectorAll('.nav-link');
    navLinks.forEach(function (link) {
      link.addEventListener('click', function () {
        navMenu.classList.remove('show');
      });
    });
  }

  // 4. Background Star Particles Canvas
  const canvas = document.getElementById('tsparticles-canvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    window.addEventListener('resize', function () {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    });

    const numParticles = Math.min(Math.floor((width * height) / 10000), 120);
    const particles = [];

    for (let i = 0; i < numParticles; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        radius: Math.random() * 2 + 0.6,
        vx: (Math.random() - 0.5) * 0.4,
        vy: (Math.random() - 0.5) * 0.4,
        alpha: Math.random() * 0.7 + 0.3,
        deltaAlpha: (Math.random() - 0.5) * 0.02,
        color: Math.random() > 0.35 ? '#1db954' : '#ffffff'
      });
    }

    function animateParticles() {
      ctx.clearRect(0, 0, width, height);

      // Draw connections
      for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
          const dx = particles[i].x - particles[j].x;
          const dy = particles[i].y - particles[j].y;
          const dist = Math.sqrt(dx * dx + dy * dy);

          if (dist < 110) {
            ctx.beginPath();
            ctx.moveTo(particles[i].x, particles[i].y);
            ctx.lineTo(particles[j].x, particles[j].y);
            const opacity = (1 - dist / 110) * 0.22;
            ctx.strokeStyle = `rgba(29, 185, 84, ${opacity})`;
            ctx.lineWidth = 0.8;
            ctx.stroke();
          }
        }
      }

      // Draw particles
      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;
        if (p.y < 0) p.y = height;
        if (p.y > height) p.y = 0;

        p.alpha += p.deltaAlpha;
        if (p.alpha <= 0.2 || p.alpha >= 0.85) {
          p.deltaAlpha = -p.deltaAlpha;
        }

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = p.color;
        ctx.globalAlpha = p.alpha;
        ctx.fill();
      }

      ctx.globalAlpha = 1.0;
      requestAnimationFrame(animateParticles);
    }

    animateParticles();
  }

  // 5. Typewriter Animation
  const typewriterElem = document.getElementById('typewriter-text');
  if (typewriterElem) {
    const roles = [
      'Backend Developer',
      'Software Engineer',
      'Full Stack Developer',
      'QA Engineer',
      'Co-Founder @ Trix Mart'
    ];

    let roleIdx = 0;
    let charIdx = 0;
    let isDeleting = false;
    let typingSpeed = 100;

    function tick() {
      const currentRole = roles[roleIdx];

      if (isDeleting) {
        typewriterElem.textContent = currentRole.substring(0, charIdx - 1);
        charIdx--;
        typingSpeed = 50;
      } else {
        typewriterElem.textContent = currentRole.substring(0, charIdx + 1);
        charIdx++;
        typingSpeed = 120;
      }

      if (!isDeleting && charIdx === currentRole.length) {
        typingSpeed = 1800; // pause at end
        isDeleting = true;
      } else if (isDeleting && charIdx === 0) {
        isDeleting = false;
        roleIdx = (roleIdx + 1) % roles.length;
        typingSpeed = 400; // pause before typing next
      }

      setTimeout(tick, typingSpeed);
    }

    setTimeout(tick, 600);
  }

  // 6. SPA Routing & Active Nav States
  const sections = {
    home: document.getElementById('view-home'),
    about: document.getElementById('view-about'),
    project: document.getElementById('view-project'),
    resume: document.getElementById('view-resume')
  };

  const navLinksMap = {
    home: document.getElementById('nav-home'),
    about: document.getElementById('nav-about'),
    project: document.getElementById('nav-project'),
    resume: document.getElementById('nav-resume')
  };

  function navigateTo(targetRoute) {
    let cleanRoute = targetRoute.replace(/^#\/?/, '').replace(/^\//, '').toLowerCase();
    if (!cleanRoute || cleanRoute === '' || !sections[cleanRoute]) {
      cleanRoute = 'home';
    }

    // Toggle views
    for (const key in sections) {
      if (sections[key]) {
        if (key === cleanRoute) {
          sections[key].style.display = 'block';
        } else {
          sections[key].style.display = 'none';
        }
      }
    }

    // Update active nav link
    for (const key in navLinksMap) {
      if (navLinksMap[key]) {
        if (key === cleanRoute) {
          navLinksMap[key].classList.add('active');
        } else {
          navLinksMap[key].classList.remove('active');
        }
      }
    }

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'instant' });

    // Update page title
    const titles = {
      home: "Anthony Obinugwu - Portfolio",
      about: "About | Anthony Obinugwu",
      project: "Projects | Anthony Obinugwu",
      resume: "Resume | Anthony Obinugwu"
    };
    document.title = titles[cleanRoute] || "Anthony Obinugwu";
  }

  // Handle Hash Change
  window.addEventListener('hashchange', function () {
    navigateTo(window.location.hash);
  });

  // Handle Initial Route
  let initialPath = window.location.pathname;
  if (initialPath.includes('/about')) {
    navigateTo('about');
  } else if (initialPath.includes('/project')) {
    navigateTo('project');
  } else if (initialPath.includes('/resume')) {
    navigateTo('resume');
  } else if (window.location.hash) {
    navigateTo(window.location.hash);
  } else {
    navigateTo('home');
  }

  // Handle Download CV Button
  window.downloadCV = function (e) {
    if (e) e.preventDefault();
    window.print();
  };

})();
