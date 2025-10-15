# Estudo Prático sobre Ransomware e Keylogger com Python

## Visão Geral

Este projeto foi desenvolvido com o objetivo de aprofundar o conhecimento sobre cibersegurança através da análise e simulação de dois tipos de malware muito comuns: **Ransomware** e **Keylogger**. O foco principal é educacional, visando compreender o funcionamento interno dessas ameaças para, assim, desenvolver estratégias de defesa mais eficazes.

**Atenção:** Todas as ferramentas e scripts aqui desenvolvidos devem ser utilizados exclusivamente em ambientes controlados e isolados (como máquinas virtuais) e para fins de estudo. A utilização indevida ou maliciosa destes scripts é ilegal e antiética.

## Objetivos do Projeto

Este estudo tem como metas principais:

- **Compreender o funcionamento prático de Ransomware e Keylogger:** Analisar o ciclo de vida, os métodos de infecção e as ações que esses malwares executam em um sistema comprometido.
- **Identificar vulnerabilidades:** Mapear como falhas de software e, principalmente, brechas humanas (engenharia social) são exploradas para a disseminação dessas ameaças.
- **Desenvolver simulações em Python:** Programar scripts simples que simulam o comportamento de um ransomware (cifrando arquivos em um diretório específico) e de um keylogger (capturando digitações) para fins de aprendizado.
- **Refletir sobre estratégias de defesa:** Com base no conhecimento adquirido, discutir e documentar as melhores práticas de prevenção, detecção e mitigação de ataques de malware.

## Aviso Ético e de Responsabilidade

Este projeto é estritamente para fins acadêmicos e de pesquisa em segurança da informação. Você, como usuário, é o único responsável por suas ações. O autor não se responsabiliza pelo uso indevido das informações e dos códigos aqui presentes.

- **NUNCA** execute estes scripts em um sistema que não seja seu ou sem autorização explícita.
- **SEMPRE** utilize um ambiente controlado e isolado, como uma Máquina Virtual (VM), para evitar danos reais.

## 📁 Estrutura do Projeto

├── ransomware/
│   ├── encryptor.py         # Script que criptografa arquivos
│   └── decryptor.py         # Script para descriptografar os arquivos com a chave correta
├── keylogger/
│   └── keylogger.py         # Script que captura e armazena as teclas digitadas
└── README.md                # Este arquivo



## 🤖 Simulações

### 1. Ransomware
#### **Como funciona?**
- O script `encryptor.py` varre um diretório pré-definido em busca de arquivos com extensões específicas (ex: `.txt`, `.jpg`).
- Para cada arquivo encontrado, ele gera uma chave de criptografia e cifra o conteúdo do arquivo, tornando-o inacessível.
- Uma mensagem de "resgate" é deixada no diretório, explicando o que aconteceu.
- O script `decryptor.py` pode ser usado para reverter o processo, desde que a chave de criptografia correta seja fornecida.

#### **Vulnerabilidades Exploradas**
- **Falta de Backups:** A eficácia do ransomware depende da inexistência de cópias de segurança dos arquivos.
- **Engenharia Social:** A execução do script malicioso geralmente depende de uma ação do usuário, como abrir um anexo de e-mail ou clicar em um link malicioso.

### 2. Keylogger
#### **Como funciona?**
- O script `keylogger.py` utiliza bibliotecas que monitoram eventos de teclado no sistema operacional.
- Cada tecla pressionada é capturada e salva em um arquivo de log.
- Em um ataque real, esse arquivo de log seria enviado secretamente para o atacante.

#### **Vulnerabilidades Exploradas**
- **Falta de Monitoramento de Processos:** Keyloggers rodam em segundo plano e podem passar despercebidos sem um bom antivírus ou EDR.
- **Concessão de Permissões Elevadas:** A instalação de softwares de fontes não confiáveis pode dar ao malware as permissões necessárias para monitorar o sistema.

## Estratégias de Defesa e Prevenção

Compreender o ataque é o primeiro passo para uma boa defesa. Abaixo estão algumas das estratégias mais eficazes:

#### Contra Ransomware
1.  **Backups Regulares:** Mantenha cópias de segurança de seus arquivos importantes em locais separados (regra 3-2-1: 3 cópias, 2 mídias diferentes, 1 cópia off-site).
2.  **Cuidado com Phishing:** Não clique em links ou baixe anexos de e-mails suspeitos ou não solicitados.
3.  **Atualizações de Software:** Mantenha o sistema operacional e todos os programas atualizados para corrigir vulnerabilidades de segurança.
4.  **Princípio do Menor Privilégio:** Utilize contas de usuário sem privilégios de administrador para as tarefas do dia a dia.

#### Contra Keyloggers
1.  **Soluções Antivírus e Anti-Malware:** Mantenha um bom software de segurança ativo e atualizado, capaz de detectar e bloquear keyloggers.
2.  **Firewall:** Utilize um firewall para monitorar e bloquear conexões de rede suspeitas que poderiam ser usadas para enviar os logs.
3.  **Teclados Virtuais:** Para inserir informações sensíveis (como senhas de banco), use teclados virtuais, que dificultam a captura por keyloggers baseados em software.
4.  **Autenticação de Múltiplos Fatores (MFA):** Mesmo que sua senha seja roubada, o MFA adiciona uma camada extra de segurança, impedindo o acesso não autorizado.

## Como Executar as Simulações

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/willamygarcia/ransomware_and_keylogger.git](https://github.com/willamygarcia/ransomware_and_keylogger.git)
    ```
2.  **Configure o ambiente virtual (Recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute os scripts dentro do ambiente controlado.**
