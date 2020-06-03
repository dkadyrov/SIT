#!/bin/bash
export JARFILE=${client.testdir}/${client.name}.jar
export POLICY=${client.testdir}/client.policy

if [ ! -e $JARFILE ] ; then
	echo "Missing jar file: $JARFILE"
	echo "Please assemble the ftpclient jar file."
	exit
fi

if [ ! -e $POLICY ] ; then
	pushd ${client.testdir}
	jar xf "$JARFILE" client.policy
	popd
fi

echo "Running client"
<<<<<<< HEAD
echo "java -Djava.security.policy=$POLICY -jar $JARFILE $*"
java -Djava.security.policy=$POLICY -jar $JARFILE $*
=======
echo "java -Djava.security.policy=$POLICY -jar $JARFILE"
java -Djava.security.policy=$POLICY -jar $JARFILE
>>>>>>> 295e9d230e4fb30a0f637417a0dbabdff205c05b
