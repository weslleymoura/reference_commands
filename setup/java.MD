## Instalação do Java 8

* Executa instalação
```
sudo yum install -y java-1.8.0-openjdk
```

* Verifica a versão
```
java -version
```

* Cria a variável de ambiente

```
export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")
```
