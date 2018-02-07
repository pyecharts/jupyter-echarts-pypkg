pip freeze
nosetests --with-coverage --cover-package jupyter_echarts_pypkg --cover-package tests  tests docs/source jupyter_echarts_pypkg && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
