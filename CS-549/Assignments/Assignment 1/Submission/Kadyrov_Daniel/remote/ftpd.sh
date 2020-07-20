#!/bin/bash
export JARFILE=/home/ec2-user/tmp/cs549/ftp-test/ftpd.jar
export POLICY=/home/ec2-user/tmp/cs549/ftp-test/server.policy
export CODEBASE=http://ec2-100-25-200-62.compute-1.amazonaws.com/~ec2-user/ftpd.jar
export SERVERHOST=ec2-100-25-200-62.compute-1.amazonaws.com

if [ ! -e $JARFILE ] ; then
	echo "Missing jar file: $JARFILE"
	echo "Please assemble the ftpserver jar file."
	exit
fi

if [ ! -e $POLICY ] ; then
	pushd /home/ec2-user/tmp/cs549/ftp-test
	jar xf "$JARFILE" server.policy
	popd
fi

echo "java -Djava.security.policy=$POLICY -Djava.rmi.server.codebase=$CODEBASE -Djva.rmi.server.hostname=$SERVERHOST -jar $JARFILE $*"
java -Djava.security.policy=$POLICY -Djava.rmi.server.codebase=$CODEBASE -Djava.rmi.server.hostname=$SERVERHOST -jar $JARFILE $*
# mvn exec:java -Dexec.mainClass="edu.stevens.cs.cs549.ftpserver.ServerMain" -Djava.security.policy=$POLICY -Djava.rmi.server.codebase=$CODEBASE