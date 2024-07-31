from colorama import Fore, Style, init
from tomarket import Tomarket, print_timestamp
import asyncio
import sys


async def main():
    init(autoreset=True)

    tom = Tomarket()
    tokens = tom.user_login()

    for (token, username) in tokens:
        print_timestamp(f"{Fore.CYAN + Style.BRIGHT}[ {username} ]{Style.RESET_ALL}")
        tom.claim_daily(token=token)
        tom.user_balance(token=token)
        tom.start_farm(token=token)
        tom.list_tasks(token=token)

    print_timestamp(f"{Fore.CYAN + Style.BRIGHT}[ Restarting Soon ]{Style.RESET_ALL}")
    await asyncio.sleep(2 * 3600)


if __name__ == '__main__':
    while True:
        try:
            asyncio.run(main())
        except Exception as e:
            print_timestamp(f"{Fore.RED + Style.BRIGHT}[ {str(e)} ]{Style.RESET_ALL}")
        except KeyboardInterrupt:
            sys.exit(0)
