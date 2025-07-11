🔄 BatchSQLExecutor  
Ferramenta Python para execução otimizada de comandos SQL em massa (INSERTs e UPDATEs), diretamente a partir de arquivos .txt.

🚀 Visão Geral  
Este projeto foi desenvolvido para resolver um problema recorrente em ambientes de banco de dados com grande volume de atualizações e inserções. Originalmente, o processamento de 500.000 registros levava entre 3 a 6 horas. Com o uso desta ferramenta, esse tempo foi reduzido para 20 a 50 minutos.

📂 Como Funciona  
1. Leitura de Arquivo: o script recebe um arquivo .txt contendo as instruções SQL (ou dados brutos a serem transformados).

2. Processamento em Lote: divide as operações em batches para melhor performance e menor uso de recursos.

3. Execução SQL: realiza os comandos diretamente no banco, utilizando conexões otimizadas.  

  

📈 Resultados
Antes: 3h ~ 6h para 500.000 registros
Depois: 20 ~ 50 minutos

Esse ganho de performance é especialmente relevante em processos periódicos, migrações e cargas de dados pesadas.  

📌 Observações  
Ideal para bancos SQL Server ou PostgreSQL.

Recomendável revisar os dados antes da execução, já que o processo é em lote e pode impactar em massa o banco.

🧑‍💼 Autor  
Desenvolvido por João Emanuel — uso interno na HLH Assessoria e Consultoria.
