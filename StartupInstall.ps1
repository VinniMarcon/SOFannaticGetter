
"@echo off" | Out-File -FilePath .\FanaticStartup.bat -enc ascii

"start pythonw .\FanaticGetter.pyw" | Out-File -FilePath .\FanaticStartup.bat -Append -enc ascii

"close" | Out-File -FilePath .\FanaticStartup.bat -Append -enc ascii


$mypath = $PSScriptRoot

$StartupPath = "$env:appdata\Microsoft\Windows\Start Menu\Programs\Startup"

$WshShell = New-Object -comObject WScript.Shell

$Shortcut = $WshShell.CreateShortcut("$StartupPath\FanaticStartup.lnk")

$Shortcut.TargetPath = "$mypath\FanaticStartup.bat"

$Shortcut.WorkingDirectory = "$mypath"

$Shortcut.Save()


Write-Output "Inicializador instalado com sucesso!"
Write-Output ""
Write-Output "Arquivo de Inicializacao criado: FanaticStartup.bat"
Write-Output ""
Write-Output "Atalho criado em: $StartupPath\FanaticStartup.lnk"
Write-Output ""

Write-Output "Mantenha todos os arquivos no mesmo diretorio. Caso mude os arquivos para outro lugar, execute esse arquivo novamente."
Write-Output ""

CMD /c PAUSE