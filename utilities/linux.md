## Comandos Linux mais utilizados

Lista todos os arquivos como "Human Readable Format" (lh) + arquivos ocultos (a) 
```
ls -lha
```

Lista os meus processos em execução
```
ps -a 
```

Lista todos os processos. As opções aux garantem que o ps exiba processos de todos os usuários (a), o nome do usuário responsável pelo processo (u) e também aqueles processos que não estão, necessariamente, sendo executados naquele terminal (x)
```
ps -aux
```

Lista todos os processos. As opções aux garantem que o ps exiba processos de todos os usuários (a), o nome do usuário responsável pelo processo (u) e também aqueles processos que não estão, necessariamente, sendo executados naquele terminal (x). A barra vertical, ou pipe (|), faz com que o resultado seja direcionado para o comando grep que, por sua vez filtrará apenas as linhas que tenham a palavra **hadoop**. A opção -i do comando grep significa **Realiza uma busca pela string ignorando o case, sendo case-insensitive**
```
ps aux | grep -i hadoop
```

Termina o processo especificado em pid
```
kill pid
```

Remove o arquivo especificado em file_name ou o diretório especificado em dir_name
```
rm file_name
rm -r dir_name
```

Exibir o diretório atual
```
pwd
```

Copia arquivo de origem para dest
```
cp origem dest -> copiar arquivo
```

Atribui permissão total no arquivo file.
Tendo em mente que o conceito de binário significa 0 = desligado e 1 = ligado, vejamos como fica na tabela abaixo:

| | rwx |
|-|---  |
|0| 000 |
|1| 001 |
|2| 010 |
|3| 011 |
|4| 100 |
|5| 101 |
|6| 110 |
|7| 111 |
 
Onde "rwx" são as permissões de um arquivo, ou seja:
* r=read (leitura)
* w=write (gravação, alteração, deleção)
* x=execute (execução)

Feito isso, sabemos que um arquivo ou diretório possui 3 modos de permissão. Uma permissão para o DONO do arquivo ou seja, quem o criou, uma outra permissão para o GRUPO do usuário dono do arquivo, e outra permissão para QUALQUER outro usuário ou grupo.

Sabendo disso, temos a tabela final abaixo:

|   |dono |grupo |outros|
|---|-----|------|------|
|   | rwx |  rwx |  rwx |
| 0 | 000 |  000 |  000 |
| 1 | 001 |  001 |  001 |
| 2 | 010 |  010 |  010 |
| 3 | 011 |  011 |  011 |
| 4 | 100 |  100 |  100 |
| 5 | 101 |  101 |  101 |
| 6 | 110 |  110 |  110 |
| 7 | 111 |  111 |  111 |

```
chmod 777 file
```

