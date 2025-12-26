# 🎛 Pedaleira Digital para Guitarra em Python

## ⚠️ Aviso de Direitos Autorais
Este projeto é protegido por direitos autorais.  
✅ É permitido o uso **exclusivamente para fins pessoais e educacionais**.  
❌ Para usos comerciais, redistribuição ou integração em produtos, entre em contato com a autora.

---

## 🚀 Visão Geral

Este projeto consiste no desenvolvimento de uma **pedaleira digital para guitarras**, criada em **Python**, com foco educacional e demonstrativo, utilizando **processamento de áudio em tempo real** e **armazenamento de presets em banco de dados**.

A aplicação simula o funcionamento de uma pedaleira física, permitindo ao usuário **aplicar, ativar, desativar, salvar e recuperar efeitos sonoros**, oferecendo uma experiência prática e interativa de manipulação de áudio.

---

## 🎚 Funcionalidades

### 🖥 Interface Intuitiva
- Tela inicial com duas opções:
  - **Acessar Pedaleira:** aplicação imediata de efeitos sonoros
  - **Acessar Efeitos Salvos:** carregamento de configurações previamente armazenadas

### 🎛 Controle de Efeitos em Tempo Real
- **Botão Ligar:** ativa os efeitos selecionados
- **Botão Desligar:** interrompe os efeitos aplicados
- Ajuste dinâmico dos parâmetros dos efeitos

### 💾 Gerenciamento de Presets
- Salvamento das configurações de efeitos no banco de dados
- Associação dos efeitos a uma música específica
- Recuperação automática das configurações salvas

### 🎵 Recuperação de Configurações
- Seleção de músicas através de **ComboBox**
- Botão **Carregar Efeitos** aplica automaticamente os presets salvos
- Atualização visual da pedaleira conforme os efeitos carregados

---

## 🗃 Banco de Dados

- Armazenamento dos presets de efeitos
- Associação entre:
  - Nome da música
  - Parâmetros dos efeitos
- Persistência de dados para reutilização futura

---

## 🛠 Tecnologias Utilizadas

- **Linguagem:** Python  
- **Interface Gráfica:** PyQt / Qt Designer  
- **Processamento de Áudio:** Bibliotecas de áudio do Python  
- **Banco de Dados:** SQLite / MySQL (armazenamento de presets)  
- **Conceitos Aplicados:**  
  - Programação Orientada a Objetos  
  - Processamento de sinais de áudio  
  - Integração interface + back-end  
  - Persistência de dados  

---


