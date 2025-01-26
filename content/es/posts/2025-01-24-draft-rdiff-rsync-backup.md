---
layout: post
title: 'Cómo resguardar tus datos mediante un backup simple'
description: "Backups mediante una combinación de rdiff-backup y rsync"
draft: true
tags: ['rdiff-backup', 'rsync', backup]
---

El concepto detrás de los respaldos (_backups_) es disponer de una copia segura de nuestros datos, en caso de que algún suceso desafortunado altere o borre información de nuestro sistema de archivos.

En ese sentido, una frase que siempre empleo es **Los backups no sirven para nada, lo que sirve es el restore**.

Los backups se hacen periódicamente, muchas veces mediante algún automatismo: un script, o servicio de backup.  Los operadores están entrenados en realizar backups, y los realizan sin percances.

Muy diferente es la actividad de restore: pocas veces ---cuando las cosas van bien--- se realizan actividades de restauración de datos.