# Visualisation d'Orientation avec MPU6500 et OpenGL

## Aperçu  
Ce projet permet de visualiser l'orientation d'un cube en 3D en temps réel, en utilisant un capteur **MPU6500** (accéléromètre et gyroscope) connecté à un **ESP32**. Les données sont lues via une communication série et fusionnées à l'aide d'un filtre de complémentarité pour obtenir une estimation précise des angles d'orientation. La visualisation du cube 3D est réalisée avec **Pygame** et **OpenGL**.

### Objectif du projet :
- Lire les données d'orientation en temps réel à partir du **MPU6500**.
- Fusionner ces données avec un **filtre de complémentarité** pour obtenir des angles d'inclinaison plus précis.
- Afficher un **cube 3D** en rotation selon l'orientation mesurée par le capteur.

## Composants utilisés  
- **Microcontrôleur :** ESP32  
- **Capteur de mouvement :** MPU6500 (accéléromètre et gyroscope)  
- **Librairies Python :**
  - `pygame` pour la gestion de la fenêtre graphique  
  - `PyOpenGL` pour le rendu 3D  
  - `pySerial` pour la communication série entre l'ESP32 et l'ordinateur  
- **Cube 3D :** Représentation d'un cube avec une rotation en temps réel en fonction des données du capteur.

## Fonctionnalités  
✔️ **Visualisation en temps réel** d'un cube 3D qui effectue une rotation basée sur l'orientation mesurée par le capteur MPU6500.  
✔️ **Fusion des données de l'accéléromètre et du gyroscope** pour obtenir une estimation fiable des angles d'inclinaison en utilisant un **filtre de complémentarité**.  
✔️ **Rotation autour des trois axes (X, Y, Z)** pour simuler l'orientation réelle du capteur dans l'espace.  
✔️ Affichage des **axes de rotation X, Y, Z** pour un suivi visuel des orientations.

## Fichiers inclus  
📁 **Fichiers du projet** :  
  - **main.py** : Script principal pour lire les données du capteur et afficher le cube.  
  - **README.md** : Ce fichier de documentation.  
  - **Schémas de câblage** (facultatif, si applicable).  
  - **Dépôt des fichiers sources** pour l'ESP32 et le capteur MPU6500.  

## Installation & utilisation  
1. **Cloner le projet** depuis GitHub :  
   ```bash
   git clone https://github.com/votre-utilisateur/nom-du-projet.git
