class m_modules:
    def __init__(self, core, client):
        core.addCommandHandler("loadmod", self, cpriv=9, chelp="loadmod.help")
        core.addCommandHandler("unloadmod", self, cpriv=9, chelp=
        "Descarga un módulo. Sintaxis: unloadmod <módulo>")
        core.addCommandHandler("reloadmod", self, cpriv=9, chelp=
        "re-carga un módulo. Sintaxis: reloadmod <módulo>")

    def reloadmod(self, bot, cli, event):
        self.unloadmod(bot, cli, event)
        self.loadmod(bot, cli, event)

    def loadmod(self, bot, cli, event):
        if not len(event.splitd) > 0:
            cli.msg(event.target, "\00304Error\003: Faltan parametros")
            return 1
        r = bot.loadmod(event.splitd[0], cli)
        if r == 1:
            cli.msg(event.target, "\00304Error\003: No se ha encontrado e" +
            "l archivo.")
        elif r == 2:
            cli.msg(event.target, "\00304Error\003: No se ha encontrado l" +
            "a clase principal.")
        elif r == 3:
            cli.msg(event.target, "\00304Error\003: El módulo ya está car" +
            "gado")
        else:
            cli.msg(event.target, "Se ha cargado el módulo " + event
             .splitd[0])

    def unloadmod(self, bot, cli, event):
        if not len(event.splitd) > 0:
            cli.msg(event.target, "\00304Error\003: Faltan parametros")
            return 1
        if bot.unloadmod(event.splitd[0]) == 1:
            cli.msg(event.target, "\00304Error\003: El módulo no está car" +
             "gado")
        else:
            cli.msg(event.target, "Se ha descargado el módulo " +
             event.splitd[0])
