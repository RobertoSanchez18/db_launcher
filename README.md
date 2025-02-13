# 🚀 Docker DB Launcher

Un script en Python para iniciar contenedores de **MySQL, SQL Server y PostgreSQL** en Docker de forma interactiva y amigable.

## 📌 Características
✅ Menú interactivo con flechas para seleccionar la base de datos.
✅ Soporte para **MySQL, SQL Server y PostgreSQL**.
✅ Mensajes amigables y barra de progreso con `rich`.
✅ Creación automática de contenedores Docker.
✅ Configuración rápida y sin complicaciones.

---

## 🛠️ Instalación y Uso

### 🔹 1. Clonar el Repositorio
```sh
git clone https://github.com/tu-usuario/docker-db-launcher.git
cd docker-db-launcher
```

### 🔹 2. Instalar Dependencias
```sh
pip install -r requirements.txt
```

### 🔹 3. Ejecutar el Script
```sh
python db_launcher.py
```

### 🔹 4. Seleccionar Base de Datos
Usa **↑ y ↓** para moverte y **Enter** para seleccionar.
```sh
📌 Selecciona la base de datos a ejecutar:
  ○ MySQL
  ● SQL Server ✅ (Seleccionado)
  ○ PostgreSQL
```

---

## ⚙️ Configuración de Contenedores

| Base de Datos  | Imagen Docker | Puerto | Variables de Entorno |
|---------------|--------------|--------|----------------------|
| **MySQL** | `mysql:latest` | 3306 | `MYSQL_ROOT_PASSWORD=TuPassword123!` `MYSQL_DATABASE=mi_bd` |
| **SQL Server** | `mcr.microsoft.com/mssql/server:latest` | 1433 | `ACCEPT_EULA=Y` `MSSQL_SA_PASSWORD=TuPassword123!` |
| **PostgreSQL** | `postgres:latest` | 5432 | `POSTGRES_PASSWORD=TuPassword123!` `POSTGRES_DB=mi_bd` |

---

## 🛑 Detener y Eliminar Contenedores
Para detener y eliminar un contenedor:
```sh
docker stop sqlserver mysqlserver postgresdb
docker rm sqlserver mysqlserver postgresdb
```

---

## 📜 Licencia
Este proyecto está bajo la **Licencia MIT**.

📌 **Autor:** [RobertoSanchez18](https://github.com/tu-usuario)

