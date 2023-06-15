# PowerShellスクリプト

# Pythonとスクリプトのパス、表示メニュー名を設定します
$pythonPath = "C:\path\to\python.exe"
$scriptPath = "C:\path\to\your\script.py"
$menuName = "Edit with my Python script"

# シェルコマンドを設定します
$shellCommand = "$pythonPath $scriptPath `"%1`""

# レジストリキーのパスを設定します
$registryPath = "HKCR:\*\shell\$menuName\command"

# レジストリキーを作成し、デフォルト値を設定します
New-Item -Path $registryPath -Force | New-ItemProperty -Name "(Default)" -Value $shellCommand -Force
