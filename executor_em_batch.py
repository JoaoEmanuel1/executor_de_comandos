import psycopg2
import time
import os
from tqdm import tqdm #Opcional para a barra de tarefas

def executar_updates_de_arquivo():

    # configuracões de conexão 
    DB_CONFIG = {
        'dbname': 'nome_do_banco',
        'user': 'postgres',
        'password': 'sua_senha',
        'host': 'seu_host',
        'port': '5432'
    }
    
    # caminho do arquivo que contenha os comandos a serem executados
    ARQUIVO_COMANDOS = r'seu\caminho\teste\comando.txt'
    
    try:
        start_time = time.time()
        
        # conectar ao banco de dados
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        if not os.path.exists(ARQUIVO_COMANDOS):
            raise FileNotFoundError(f"Arquivo {ARQUIVO_COMANDOS} não encontrado")
        
        print("Contando número de comandos...")

        # contar o número total de linhas
        with open(ARQUIVO_COMANDOS, 'r', encoding='utf-8') as f:
            total_comandos = sum(1 for line in f if line.strip())
        
        print(f"Total de comandos a executar: {total_comandos:,}")
        
        BATCH_SIZE = 1000  # número de comandos por lote
        contador = 0
        batch = []
        erros = 0
        
        print("Iniciando execução dos comandos...")

        with open(ARQUIVO_COMANDOS, 'r', encoding='utf-8') as f:

            for linha in tqdm(f, total=total_comandos, desc="Executando UPDATEs"):
                linha = linha.strip()
                if linha:
                    batch.append(linha)
                    contador += 1
                    
                    # executar quando atingir o tamanho do batch
                    if len(batch) >= BATCH_SIZE:
                        try:
                            # executar todos os comandos do batch
                            for comando in batch:
                                cur.execute(comando)
                            conn.commit()
                            batch = []
                        except Exception as e:
                            erros += 1
                            conn.rollback()
            
                            for cmd in batch:
                                try:
                                    cur.execute(cmd)
                                    conn.commit()
                                except Exception as e:
                                    print(f"\nErro no comando: {cmd[:100]}...")
                                    print(f"Erro detalhado: {str(e)}")
                            batch = []
            
            if batch:
                try:
                    for comando in batch:
                        cur.execute(comando)
                    conn.commit()
                except Exception as e:
                    erros += 1
                    print(f"\nErro no último batch: {str(e)}")
                    conn.rollback()
        
        tempo_execucao = time.time() - start_time
        print("\n" + "="*50)
        print(f"PROCESSO CONCLUÍDO")
        print(f"Total de comandos processados: {contador:,}")
        print(f"Comandos com erro: {erros}")
        print(f"Tempo total de execução: {tempo_execucao:.2f} segundos")
        print(f"Velocidade média: {contador/tempo_execucao:.2f} comandos/segundo")
        print("="*50)
        
    except Exception as e:
        print(f"ERRO GRAVE durante o processo: {str(e)}")
        if 'conn' in locals():
            conn.rollback()
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    executar_updates_de_arquivo()