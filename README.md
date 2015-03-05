# scout
Sistemas para a região escoteira do Rio Grande do Sul

Modulos:
- Campotec

# Dependencies


Apps instalados atraves do pip:
 - Pyllow

Apps instalados manualmente:

 - Django-admin-bootstrap: https://github.com/douglasmiranda/django-admin-bootstrap
    Suporta: Django 1.7+, utiliznado o Bootstrap v3

 - Django-bootstrap3: https://github.com/dyve/django-bootstrap3
    Documentation: http://django-bootstrap3.readthedocs.org/en/latest/installation.html
    Suporta: Python 2.6, 2.7, 3.2 ou 3.3 e Django >= 1.4
    Dependências instaladas com pip install ...:
    - Pillow
    - Sphinx
    - sphinx_rtd_theme
    - xlrd
    - xlwt
    - django-debug-toolbar

    Dependências instaladas manualmente:
    - Bootstrap v3.3.2

    CKeditor configurações:
    - http://docs.cksource.com/ckeditor_api/symbols/CKEDITOR.config.html#.autoGrow_onStartup

# Deploy:

  - Executar:
    - python manage.py collectstatic # para mover os arquivos estáticos dos apps e do diretorio /sitestatic para /static
    - Configurar /static para servir arquivos estáticos no apache.
  - OBS: os arquivos setup.py e wsgi.py na raiz do projeto são exclusivos para rodar em ambiente online, em servidor de aplicação.

Diretório dos pacotes zip: /install/

