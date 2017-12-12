## Instalação do Java 8

### Pré requisitos e comentários
* Procedimento realizado no Linux CentOS
* Verifique a versão que você quer instalar (este procedimento refere-se à versão Java 8)

### Instalação

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
