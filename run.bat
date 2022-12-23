@echo off
TITLE Pyger Batch Script File

@REM HELP
cls
if "%1" == "help" set true=1
if "%1" == "" set true=1
if defined true (
    echo Usage: run [delete^|docs^|freeze^|test^|main] [open]
    echo.
    echo 'test' - upload to test-pypi
    echo 'main' - upload to pypi
    echo 'docs' - only update docs
    echo 'delete' - only delete folders
    exit /b 0
)

@REM DELETE
echo [Deleting Unnecessary Folders]
set folder='dist'
rmdir dist /q/s && (
  echo Deleted %folder%
) || (
  echo Cannot found %folder%
)
set folder2='Pyger.egg-info'
rmdir Pyger.egg-info /q/s && (
  echo Deleted %folder2%
) || (
  echo Cannot found %folder2%
)
set folder3='docs/_build'
rmdir "docs/_build" /q/s && (
  echo Deleted %folder3%
) || (
  echo Cannot found %folder3%
)
if "%1" == "delete" exit /b 0
echo.

@REM DIST
echo [Creating Distribution Files]
python setup.py sdist
if "%1" == "dist" exit /b 0
echo.

@REM FREEZE
echo [Freezing Requirements]
pip freeze > frozen-requirements.txt
if "%1" == "freeze" exit /b 0
echo.

@REM TEST/MAIN

if "%1" == "test" goto :test
if "%1" == "main" goto :main
if "%1" == "docs" goto :docs

:test
echo [Upload to TestPyPI]
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
if "%2" == "open" start https://test.pypi.org/project/pyger
echo.
echo [All Done]
exit /b 0

:docs
echo [Deploying Docs]
call mkdocs gh-deploy -m "Deployed {sha} with MkDocs version: {version}"
if "%2" == "open" start https://pyger.codes/
if "%1" == "docs" exit /b 0
echo.
echo [All Done]
exit /b 0

:main
echo [Upload to PyPI]
twine upload dist/*
if "%2" == "open" start https://pypi.org/project/pyger
echo.
echo [All Done]
exit /b 0

@REM To-Do : Create command-line tool using Python/GoLang instead
