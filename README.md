# Detecção de extintores de incêndio

## Introdução

### Identificação 
* Adriando de Arruda Pereira Filho - 20220025597. 
* Colocar o link para o vídeo da apresentação do trabalho. 

### Informações Gerais 
* Descrever o problema.

Identificar extintores de incêndio é uma atividade essencial para a segurança em diferentes ambientes e locais públicos. O fácil acesso a esses dispositivos de segurança é indispensável para garantir a segurança pública em casos de incêndios, e deve estar de acordo com as normas de segurança.

Este projeto tem como objetivo criar um sistema que identifique e reconheça extintores de incêndio utilizando o modelo de detecção de objetos conhecido como [YOLO](https://docs.ultralytics.com/pt) (You Only Look Once). A tarefa envolve o treinamento de um modelo capaz de identificar e localizar extintores em vídeos ou imagens, com o intuito de facilitar a verificação da presença desses dispositivos em locais críticos.

* Descrever a base de dados.

Para o treinamento do modelo de detecção de extintores de incêndio, foram utilizados dois datasets já existentes da plataforma [Roboflow](https://roboflow.com/) que fornecem imagens anotadas para a detecção de extintores em diferentes cenários.

1. [Extinguisher Computer Vision Project](https://universe.roboflow.com/project-9mb4j/extinguisher-cl4yq-ynvpd/dataset/1)
* Quantidade de imagens: 5529
* Anotações: As imagens estão anotadas com caixas delimitadoras e a classe “fire_extinguisher”.
<div style="display: flex; justify-content: space-around;">
  <img src="https://github.com/user-attachments/assets/00611911-e3a5-4af1-b422-aad826382feb" width="300" />
  <img src="https://github.com/user-attachments/assets/3e3c520d-2032-4d1f-9078-1153f59abb65" width="300" />
</div>


2. [Fire Extinguisher Detect Computer Vision Project](https://universe.roboflow.com/fire-extinguisher-detect-ddy5c/fire-extinguisher-detect)
* Quantidade de imagens: 9636
* Anotações: As imagens estão anotadas com caixas delimitadoras e a classe “fire_extinguisher”.

## Metodologia 
* Explicar quais técnicas de _machine learning_ (ML) que você está trabalhando. 
* Explicar as etapas do treinamento e teste. 
* Caso tenha selecionado atributos, explicar a motivação para a seleção de tais atributos. 

## Códigos 
* Mostrar trechos de códigos mais importantes e explicações.  
* Informar o link para acessar o código. 

## Experimentos 
* Descrever em detalhes os tipos de testes executados. 
* Descrever os parâmentros avaliados. 
* Explicar os resultados. 

## Conclusão 
* O trabalho atendeu aos objetivos? 
![val_batch2_pred](https://github.com/user-attachments/assets/00611911-e3a5-4af1-b422-aad826382feb)
![val_batch2_labels](https://github.com/user-attachments/assets/3e3c520d-2032-4d1f-9078-1153f59abb65)
![val_batch1_pred](https://github.com/user-attachments/assets/19ed1f81-50c4-48e4-8855-72b593449f11)
![val_batch1_labels](https://github.com/user-attachments/assets/3a3209b3-9d27-4814-9d74-5c36696a978f)
![val_batch0_pred](https://github.com/user-attachments/assets/449efb09-31bd-4620-8684-d2d8d786f2ce)
![val_batch0_labels](https://github.com/user-attachments/assets/08dde33d-b293-4cc2-bc89-b281b32b4277)
![train_batch4222](https://github.com/user-attachments/assets/3fb7d263-38e9-4cf5-969e-bdbb853820ba)
![train_batch4221](https://github.com/user-attachments/assets/ec52a242-8086-46ca-ae29-38f201a5f128)
![train_batch4220](https://github.com/user-attachments/assets/d6d52300-b657-48e7-8d09-3d0856df5107)
![train_batch2](https://github.com/user-attachments/assets/7d3d13f7-22f2-48c1-a9ed-215e17c8ac76)
![train_batch1](https://github.com/user-attachments/assets/8f359e40-2ccc-4a55-b573-29388cd8fc0d)
![train_batch0](https://github.com/user-attachments/assets/13096070-9ece-4d4e-a8b8-cba26811fcea)
![results](https://github.com/user-attachments/assets/5b71c1f7-4af3-42f5-89ac-cc97d15e8725)
![R_curve](https://github.com/user-attachments/assets/aa9234d0-c5d6-4882-9e4d-3d206b8f319e)
![PR_curve](https://github.com/user-attachments/assets/31178bbb-dbcf-4439-839d-59b4bc9eb4fc)
![P_curve](https://github.com/user-attachments/assets/383ab86a-e220-4348-99f0-ad2854d6c1bc)
![labels_correlogram](https://github.com/user-attachments/assets/1deee6d5-b6cd-4856-ba5d-faabe008b3fa)
![labels](https://github.com/user-attachments/assets/c41f8faf-7284-409b-9ced-15ecdf1de919)
![F1_curve](https://github.com/user-attachments/assets/8d5f781a-57b2-4791-b6d1-83c459a77b4b)
![confusion_matrix_normalized](https://github.com/user-attachments/assets/3be70897-8528-4eaa-8ad3-83bd6999e098)
![confusion_matrix](https://github.com/user-attachments/assets/eaf08e8c-bc0c-4b41-86d4-07ac59263092)
