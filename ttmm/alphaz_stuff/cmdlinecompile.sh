#!/bin/bash

ECLIPSE=/s/chopin/e/proj/AlphaZ/BinTree/eclipse-alphaz-bundle/eclipse/eclipse
SCRIPT=TMMScript.cs
WORKSPACE=./..

${ECLIPSE} -application fr.irisa.r2d2.gecos.framework.compiler -c ${SCRIPT} -data ${WORKSPACE} -noSplash
