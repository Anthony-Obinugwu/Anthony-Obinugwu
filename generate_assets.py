import os

os.makedirs("./assets/images/projects", exist_ok=True)

# 1. Logo SVG
logo_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 40" width="120" height="40">
  <defs>
    <linearGradient id="logo-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1db954" />
      <stop offset="100%" stop-color="#15803d" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="1.5" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <text x="5" y="30" font-family="'Raleway', sans-serif" font-weight="900" font-size="32" fill="url(#logo-grad)" filter="url(#glow)">AO<tspan fill="#1db954">.</tspan></text>
</svg>'''

with open("./assets/images/logo.svg", "w") as f:
    f.write(logo_svg)

# 2. Home Main Hero SVG
home_main_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 500" width="100%" height="100%">
  <defs>
    <linearGradient id="purp-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1db954"/>
      <stop offset="100%" stop-color="#0c4a2a"/>
    </linearGradient>
    <linearGradient id="desk-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10301f"/>
      <stop offset="50%" stop-color="#164a2e"/>
      <stop offset="100%" stop-color="#0d2419"/>
    </linearGradient>
    <linearGradient id="screen-glow" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#1db954" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#15803d" stop-opacity="0.2"/>
    </linearGradient>
    <filter id="neon-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Ambient background glow circles -->
  <circle cx="300" cy="240" r="180" fill="#15803d" opacity="0.2" filter="url(#neon-glow)"/>
  <circle cx="360" cy="180" r="90" fill="#1db954" opacity="0.15" filter="url(#neon-glow)"/>

  <!-- Floating Tech Badges / Windows -->
  <!-- Window 1: Code Editor -->
  <g transform="translate(60, 60)" opacity="0.9">
    <rect width="180" height="110" rx="8" fill="#0a1812" stroke="#1db954" stroke-width="1.5"/>
    <circle cx="14" cy="14" r="4" fill="#ff5f56"/>
    <circle cx="26" cy="14" r="4" fill="#ffbd2e"/>
    <circle cx="38" cy="14" r="4" fill="#27c93f"/>
    <!-- Code lines -->
    <rect x="14" y="32" width="70" height="6" rx="3" fill="#1db954" opacity="0.8"/>
    <rect x="90" y="32" width="50" height="6" rx="3" fill="#00d2d3" opacity="0.7"/>
    <rect x="24" y="46" width="110" height="6" rx="3" fill="#ffffff" opacity="0.6"/>
    <rect x="34" y="60" width="80" height="6" rx="3" fill="#1db954" opacity="0.9"/>
    <rect x="34" y="74" width="95" height="6" rx="3" fill="#ff9ff3" opacity="0.7"/>
    <rect x="14" y="88" width="40" height="6" rx="3" fill="#00d2d3" opacity="0.8"/>
  </g>

  <!-- Window 2: Analytics / Cloud -->
  <g transform="translate(380, 70)" opacity="0.9">
    <rect width="160" height="95" rx="8" fill="#0a1812" stroke="#74c69d" stroke-width="1.5"/>
    <circle cx="14" cy="14" r="4" fill="#ff5f56"/>
    <circle cx="26" cy="14" r="4" fill="#ffbd2e"/>
    <circle cx="38" cy="14" r="4" fill="#27c93f"/>
    <!-- Bars -->
    <rect x="25" y="65" width="16" height="18" rx="2" fill="#15803d"/>
    <rect x="48" y="50" width="16" height="33" rx="2" fill="#74c69d"/>
    <rect x="71" y="38" width="16" height="45" rx="2" fill="#1db954"/>
    <rect x="94" y="44" width="16" height="39" rx="2" fill="#00d2d3"/>
    <rect x="117" y="30" width="16" height="53" rx="2" fill="#22c55e"/>
  </g>

  <!-- Floating Symbols -->
  <g fill="#1db954" font-family="monospace" font-weight="bold" font-size="22">
    <text x="70" y="240" opacity="0.7">&lt;/&gt;</text>
    <text x="500" y="220" opacity="0.7">{ }</text>
    <text x="490" y="330" opacity="0.6">( ) =&gt;</text>
    <text x="50" y="340" opacity="0.5">/* AI */</text>
  </g>

  <!-- Desk Surface -->
  <ellipse cx="300" cy="420" rx="270" ry="25" fill="url(#desk-grad)" stroke="#15803d" stroke-width="1"/>
  <rect x="120" y="420" width="360" height="12" rx="4" fill="#0b2015"/>
  <!-- Desk Legs -->
  <rect x="160" y="432" width="12" height="60" fill="#0a1812"/>
  <rect x="428" y="432" width="12" height="60" fill="#0a1812"/>

  <!-- Laptop Setup -->
  <g transform="translate(230, 270)">
    <!-- Laptop screen -->
    <rect x="10" y="10" width="120" height="85" rx="6" fill="#06130c" stroke="#74c69d" stroke-width="2"/>
    <rect x="16" y="16" width="108" height="73" rx="4" fill="url(#screen-glow)"/>
    <!-- Laptop screen content -->
    <circle cx="70" cy="40" r="16" fill="#1db954" opacity="0.4"/>
    <path d="M 64 40 L 76 40 M 70 34 L 70 46" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
    <rect x="30" y="65" width="80" height="4" rx="2" fill="#fff" opacity="0.8"/>
    <rect x="45" y="73" width="50" height="4" rx="2" fill="#1db954"/>
    <!-- Laptop base -->
    <path d="M 0 95 L 140 95 L 128 105 L 12 105 Z" fill="#11301f" stroke="#1db954" stroke-width="1"/>
    <!-- Trackpad -->
    <rect x="58" y="98" width="24" height="5" rx="1" fill="#1a5636"/>
  </g>

  <!-- Developer Character Behind Desk -->
  <!-- Chair Back -->
  <rect x="260" y="210" width="80" height="110" rx="14" fill="#0a1812" stroke="#15803d" stroke-width="2"/>
  <!-- Character Body / Hoodie -->
  <path d="M 250 360 C 250 290, 350 290, 350 360 Z" fill="url(#purp-grad)"/>
  <!-- Collar / Neck -->
  <path d="M 285 285 Q 300 305 315 285" fill="#e0a96d"/>
  <!-- Head -->
  <ellipse cx="300" cy="255" rx="24" ry="28" fill="#f5c290"/>
  <!-- Hair (Modern styled) -->
  <path d="M 275 250 C 275 225, 325 220, 325 245 C 322 235, 305 230, 290 236 C 280 240, 276 245, 275 250 Z" fill="#0a1b12"/>
  <!-- Glasses -->
  <rect x="282" y="250" width="14" height="10" rx="2" fill="none" stroke="#1db954" stroke-width="2"/>
  <rect x="304" y="250" width="14" height="10" rx="2" fill="none" stroke="#1db954" stroke-width="2"/>
  <line x1="296" y1="254" x2="304" y2="254" stroke="#1db954" stroke-width="2"/>
  <!-- Smile -->
  <path d="M 294 270 Q 300 274 306 270" stroke="#8d5b4c" stroke-width="2" fill="none" stroke-linecap="round"/>

  <!-- Coffee Mug with steam -->
  <g transform="translate(180, 385)">
    <rect width="22" height="26" rx="4" fill="#1db954"/>
    <path d="M 22 7 C 28 7, 28 19, 22 19" fill="none" stroke="#1db954" stroke-width="3"/>
    <!-- Steam -->
    <path d="M 6 0 Q 3 -8 7 -14" stroke="#74c69d" stroke-width="1.5" fill="none" stroke-linecap="round" opacity="0.7"/>
    <path d="M 14 -2 Q 18 -9 15 -16" stroke="#74c69d" stroke-width="1.5" fill="none" stroke-linecap="round" opacity="0.7"/>
  </g>

  <!-- Small Plant on Desk -->
  <g transform="translate(395, 375)">
    <!-- Pot -->
    <polygon points="10,40 30,40 35,22 5,22" fill="#1db954" opacity="0.8"/>
    <!-- Leaves -->
    <path d="M 20 22 Q 12 10 10 2" stroke="#27c93f" stroke-width="4" stroke-linecap="round" fill="none"/>
    <path d="M 20 22 Q 28 8 32 3" stroke="#27c93f" stroke-width="4" stroke-linecap="round" fill="none"/>
    <path d="M 20 16 Q 16 8 20 0" stroke="#00d2d3" stroke-width="3" stroke-linecap="round" fill="none"/>
  </g>
</svg>'''

