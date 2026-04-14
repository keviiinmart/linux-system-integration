Write-Host "=== SYSTEM STATUS CHECK ===" -ForegroundColor Cyan

$scripts = @("system_monitor.py", "log_processor.py", "file_manager.py")

foreach ($script in $scripts) {
	if (Test-Path "scripts/$script"){
		Write-Host "$script found" -ForegroundColor Green
	} else{
		Write-Host "%script MISSING" -ForegroundColor Red
	}
}


Write-Host "Check Complete" -ForegroundColor Cyan
