Push-Location $PSScriptRoot

$env:PYGAME_HIDE_SUPPORT_PROMPT = "1"
poetry run python -m disco

Pop-Location