# NOTE: Pic.svg is Anthony's uploaded hero image — do NOT overwrite it.
# The generated placeholder is kept as home-main.svg instead.
with open("./assets/images/home-main.svg", "w") as f:
    f.write(home_main_svg)

# 3. Avatar SVG
avatar_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300" width="100%" height="100%">
  <defs>
    <linearGradient id="bg-avatar" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#15803d"/>
      <stop offset="50%" stop-color="#11301f"/>
      <stop offset="100%" stop-color="#07140d"/>
    </linearGradient>
    <linearGradient id="glow-circle" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1db954"/>
      <stop offset="100%" stop-color="#15803d"/>
    </linearGradient>
    <clipPath id="avatar-clip">
      <circle cx="150" cy="150" r="135"/>
    </clipPath>
  </defs>

  <!-- Outer Glow Circle -->
  <circle cx="150" cy="150" r="140" fill="none" stroke="url(#glow-circle)" stroke-width="5" opacity="0.9"/>
  <circle cx="150" cy="150" r="135" fill="url(#bg-avatar)"/>

  <g clip-path="url(#avatar-clip)">
    <!-- Ambient Stars -->
    <circle cx="60" cy="70" r="2" fill="#fff" opacity="0.6"/>
    <circle cx="230" cy="90" r="2.5" fill="#1db954" opacity="0.8"/>
    <circle cx="80" cy="200" r="1.5" fill="#fff" opacity="0.4"/>
    <circle cx="240" cy="180" r="2" fill="#1db954" opacity="0.5"/>

    <!-- Developer Character Portrait -->
    <!-- Hoodie / Shoulders -->
    <path d="M 50 320 C 50 230, 250 230, 250 320 Z" fill="#11301f"/>
    <!-- Collar details -->
    <path d="M 120 238 L 150 270 L 180 238 Z" fill="#0a1710"/>
    <path d="M 135 220 L 150 248 L 165 220" stroke="#1db954" stroke-width="2" fill="none"/>

    <!-- Neck -->
    <rect x="135" y="190" width="30" height="40" rx="4" fill="#e2a77a"/>

    <!-- Head -->
    <ellipse cx="150" cy="150" rx="46" ry="52" fill="#f4be91"/>

    <!-- Hair -->
    <path d="M 102 145 C 98 100, 140 80, 198 90 C 204 110, 202 135, 198 145 C 190 120, 160 100, 130 110 C 110 116, 105 130, 102 145 Z" fill="#0a1710"/>
    <!-- Side hair / ears -->
    <ellipse cx="103" cy="152" rx="7" ry="10" fill="#f4be91"/>
    <ellipse cx="197" cy="152" rx="7" ry="10" fill="#f4be91"/>

    <!-- Eyebrows -->
    <path d="M 122 132 Q 134 128 142 133" stroke="#0a1710" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M 158 133 Q 166 128 178 132" stroke="#0a1710" stroke-width="3" fill="none" stroke-linecap="round"/>

    <!-- Glasses Frame -->
    <rect x="116" y="137" width="28" height="22" rx="5" fill="#1db954" fill-opacity="0.15" stroke="#1db954" stroke-width="3"/>
    <rect x="156" y="137" width="28" height="22" rx="5" fill="#1db954" fill-opacity="0.15" stroke="#1db954" stroke-width="3"/>
    <line x1="144" y1="148" x2="156" y2="148" stroke="#1db954" stroke-width="3"/>
    <line x1="104" y1="145" x2="116" y2="145" stroke="#1db954" stroke-width="2"/>
    <line x1="184" y1="145" x2="196" y2="145" stroke="#1db954" stroke-width="2"/>

    <!-- Eyes -->
    <circle cx="130" cy="148" r="4.5" fill="#11301f"/>
    <circle cx="170" cy="148" r="4.5" fill="#11301f"/>
    <circle cx="132" cy="146" r="1.5" fill="#fff"/>
    <circle cx="172" cy="146" r="1.5" fill="#fff"/>

    <!-- Nose -->
    <path d="M 150 152 L 148 165 L 153 166" stroke="#d89669" stroke-width="2.5" fill="none" stroke-linecap="round"/>

    <!-- Confident Smile -->
    <path d="M 136 178 Q 150 188 164 178" stroke="#a65942" stroke-width="3" fill="none" stroke-linecap="round"/>
    <!-- Teeth glimmer -->
    <path d="M 140 178 Q 150 184 160 178" fill="#fff" opacity="0.9"/>
  </g>
