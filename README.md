# ⚡ Projeto Django — Views Síncronas e Assíncronas

Este projeto demonstra como criar **views síncronas** e **assíncronas** no Django 5, utilizando o servidor **Uvicorn (ASGI)** para suportar chamadas `async/await`.

---

## 🧩 Requisitos

Certifique-se de ter o **Python 3.11+** instalado.

As dependências principais estão no arquivo `requirements.txt`, incluindo:

- **Django 5.2.7**
- **httpx** (requisições assíncronas)
- **requests** (requisições síncronas)
- **uvicorn** (servidor ASGI)
- Outras libs auxiliares (`asgiref`, `anyio`, etc.)

---

## 🚀 Como iniciar o projeto

### 1️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv env
```

No **Windows (PowerShell)**:

```bash
.\env\Scripts\activate
```

No **Linux/macOS**:

```bash
source env/bin/activate
```

---

### 2️⃣ Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Rodar o servidor com Uvicorn

```bash
uvicorn --reload core.asgi:application
```

O servidor será iniciado em:

```
http://127.0.0.1:8000
```

---

## ⚙️ Estrutura principal do projeto

```
async-views/
│
├── core/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🧠 Endpoints disponíveis

| Rota          | Tipo      | Descrição                                   |
| ------------- | --------- | ------------------------------------------- |
| `/api/async/` | **Async** | Executa uma view assíncrona usando `httpx`  |
| `/api/sync/`  | **Sync**  | Executa uma view síncrona usando `requests` |

---

## 🧩 Exemplo de execução

### View Assíncrona (`/api/async/`)

- Executa com `await` e não bloqueia o event loop.
- Ideal para operações paralelas, chamadas externas ou I/O.

### View Síncrona (`/api/sync/`)

- Executa passo a passo, bloqueando o fluxo até finalizar.
- Simula o comportamento tradicional do Django (WSGI).

---

## 🧰 Tecnologias utilizadas

- 🐍 **Python 3.13**
- 🌐 **Django 5.2**
- ⚡ **Uvicorn (ASGI Server)**
- 🔄 **httpx** e **requests**

---

📘 **Autor:** _Renato Luiz_  
💻 **Tecnologia:** Django + Git + GitHub  
📅 **Atualizado:** Outubro de 2025
