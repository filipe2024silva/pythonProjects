@echo off
setlocal enabledelayedexpansion

:: Mensagem do commit
set /p commit_msg=Mensagem do commit: 
if "%commit_msg%"=="" set commit_msg=Atualização do projeto

:: Verifica a branch atual
for /f %%i in ('git rev-parse --abbrev-ref HEAD') do set branch=%%i

:: Puxa alterações do remoto (git pull)
echo 🔄 A obter últimas alterações da branch %branch%...
git pull origin %branch%

:: Adiciona e envia alterações
git add .
git commit -m "%commit_msg%"
git push origin %branch%

echo ✅ Alterações enviadas com sucesso para a branch %branch%
pause

