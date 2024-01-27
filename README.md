# sparkTraining
spark training 
1. install java 
   1. sudo apt install openjdk-19-jdk
2. set JAVA_HOME 
   1.   javac --version
        ls /usr/lib/jvm
        readlink -f $(which javac) | sed "s:/bin/javac::"
        export JAVA_HOME=/usr/lib/jvm/java-19-openjdk-amd64
        echo $JAVA_HOME
    