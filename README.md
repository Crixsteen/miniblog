# Miniblog

### Descrizione
Miniblog è un semplice progetto di blog creato utilizzando Django, il blog include una **homepage**, una **pagina delle destinazioni** 
### Funzionalità principali
- **Homepage**: Una semplice pagina di benvenuto con un'immagine introduttiva e una navigazione di base.
- **Pagina delle destinazioni**: Elenco delle destinazioni di viaggio visitate, facilmente estendibile.
- **Gestione dei post**: Modello di base per i post, con funzionalità per elencare e visualizzare contenuti dinamici.
- **Utilizzo di immagini**: Gestione di file statici (come immagini) attraverso il framework Django.

### Struttura del Progetto
- `blog`: Contiene le app Django principali, come i modelli, le viste e i template.
  - `static/images`: Cartella contenente le immagini utilizzate nel sito.
  - `templates/blog`: Contiene i template HTML per le varie pagine del sito.
    - `home.html`: La homepage del blog.
    - `destinazioni.html`: La pagina delle destinazioni.
    - `post_list.html`: La lista dei post pubblicati.
  - `models.py`: Definisce il modello **Post** usato per gestire i contenuti del blog.
  - `views.py`: Contiene la logica delle viste per le pagine principali (homepage, destinazioni e post).
  - `urls.py`: Configura le rotte per navigare tra le pagine del blog.

### Come eseguire il progetto
1. Clonare il repository:
    ```bash
    git clone https://github.com/Crixsteen/miniblog.git
    cd miniblog
    ```
2. Creare un ambiente virtuale ed installare le dipendenze:
    ```bash
    python -m venv env
    source env/bin/activate (su Windows: .\env\Scripts\activate)
    pip install -r requirements.txt
    ```
3. Avviare il server Django:
    ```bash
    python manage.py runserver
    ```
4. Apri il browser e vai all'indirizzo `http://127.0.0.1:8000/`.

### Requisiti
- **Python 3.x**
- **Django 5.x**

### Funzionalità future
- Aggiunta di autenticazione utenti per la gestione dei post.
- Creazione di una sezione per caricare nuove destinazioni dinamicamente.
- Integrazione con un database più complesso (es. PostgreSQL).
  
### Screenshot
![Homepage](static/images/immagine%20sito.jpg)

### Autore
- Cristina Ferrara
