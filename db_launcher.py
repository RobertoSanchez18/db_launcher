import subprocess as sp
import time
import questionary
from rich.console import Console
from rich.progress import Progress

console = Console()


opcion = questionary.select(
    "📌 Selecciona la base de datos a ejecutar:",
    choices=["MySQL", "SQL Server", "PostgreSQL"]
).ask()


def iniciar_contenedor(image, env_vars, ports, container_name):
    console.print(f"[blue]🚀 Iniciando {container_name} en Docker...[/blue]")
    
    with Progress() as progress:
        task = progress.add_task("[bold green]Cargando...", total=100)
        for _ in range(10):
            time.sleep(0.3)
            progress.update(task, advance=10)

    sp.call([
        "docker", "run", "-d", "--name", container_name, "-p", ports,
        *sum([["-e", env] for env in env_vars], []),
        image
    ])

    console.print(f"[green]✅ {container_name} está corriendo en Docker[/green]\n")
    console.print("[bold cyan]🎉 Listo para usar![/bold cyan] 🚀")

# 🔹 SQL SERVER
if opcion == "SQL Server":
    iniciar_contenedor(
        "mcr.microsoft.com/mssql/server:latest",
        ["ACCEPT_EULA=Y", "MSSQL_SA_PASSWORD=TuPassword123!"],
        "1433:1433",
        "sqlserver"
    )

# 🔹 MySQL
elif opcion == "MySQL":
    iniciar_contenedor(
        "mysql:latest",
        ["MYSQL_ROOT_PASSWORD=TuPassword123!", "MYSQL_DATABASE=mi_bd"],
        "3306:3306",
        "mysqlserver"
    )

# 🔹 PostgreSQL
elif opcion == "PostgreSQL":
    iniciar_contenedor(
        "postgres:latest",
        ["POSTGRES_PASSWORD=TuPassword123!", "POSTGRES_DB=mi_bd"],
        "5432:5432",
        "postgresdb"
    )
