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

Atribui permissão total no arquivo file
```
chmod 777 file
```

