import click

import sys
sys.path.append("..")

from sub_pkg1.sub_pkg1_pkg1 import module1

__all__ =["main_fonksiyon"]

module1.fonksiyon()

print ("ben main_pkk paketi içindeki main_module üm")


@click.command()
@click.option('--isim', default="murat", help='mesaj verilecek kişi')
@click.option('--mesaj', default='Your name', help='isme verilecek mesaj')
def main_fonksiyon(isim:str, mesaj:str):
    click.echo(f"{mesaj}, {isim}")








