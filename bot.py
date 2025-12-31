import os
import discord
import asyncio
import logging
from discord.ext import commands
from dotenv import load_dotenv
from colorama import init, Fore, Style
import aioconsole

init(autoreset=True)

# Configuração de Logs
logging.basicConfig(
    level=logging.INFO,
    format=f'{Fore.CYAN}[%(asctime)s]{Style.RESET_ALL} {Fore.WHITE}[%(levelname)s]{Style.RESET_ALL} %(message)s',
    datefmt='%H:%M:%S'
)
log = logging.getLogger("ZEN_BOT")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

def print_banner():
    banner = r"""
_____________________ _______    
\____    /\_    _____/ \      \  
  /     /  |    __)_  /    |   \ 
 /     /_  |        \/     |     \
/_______ \/_______  /\____|__   /
        \/        \/         \/  
    """
    print(Fore.YELLOW + banner + Style.RESET_ALL)
    print(f"{Fore.YELLOW}ZEN - Minecraft Solutions System v1.4 (Auto-Loader){Style.RESET_ALL}")
    print(f"{Fore.CYAN}Desenvolvido por zen studios - https://dsc.gg/zenstudios{Style.RESET_ALL}")
    print("-" * 40)

async def load_extensions():
    if not os.path.exists('./cogs'):
        log.warning(f"{Fore.YELLOW}Pasta 'cogs' não encontrada. Criando pasta...{Style.RESET_ALL}")
        os.makedirs('./cogs')
        return

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            extension_name = f'cogs.{filename[:-3]}'
            try:
                await bot.load_extension(extension_name)
                log.info(f"{Fore.GREEN}Extensão '{extension_name}' carregada.{Style.RESET_ALL}")
            except Exception as e:
                log.error(f"{Fore.RED}Falha ao carregar '{extension_name}': {e}{Style.RESET_ALL}")

async def console_listener():
    await bot.wait_until_ready()
    log.info("Console pronto. Digite 'help' para comandos.")
    
    while not bot.is_closed():
        try:
            cmd_input = await aioconsole.ainput(f"{Fore.YELLOW}ZEN Console > {Style.RESET_ALL}")
            args = cmd_input.split()
            
            if not args:
                continue

            command = args[0].lower()

            if command == "reload":
                if len(args) < 2:
                    print(f"{Fore.RED}Uso: reload <nome_da_cog> OU reload all{Style.RESET_ALL}")
                    continue
                
                target = args[1]

                if target == "all":
                    log.info("Recarregando TODAS as extensões...")
                    for filename in os.listdir('./cogs'):
                        if filename.endswith('.py'):
                            ext_name = f'cogs.{filename[:-3]}'
                            try:
                                await bot.reload_extension(ext_name)
                                log.info(f"{Fore.GREEN}Recarregado: {ext_name}{Style.RESET_ALL}")
                            except Exception as e:
                                log.error(f"{Fore.RED}Erro em {ext_name}: {e}{Style.RESET_ALL}")

                else:
                    try:
                        full_name = f"cogs.{target}" if not target.startswith("cogs.") else target
                        await bot.reload_extension(full_name)
                        log.info(f"{Fore.GREEN}Cog '{target}' recarregada com sucesso!{Style.RESET_ALL}")
                    except commands.ExtensionNotLoaded:
                        try:
                            full_name = f"cogs.{target}" if not target.startswith("cogs.") else target
                            await bot.load_extension(full_name)
                            log.info(f"{Fore.GREEN}Cog '{target}' carregada (nova).{Style.RESET_ALL}")
                        except Exception as e:
                            log.error(f"{Fore.RED}Erro ao carregar: {e}{Style.RESET_ALL}")
                    except Exception as e:
                        log.error(f"{Fore.RED}Erro ao recarregar '{target}': {e}{Style.RESET_ALL}")

            elif command == "stop" or command == "exit":
                log.info("Desligando o bot via console...")
                await bot.close()
                break
            
            elif command == "help":
                print(f"\n{Fore.CYAN}--- Comandos do Console ---{Style.RESET_ALL}")
                print(f" {Fore.YELLOW}reload all{Style.RESET_ALL}         : Recarrega TODAS as cogs.")
                print(f" {Fore.YELLOW}reload <nome>{Style.RESET_ALL}      : Recarrega um arquivo específico (ex: ticket).")
                print(f" {Fore.YELLOW}stop{Style.RESET_ALL}               : Desliga o bot.")
                print(f" {Fore.YELLOW}clear{Style.RESET_ALL}              : Limpa o terminal.\n")
            
            elif command == "clear":
                os.system('cls' if os.name == 'nt' else 'clear')
                print_banner()

            else:
                print(f"Comando desconhecido. Digite 'help'.")

        except Exception as e:
            log.error(f"Erro no console: {e}")

@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    log.info(f'{Fore.GREEN}Bot conectado como: {bot.user}{Style.RESET_ALL}')
    # Custom status removido
    try:
        synced = await bot.tree.sync()
        log.info(f"Comandos Slash sincronizados: {len(synced)}")
    except Exception as e:
        log.error(f"Erro ao sincronizar comandos: {e}")

async def main():
    async with bot:
        await load_extensions()
        await asyncio.gather(
            bot.start(TOKEN),
            console_listener()
        )

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Bot interrompido manualmente.{Style.RESET_ALL}")