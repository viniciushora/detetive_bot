import discord
import random

from discord.ext import commands

global assassinato, servers

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='det!', intents=intents)

servers = {}

cartas_locais = ["Restaurante", "Prefeitura", "Banco", "Hospital", "Floricultura", "Praça Central", "Mansão", "Hotel", "Cemitério", "Estação de Trem", "Boate"]
cartas_armas = ["Faca", "Soco Inglês", "Pé de Cabra", "Tesoura", "Pá", "Arma Química", "Veneno", "Espingarda"]
cartas_suspeitos = ["Sargento Bigode", "Florista Dona Branca", "Advogado Senhor Marinho", "Chef de Cozinha Tony Gourmet", "Dançarina Srta Rosa", "Médica Dona Violeta", "Coveiro Sérgio Noturno", "Mordomo James"]

@bot.event
async def on_ready():
    print('Estou funcionando como {0.user}'.format(bot))
    print("Tudo Ok")

@bot.command()
async def jogar(ctx):
    global servers
    guild_id = ctx.message.guild.id
    if not guild_id in servers:
        jogadores = []
        select = discord.Embed(
            title=f"""*Iniciando partida de detetive*""",
            description="Clique em :white_check_mark: para participar *(Máximo 11 jogadores)* | Para iniciar clique no Ok",
            colour=discord.Colour.red()
        )
        emb_msg = await ctx.send(embed=select)
        await emb_msg.add_reaction("✅")
        await emb_msg.add_reaction("👌")
        ok = 0
        while ok == 0:
            reaction, user = await bot.wait_for('reaction_add', timeout=None)
            if str(reaction) == "✅" and str(user) != "Detetive Bot#1694":
                jogadores.append(user)
            if str(reaction) == "👌" and str(user) != "Detetive Bot#1694":
                ok = 1
        cartas = cartas_locais + cartas_armas + cartas_suspeitos
        local = cartas_locais[random.randint(0, len(cartas_locais)-1)]
        arma = cartas_armas[random.randint(0, len(cartas_armas)-1)]
        suspeito = cartas_suspeitos[random.randint(0, len(cartas_suspeitos)-1)]
        assassinato = (local,arma,suspeito)
        servers[guild_id] = assassinato
        await ctx.send("*Assassino definido!* :knife:")
        cartas.remove(local)
        cartas.remove(arma)
        cartas.remove(suspeito)
        jogadores_cartas = []
        quant_cartas = len(cartas) // len(jogadores)
        quant_extra = len(cartas) % len(jogadores)
        for i in range(len(jogadores)):
            mao = []
            for j in range(quant_cartas):
                if cartas != []:
                    carta = cartas[random.randint(0, len(cartas)-1)]
                    mao.append(carta)
                    cartas.remove(carta)
            mao_jogador = (jogadores[i],mao)
            jogadores_cartas.append(mao_jogador)
        embed_cartas = discord.Embed(
            title=f"""*Sua mão dessa partida de Detetive*""",
            description="Suas cartas são:",
            colour=discord.Colour.blue()
        )
        for k in range(len(jogadores_cartas)):
            jogador, cartas = jogadores_cartas[k]
            i = 1
            for carta in cartas:
                texto = "*" + carta + "*"
                embed_cartas.add_field(name=i, value=texto, inline=True) 
                i += 1
            await jogador.send(embed=embed_cartas)
        await ctx.send("*Cartas distribuídas!* :black_joker:")
    else:
        await ctx.send("*Partida já em andamento*")

@bot.command()
async def resetar(ctx):
    guild_id = ctx.message.guild.id
    if guild_id in servers:
        del servers[guild_id]
        await ctx.send("*Jogo resetado!* :game_die:")

@bot.command()
async def assassino(ctx):
    guild_id = ctx.message.guild.id
    if guild_id in servers:
        texto = "O assassino é o(a) " + servers[guild_id][2] + " no(a) " + servers[guild_id][0] + " com o(a) " + servers[guild_id][1]
        await ctx.send(texto)
    else:
        await ctx.send("Sem assassino definido!")

@bot.command()
async def ajuda(ctx):
    await ctx.send("Siga o passo a passo em: https://github.com/ViniciusHora1009/detetive_bot | Para comandos use **det!comandos**")

@bot.command()
async def tabuleiro(ctx):
    await ctx.send("Clique em configurações e vá em 'Copiar Jogo': https://app.roll20.net/campaigns/details/8490759/detetive")

@bot.command()
async def comandos(ctx):
    embed_comandos = discord.Embed(
            title=f"""*Lista de comandos de Detetive Bot*""",
            description="Prefixo: **det!**",
            colour=discord.Colour.blue()
    )
    embed_comandos.add_field(name="ajuda", value="Link do passo a passo de como usar o bot", inline=False)
    embed_comandos.add_field(name="jogar", value="Inicia uma partida de detetive caso não tenha iniciado", inline=False)
    embed_comandos.add_field(name="tabuleiro", value="Link para o tabuleiro do jogo", inline=False)
    embed_comandos.add_field(name="assassino", value="Revela o assassino da partida", inline=False)
    embed_comandos.add_field(name="resetar", value="Reseta todas as informações da partida", inline=False)
    await ctx.send(embed=embed_comandos)

bot.run('INSIRA O BOT TOKEN')