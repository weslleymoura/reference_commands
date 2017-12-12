## Comandos Linux mais utilizados

Lista todos os arquivos como "Human Readable Format" (lh) + arquivos ocultos (a) 
```
ls -lha
```

ps -a -> Lista os meus processos em execução
ps -aux -> Lista todos os processos

As opções aux garantem que o ps exiba processos de todos os usuários (a), o nome do usuário responsável pelo processo (u) e também aqueles processos que não estão, necessariamente, sendo executados naquele terminal (x)

kill pid -> Termina o processo especificado em pid
rm file_name -> remove the given file_name
cd -   -> voltar pro diretorio anterior
pwd  -> working directory
echo $SHELL -> Mostra o conteudo da var
echo $PATH  -> Mostra o conteudo da var
cp origem dest -> copiar arquivo
rm -r dir  -> remover diretorio
chmod 777 file
dpkg -l -> Lista pacotes instalados
dpkg -l java -> Lista o pacote com o nome java
dpkg -l | grep pdf -> Lista os pacotes que contem java no nome
Lixux IP 52.54.183.19:8890

cat *.csv > newfile.csv    -> Merge files

head -1 one_file.csv > output.csv   ## writing the header to the final file
tail -n +2  *.csv >> output.csv  ## writing the content of all csv starting with second line into final file
