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

