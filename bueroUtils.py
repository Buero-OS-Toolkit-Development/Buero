"""
Werkzeuge fÃ¼r BÃ¼ro.
"""
class bueroUtils:
    """
    Werkzeuge fÃ¼r BÃ¼ro.
    """
    def __init__(self, spec: bool = False, packageName: str = "BÃ¼ro"):
        """
        Initialisiert bueroUtils.
        spec -- Verhindert erneutes Laden eines debugLogs.
        packageName -- spezifiert Namen des ausgefÃ¼hrten Pakets.
        """
        import pycols, os, sys
        from pyimager.message import errorMessage
        self.privateOS = outputSuppressor(sys)
        self.status = status
        self.debugLog = debugLog
        if not spec:
            self.dLg = debugLog(packageName=packageName)
            self.dLg.entry(self.dLg)
        self.c = pycols.color()
        self.os = os
        self.errorMessage = errorMessage
        self.installed = self.get_installed()[1]
        self.__version__ = (4, 3, 1)
    def installmod(self, module: str):
        """
        Installiert gegebenes Modul in subshell.
        """
        print(module, "wird installiert...")
        self.os.system("py -m pip install " + module)
        print("Installation erfolgreich abgeschlossen.")
    def installmodules(self, modules: list[str]):
        """
        Installiert gegebene Module mit obiger Funktion
        """
        if len(modules) > 0:
            C_, C, T = self.get_colors()
            s = self.status("Modulinstallation: ", parts=len(modules)+1, colors=C, tcolors=T)
            s.send_message(" #Modulinstallation beginnen")
            for i in modules:
                self.installmod(i)
                s.send_message(" #Modul "+i+" installiert")
            s.send_message(" #Vorgang abschlieÃŸen")
    def install_check(self, modules: list[str]):
        """
        ÃœberprÃ¼ft fÃ¼r  jedes Modul, ob dieses installiert ist.
        Installiert fehlende Module.
        """
        x = []
        C_, C, T = self.get_colors()
        s = self.status("ModulÃ¼berprÃ¼fung: ", parts=len(modules)+1, fill=">", number=40, colors=C, tcolors=T)
        for i in modules:
            s.send_message(add=" #Modul "+i+" prÃ¼fen")
            if not self.is_installed(i if i != "pillow" else "PIL"):
                x.append(i)
        s.send_message(add=" #fehlende Module ({}{}{}) installieren".format(self.c.col(self.traffic(len(x),\
                       0, len(modules), duo=False, traffic_col=T))+self.c.BRIGHT,str(len(x)), self.c.RESET_ALL+self.c.col(C[1])))
        self.installmodules(x)
        s.send_message(add=" #Vorgang abschlieÃŸen")
    def is_installed(self, pkcg) -> bool:
        """
        PrÃ¼ft, ob Modul installiert ist.
        """
        import sys, io
        x = sys.stderr; sys.stderr = io.StringIO(); IN = True
        y = sys.stdout; sys.stdout = sys.stderr
        try:
            __import__(pkcg)
        except:
            IN = False
        finally:
            self.dLg.entry(sys.stderr.getvalue())
            sys.stderr = x
            sys.stdout = y
            return IN
    def get_version(self, module: str = "pip") -> str:
        """
        Gibt installierte Version von Modul zurÃ¼ck, falls diese gefunden wird.
        """
        try:
            import io, sys
            x = sys.stderr; sys.stderr = io.StringIO()
            moduleSrc = {module: __import__(module)}
        except:
            return "VersionReadingErrorOccuredWhileImporting"
        finally:
            sys.stderr = x
        try:
            return str(eval(module+".__version__", moduleSrc))
        except:
            try:
                return str(eval(module+".about()['Version']", moduleSrc))
            except:
                try:
                    return str(eval(module+".about()['version']", moduleSrc))
                except:
                    return "VersionReadingErrorOccured"
    def update(self, module="pip"):
        """
        Installiert Ã¼ber subshell Update fÃ¼r gegebenes Paket.
        """
        import subprocess
        vOld = self.get_version(module)
        sOutput = subprocess.check_output("py -m pip install --upgrade " + module, shell=True)
        if "Downloading" in str(sOutput, encoding="utf-8"):
            print(f"Erfolgreich Update von {vOld} installiert.")#
        else:
            print(f"Keine Updates fÃ¼r Version {vOld} gefunden.")#
    def updates(self, modules: list[str, str]):
        """
        Updated mehrere Pakete Ã¼ber obige Funktion.
        """
        C_, C, T = self.get_colors()
        s = status("Modulupdates: ", parts=len(modules), colors=C, tcolors=T)
        for i in modules:
            s.send_message(" #Modul "+(i if i != "" else "pip")+" aktualisieren")#
            if  i == "":
                self.update()
            else:
                self.update(i)
        s.send_message(" #Updatevorgang abschlieÃŸen")#
    def remove_(self, files: list[str, str] = [], filepath: str = "./"):
        """
        Entfernt mehrere Dateien
        """
        import os
        self.dLg.entry(files)
        for i in files:
            os.remove(filepath+i)
    def round_agent(self, zÃ¤hler: int = 10, nenner: int = 10, max_: int = 90, min_: int = 10) -> tuple[int, int]:
        """
        KÃ¼rzt Wert
        """
        import math
        while nenner > max_:
            zÃ¤hler /= 1.3; nenner /= 1.3
        while nenner < min_:
            zÃ¤hler *= 1.3; nenner *= 1.3
        return math.ceil(zÃ¤hler), math.ceil(nenner)
    def getad(self, Id: str, end=".png"):
        """
        Sendet Anzeige.
        """
        self.dLg.entrys("bÃ¼.getad called", Id, end)
        file = "./programdata/ads/" + Id + end
        from easygui import buttonbox
        buttonbox("", "Ad", [], image=file)
    def pruefePIN(self, toCheck: str, PIN_e: str, lenge: int):
        """
        ÃœberprÃ¼ft eingegebene PIN mit echter, verschlÃ¼sselter PIN.
        """
        self.dLg.entrys("bÃ¼.pruefePIN called", toCheck, PIN_e, lenge)
        import pyautogui as py
        if len(toCheck) == lenge:
            import random
            random.seed(int(toCheck))
            if str(random.randint(1, 10**30)) == PIN_e:
                return True
            else:
                py.alert("Falsche Eingabe!", "FALSCH!")
                return False
        else:
            py.alert("Fehlerhafte Eingabe!", "FALSCH!")
            return False
    def PIN_check(self, PIN_e: str, lenge: int, act: str):
        """
        komplette Methode zur ÃœberprÃ¼fung der PIN, falls PIN aktiv
        """
        self.dLg.entrys("bÃ¼.PIN_check called", PIN_e, lenge, act)
        if act == "True":
            import pyautogui as py
            PIN_u = py.password("PIN eingeben:")
            return self.pruefePIN(PIN_u, PIN_e, lenge)
        else:
            return True
    def PIN_erstellen(self, PIN_e: str = "198441737587687207744109680148", lenge: int = 4):
        """
        Methode zum erstellen einer neuen PIN.
        Falls der Vorgang abgebrochen wird, wird die PIN bei in BÃ¼ro auftretenden Fehlern auf 0000 gesetzt.
        """
        self.dLg.entry("bÃ¼.PIN_erstellen called")
        import pyautogui as py
        import random
        pin = 1; pin2 = 2; restore = 0; breakForced = False
        while pin != pin2 or len(str(pin)) not in list(range(4, 31)):
            pin_ = py.password("4- bis 30-stellige BÃ¼ro-PIN erstellen:", "BÃ¼ro-PIN")
            pin2_ = py.password("BÃ¼ro-PIN bestÃ¤tigen:", "BÃ¼ro-PIN")
            if pin_ == None or pin2_ == None:
                breakForced = True
                break
            else:
                pin = int(pin_); pin2 = int(pin2_)
        if not breakForced:
            while restore == 0 or len(str(restore)) != 32:
                restore = int(py.prompt("Wiederherstellungs-PIN erstellen:\nHinweis: Der WiederherstellungsschlÃ¼ssel wird benÃ¶tigt, um deine PIN wiederherzustellen und hat 32 Stellen.", "WiederherstellungsschlÃ¼ssel", random.randint(1, 10**32-1)))
            random.seed(pin)
            lenge = len(str(pin))
            PIN_e = str(random.randint(1, 10**30))
            with open("./programdata/buero/PIN.txt", "w") as pin_f:
                pin_f.write(PIN_e)
            with open("./programdata/buero/PIN_l.txt", "w") as pin_l:
                pin_l.write(str(lenge))
            random.seed(restore)
            with open("./programdata/buero/restore.txt", "w") as rest:
                rest.write(str(random.randint(1, 10**40)))
            return PIN_e, lenge
        else:
            py.alert("Achtung:\nFalls Sie gerade eine PIN zum ersten Mal erstellen sollten, wurde sie soeben auf 0000 zurÃ¼ckgesetzt.", "Achtung")
            return PIN_e, lenge
    def uninstallmessage(self):
        """
        Sendet Nachricht, dass BÃ¼ro deinstalliert wurde.
        """
        self.dLg.entry("bÃ¼.uninstallmessage called")
        import pyautogui as py
        py.alert("BÃ¼ro deinstalliert!")
        quit()
    def get_size(self, path: str) -> float:
        """
        Ermittelt GrÃ¶ÃŸe einer Datei oder rekursiv aller untergeordneten Dateien.
        """
        self.dLg.entrys("bÃ¼.get_size called", path)
        size = 0
        if self.os.path.isdir(path):
            for file in self.os.listdir(path):
                size += self.get_size(path+"/"+file)
        else:
            size = self.os.stat(path).st_size
        return size
    def get_sizes(self, pathlist: list[str, str] = [], prepath: str = "") -> float:
        """
        Wendet obige Methode auf mehrere Dateien/Ordner an.
        Falls impath == True wird automatisch ein Pfadbestandteil ergÃ¤nzt.
        """
        self.dLg.entrys("bÃ¼.get_sizes called", pathlist, prepath)
        size = 0
        for i in pathlist:
            size += self.get_size(prepath + i)
        return size
    def countFiles(self, path: str) -> int:
        """
        ZÃ¤hlt die Anzahl aller Dateien in einem Ordner und allen untergeordneten Ordnern.
        """
        count = 0
        for i in self.os.listdir(path):
            if self.os.path.isdir(path+"/"+i):
                count += self.countFiles(path+"/"+i)
            else:
                count += 1
        return count
    def traffic(self, numb: int = 1, prgs_min: int = 0, prgs_max = 2, traffic_col = ["RED", "YELLOW", "GREEN"], expt: str = "min", duo: bool = True):
        """
        Gibt Farbe aus 2/3 langer Liste je nach gegebenem Wert und Prognosen zurÃ¼ck.
        """
        self.dLg.entrys("bÃ¼.traffic called", numb, prgs_min, prgs_max, traffic_col, expt, duo)
        t_c = traffic_col.copy()
        if expt == "min":
            t_c.reverse()
        x = (prgs_max-prgs_min+1)/(2 if duo else 3)
        a = t_c[2]
        if numb < prgs_min+(0 if duo else x):
            a = t_c[0]
        if numb < prgs_min+(x if duo else 2*x) and numb >= prgs_min+(0 if duo else x):
            a = t_c[1]
        return a
    def trafficer(self, numb: int = 1, prgs_min: int = 0, prgs_max = 2, traffic_col = ["RED", "YELLOW", "GREEN"], expt: str = "min", duo: bool = True, mthd: callable = str):
        """
        Verwaltet mit obiger Methode Nachricht.
        """
        return self.c.col(self.traffic(numb, prgs_min, prgs_max, traffic_col, expt, duo))+mthd(numb)+self.c.RESET_ALL
    def get_colors_(self):
        """
        Liest gespeicherte Farben aus.
        """
        with open("./programdata/buero/color.txt", "r") as f:
            x = list(f.read().rstrip("#*#").split("#*#"))
        self.dLg.entrys("get_colors:", x)
        return x
    def get_colors(self):
        """
        Verpackt gespeicherte Farben in Listen.
        """
        x = self.get_colors_()
        return x, x[0:2], x[2:6]
    def display_achievement(self, name: str):
        """
        Zeigt Erfolg an.
        """
        import pyimager as pi
        schabl = "./programdata/achievements/{}.lkim"; self.dLg.entry(name)
        try:
            pi.display(schabl.format(name))
        except:
            pi.display("display_content", "7#*#9#**#$a$aaabcdef$a$agaanmlkhaao$a$apqrbc%a%af%a%")
            self.dLg.entry("MISSING!"); print("ERFOLG FEHLT! SIE HABEN EIN UPDATE NICHT INSTALLIERT! WENDEN SIE SICH AN DEN KUNDENSERVICE!")
    def numeral(self, grade:int = 1, sex: str = "m"):
        """
        Ermittelt Numeral (Zahlwort) fÃ¼r gegebene Zahl mit gegebenem Geschlecht.
        Range: 1 bis 12, danach ValueError
        """
        match grade:
            case 1:
                a = "erste"
            case 2:
                a = "zweite"
            case 3:
                a = "dritte"
            case 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
                b = ["vier", "fÃ¼nf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwÃ¶lf"]
                a = b[grade-4]+"te"
            case _:
                raise ValueError("Value not in Range")
        if sex == "m":
            a += "r"
        elif sex == "n":
            a += "s"
        return a
    def web_content(self, url: str, data: dict = {}) -> str:
        """
        LÃ¤dt Webinhalte herunter.
        """
        import requests
        rq = requests.post(url, data).content
        self.dLg.entrys(rq, url, data, "webContent called")
        return rq.decode()
    def web_update(self, versionUrl: str = "https://lkunited.pythonanywhere.com/bueroVersion", username: str = "RANDOM_USER"):
        """
        LÃ¤dt Update aus Web herunter.
        """
        import pyautogui as py
        import requests
        update_version = self.web_content(versionUrl, {"message": username, "pw": "lkunited"})
        try:
            self.dLg.entry(str(update_version.split(".")))
        except:
            py.alert("Ein Fehler ist beim Download der aktuellsten Version aufgetreten.", "Error")
            return False
        if self.buttonLog("Es wird versucht, die folgende Version herunterzuladen:\n" + update_version) == "Fortfahren":
            update_ = requests.get("https://leanderkafemann.github.io/bueroWebsite/data/bÃ¼ro" + update_version + ".zip").content
            if not "<!DOCTYPE"+" html>" in str(update_):
                with open("./bÃ¼ro" + update_version + ".zip", "wb") as f:
                    f.write(update_)
                return True
            else:
                if not "beta" in versionUrl:
                    py.alert("Ein unbekannter Fehler ist aufgetreten.", "Error")
                else:
                    py.alert("Diese BETA-Version ist momentan nicht verfÃ¼gbar.", "Error")
                return False
        else:
            return False
    def checkPREMIUM(self, pass_: str = "", getPass: bool = False) -> bool:
        """
        ÃœberprÃ¼ft, ob der gegebene Pass des Nutzers gÃ¼ltig ist.
        Setzen Sie getpass auf True, damit bueroUtils den Pass automatisch selbst ausliest.
        """
        if getPass:
            try:
                with open("./premiumpass.txt", "r", encoding="utf-8") as f:
                    pass_ = f.read()
            except:
                return False; bool
        preToTest = self.web_content("https://lkunited.pythonanywhere.com/checkerP", {"message":pass_, "pw":"lkunited"})
        self.dLg.entry(preToTest)
        checkPRE = "True" in preToTest
        return checkPRE; bool
    def checkBETA(self, username: str) -> bool:
        """
        PrÃ¼ft, ob der gegebene Nutzer fÃ¼r BETA registriert ist.
        """
        return self.web_content("https://lkunited.pythonanywhere.com/cB", {"message": username, "pw": "lkunited"}) == "registered"
    def checkLogActive(self) -> bool:
        """
        PrÃ¼ft, ob DebugLogs aktiviert sind.
        Gibt True zurÃ¼ck, wenn die Logs deaktiviert wurden.
        """
        from time import sleep
        with open("./programdata/buero/log.txt", "r") as lg:
            a = lg.read()
        if a not in ["True", "False"]:
            a = "False"
            print("Ihre DebugLog-Einstellung ist fehlerhaft. Ihre Logs bleiben daher automatisch aktiv.");sleep(3)
            self.errorMessage("Eventuell wurden Sie gehackt.")
        return a=="True"
    def createPreMail(self, to: str, subject: str, content: str) -> bool:
        """
        Creates presaved Mail for BÃ¼roMail,
        overwriting any other presaved mails.
        """
        if "BÃ¼roMail" in self.installed:
            with open("./programdata/mail/pre_mail.txt", "w", encoding="utf-8") as f:
                f.write(f"{to}#**#{subject}#**#{content}")
            return True
        else:
            import pyautogui as py
            py.alert("Sie benÃ¶tigen BÃ¼roMail, um diese Aktion durchzufÃ¼hren!", "BÃ¼roMail erforderlich")
            return False
    def shareViaMail(self, to: str, subject: str, content: str):
        """
        Opens BÃ¼roMail in a new window and creates preMail.
        """
        if self.createPreMail(to, subject, content):
            self.executePackage("./mail.py")
    def createPreBank(self, to: str, sum_: str, descr: str) -> bool:
        """
        Creates presaved Mail for BÃ¼roMail,
        overwriting any other presaved mails.
        """
        if "BÃ¼roBank" in self.installed:
            with open("./programdata/bank/pre_bank.txt", "w", encoding="utf-8") as f:
                f.write(f"{to}#**#{sum_}#**#{descr}")
            return True
        else:
            import pyautogui as py
            py.alert("Sie benÃ¶tigen BÃ¼roBank, um diese Aktion durchzufÃ¼hren!", "BÃ¼roBank erforderlich")
            return False
    def payViaBank(self, to: str, sum_: str, descr: str):
        """
        Opens BÃ¼roBank with preBank.
        """
        if self.createPreBank(to, sum_, descr):
            self.executePackage("./bank.py")
    def executePackage(self, packagePath: str):
        """
        Executes Package in seperate thread.
        """
        import threading
        def a():
            self.os.system("py "+packagePath)
        threading.Thread(target=a).start()
    def buttonLog(self, text: str = "Bitte bestÃ¤tigen:", title: str = "BestÃ¤tigen", buttons: tuple = ("Fortfahren", "Abbrechen")) -> str:
        """
        Fragt den Nutzer nach gegebenen Aspekten und trÃ¤gt Antwort in debugLog ein.
        """
        import pyautogui as py
        aw = py.confirm(text, title, buttons)
        self.dLg.entry(aw)
        return aw
    def error_quit(self):
        """
        Beendet BÃ¼ro nach User-Error.
        """
        try:
            self.error_message()
        finally:
            self.os.remove("./programdata/run/running.txt")
            self.dLg.entry("User-Error; Quitting")
            self.dLg.finalsave_log()
            quit(code="Error-Edited")
    def get_installed(self) -> tuple[list[str], list[str], list[str], list[str], list[str], list[str], list[str]]:
        """
        Returns all packages installed and information about packages not installed.
        """
        upgr = ["VerschlÃ¼sseler", "Haustier", "Ballonfahrt", "SchingSchangSchongIQ", "abstrakte Verzerrung", "im Verlies", "Passwortgenerator", "Musik",\
                "Garten im GlÃ¼ck", "Lebensmittel", "Das groÃŸe Quiz", "Rechnungen", "BÃ¼roMail", "BÃ¼roBank", "LTP Agent", "BÃ¼roBonus", "Kaffeemanager"]
        files = self.os.listdir()
        werkzeuge = []; unterhaltung = []; lernen = []; medien = []; plugin = []; miniwelt = []
        if "verschlÃ¼sseln.py" in files:
            werkzeuge.append("VerschlÃ¼sseler")
        if "Haustier.py" in files:
            unterhaltung.append("Haustier")
        if "Ballonfahrt.py" in files and "Ballonfahrt-M2_1.py" in files and "Ballonfahrt-M2_2.py" in files:
            unterhaltung.append("Ballonfahrt")
        if "SchingSchangSchongIntelligent.py" in files:
            lernen.append("SchingSchangSchongIQ")
        if "abstrakt.py" in files:
            medien.append("abstrakte Verzerrung")
        if "quest.py" in files and "level-editor.py" in files:
            lernen.append("im Verlies")
        if "Passwortgenerator.py" in files:
            werkzeuge.append("Passwortgenerator")
        if "Musik.py" in files:
            medien.append("Musik")
        if "Garten-im-GlÃ¼ck.py" in files:
            unterhaltung.append("Garten im GlÃ¼ck")
        if "lebensmittel.py" in files:
            werkzeuge.append("Lebensmittel")
        if "quiz.py" in files:
            lernen.append("Das groÃŸe Quiz")
        if "Rechnung.pyw" in files:
            werkzeuge.append("Rechnungen")
        if "mail.py" in files and "mail_agent.pyw" in files:
            plugin.append("BÃ¼roMail")
        if "bank.py" in files:
            plugin.append("BÃ¼roBank")
        if "ltp_agent.py" in files:
            lernen.append("LTP Agent")
        if "ritter_launcher.py" in files:
            miniwelt.append("Die Ritter - Launcher")
        if "bonus.py" in files:
            plugin.append("BÃ¼roBonus")
        if "kaffee.py" in files:
            werkzeuge.append("Kaffee Manager")
        if "goodFood.py" in files:
            werkzeuge.append("GoodFood")
        installiert = werkzeuge+unterhaltung+medien+plugin+lernen
        upgr = [i for i in upgr if i not in installiert]
        return [upgr, installiert, werkzeuge, unterhaltung, lernen, medien, plugin]#spÃ¤ter auch miniwelt
    def logListDir(self, file: str) -> list:
        fileList = self.os.listdir(file)
        self.dLg.entry(fileList)
        return fileList
    def importPyautoguiCatched(self):
        self.privateOS.suppressErrorOutput()
        import pyautogui
        self.privateOS.restoreOutputs()
        return pyautogui
    def error_message(self):
        """
        Sendet Fehlermeldung.
        """
        import pyautogui as py
        py.alert("BÃ¼ro ist abgestÃ¼rzt. Nutzen Sie fehleranalyse.py, um ein DebugLog zu Ã¼bermitteln.")
    def restart(self):
        """
        Startet BÃ¼ro ggf. neu.
        """
        import sys
        if self.buttonLog("Eventuell muss BÃ¼ro neugestartet werden, um alle Ã„nderungen zu Ã¼bernehmen.", "Neustart erforderlich", buttons=("NEU STARTEN", "IGNORIEREN")) == "NEU STARTEN":
            self.dLg.finalsave_log()
            self.os.remove("./programdata/run/running.txt")
            self.os.system("cls")
            self.os.execv(sys.executable, ['python'] + sys.argv)
    def normal_quit(self):
        """
        Beendet BÃ¼ro regulÃ¤r.
        """
        self.os.remove("./programdata/run/running.txt")
        self.dLg.finalsave_log()
        quit(code="Ende-Edited")