</svg>'''

with open("./assets/images/avatar.svg", "w") as f:
    f.write(avatar_svg)

# 4. About Illustration SVG
about_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400" width="100%" height="100%">
  <defs>
    <linearGradient id="card-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d2419"/>
      <stop offset="100%" stop-color="#06130c"/>
    </linearGradient>
  </defs>

  <!-- Background Orbit -->
  <circle cx="250" cy="195" r="150" fill="none" stroke="#15803d" stroke-width="1.5" stroke-dasharray="6,8" opacity="0.6"/>
  <circle cx="250" cy="195" r="178" fill="none" stroke="#1db954" stroke-width="1" stroke-dasharray="4,12" opacity="0.4"/>

  <!-- Central Workstation Card -->
  <rect x="45" y="60" width="410" height="215" rx="16" fill="url(#card-grad)" stroke="#1db954" stroke-width="2"/>
  <!-- Top bar -->
  <rect x="45" y="60" width="410" height="30" rx="16" fill="#11301f"/>
  <circle cx="65" cy="75" r="5" fill="#ff5f56"/>
  <circle cx="80" cy="75" r="5" fill="#ffbd2e"/>
  <circle cx="95" cy="75" r="5" fill="#27c93f"/>
  <text x="250" y="80" fill="#74c69d" font-family="sans-serif" font-size="12" text-anchor="middle">anthony@activedge: ~</text>

  <!-- Terminal Content inside Card -->
  <g font-family="monospace" font-size="12.5" fill="#fff">
    <text x="62" y="120"><tspan fill="#1db954">$</tspan> cat anthony.json</text>
    <text x="62" y="144" fill="#00d2d3">"role": "Backend Developer",</text>
    <text x="62" y="166" fill="#56d98a">"stack": ["React", "Node.js", "PostgreSQL"],</text>
    <text x="62" y="188" fill="#8be0a9">"passion": ["Basketball", "Development"],</text>
    <text x="62" y="210" fill="#1dd1a1">"status": "Open to opportunities"</text>
    <text x="62" y="240"><tspan fill="#1db954">$</tspan> <tspan fill="#fff" opacity="0.8">_</tspan></text>
  </g>

  <!-- Floating Badges -->
  <!-- Badge 1: University / Major -->
  <g transform="translate(30, 298)">
    <rect width="160" height="54" rx="10" fill="#08160f" stroke="#74c69d" stroke-width="1.5"/>
    <text x="15" y="24" fill="#1db954" font-family="sans-serif" font-weight="bold" font-size="12">Nile University</text>
    <text x="15" y="42" fill="#bbb" font-family="sans-serif" font-size="10">B.Sc. Computer Science</text>
  </g>

  <!-- Badge 2: Organization role -->
  <g transform="translate(310, 298)">
    <rect width="160" height="54" rx="10" fill="#08160f" stroke="#74c69d" stroke-width="1.5"/>
    <text x="15" y="24" fill="#1db954" font-family="sans-serif" font-weight="bold" font-size="12">COO / Co-Founder</text>
    <text x="15" y="42" fill="#bbb" font-family="sans-serif" font-size="10">Trix Mart</text>
  </g>

  <!-- Badge 3: City, Country -->
  <g transform="translate(170, 362)">
    <rect width="160" height="32" rx="10" fill="#08160f" stroke="#1db954" stroke-width="1.5"/>
    <text x="80" y="21" fill="#fff" font-family="sans-serif" font-weight="bold" font-size="12" text-anchor="middle">Lagos, Nigeria</text>
  </g>
</svg>'''

