cp -r %~dp0..\cocotest\src\* %~dp0src
coconut %~dp0src\cocotest\py2_test.coc -s -t2
coconut %~dp0src\cocotest\py3_test.coc -s -t3
rm %~dp0src\cocotest\py2_test.coc
rm %~dp0src\cocotest\py3_test.coc
coconut %~dp0src -s
rm %~dp0src\*.coc
rm %~dp0src\cocotest\*.coc
cp -r %~dp0src\* %~dp0..\cocotest\src
PAUSE