class debugLog(bueroUtils):
    """
    Klasse zum Erstellen eines Debug-Logs.
    """
    def __init__(self, packageName: str = "BÃ¼ro", sep: str = "\n"):
        from io import StringIO
        self.out = StringIO()
        self.canceled = False
        self.packageName = packageName
        self.sep = sep
        self.autoPresave = False
        bueroUtils.__init__(self, spec=True)
    def entry(self, entry: str = "noEntryErrorCatched"):
        """
        FÃ¼gt Eintrag in Debug-Log-Objekt hinzu.
        """
        print(entry, file=self.out, sep=self.sep)
        if self.autoPresave:
            self.presave_log()
    def entrys(self, *arg):
        """
        FÃ¼gt Ã¼ber obige Methode mehrere EintrÃ¤ge hinzu.
        """
        b = self.autoPresave
        self.autoPresave = False
        for i in arg:
            self.entry(str(i))
        self.presave_log()
        self.autoPresave = b
    def save_log(self, name_add: str = ""):
        """
        Speichert Debug-Log.
        """
        import datetime
        if self.canceled == False:
            with open("./programdata/buero/debug/{}{}_debug_log_{}.txt".format(name_add, self.packageName, str(datetime.datetime.today())[0:-7].replace(" ", "-").replace(":", "-")), "a", encoding="utf-8") as f:
                f.write("---"+self.out.getvalue())
    def presave_log(self):
        """
        Speichert Debug-Log mit vorangehendem 'pre_'-Code.
        """
        if not self.canceled:
            self.autoPresave = False
            self.entry("Presaving log...")
            self.autoPresave_()
            self.save_log(name_add="pre_")
    def finalsave_log(self):
        """
        Speichert Debug-Log und entfernt alle presaves.
        """
        for i in list(self.os.listdir("./programdata/buero/debug")):
            if i.startswith("pre_"):
                self.os.remove("./programdata/buero/debug/"+i)
        self.save_log()
    def alter_package_name(self, newPackageName: str):
        self.packageName = newPackageName
    def cancel_(self):
        """
        Kehrt canceled-Einstellung um.
        """
        from naturalsize import reverse
        self.canceled = reverse(self.canceled)
        self.entrys(self.canceled, "log cancel_")
    def autoPresave_(self):
        """
        Kehrt autoPresave-Eistellung um.
        """
        from naturalsize import reverse
        self.autoPresave = reverse(self.autoPresave)

