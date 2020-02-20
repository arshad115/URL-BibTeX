# URL-BibTex/Bibitem generator

*URL BibTeX/Bibitem Generator for LaTex*

This project uses python flask to extract information about author and title
using the URL and then formats a citation for that article for use
with BibTeX along with Bibitem.

## Things that happen when you click the button

1. The URL is sent to the flask micro api through an ajax request.
2. Url content is fetched.
3. The details for the title and author are retrieved.
4. The BibTeX, Bibitem and HTML representations for the citation are updated.

## Bundled dependencies

This project uses:

 * Twitter Bootstrap
 * jQuery
 * Python Flask
 
## Developer

Arshad Mehmood 2020. https://arshadmehmood.com