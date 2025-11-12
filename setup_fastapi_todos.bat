@echo off
title FastAPI Todos Setup
color 0A

echo ==============================
echo     FASTAPI TODOS SETUP
echo ==============================
echo.

REM Verifica se o Python está instalado
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado no PATH.
    echo Instale o Python 3.11+ e marque a opção "Add to PATH".
    pause
    exit /b
)

echo ✅ Python encontrado!
python --version
echo.

REM Verifica se o pip existe
python -m pip --version >nul 2>nul
if %errorlevel% neq 0 (
    echo ⚙️ Instalando pip...
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    del get-pip.py
)

echo ✅ pip instalado!
echo.

REM Instala dependências do projeto
echo 📦 Instalando dependências...
python -m pip install --upgrade pip
pip install fastapi[all] sqlalchemy pytest httpx
echo.

REM Cria o banco de dados se não existir
if not exist "todos.db" (
    echo 🧱 Criando banco de dados SQLite...
    python -c "from app.db import init_db; init_db(); print('Banco todos.db criado com sucesso!')"
    echo ✅ Banco criado!
    echo.
) else (
    echo 🧱 Banco de dados todos.db já existe.
    echo.
)

REM Pergunta se quer rodar os testes
set /p run_tests="Deseja rodar os testes antes de iniciar o servidor? (S/N): "
if /I "%run_tests%"=="S" (
    echo 🧪 Executando testes com pytest...
    pytest > test_output.txt
    if %errorlevel% neq 0 (
        echo ❌ Alguns testes falharam! Veja o arquivo test_output.txt para detalhes.
        pause
        exit /b
    )
    echo ✅ Todos os testes passaram com sucesso!
    echo.
)

REM Inicializa o servidor FastAPI
echo 🚀 Iniciando servidor FastAPI...
echo Acesse: http://127.0.0.1:8000/docs
echo.
uvicorn app.main:app --reload