class status(bueroUtils):
    """
    Klasse fÃ¼r das Erstellen eines Status-Bars.
    """
    def __init__(self, message: str = "", number: int = 50, start: int = 0, fill: str = "-", unfill: str = " ", end: str = "|", \
                 parts: int = 1, colors: list[str, str] = ["WHITE"]*2, tcolors: list[str, str, str] = ["WHITE"]*3):
        import sys
        bueroUtils.__init__(self)
        self.message = message
        self.number = number
        self.fill = fill
        self.unfill = unfill
        self.end = end
        self.akt = start
        self.parts = parts
        self.colors = colors
        self.tcolors = tcolors
        self.currentStrLen = 0
        self.sysStdoutObj = sys.stdout
        #self.sM_isInitialized = False
        while self.number % self.parts != 0:
            self.number += 1
        self.dLg.entry("Status-Class used: {}#{}#{}#{}#{}#{}#{}#{}".format(message, str(number), str(self.number), fill, unfill, end, start, parts))
    def send_message_new(self, add: str = ""):
        """
        Sendet vollstÃ¤ndigen Status-Bar mit variabler Nachricht, aber ohne Farbe.
        LÃ¶scht vorher vorrangegangenen Status-Bar.
        """
        #print(self.currentStrLen)
        #if not self.sM_isInitialized:
        #    self.sysStdoutObj.write(self.message+self.end)
        #    self.sM_isInitialized = True
        self.sysStdoutObj.write("\b"*self.currentStrLen)
        WStr = self.message+self.end+self.akt*self.fill+(self.number-self.akt)*self.unfill+self.end+add
        self.currentStrLen = len(WStr)#len(self.akt*self.fill+(self.number-self.akt)*self.unfill+self.end+add)
        self.sysStdoutObj.write(WStr)
        self.sysStdoutObj.flush()
        self.akt += int(self.number/self.parts)
        self.dLg.entry("Number:{};Message:{}".format(self.akt, add))
    def send_message(self, add: str = ""):
        """
        Sendet vollstÃ¤ndigen Status-Bar mit variabler Nachricht und Farbe.
        """
        print(self.c.col(self.colors[0])+self.message+self.c.RESET_ALL+self.end+\
              self.c.col(self.traffic(self.akt, 0, self.number, self.tcolors, "max", False))+self.akt*self.fill+\
              (self.number-self.akt)*self.unfill+self.c.RESET_ALL+self.end+self.c.col(self.colors[1])+add+self.c.RESET_ALL)
        self.akt += int(self.number/self.parts)
        self.dLg.entry("Number:{};Message:{}".format(self.akt, add))
    def init_one_bar(self):
        """
        Initialisiert einen Status-Bar.
        """
        print(self.c.col(self.colors[0])+self.message+self.c.col("RESET")+self.end+self.c.col(self.colors[1])+\
              self.akt*self.fill, end="")
        self.dLg.entry("One-Bar-Init")
    def draw_one_bar(self):
        """
        Setzt initialisierten Status-Bar fort.
        Hinweis: Diese Methode ergibt nur bei einem schnellen Prozess Sinn!
        """
        print(int(self.number/self.parts)*self.fill, end="")
        self.dLg.entry("Draw-One-Bar")
    def finish_one_bar(self):
        """
        Beendet fertigen Status-Bar.
        """
        print(self.c.col("RESET")+self.end)
        self.dLg.entry("Finish-One-Bar")

