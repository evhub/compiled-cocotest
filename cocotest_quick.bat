cp -r %~dp0..\cocotest\src\* %~dp0src
rm %~dp0src\cocotest\py2_test.*
rm %~dp0src\cocotest\py3_test.*
rm %~dp0src\cocotest\py33_test.*
coconut %~dp0src -s
rm %~dp0src\*.coc
rm %~dp0src\cocotest\*.coc
cp -r %~dp0src\* %~dp0..\cocotest\src
PAUSE
