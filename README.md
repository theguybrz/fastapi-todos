# 🧠 Projeto FastAPI Todo App

Este projeto foi desenvolvido como um **exemplo prático de criação de uma API RESTful com FastAPI**, demonstrando na prática o uso de boas práticas de desenvolvimento backend, integração com banco de dados relacional e organização de um projeto escalável.

---

## 🚀 Sobre o Projeto

A API implementa um sistema de **gerenciamento de tarefas (To-Do List)** completo, com **CRUD (Create, Read, Update, Delete)**, autenticação via **JWT**, e conexão com banco de dados **SQLite** (podendo facilmente ser adaptada para PostgreSQL, MySQL, etc).  

O objetivo principal foi **construir uma base sólida de API moderna**, com rotas bem estruturadas, organização de módulos e separação entre camadas de dados e regras de negócio — tudo seguindo boas práticas de desenvolvimento backend em Python.  

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.11+**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic**
- **Uvicorn**
- **JWT (Autenticação)**
- **SQLite** (para armazenamento local)

---

## 📂 Estrutura do Projeto

```
📦 fastapi_todo_app
 ┣ 📂 app
 ┃ ┣ 📜 main.py           # Arquivo principal da aplicação
 ┃ ┣ 📜 models.py         # Definições do banco de dados (SQLAlchemy)
 ┃ ┣ 📜 schemas.py        # Schemas de validação (Pydantic)
 ┃ ┣ 📜 crud.py           # Funções de CRUD separadas por responsabilidade
 ┃ ┣ 📜 database.py       # Conexão e configuração do banco
 ┃ ┣ 📜 auth.py           # Módulo de autenticação JWT
 ┃ ┗ 📜 create_db.py      # Script para criar o banco e tabelas
 ┣ 📜 run.py              # Arquivo para iniciar o servidor com Uvicorn
 ┗ 📜 requirements.txt    # Dependências do projeto
```

---

## ▶️ Como Rodar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seuusuario/fastapi-todo-app.git
   cd fastapi-todo-app
   ```

2. **Crie e ative um ambiente virtual (recomendado):**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Crie o banco de dados:**
   ```bash
   python app/create_db.py
   ```

5. **Execute o servidor FastAPI:**
   ```bash
   python run.py
   ```
   Ou:
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Acesse a documentação interativa:**
   👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔒 Recursos Implementados

✅ Autenticação JWT  
✅ Operações CRUD completas  
✅ Conexão com banco relacional (SQLAlchemy)  
✅ Validação de dados com Pydantic  
✅ Documentação automática via Swagger/OpenAPI  
✅ Estrutura modular e escalável  

---

## 💡 O que esse projeto demonstra

Este projeto foi desenvolvido para **demonstrar domínio em construção de APIs modernas com Python**, aplicando boas práticas como:  
- Separação de responsabilidades entre camadas (models, schemas, CRUD e rotas)  
- Uso eficiente do SQLAlchemy ORM  
- Manipulação segura de tokens JWT  
- Estrutura limpa e de fácil manutenção  

---

## 🧩 O que aprendi com este projeto

Durante o desenvolvimento, aprimorei meu entendimento sobre:  
- Criação e organização de APIs RESTful com FastAPI  
- Integração com banco de dados via SQLAlchemy  
- Boas práticas de autenticação e segurança com JWT  
- Estruturação de código limpo e escalável  

---

## 👨‍💻 Autor

**Guylherme Oliveira**  
Analista de Cibersegurança e Dados | Desenvolvedor Backend Python  
🔗 [LinkedIn](https://www.linkedin.com/in/guylhermeoliveira)