class outputSuppressor:
    """
    Klasse zum UnterdrÃ¼cken von Outputs.
    """
    def __init__(self, sys):
        self.sys = sys
        import io
        self.io = io
        self.stdout = sys.stdout
        self.stderr = sys.stdin
    def suppressErrorOutput(self):
        self.sys.stderr = self.io.StringIO()
    def suppressPrintOutput(self):
        self.sys.stdout = self.io.StringIO()
    def restoreOutputs(self):
        self.sys.stdout = self.stdout
        self.sys.stderr = self.stderr

if __name__ == "__main__":
    import naturalsize
    print("Warten Sie einige Sekunden, um alle Ihre Module aktualisieren zu lassen.\nDrÃ¼cken Sie Strg+c zum Abbrechen.")
    if not naturalsize.special_starter(300000000):
        bueroUtils().updates(modules=['', 'colorama', 'easygui', 'eyed3', 'datetime', 'keyboard', 'naturalsize', 'numpy', 'pgzero', 'pillow', 'ping3', 'pyautogui',\
                                      'pycols', 'pygame', 'pyimager', 'pymsgbox', 'pyperclip', 'pyscreeze', 'pysounds', 'reportlab', 'requests'])
    else:
        print("Vorgang abgebrochen.")
        naturalsize.special_starter(75000000)
elif __name__ == "bueroUtils":
    import sys
    allowed = ["", "bÃ¼ro.py", "bueroUtils.py", "update.py", "mail.py", "mail_agent.pyw", "bank.py",\
               "ltp_agent.py", "ritter_launcher.py", "bonus.py", "kaffee.py", "goodFood.py"]
    sys_ = [i.split("\\")[-1].split("./")[-1] for i in sys.argv]
    #print(sys_)
    proceed = True
    for i in sys_:
        if i not in allowed and not "test" in i:
            proceed = False
            break
    if not proceed:
        raise ImportError("Invalid or unauthorized script or plugin.")
