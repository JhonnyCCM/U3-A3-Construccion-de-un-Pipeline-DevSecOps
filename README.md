# 🧪 U3-A3: Construcción de un Pipeline DevSecOps

Este repositorio contiene la implementación práctica del laboratorio de DevSecOps para la asignatura **Ciclos de Desarrollo de Software Seguro** en la **Universidad Laica Eloy Alfaro de Manabí (ULEAM)**.

## 👥 Integrantes - Grupo 7
- **Castillo Mero Jhonny Cristhian**
- **García Reyes Robert Alejandro**
- **Ortiz García Carlos Luis**

---

## 🎯 Objetivo
Configurar un flujo de Integración Continua (CI) mediante **GitHub Actions** que ejecute automáticamente análisis de código estático (**SAST**) con `Bandit` y análisis de dependencias de terceros (**SCA**) con `Safety`, implementando el criterio de **Build Breaker** para bloquear la integración si se detectan vulnerabilidades de seguridad críticas.

---

## ⚙️ Arquitectura del Pipeline (`.github/workflows/devsecops-pipeline.yml`)
El flujo se activa ante eventos `push` y `pull_request` dirigidos a la rama `main`:
1. **Ambiente:** Contenedor `ubuntu-latest` con Python 3.10.
2. **SAST (Static Application Security Testing):** Ejecución de `bandit -r .` para detección de malas prácticas y secretos expuestos en código fuente.
3. **SCA (Software Composition Analysis):** Ejecución de `safety check -r requirements.txt --full-report` para contrastar dependencias contra la base de datos de vulnerabilidades conocidas (CVEs).
