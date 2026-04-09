# [Comia's](https://comias-home.onrender.com/) - Arquitectura de Software 2024

<img style="width: 40%; height: auto;" alt="image" src="https://github.com/user-attachments/assets/0a260bff-9336-41ee-8bdb-d428eb5c7e39" /> <img style="width: 10%; height: auto;" alt="image" src="https://github.com/user-attachments/assets/6b74b874-fe94-4b75-86c6-d5c6bec34fff" />



## Contexto y Evolución del Proyecto

Este proyecto es una implementación avanzada de una arquitectura de microservicios diseñada para la gestión integral de un restaurante. Desarrollado en el marco de la asignatura **Arquitectura de Software (2024)** de la **Universidad de Bogotá Jorge Tadeo Lozano**, el sistema integra patrones modernos de desarrollo, principios de DevOps y una infraestructura resiliente basada en la contenerización. se realizó una intervención técnica para migrar la lógica de consumo hacia una infraestructura en **Vercel** y el despliegue de microservicios en **Render**. Esta transición no solo mantuvo la operatividad, sino que permitió optimizar los tiempos de respuesta y la disponibilidad del servicio.

El enfoque central es demostrar el **desacoplamiento total de responsabilidades** mediante el uso de microservicios independientes, garantizando que fallos en un componente no comprometan la totalidad del sistema.

<!-- PONER AQUÍ UNA IMAGEN O CAPTURA DE LA LANDING PAGE DESPLEGADA EN RENDER -->

---

## Arquitectura y Patrones de Diseño

La solución se fundamenta en un ecosistema de cuatro microservicios que operan en una red virtualizada aislada (`restaurant-network`):

1.  **Home (Gateway & Proxy):** Implementa el patrón **Reverse Proxy**. Centraliza el tráfico y redirige peticiones de forma dinámica a los servicios internos, abstrayendo la complejidad de la infraestructura al cliente final.
<img width="1904" height="902" alt="image" src="https://github.com/user-attachments/assets/6811f5f8-ccc4-4de6-87f5-44c768e3614b" />

2.  **Inventario:** Servicio especializado en la gestión de stock. Implementa lógica de reabastecimiento automático mediante integraciones externas con la API Marketplace.
<img width="1905" height="905" alt="image" src="https://github.com/user-attachments/assets/fc969b09-164f-4a17-9e66-157160f74dcc" />

3.  **Cocina:** Orquestador de pedidos que interactúa en tiempo real con el inventario para validar la viabilidad de las recetas.
<img width="1906" height="904" alt="image" src="https://github.com/user-attachments/assets/ff75a838-767a-4589-9487-93b74ec99d64" />

4.  **Historial:** Componente de auditoría y persistencia de eventos para el seguimiento de transacciones.
<img width="1902" height="903" alt="image" src="https://github.com/user-attachments/assets/ef927ffe-c1c8-4104-bcfd-134fde7ab7db" />


### Diagrama de Comunicación e Infraestructura

```mermaid
graph TD
    User((Usuario)) --> Home[Microservicio: Home]
    Home -->|Proxy Inverso| Inventario[Microservicio: Inventario]
    Home -->|Proxy Inverso| Cocina[Microservicio: Cocina]
    Home -->|Proxy Inverso| Historial[Microservicio: Historial]
    Inventario -->|Persistencia| DB[(PostgreSQL)]
    Cocina -->|Transacción| DB
    Historial -->|Auditoría| DB
    Inventario -.->|REST API| UTadeoAPI(API Marketplace - Vercel)
```

<!-- PONER AQUÍ UN DIAGRAMA MÁS DETALLADO DE LA BASE DE DATOS O RELACIONES DE SERVICIOS -->

---

## DevOps e Integración Continua (CI)

El proyecto adopta una mentalidad de **DevOps** para asegurar que cada cambio en el código sea estable y escalable:

*   **GitHub Actions (CI Workflow):** Ubicado en `.github/workflows/ci.yml`, el pipeline automatizado ejecuta:
    *   **Linting:** Validación estricta de código Python utilizando `flake8` para mantener estándares de calidad y legibilidad.
    *   **Automated Builds:** Verificación de la integridad de las imágenes de Docker para cada microservicio en cada `push` a la rama principal.
*   **Gestión de Infraestructura:** Uso de **Docker Compose** para definir y correr aplicaciones multi-contenedor, incluyendo:
    *   **Aislamiento de Red:** Los servicios se comunican internamente sin exponer puertos innecesarios, mejorando la seguridad.
    *   **Healthchecks:** Monitoreo activo de la salud de cada servicio para asegurar que el tráfico solo se dirija a instancias operativas.
    *   **Límites de Recursos:** Configuración de cuotas de CPU y Memoria (256MB/0.50 CPU) para simular un entorno de producción optimizado.

---

## Tecnologías y Herramientas

*   **Frontend:** HTML5, CSS3, JavaScript (JQuery), Bootstrap.
*   **Backend:** Python 3.x con el framework Flask.
*   **Persistencia:** PostgreSQL como motor de base de datos relacional.
*   **Contenerización:** Docker para el empaquetado y aislamiento de dependencias.
*   **Cloud & Networking:** Integraciones con Vercel API y despliegue distribuido.

<!-- PONER AQUÍ UNA CAPTURA DE PANTALLA DE LA TERMINAL CORRIENDO LOS CONTENEDORES CON 'docker compose ps' -->

---