with open("./assets/images/about.svg", "w") as f:
    f.write(about_svg)

# 5. Project Preview SVG Generator
def make_project_svg(filename, title, subtitle, icon, color1, color2):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 280" width="100%" height="100%">
  <defs>
    <linearGradient id="bg-{filename}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{color1}"/>
      <stop offset="100%" stop-color="{color2}"/>
    </linearGradient>
    <filter id="p-glow">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="500" height="280" fill="url(#bg-{filename})"/>
  <!-- UI Grid overlay -->
  <circle cx="250" cy="110" r="70" fill="rgba(255,255,255,0.06)"/>
  <circle cx="250" cy="110" r="50" fill="rgba(255,255,255,0.1)"/>

  <!-- Icon / Emoji -->
  <text x="250" y="125" font-size="48" text-anchor="middle" filter="url(#p-glow)">{icon}</text>

  <!-- Text -->
  <rect x="40" y="195" width="420" height="65" rx="8" fill="rgba(5, 16, 10, 0.75)" stroke="rgba(29, 185, 84, 0.4)" stroke-width="1"/>
  <text x="250" y="222" font-family="'Raleway', sans-serif" font-weight="bold" font-size="18" fill="#ffffff" text-anchor="middle">{title}</text>
  <text x="250" y="245" font-family="sans-serif" font-size="12" fill="#22c55e" text-anchor="middle">{subtitle}</text>
</svg>'''
    with open(f"./assets/images/projects/{filename}.svg", "w") as pf:
        pf.write(svg)

make_project_svg("trixmart", "Trix Mart", "University Commerce, Reimagined", "🛒", "#0c4a2a", "#05140c")
make_project_svg("artisian", "Artisian", "Discover Trusted Service Providers", "🔍", "#144439", "#0e2024")
make_project_svg("repricer", "TdotWheels Repricer", "Automated Competitive Pricing", "💰", "#4a1c5e", "#1b0d2d")

print("All SVGs created successfully!")
