# PowerShellスクリプト

# 表示メニュー名を設定します
$menuName = "Edit with my Python script"

# レジストリキーのパスを設定します
$registryPath = "HKCR:\*\shell\$menuName"

# レジストリキーを削除します
Remove-Item -Path $registryPath -Recurse
