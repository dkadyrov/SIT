SET JARFILE=${client.testdir}/${client.name}.jar
REM To convert forward slash to back-slash for windows paths
SET "JARFILE=%JARFILE:/=\%"
SET POLICY=${client.testdir}/client.policy
SET "POLICY=%POLICY:/=\%"
SET TESTDIR=${client.testdir}
SET "TESTDIR=%TESTDIR:/=\%"

if NOT EXIST %JARFILE% (
	echo "Missing jar file: %JARFILE%"
	echo "Please assemble the ftpclient jar file."
	exit 1
)

if NOT EXIST %POLICY% (
	pushd %TESTDIR%
	jar xf "%JARFILE%" client.policy
	popd
)

echo "Running client"
echo "java -Djava.security.policy=%POLICY% -jar %JARFILE%"
java -Djava.security.policy=%POLICY% -jar %JARFILE%