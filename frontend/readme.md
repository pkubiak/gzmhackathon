ZDANIA - main page
====================

Projekt poświęcony jest witrynie internetowej[**ZDANIA sp. z o.o.**](http://zdania.com.pl/)

Firma ta jest producentem zintegrowanych systemów automatyzacji budynków.

Jest autoryzowanym dostawcą produktów i Know-How dla standardów takich jak LON, DALI oraz producentem urządzeń dla technologii komunikacyjnych LONWORKS, BACnet.

Jest to także Centrum Kompetencji firmy LOYTEC w Polsce. Wspomaga klientów wykorzystujących zaawansowane produkty, zwłaszcza wielofunkcyjne, wieloprotokołowe sterowniki.

Niniejsza dokumentacja ma stanowić podstawę dalszego rozwoju tej witryny.

Wykorzystane technologie
--------------------------------

Strona wykorzystuje projekt [**butio starter pack**](https://gitlab.com/butio/theme-starter-pack), a zatem czerpie z możliwości następujących rozwiązań:
 - NPM ([docs](https://www.npmjs.com/))
 - Gulp JS
 - kompilator SASS (gulp-sass)
 - generator dokumentacji styli (SassDoc)
 - minifikator plików JS / CSS
 - wiele, wiele innych!
 

Wymagania
--------------------------



Struktura plików
--------------

```
assets/
├── css/
│   ├── jquery-ui.css        - http://jqueryui.com
│   ├── slick.css            - Slick-slider
│   └── slick-theme.css      - Theme-specific for slider
├── fonts/                   - Fontawesome files are put here
├── images/                  - Image files are put here
│   ├── background/          - Background images
│   ├── icons/               - Icons are put here
│   ├── social-icons/        - Social icons are put here
├── js/
│   ├── libs/                - Javascript libraries 
│   │   ├── jquery-3.2.1     - The jQuery javascript library v.3.2.1
│   │   ├── jquery-ui.js     - The jQuery UI - v1.12.1
│   │   ├── select2.full.js  - Select2 4.0.3
│   │   └── slick.js         - The slick library Version: 1.8.0
│   ├── src/      
│   │   └── ui-scripts.js    - Javascript specific functions
├── sass/
│   ├── _colors.scss         - Specific colors for page are put here
│   ├── _fonts.scss          - Specific fonts are put here
│   ├── _layout.scss         - Layout of page is put here
│   ├── _mixins.scss         - All mixins are put here
│   ├── _variables.scss      - The variables are put here
│   ├── _links.scss          - Style of links and buttons is defined here
│   └── styles.scss          - Imports of .scss files are put here
dist/
├── maps/
├── jquery-ui.css            - http://jqueryui.com
├── slick.css                - Slick-slider
├── slick-theme.css          - Theme-specific for slider
└── styles.css               - Styles compiled
gulp_tasks/
├── js.js                    
└── sass.js                  
node_modules/
pages/
├── home.php                 - Homepage
└── products.php 
partials/
└── head.php                 - Head part
sassdoc/
├── assets/
│   ├── css/    
│   ├── images/ 
│   ├── js/    
│   └── index.html     
```


Jak zacząć?
---------------



Edycja szablonu HTML
-------------------------------




