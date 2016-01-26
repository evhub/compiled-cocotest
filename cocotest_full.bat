cp -r %~dp0..\cocotest\src\* %~dp0src
rm %~dp0src\cocotest\py2_test.*
coconut %~dp0src -sft3
rm %~dp0src\*.coc
rm %~dp0src\cocotest\*.coc
cp -r %~dp0src\* %~dp0..\cocotest\src
PAUSE
