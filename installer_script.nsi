!include "MUI2.nsh"

!define APP_NAME "AutoCloudfareConnect"
!define APP_EXE "connect_cloudflare.exe"
!define APP_EXE2 "task_scheduler.exe"

Name "${APP_NAME}"
OutFile "${APP_NAME}_Setup.exe"
InstallDir "$PROGRAMFILES\${APP_NAME}"

Section
SetOutPath $INSTDIR
File "dist\${APP_EXE}"
File "dist\${APP_EXE2}"
SectionEnd