@echo off

@call git add %~dp0\..\langs

@call git commit -m "add lang zips"

if '%ERRORLEVEL%' == '0' (
    echo "Yes, committed"
) else (
    echo "Not committed, check the logs."
)

exit /b 0