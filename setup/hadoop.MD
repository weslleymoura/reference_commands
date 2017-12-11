## Instalação do Hadoop modo stand alone com Yarn

Pré-requisitos:
* Instalação do Java

Configuração do servidor
* 2 vcores
* 1GB RAM

### Download e instação inicial

* Primeiramente, crie um usuário hadoop e garanta que ele consiga fazer ssh localhost

* Download
Verifique a última versão disponível em https://hadoop.apache.org/releases.html
```
wget http://www-us.apache.org/dist/hadoop/common/hadoop-2.8.1/hadoop-2.8.1.tar.gz
```

* Extrai os arquivos para um diretório específico (crie o diretório antes se for necessário)
```
sudo tar -zxvf hadoop-2.8.1.tar.gz -C /etc
```

* Cria um link para o diretório de instalação do hadoop (este procedimento pode ser útil em atualizações de versão)
```
ln -s hadoop-2.8.1 hadoop
```

* Configure o arquivo hadoop-env com a localização do $JAVA_HOME
```
sudo vi /etc/hadoop/etc/hadoop/hadoop-env.sh
```

Encontre a linha 
```
export JAVA_HOME=$
```

E troque por
```
export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")
```

* Configure as variáveis de ambiente no arquivo .bashrc
```
export HADOOP_HOME=/etc/hadoop
export HADOOP_PREFIX=$HADOOP_HOME
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HADOOP_TMP_DIR=/home/hadoop/hadoopdata
export HADOOP_LOG_DIR=$HADOOP_TMP_DIR/log
```

* Adiciona PATH do hadoop nas variáveis de ambiente por conveniência
```
echo "export PATH=/etc/hadoop-2.8.1/bin:$PATH" | sudo tee -a /etc/profile
source /etc/profile
```

* Crie os diretorios utilizados nas configuracoes
```
mkdir /home/hadoop/hadoopdata/hdfs/namenode
mkdir /home/hadoop/hadoopdata/hdfs/datanode
mkdir /home/hadoop/hadoopdata/log
```

### Configurações específicas

Acesse o diretório dos arquivos de configuração do Hadoop
```
cd $HADOOP_HOME/etc/hadoop
```

* core-site.xml
```
sudo vi core-site.xml
```

```
<configuration>
<property>
  <name>fs.default.name</name>
    <value>hdfs://localhost:9000</value>
</property>

<property>
  <name>hadoop.security.authentication</name>
    <value>simple</value>
</property>

</configuration>
```

* hdfs-site.xml

```
<configuration>
<property>
 <name>dfs.replication</name>
 <value>1</value>
</property>

<property>
  <name>dfs.name.dir</name>
    <value>file:///home/hadoop/hadoopdata/hdfs/namenode</value>
</property>

<property>
  <name>dfs.data.dir</name>
    <value>file:///home/hadoop/hadoopdata/hdfs/datanode</value>
</property>
</configuration>
```

* mapred-site.xml

```
<configuration>
 <property>
  <name>mapreduce.framework.name</name>
   <value>yarn</value>
 </property>


 <property>
  <name>mapreduce.map.memory.mb</name>
    <value>2048</value>
 </property>

 <property>
  <name>mapreduce.reduce.memory.mb</name>
    <value>4096</value>
 </property>

</configuration>
```

* yarn-site.xml

```
<configuration>
 <property>
  <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
 </property>

 <property>
  <name>yarn.nodemanager.resource.cpu-vcores</name>
    <value>2</value>
 </property>
 <property>
  <name>yarn.nodemanager.resource.memory-mb</name>
    <value>1024</value>
 </property>

 <property>
  <name>yarn.scheduler.maximum-allocation-mb</name>
    <value>512</value>
 </property>
 <property>
  <name>yarn.scheduler.minimum-allocation-mb</name>
    <value>256</value>
 </property>
 <property>
  <name>yarn.scheduler.maximum-allocation-vcores</name>
    <value>2</value>
 </property>
 <property>
  <name>yarn.scheduler.minimum-allocation-vcores</name>
    <value>1</value>
 </property>

</configuration>
```

### Formatação do file system e inicialização dos serviços

* Format HDFS
```
hdfs namenode -format
```

* Iniciar os serviços hds e yarn
```
cd $HADOOP_HOME/sbin/
./start-dfs.sh (starts the namenode and the datanode)
./start-yarn.sh
```

* Accesse Hadoop Services no Browser - http://your_server:50070/
* Informacoes sobre o cluster and todas as aplicacoes - http://your_server:8088/
* Informacoes sobre o datanode - http://your_server:50075/ 

### Referências
https://www.vultr.com/docs/how-to-install-hadoop-in-stand-alone-mode-on-centos-7 

https://tecadmin.net/setup-hadoop-single-node-cluster-on-centos-redhat/


