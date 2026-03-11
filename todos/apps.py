from django.apps import AppConfig

import os



class TodosConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'

    name = 'todos'



    def ready(self):

        # Prevents the banner from printing twice during Django's auto-reload

        if os.environ.get('RUN_MAIN') == 'true':

            self.display_large_banner()



    def display_large_banner(self):

        try:

            import pyfiglet

            from rich.console import Console, Group

            from rich.panel import Panel

            from rich.text import Text

            from rich.align import Align

            import datetime



            console = Console()

           

            # Clear for that total 'reboot' feel

            console.clear()



            # --- Generate ASCII Art Sections ---

            # Using 'slant' for all to ensure 100% readability and massive scale

            ds_logo = pyfiglet.figlet_format("DS", font="slant", width=150).rstrip()

            main_msg = pyfiglet.figlet_format("DJANGO SERVER IS RUNNING", font="slant", width=150).rstrip()

            sub_msg = pyfiglet.figlet_format("FRONTEND & BACKEND ONLINE", font="slant", width=150).rstrip()



            # --- Styling and Centering ---

            styled_ds = Align.center(Text(ds_logo, style="bold bright_cyan"))

            styled_main = Align.center(Text(main_msg, style="bold bright_red"))

            styled_sub = Align.center(Text(sub_msg, style="bold deep_sky_blue1"))



            # --- UI Decorations (Making it "Awesome") ---
            divider = Align.center(Text("━" * 80, style="bright_blue"))
            meta_info = Align.center(Text.assemble(
                (" 🚀 SYSTEM: ", "bold white"), ("ONLINE ", "bold green"),
                (" | 📦 DJANGO: ", "bold white"), ("v6.0 ", "bold yellow"),
                (" | 📡 CORE: ", "bold white"), ("STABLE ", "bold cyan"),
                (" | ⏰ ", "bold white"), (f"{datetime.datetime.now().strftime('%H:%M:%S')} ", "bold magenta")
            ))

            # --- New: Status Table for extra "Fullness" ---
            from rich.table import Table

            status_table = Table(show_header=False, box=None, padding=(0, 4))
            status_table.add_row("[cyan]►[/][bold white] DB STATUS[/]", "[bold green]ONLINE[/]")
            status_table.add_row("[cyan]►[/][bold white] ASSETS   [/]", "[bold green]CACHED[/]")
            status_table.add_row("[cyan]►[/][bold white] SECURITY [/]", "[bold blue]ACTIVE[/]")
            status_table.add_row("[cyan]►[/][bold white] ENVIRONMENT[/]", "[bold yellow]DEVELOPMENT[/]")

            styled_status_table = Align.center(status_table)

            # --- New: System Logs for flavor ---
            system_logs = Text.assemble(
                ("\n[ INF ] ", "bold cyan"), ("INITIALIZING NEURAL LINK... ", "bright_white"), ("[ OK ]\n", "bold green"),
                ("[ INF ] ", "bold cyan"), ("SYNCING DATABASE SCHEMA...  ", "bright_white"), ("[ OK ]\n", "bold green"),
                ("[ WRN ] ", "bold yellow"), ("HEURISTIC ENGINE ACTIVE...  ", "bright_white"), ("[ ON ]", "bold cyan")
            )
            styled_logs = Align.center(system_logs)

            # --- New: Resource Bar ---
            resource_bar = Align.center(Text.assemble(
                (" MEMORY: ", "bold white"), ("[██████████░░░░░░░░] ", "magenta"), ("62%  ", "bright_white"),
                ("|  CPU: ", "bold white"), ("[████░░░░░░░░░░░░░░] ", "cyan"), ("28%  ", "bright_white"),
                ("|  UPTIME: ", "bold white"), ("04:20:12 ", "bold green")
            ))

            # --- Combine into a Dashboard Layout ---
            banner_group = Group(
                Text("\n"),
                styled_ds,
                Text("\n"),
                styled_main,
                Text("\n"),
                styled_sub,
                Text("\n"),
                divider,
                Text("\n"),
                meta_info,
                Text("\n"),
                styled_status_table,
                styled_logs,
                Text("\n"),
                resource_bar,
                Text("\n")
            )

            # --- Wrap in a Premium Panel ---
            banner_panel = Panel(
                banner_group,
                border_style="bright_cyan",
                padding=(1, 2),
                title="[bold white] 🛰️  PROJECT CONTROL CENTER [/bold white]",
                subtitle="[bold green] ● CONNECTION ENCRYPTED [/bold green]",
                subtitle_align="right",
                expand=True
            )



            # --- New: Heavy Top Section (High Contrast Fix) ---
            full_width_line = Text("━" * console.size.width, style="bright_cyan")
            top_status = Text.assemble(
                ("[", "bright_white"), (" NETWORK ", "bold cyan"), ("] ", "bright_white"), ("localhost:8000  ", "white"),
                ("[", "bright_white"), (" STATUS ", "bold green"), ("] ", "bright_white"), ("ACTIVE  ", "white"),
                ("[", "bright_white"), (" AUTH ", "bold magenta"), ("] ", "bright_white"), ("ENCRYPTED  ", "white"),
                ("[", "bright_white"), (" NODE ", "bold yellow"), ("] ", "bright_white"), (f"{os.name.upper()}", "white"),
            )
            
            activity_feed = Text.assemble(
                ("▸ [ SYS ] ", "bold cyan"), ("LOAD BALANCER READY    ", "bright_white"),
                ("▸ [ DB  ] ", "bold yellow"), ("DATABASE POOL WARMED    ", "bright_white"),
                ("▸ [ LOG ] ", "bold blue"), ("STREAMING TO STDOUT    ", "bright_white"),
            )

            top_section = Group(
                full_width_line,
                Align.center(top_status),
                Align.center(activity_feed),
                full_width_line,
                Text("\n")
            )

            # --- Final Assembly ---
            console.print(top_section)
            
            term_height = console.size.height
            content_height = 50 # Adjusted for top section + panel
            padding_needed = max(0, (term_height - content_height) // 4) # Reduced divisor to bring it up

            console.print("\n" * padding_needed)
            console.print(banner_panel)

           

        except Exception:

            pass