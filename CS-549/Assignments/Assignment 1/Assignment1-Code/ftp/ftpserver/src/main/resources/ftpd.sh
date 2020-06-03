#!/bin/bash
export JARFILE=${server.testdir}/${server.name}.jar
export POLICY=${server.testdir}/server.policy
export CODEBASE=${server.codebase}
export SERVERHOST=${server.machine}

if [ ! -e $JARFILE ] ; then
	echo "Missing jar file: $JARFILE"
	echo "Please assemble the ftpserver jar file."
	exit
fi

if [ ! -e $POLICY ] ; then
	pushd ${server.testdir}
	jar xf "$JARFILE" server.policy
	popd
fi

echo "java -Djava.security.policy=$POLICY -Djava.rmi.server.codebase=$CODEBASE -Djva.rmi.server.hostname=$SERVERHOST -jar $JARFILE $*"
java -Djava.security.policy=$POLICY -Djava.rmi.server.codebase=$CODEBASE -Djava.rmi.server.hostname=$SERVERHOST -jar $JARFILE $*
# mvn exec:java -Dexec.mainClass="edu.stevens.cs.cs549.ftpserver.ServerMain" -Djava.security.policy=$POLICY -Djava.rmi.server.codebase=$CODEBASE