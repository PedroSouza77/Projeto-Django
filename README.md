# 📚 LinkPedia

Sistema web desenvolvido com **Python + Django** para gerenciamento de links através das operações **CRUD (Create, Read, Update e Delete)**, utilizando a metodologia **TDD (Test Driven Development)**.

O projeto foi desenvolvido com foco em **autenticação, testes automatizados e organização de funcionalidades**, permitindo que apenas usuários autenticados possam acessar o sistema.

---

# 📌 Sobre o Projeto

O **LinkPedia** é uma aplicação web que permite cadastrar, listar, atualizar e remover links através de uma interface protegida por login.

O sistema foi desenvolvido durante atividades práticas de **TDD com Django**, aplicando conceitos de desenvolvimento orientado a testes, Fluxo MTV, organização MVC do framework e controle de autenticação.

---

# 🎯 Objetivos do Projeto

- Desenvolver uma aplicação CRUD utilizando Django
- Aplicar autenticação e proteção de rotas
- Utilizar a metodologia **TDD (Test Driven Development)**
- Implementar testes automatizados
- Praticar Organização de código
- Criar interfaces utilizando Bootstrap
- Refatoração de código

---

# 🚀 Funcionalidades

✅ Login com autenticação por email

✅ Logout do sistema

✅ Cadastro de links

✅ Listagem de links cadastrados

✅ Atualização de links

✅ Exclusão de links

✅ Proteção de páginas para usuários autenticados

✅ Testes automatizados

✅ Interface responsiva utilizando Bootstrap

---

# 🧠 Conceitos Aplicados

Durante o desenvolvimento foram utilizados os seguintes conceitos:

### Django

- Models
- Views
- Forms
- Templates
- URL Routing
- Login Required
- Utilização do SuperUser

### TDD (Test Driven Development)

- TestCase
- Testes de templates
- Testes de autenticação
- Testes de CRUD

### Banco de Dados com SQLite3

- Migrações
- ORM do Django
- CRUD

### Front-End

- Bootstrap 5
- HTML5
- CSS3

### Versionamento

- Git
- GitHub

---

# 🏁 Resultado do Projeto

Ao final do desenvolvimento foi entregue um sistema contendo:

✅ Sistema de login e logout

✅ CRUD funcional de links

✅ Separação de telas

✅ Proteção por autenticação

✅ Testes automatizados

✅ Interface estilizada

✅ Estrutura organizada

---

Fluxo do sistema:

```txt
Login
   ↓

Painel de Ações
   ↓

Cadastrar
Listar
Editar
Excluir

   ↓

Logout
```

---

# 📂 Estrutura do Projeto

```txt
linkpedia/

│── core/
│   │── migrations/
│   │── tests/
│   │
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   └── urls.py
│
│── templates/
│   ├── login.html
│   ├── logout.html
│   ├── index.html
│   ├── create.html
│   ├── update.html
│   ├── list.html
│   ├── edit.html
│   └── delete_list.html
│
│── manage.py
│── requirements.txt
└── README.md
```

---

# 🛠 Tecnologias Utilizadas

<div align="center">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="70"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="70"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="70"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="70"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" width="70"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="70"/>

</div>

<br>

<div align="center">

Python • Django Framework • Bootstrap 5 • HTML5 • CSS3 • Git

</div>

---


# Como Executar o Projeto:


## Ambiente Windows

```bash
git clone https://github.com/PedroSouza77/Projeto-Django

cd Pratica_TDD_5/

virtualenv venv

cd venv

cd Scripts

activate.bat

cd ..

cd ..

pip install -r requirements.txt

cd linkpedia/

python manage.py migrate

python manage.py test

coverage run --source='.' manage.py test

coverage html

python manage.py createsuperuser

python manage.py runserver

Acessar Pagina Web: http://127.0.0.1:8000/
```

---

##  Ambiente Linux

```bash
git clone https://github.com/PedroSouza77/Projeto-Django

cd Pratica_TDD_5/

virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt

cd linkpedia/

python manage.py migrate

python manage.py test

coverage run --source='.' manage.py test

coverage html

python manage.py createsuperuser

python manage.py runserver

Acessar Pagina Web: http://127.0.0.1:8000/
```

---

# Autor

Projeto desenvolvido por **Pedro Benevides Souza** como prática acadêmica e aplicação dos conceitos de **Desenvolvimento Web**, **TDD** e **Django Framework** 🚀