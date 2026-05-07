# Week 7 Chrome DevTools Locators 

The purpose of this file is to showcase the use of Chrome DevTools in identifying and documenting stable CSS locators. A locator is stable if it targets what an element is or what it does, which in turn means design changes to the site are unlikely to break it.   
The sections below showcase the locators I found, the sites where they were identified, and a brief explanation for why each was chosen


# Sites
## Site 1 — awwwards.com

a[href="/submit/"] - Targets the "submit" link by where it is exactly. 

a[href="https://obys.agency/"]  - Same reasoning as above, the href attribute is specific to this link

[data-search-target="input"]  - Uses a "data attribute", an attribute that is added by developers intentionally for easy identification, which makes this a very stable locator.

## Site 2 — oakharborwebdesigns.com

#dark-mode-toggle  - A unique ID used to toggle dark mode. 

a[href="/pricing/"]  - Targets the "Pricing" link 

a[href="/"][aria-label="back to home"] - Two attributes were combined to target one element. The "back to home" element alone matched two logos on the page. 

## Site 3 — playwright.dev

a[href="/docs/intro"].navbar__item - The href attribute targets the docs link functionally, while navbar__item narrows it down to only the Docs link on the top of the page. Note: navbar__item does describe position, as such it is considered "fragile" and can change in the future.

a[href="https://github.com/microsoft/playwright"].navbar__link.header-github-link - Contains the link to the playwright github page. the header-github-link class is chained with the navbar__link class to narrow down to one match. 

[aria-label="Search (Ctrl+K)"] - Targets the search bar by name, describing exactly what the locator is for

## Site 4 — the-internet.herokuapp.com

a[href="https://github.com/tourdedave/the-internet"] - Targets the GitHub link. 

a[href="/drag_and_drop"] - Targets the Drag and Drop page clearly.

a[href="/status_codes"] - Targets the Status Codes page clearly. 

## Site 5 — wikipedia.org

#SearchInput - Uses a unique ID, clearly identifiable. 

#searchLanguage - Unique ID. 

[data-jsl10n="search-input-button"] - Uses a data attribute.
