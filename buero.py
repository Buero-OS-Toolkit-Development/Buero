"""
COPYRIGHT
DE: 'BÃ¼ro', alle zugehÃ¶rigen Pakete und Funktionen wurden von Leander Kafemann programmiert und zusammengestellt.
    Die Weiterverbreitung ist strengstens untersagt.
EN: 'BÃ¼ro', all accompanying packages and functions were programmed and compiled by Leander Kafemann.
    The redistribution is forbidden strictly.
LA: 'BÃ¼ro', cuncti fasces comitantes finctionesque programmati confecti et conventi sunt Leandre Kafemanne.
    Diffundum interdictum severe est.
IT: 'BÃ¼ro', tutti i pachi relativi e funzioni sono stati programmati da Leander Kafemann.
    La ritrasmissione Ã¨ severamente vietata.
{Ihre aktuelle Version erschien am/
 Your version was released the/
 Tua varianta singularis apparebat ad/
 La Loro versione Ã¨ stata pubblicata il}
04.09.2025/IV.IX.MMXXV.
"""

__version__ = "4.4.0"

#Python-Version prÃ¼fen
import sys, os
from time import sleep
import webbrowser as wb
if sys.version_info < (3, 11, 0):
    wb.open("www.python.org/downloads")
    print("Sie benÃ¶tigen eine hÃ¶here Python-Version!\nEinige Features sind mit Ihrer Version eventuell nicht verfÃ¼gbar.");sleep(3)
    print("\n\n\nEventuell wird Python gleich abstÃ¼rzen! Es wird dringend mindestens Python 3.11 benÃ¶tigt!");sleep(5)
if sys.version_info > (3, 12, 0):
    print("BÃ¼ro ist fÃ¼r Ihre Python-Version nicht getestet.\nBitte melden Sie auftretende Fehler dem Kundenservice.")
print("Bootvorgang gestartet. Dies kann einen Moment in Anspruch nehmen.")

#Running-Check
if "running.txt" in os.listdir("./programdata/run"):
    run = input("BÃ¼ro lÃ¤uft bereits.\nDas erneute AusfÃ¼hren kann zu erheblichen Fehlern fÃ¼hren.\nWie wollen Sie fortfahren?\nOptionen: Quit, Fehler beheben --> ")
    if run == "Fehler beheben":
        os.remove("./programdata/run/running.txt")
        print("Fehler erfolgreich behoben."); sleep(1.1)
        input("Sie kÃ¶nnen BÃ¼ro nun schlieÃŸen oder starten (Eingabe-Taste drÃ¼cken).")
        open("./programdata/run/running.txt", "x").close()
    else:
        quit(code="Already running")
else:
    open("./programdata/run/running.txt", "x").close()

#preimport und notwendige Daten
import bueroUtils, pycols
bÃ¼ = bueroUtils.bueroUtils()
dLg = bÃ¼.dLg
dLg.autoPresave_()
cOl = pycols.color()
COLORS_, COLORS, TCOLORS = bÃ¼.get_colors()
PACKAGES = ['colorama', 'easygui', 'eyed3', 'datetime', 'keyboard', 'naturalsize', 'numpy', 'pgzero', 'pillow', 'ping3', 'pyautogui', 'pycols', 'pygame', 'pyimager',\
            'pymsgbox', 'pyperclip', 'pyscreeze', 'pysounds', 'reportlab', 'requests']
s = bÃ¼.status("Bootvorgang: ", number=45, start=3, parts=15, colors=COLORS, tcolors=TCOLORS)
s.send_message(" #Preimport getÃ¤tigt");s.send_message(" #Python-Version geprÃ¼ft"); s.send_message(" #Running-Daten Ã¼berprÃ¼ft")

#notwendige Imports
s.send_message(" #weitere Imports abschlieÃŸen")
import shutil, threading, requests, zipfile
from random import choice, randint
from tkinter.filedialog import askopenfilename
import update

#ModulÃ¼berprÃ¼fung
s.send_message(" #Module prÃ¼fen")
bÃ¼.install_check(PACKAGES)
py = bÃ¼.importPyautoguiCatched()
import pyimager, pysounds, pyperclip, pycols
from naturalsize import *

#Initialisierung
s.send_message(" #Daten initialisieren")
antwort = ""
adlist = ["bÃ¼ro4.4.png", "bueroLogo.png", "LTP.png", "Bonus.png", "GoodFood.png"]
lklist = []#"HandballWM25Special.lkim"]
winlist = ["z!GG100010.txt"]
PREMIUM = False; ILLEGAL = False; OFFLINE = False; AGB = True
FLAG = False
toBook = False
BPATH = "./programdata/buero/"

#Dateilisten fÃ¼r ausgewÃ¤hlte Pakete
imlist = ['crack1.png', 'crack2.png', 'door.png', 'energie.png', 'floor1.png', 'floor2.png',\
          'guard.png', 'key.png', 'player.png', 'superguard.png', 'wall.png']
balims = ['background.png', 'background2.png', 'balloon.png', 'balloon2.png', 'balloon_am fettesten.png', 'balloon_am kleinsten.png',\
          'balloon_antrieb.png', 'balloon_bierbauch.png', 'balloon_fett.png', 'balloon_fetter.png', 'balloon_kampf.png', 'balloon_klein.png',\
          'balloon_kleiner.png', 'balloon_lachend.png', 'balloon_leicht entzÃ¼ndlich.png', 'balloon_magie.png', 'balloon_schild.png',\
          'balloon_unsichtbar.png', 'bird-down.png', 'bird-up.png', 'bomb.png', 'coin.png', 'explosion.png', 'house.png', 'mystery.png',\
          'rocket.png', 'tree.png', 'ufo_ballonfahrt.png']
gigims = ['cow.png', 'cow-water.png', 'fangflower.png', 'flower.png', 'flower-wilt.png',\
          'garden.png', 'ufo.png', 'zap.png']
quizmusic = ['quiz-music.mp3']

#Button-Datenbank
konfig = ["Tools", "Informationen", "Shopping & Weiteres", "Account", "BÃ¼roOnline", "FÃ¼r Dich", "Debug", "Speicherplatz", "ZurÃ¼ck"]
buttons = [["Update", "Upgrade", "Systemupdate", "Hintergrundsystemupdate", "Update herunterladen", "Aktualisieren", "Notizen"],\
           ["VersionInfo", "UpgradeInfo", "BÃ¼roUpdateInfo", "Coming Soon", "What's new?", "Tipps"],\
           ["Anfordern", "Releases abonnieren", "BÃ¼ro PREMIUM", "Gewinnspiele", "Feedback & FunktionsvorschlÃ¤ge", "AGB ablehnen"],\
           ["PIN Ã¤ndern", "PIN-Status Ã¤ndern", "Nutzernamen ansehen", "Nutzernamen Ã¤ndern"],\
           ["DeviceID ansehen", "statische DeviceID", "DeviceID aktualisieren", "Online einloggen", "Ãœber BÃ¼ro"],\
           ["Status personalisieren", "StartmenÃ¼ personalisieren", "Erfolge ansehen", "Fortschritt ansehen"],\
           ["schnelle Fehleranalyse", "Debug-Log Ã¼bermitteln","PREMIUM funktioniert nicht", "PIN vergessen", "Erfolge aktualisieren", "aktuelles Log", "jedes Log"],\
           ["SpeicherInfo", "Deinstallieren", "DebugLogInfo", "AufrÃ¤umen"]]
skip = False; skip2 = False; skipagb = False; skipwin = False
get_package = ""
PLUS = []

#verfÃ¼gbare Pakete prÃ¼fen
s.send_message(" #verfÃ¼gbare Pakete prÃ¼fen")
upgr, installiert, werkzeuge, unterhaltung, lernen, medien, plugin = bÃ¼.get_installed()

#Bereich-Listen erstellen
s.send_message(" #Pakete verarbeiten")
files = os.listdir()
list_container = [werkzeuge, unterhaltung, medien, lernen, plugin]
name_container = ["Werkzeuge", "Unterhaltung", "Medien", "Lernen", "Plugins"]
bereiche = [name_container[i] for i in range(len(list_container)) if len(list_container[i]) > 0]

#FF prÃ¼fen        
s.send_message(" #Feature-Flags prÃ¼fen")
try:
    if bÃ¼.web_content("https://lkunited.pythonanywhere.com/featureFlag") == "True":
        FLAG = True
except:
    OFFLINE = True; FLAG = False
    pyimager.message.errorMessage("Sie sind OFFLINE.")

#PREMIUM prÃ¼fen    
s.send_message(" #BÃ¼ro PREMIUM prÃ¼fen")
pre_check = ""; pre_z = []
if "premiumpass.txt" in files:
    if not OFFLINE:
        with open("./premiumpass.txt", "r", encoding="utf-8") as f:
            x = f.read()
        pre_check = bÃ¼.web_content("https://lkunited.pythonanywhere.com/checkerP", {"message":x, "pw":"lkunited"})
        if "True" in pre_check:
            PREMIUM = True
            pre_z = list(pre_check.split(";*;"))[1].split(":")
        else:
            ILLEGAL = True
    else:
        PREMIUM = False

#PIN lesen
s.send_message(" #BÃ¼ro-PIN auslesen")
with open(BPATH+"PIN_opt.txt", "r") as PIN_opt:
    act = PIN_opt.read()
with open(BPATH+"PIN_l.txt", "r") as PIN_l:
    lenge = int(PIN_l.read())
try:
    with open(BPATH+"PIN.txt", "r") as PIN_f:
        PIN_e = PIN_f.read()
except:   
    PIN_e, lenge = bÃ¼.PIN_erstellen()

#weitere Daten lesen und aufbereiten    
s.send_message(" #weitere Daten vorbereiten und auslesen")
a = bÃ¼.checkLogActive()
if a:
    dLg.cancel_()
with open(BPATH+"tipps.txt", "r", encoding="utf-8") as f:
    tipps = list(f.read().split("#*#"))
with open(BPATH+"agb.txt", "r") as f:
    if f.read() == "False":
        AGB = False
with open(BPATH+"menu.txt", "r", encoding="utf-8") as f:
    for i in f.read().split("#*#"):
        if i != "":
            PLUS.append(i)
try:
    with open(BPATH+"username.txt", "r", encoding="utf-8") as f:
        USER = f.read()
except:
    USER = "RANDOM_NAME_NO_PROFILE_"+str(randint(10**4, 10**5-1))

#Erfolge initialisieren
s.send_message(" #Erfolgsdaten initialisieren")
with open(BPATH+"achievements.txt", "r", encoding="utf-8") as f:
    achievements, unlocked = f.read().split("#*#")
achievements = achievements.split(" ")
for i in range(len(achievements)):
    achievements[i] = int(achievements[i])
unlocked = unlocked.strip().split(" ")
achs = [["Paketbote"], ["Baby", "AnfÃ¤nger", "Kenner", "Profi", "Experte", "Topuser"], ["Kunde", "Bankier", "Investor"],\
        ["Sender", "Vielsender", "Mailfanatiker"], ["EmpfÃ¤nger", "VielempfÃ¤nger"],\
        ["Klassenmitglied", "Klassenbester", "Student"],\
        ["Multitalent", "Allzweckgelehrter"],\
        ["Pluginliebhaber"], ["Ungeduldiger"], ["Getaufter"],\
        ["Offline"], ["MillionÃ¤r"], ["Entdecker"], ["Partygast"], ["Akzeptant"],\
        ["TreuerKunde"],\
        ["Greenhorn", "Neuling", "Lernender", "Fortgeschrittener", "KÃ¶nner", "Meister"]]; gesamt = 35
needs = [[10], [3, 10, 100, 200, 1000, 2000], [3, 10, 50], [1, 20, 50],\
         [1, 20], [1, 1000, 1000000],\
         [3, 5], [2], [True], [True], [True], [True], [True], [True], [True],\
         [True],\
         [1, 3, 5, 10, 20, 25]]
texts = ["(installiere {} Pakete)", "(fÃ¼hre BÃ¼ro {} mal aus)", "(habe {}â‚¬ auf der BÃ¼roBank)", "(sende {} Mails)",\
         "(empfange {} Mails)", "(habe {} LateinTrainer-Punkte)", "(installiere Pakete aus {} Bereichen)",\
         "(installiere {} Plugins)", "(teste eine BETA-Funktion)", "(habe einen Nutzernamen)", "(gehe offline - 'nicht ernsthaft, oder?!')",\
         "(buche PREMIUM)", "(das ist geheim)", "(sei beim JubilÃ¤umsspecial dabei)", "(akzeptiere die AGB)",\
         "(bleibe bis zuletzt dabei)", "(schalte {} Erfolge frei)"]
#Target-Liste
if "BÃ¼roBank" in installiert:
    with open("./programdata/bank/konto.txt", "r") as f:
        kontostand_e = float(f.read())
else:
    kontostand_e = 0
if "BÃ¼roMail" in installiert:
    sentMails_e = len(os.listdir("./programdata/mail/sent"))
    recievedMails_e = bÃ¼.countFiles("./programdata/mail/inbox")
else:
    sentMails_e = 0
    recievedMails_e = 0
if "LTP Agent" in installiert:
    with open("./programdata/ltp/savedData.txt", "r", encoding="utf-8") as f:
        ltpScore_e = int(f.read().split("#*#")[1])
else:
    ltpScore_e = 0
targets = [len(installiert), achievements[0], kontostand_e, sentMails_e,\
           recievedMails_e, ltpScore_e,\
           len(bereiche), len(plugin), FLAG,\
           not "RANDOM" in USER, OFFLINE, PREMIUM, False, False,\
           AGB, __version__=="4.4.0", len(unlocked)]

#Erfolge prÃ¼fen und verleihen
s.send_message(" #Erfolge prÃ¼fen und verleihen")
achievements[0] += 1
for i in range(len(achs)):
    for j in range(len(achs[i])):
        target = targets[i]
        if target >= needs[i][j] and achs[i][j] not in unlocked:
            unlocked.append(achs[i][j]); targets[-1] += 1
            bÃ¼.display_achievement(achs[i][j])
            print(achs[i][j], texts[i].format(str(needs[i][j])))
            pysounds.fanfare()
with open(BPATH+"achievements.txt", "w", encoding="utf-8") as f:
    for i in achievements:
        f.write(str(i)+(" " if achievements.index(i) != len(achievements)-1 else "#*#"))
    for i in unlocked:
        f.write(str(i)+" ")

#Version und DeviceID-Daten auslesen
s.send_message(" #Version auslesen und Bootvorgang abschlieÃŸen")
with open(BPATH+"versioninfo.txt", "r") as versioninfo:
    version = versioninfo.read()
with open(BPATH+"deviceidstatic.txt", "r", encoding="utf-8") as f:
    devidst = True if f.read() == "True" else False
if devidst:
    with open(BPATH+"devid.txt", "r", encoding="utf-8") as f:
        DEVID = f.read(); DEVID_ = DEVID
else:
    with open(BPATH+"devid.txt", "r", encoding="utf-8") as f:
        DEVID_ = f.read()
    with open(BPATH+"devid.txt", "w", encoding="utf-8") as f:
        DEVID = version.split(".")[0]+"-"+str(randint(10000, 99999))+"-"+version.split(".")[1]+"."+version.split(".")[2]
        f.write(DEVID)

#Nutzer registrieren            
if not OFFLINE:
    if bÃ¼.web_content("https://lkunited.pythonanywhere.com/rU", {"message":USER, "pw": "lkunited", "devid": DEVID, "devidcheck": DEVID_, "version": version}) == "failed":
        py.alert("Web-Registrierung sicherheitsrelevanter Daten fehlgeschlagen.\nWenden Sie sich an den Kundenservice.", "rU-Fehler")
        dLg.entry("WEB-rU-Fehler")

#BueroOSFinishedFlag
py.alert("Bitte beachten Sie, dass Ihre Version nicht lÃ¤nger unterstÃ¼tzt wird.\n"+\
         "An einer neuen Version wird gearbeitt.", "Buero")
if not OFFLINE:
    if bÃ¼.web_content("https://lkunited.pythonanywhere.com/bueroOSFinishedFlag") == "True":
        if bÃ¼.buttonLog("Eine neue Version von BÃ¼ro ist verfÃ¼gbar: BueroOS!\nIhre Version wird nicht mehr unterstÃ¼tzt.", "BueroOS") != "Fortfahren":
            dLg.entry("BueroOS-Flag UP and User cancelled")
            bÃ¼.normal_quit()

#Debug
dLg.entrys(act, lenge, PIN_e, version, bereiche, werkzeuge, unterhaltung, medien, lernen, plugin, PREMIUM, pre_check,\
           ILLEGAL, installiert, bÃ¼, AGB, COLORS_, PLUS, unlocked, achievements, OFFLINE, USER, DEVID, devidst,\
           [bÃ¼.get_version(i) for i in PACKAGES], FLAG, pre_z, upgr, PACKAGES)

#variable Nachricht
try:
    if OFFLINE:
        bcolb = ""
        quit(code="exc")
    a = bÃ¼.web_content("https://lkunited.pythonanywhere.com/bueroMessage")
    bcol = cOl.bcol(a.split("%%")[0].lstrip('bcol-')) if "%%" in a else ""
    b = a.split("%%")[1]+cOl.RESET_ALL if "%%" in a else a
    bcolb = bcol + b
except:
    OFFLINE = True
    dLg.entry("Offline Mode")
print(bcolb); dLg.entry(bcolb)

#Specials
for i in os.listdir("./programdata/lkims"):
    pyimager.display("./programdata/lkims/"+i)
    print(i[0:-5])

#MenÃ¼
while True:
    try:
        if not PREMIUM:
            dLg.entry("Loading ad...")
            for i in range(1 if not ILLEGAL else 3):
                bÃ¼.getad(choice(bÃ¼.logListDir("./programdata/ads")), end="")
            if ILLEGAL:
                if bÃ¼.buttonLog("SIE SIND ILLEGAL! FAHREN SIE FORT ODER LÃ–SCHEN SIE IHREN PREMIUM-PASS.", "ILLEGAL", buttons=("LÃ–SCHEN", "WEITER")) == "LÃ–SCHEN":
                    os.remove("./premiumpass.txt");bÃ¼.restart()

        ## Platz fÃ¼r ANNOUNCEMENTS
        ## py.alert("Bitte beachten Sie, dass Sie in naher Zukunft nur noch Ã¼ber BÃ¼roMail an Gewinnspielen teilnehmen werden kÃ¶nnen.", "BÃ¼roMail")
        ## print("Es dÃ¼rfen hier auch Aktionen ausgefÃ¼hrt werden")   
         
    except IndexError:
        dLg.entry("NO ADS!!")
    except:
        dLg.entry("Error loading ad / sending beta feedback")
    finally:
        while True:
            if antwort == "TEST":
                antwort = "NOTEST"
                break
            dLg.entry("Main Menu"); 

            discover = randint(1, 77) if "Entdecker" not in unlocked else 0; dLg.entry(discover)
            if not skipwin:
                antwort = py.confirm("Welches unserer Programme wollen Sie nutzen?", "BÃ¼ro V" + version, buttons=bereiche+PLUS+(["KLICK ME"] if discover == 1 else [])+["Konfigurieren", "Quit"])
            dLg.entry(antwort)
            if not skip2 and not skipwin:
                if antwort in bereiche+["KLICK ME"]:
                    target = ["Erfolg freischalten"] if antwort == "KLICK ME" else ["JUBILÃ„UMS-SPECIAL"]
                    if antwort in name_container:
                        target = list_container[name_container.index(antwort)].copy()
                    antwort = py.confirm("Welches unserer Programme wollen Sie nutzen?", antwort, buttons=(target+["ZurÃ¼ck"]))
            else:
                skip2 = False
            dLg.entry(antwort)

            if antwort == "Erfolg freischalten":
                unlocked.append("Entdecker"); bÃ¼.display_achievement("Entdecker"); print(achs[-4][0], texts[-4])
                pysounds.fanfare()
                with open(BPATH+"achievements.txt", "a") as f:
                    f.write("Entdecker ")
            elif antwort == "JUBILÃ„UMS-SPECIAL":
                py.alert("Das Special ist leider nicht mehr verfÃ¼gbar.", "Fehler")
            elif antwort == "VerschlÃ¼sseler":
                bÃ¼.executePackage("./verschlÃ¼sseln.py")
            elif antwort == "Passwortgenerator":
                bÃ¼.executePackage("./Passwortgenerator.py")
            elif antwort == "Musik":
                bÃ¼.executePackage("./Musik.py")
            elif antwort == "Lebensmittel":
                bÃ¼.executePackage("./lebensmittel.py")
            elif antwort == "Rechnungen":
                bÃ¼.executePackage("./Rechnung.pyw")
            elif antwort == "Kaffee Manager":
                bÃ¼.executePackage("./kaffee.py")
            elif antwort == "Haustier":
                bÃ¼.executePackage("./Haustier.py")
            elif antwort == "Das groÃŸe Quiz":
                bÃ¼.executePackage("./quiz.py")
            elif antwort == "Ballonfahrt":
                antwort2 = bÃ¼.buttonLog("Single- oder Multiplayer?", "Ballonfahrt", buttons=("Single", "Multi", "ZurÃ¼ck"))
                match antwort2:
                    case "Single":
                        bÃ¼.executePackage("./Ballonfahrt.py")
                    case "Multi":
                        antwort3 = bÃ¼.buttonLog("Wollen Sie die Verbindung im lokalen Netzwerk herstellen oder verbunden werden?", "Ballonfahrt-2P", buttons=("Aktiv", "Passiv"))
                        dLg.entry(antwort3)
                        if antwort3 == "Aktiv":
                            bÃ¼.executePackage("./Ballonfahrt-M2_1.py")
                        elif antwort3 == "Passiv":
                            bÃ¼.executePackage("./Ballonfahrt-M2_2.py")
                    case "ZurÃ¼ck":
                        continue
                    case _:
                        bÃ¼.error_quit()
            elif antwort == "im Verlies":
                antwort2 = bÃ¼.buttonLog("WÃ¤hlen Sie eine der folgenden Optionen:", "im Verlies",\
                                        buttons=("im Verlies", "im Verlies - Level-editor", "ZurÃ¼ck"))
                match antwort2:
                    case "im Verlies":
                        bÃ¼.executePackage("./quest.py")
                    case "im Verlies - Level-editor":
                        bÃ¼.executePackage("./level-editor.py")
                    case "ZurÃ¼ck":
                        continue
                    case _:
                        bÃ¼.error_quit()
            elif antwort == "SchingSchangSchongIQ":
                bÃ¼.executePackage("./SchingSchangSchongIntelligent.py")
            elif antwort == "Garten im GlÃ¼ck":
                bÃ¼.executePackage("./Garten-im-GlÃ¼ck.py")
            elif antwort == "abstrakte Verzerrung":
                bÃ¼.executePackage("./abstrakt.py")
            elif antwort == "Die Ritter - Launcher":
                py.alert("Diese Option ist noch nicht bereit.", "Fehler")
            elif antwort == "BÃ¼roMail":
                if not skipwin:
                    antwort5 = bÃ¼.buttonLog("Wollen Sie mit dem Hauptprogramm Mails lesen/senden oder den BackgroundAgent aktivieren,\num Ihren Posteingang im Hintergrund Ã¼berprÃ¼fen zu lassen?",\
                                            "BÃ¼roMail", ("BÃ¼roMail", "BackgroundAgent", "ZurÃ¼ck"))
                else:
                    skipwin = False
                    antwort5 = "BÃ¼roMail"
                    dLg.entrys(antwort5, "called via skipwin mode")
                    py.alert("BÃ¼roMail wird gestartet, um die Mail zu senden.", "BÃ¼roMail")
                if antwort5 == "BÃ¼roMail":
                    if bÃ¼.PIN_check(PIN_e, lenge, act):
                        bÃ¼.executePackage("./mail.py")
                elif antwort5 == "BackgroundAgent":
                    def a():
                        bÃ¼.executePackage("./mail_agent.pyw")
                    threading.Thread(target=a).start()
            elif antwort == "BÃ¼roBank":
                if skipwin:
                    skipwin = False
                    dLg.entry("BÃ¼roBank called via skipwin mode")
                    py.alert("BÃ¼roBank wird gestartet, um die Ãœberweisung zu tÃ¤tigen.", "BÃ¼roBank")
                if bÃ¼.PIN_check(PIN_e, lenge, act):
                    bÃ¼.executePackage("./bank.py")
            elif antwort == "BÃ¼roBonus":
                bÃ¼.executePackage("./bonus.py")
            elif antwort == "LTP Agent":
                bÃ¼.executePackage("./ltp_agent.py")
            elif antwort == "GoodFood":
                bÃ¼.executePackage("./goodFood.py")
            elif antwort == "Konfigurieren":
                if not AGB:
                    if py.confirm("Sie haben unseren Nutzungsbedingungen nicht zugestimmt. Stimmen Sie zu?", "AGB", buttons=("JA", "NEIN")) == "JA":
                        with open(BPATH+"agb.txt", "w") as f:
                            f.write("True")
                        AGB = True
                    else:
                        continue
                while True:
                    if not skipagb and not skipwin:
                        antwort2 = py.confirm("Mit welchem der folgenden Bereiche wollen Sie fortfahren?", "Konfiguration", buttons=konfig)
                        dLg.entry(antwort2)
                    else:
                        skipagb = False
                    if antwort2 != "ZurÃ¼ck":
                        while True:
                            if not skip and not skipwin:
                                antwort3 = py.confirm("Welche der Optionen wollen Sie nutzen?", antwort2, buttons=buttons[konfig.index(antwort2)]+["ZurÃ¼ck"])
                            else:
                                skip = False
                            dLg.entry(antwort3); 
                            if antwort3 == "Update":
                                if bÃ¼.PIN_check(PIN_e, lenge, act):
                                    try:
                                        update.update()
                                    except:
                                        dLg.entry("Fehler bei Updatevorgang")
                                        bÃ¼.error_quit()
                            elif antwort3 == "Upgrade":
                                if bÃ¼.PIN_check(PIN_e, lenge, act):
                                    try:
                                        update.update(alter="Upgrade")
                                    except:
                                        dLg.entry("Fehler bei Upgradevorgang")
                                        bÃ¼.error_quit()
                            elif antwort3 == "Systemupdate":
                                if bÃ¼.PIN_check(PIN_e, lenge, act):
                                    try:
                                        os.system("py ./systemupdate.py")
                                    finally:
                                        skip = True; antwort3 = "Aktualisieren"; print("Aktualisierung gestartet...")
                            elif antwort3 == "Hintergrundsystemupdate":
                                if bÃ¼.buttonLog("Dies installiert ein Update fÃ¼r die Systemupdate-Funktion.", "Hintergrundsystemupdate") == "Fortfahren":
                                    pf = askopenfilename(title="Zip-Datei mit Update auswÃ¤hlen", filetypes=[("ZIP comprimized folder", "*.zip")])
                                    dLg.entry(pf)
                                    with zipfile.ZipFile(pf, "r") as zipRef:
                                        zipRef.extractall("./programdata/update")
                                    os.remove("./systemupdate.py")
                                    shutil.move("./programdata/update/systemupdate.py", "./systemupdate.py")
                                    py.alert("Update erfolgreich installiert!", "Hintergrundsystemupdate")
                            elif antwort3 == "Aktualisieren":
                                bÃ¼.updates([""]+PACKAGES)
                                print("Pakete aktualisiert...")
                                for i in bÃ¼.logListDir("./programdata/ads"):
                                    if i not in adlist:
                                        os.remove("./programdata/ads/" + i)
                                print("Anzeigen aktualisiert...")
                                for i in bÃ¼.logListDir("./programdata/win"):
                                    if i not in winlist:
                                        os.remove("./programdata/win/"+i)
                                print("Gewinnspiele aktualisiert...")
                                for i in bÃ¼.logListDir("./programdata/lkims"):
                                    if i not in lklist:
                                        os.remove("./programdata/lkims/"+i)
                                print("Specials aktualisiert...\nVorgang abschlieÃŸen...")
                                bÃ¼.restart()
                            elif antwort3 == "Update herunterladen":
                                if bÃ¼.web_update("https://lkunited.pythonanywhere.com/bueroVersion"):
                                    if bÃ¼.buttonLog("Wollen Sie das Update nun installieren?", "Update", ("JA", "NEIN")) == "JA":
                                        skip = True; antwort3 = "Update"
                            elif antwort3 == "Notizen":
                                try:
                                    with open(BPATH+"notizen.txt", "r") as f:
                                        notizen = f.read()
                                except:
                                    with open(BPATH+"notizen.txt", "x") as f:
                                        f.write("")
                                    notizen = ""
                                finally:
                                    notizen_ = py.prompt("Notizen eingeben", "Notizen", notizen)
                                    if notizen_ == None:
                                        notizen_ = notizen
                                    with open(BPATH+"notizen.txt", "w") as f:
                                        f.write(notizen_)
                            elif antwort3 == "VersionInfo":
                                vs = bueroUtils.status("VersionInfo", colors=COLORS, tcolors=TCOLORS, parts=len(installiert)+2)
                                alerttext = "Sie haben folgende Versionen:\n\nBÃ¼ro: " + version + "\n\n"
                                vs.init_one_bar()
                                vs.draw_one_bar()
                                uglCount = 0
                                for i in installiert+["System"]:
                                    filename = BPATH+"versioninfo_" + i + ".txt"
                                    with open(filename, "r") as r:
                                        read = r.read().rstrip(" (zurÃ¼ckgesetzt-installieren Sie ein Update)")
                                    newest = bÃ¼.web_content("https://lkunited.pythonanywhere.com/readPackageVersion", {"package": i})
                                    alerttext += i + ": " + read + " (neueste: " + newest + ")\n"
                                    vs.draw_one_bar()
                                    if read != newest:
                                        uglCount += 1
                                vs.draw_one_bar()
                                vs.finish_one_bar()
                                alerttext += "\n"+str(uglCount)+" Updates verfÃ¼gbar oder empfohlen"
                                if bÃ¼.buttonLog(alerttext, "VersionInfo", ["ZurÃ¼ck", "Jetzt anfordern"]) == "Jetzt anfordern":
                                    skip = True; antwort2 = "Shopping & Weiteres"; antwort3 = "Anfordern";
                            elif antwort3 == "UpgradeInfo":
                                alerttext = "Sie kÃ¶nnen folgende Pakete anfordern (und mit der Upgrade-Funktion installieren):\n"
                                for i in upgr:
                                    alerttext = alerttext + i + "\n"
                                if upgr == []:
                                    py.alert("Keine Aktualisierungen vorhanden.", "UpgradeInfo")
                                else:
                                    antwort4 = bÃ¼.buttonLog(alerttext, "UpgradeInfo", ("Jetzt anfordern", "Jetzt installieren", "ZurÃ¼ck"))
                                    if antwort4 == "Jetzt installieren":
                                            skip = True; antwort2 = "Tools"; antwort3 = "Upgrade"
                                    elif antwort4 == "Jetzt anfordern":
                                            skip = True; antwort2 = "Shopping & Weiteres"; antwort3 = "Anfordern"
                            elif antwort3 == "BÃ¼roUpdateInfo":
                                if not OFFLINE:
                                    v_a = bÃ¼.web_content("https://lkunited.pythonanywhere.com/bueroVersion").split("#**"+"*#")[0]
                                    if v_a == version:
                                        py.alert("Sie sind auf dem neuesten Stand.", "BueroUpdateInfo")
                                    else:
                                        antwort4 = bÃ¼.buttonLog("Ihre Version: "+version+"\naktuellste Version: "+v_a, "BueroUpdateInfo", ("ZurÃ¼ck", "Jetzt aktualisieren", "Jetzt anfordern", "Jetzt herunterladen"))
                                        if antwort4 == "Jetzt aktualisieren":
                                            skip = True; antwort2 = "Tools"; antwort3 = "Update"
                                        elif antwort4 == "Jetzt anfordern":
                                            skip = True; antwort2 = "Shopping & Weiteres"; antwort3 = "Anfordern"; get_package = "BÃ¼ro, "+v_a
                                        elif antwort4 == "Jetzt herunterladen":
                                            skip = True; antwort2 = "Tools"; antwort3 = "Update herunterladen"
                                else:
                                    py.alert("Sie sind offline.", "Netzwerkfehler")
                            elif antwort3 == "Coming Soon":
                                up_list = ["im Verlies - levelEditor EasyMode", "Haustier - BÃ¶rse2"];addtext = ""
                                for i in up_list:
                                    addtext += "\n+" + i
                                neu_list = ["Flappy Bird", "VerschlÃ¼sseln 7*"];addtext2 = ""
                                for i in neu_list:
                                    addtext2 += "++" + i + "\n"
                                py.alert("Folgende Pakete werden bald erscheinen:\n"+addtext2+"Folgende wichtige Updates sind geplant:"+addtext, "Coming Soon")
                            elif antwort3 == "What's new?":
                                py.alert("Neu:\nMit diesem Update wurden einige kleinere Fehler behoben.\n"+\
                                         "Zudem wurden experimentelle Features entfernt, sodass BÃ¼ro nun wieder schneller lÃ¤uft.\n"+\
                                         "AuÃŸerdem gibt es einen neuen Erfolg.", "What's new?")
                            elif antwort3 == "Tipps":
                                antwort4 = "Noch ein Tipp"
                                while antwort4 == "Noch ein Tipp":
                                    antwort4 = bÃ¼.buttonLog(choice(tipps), "Tipp", ("Noch ein Tipp", "ZurÃ¼ck"))
                            elif antwort3 == "Anfordern":
                                if bÃ¼.PIN_check(PIN_e, lenge, act):
                                    anfordern = py.prompt("{Paket}, {Version} anfordern", "Anfordern", get_package)
                                    if anfordern != None:
                                        try:
                                            spl = anfordern.split(", ")
                                            with open("./downloadedPackage_"+spl[0]+spl[1]+".zip", "wb") as f:
                                                dwl = requests.get("https://buero-os-toolkit-development.github.io/bueroWebsite/data/" + spl[0] + spl[1] + ".zip").content
                                                if "<!DOCTYPE"+" html>" in str(dwl):
                                                    raise ValueError()
                                                f.write(dwl)
                                            match bÃ¼.buttonLog(anfordern+" erfolgreich heruntergeladen.", "Erfolg", ["ZurÃ¼ck", "Jetzt updaten", "Jetzt upgraden"]):
                                                case "Jetzt updaten":
                                                    antwort2 = "Tools"; antwort3 = "Update"; skip = True
                                                case "Jetzt upgraden":
                                                    antwort2 = "Tools"; antwort3 = "Upgrade"; skip = True
                                                case _:
                                                    py.alert("Das Update wurde unter dem Namen downloadedPackage_"+spl[0]+spl[1]+" gespeichert.", "Erfolg")
                                        except:
                                            py.alert(anfordern+" ist nicht verfÃ¼gbar.\nVielleicht gibt es eine neuere Version oder Sie haben den Paketsbezeichner falsch geschrieben.\nEine BÃ¼roMail wird gesendet.", "Fehler")
                                            bÃ¼.createPreMail("The Creator", "Anfordern", f"Ich mÃ¶chte hiermit {anfordern} anfordern.")
                                            get_package = ""
                                            antwort3 = "ZurÃ¼ck"; antwort2 = "ZurÃ¼ck"; antwort = "BÃ¼roMail"; skipwin = True; break
                            elif antwort3 == "Releases abonnieren":
                                if bÃ¼.PIN_check(PIN_e, lenge, act):
                                    bÃ¼.createPreMail("The Creator", "Abo", "Ich mÃ¶chte alle erscheinenden Versionen von BÃ¼ro kostenlos zugesandt bekommen und bin mit den Bedingungen einverstanden.")
                                    antwort3 = "ZurÃ¼ck"; antwort2 = "ZurÃ¼ck"; antwort = "BÃ¼roMail"; skipwin = True; break
                            elif antwort3 == "BÃ¼ro PREMIUM":
                                if bÃ¼.PIN_check(PIN_e, lenge, act):
                                    if PREMIUM:
                                        antwort4 = bÃ¼.buttonLog(f"Sie haben BÃ¼ro PREMIUM bis {pre_z} (Jahr, Monat) gebucht.", "PREMIUM vorhanden", ("ZurÃ¼ck", "PREMIUM verlÃ¤ngern", "PREMIUM erneuern"))
                                        if antwort4 == "PREMIUM verlÃ¤ngern":
                                            monat = py.prompt("Um wie viele Monate wollen Sie BÃ¼ro PREMIUM verlÃ¤ngern?\nKosten: 1,69 â‚¬ pro Monat", "PREMIUM verlÃ¤ngern")
                                            if monat != None:
                                                monat = int(monat)
                                                new_date = [0, 0];preis = 0;new_year = int(pre_z[0])
                                                if monat > 0 and monat < 13:
                                                    new_month = int(pre_z[1])
                                                    while monat > 0:
                                                        preis += 1.69
                                                        if new_month < 12:
                                                            new_month += 1
                                                        else:
                                                            new_month = 1
                                                            new_year += 1
                                                        monat -= 1
                                                    new_date = [str(new_year), str(new_month)]
                                                    preis += monat * 1.69
                                                    match bÃ¼.buttonLog("Wollen Sie Ã¼ber BÃ¼roBank Ã¼berweisen oder Ihre Buchung verbindlich Ã¼ber BÃ¼roMail ankÃ¼ndigen?", "Zahlung", ["BÃ¼roBank", "BÃ¼roMail"]):
                                                        case "BÃ¼roBank":
                                                            py.alert("Die Buchung kann einige Zeit in Anspruch nehmen.\nSie erhalten Ihren Pass Ã¼ber BÃ¼roMail.", "Buchung")
                                                            bÃ¼.createPreBank("The Creator", str(preis) + " â‚¬", f"Ich mÃ¶chte BÃ¼ro PREMIUM verbindlich fÃ¼r {str(preis)}â‚¬ bis {new_date} verlÃ¤ngern. Hier mein Geld.")
                                                            antwort3 = "ZurÃ¼ck"; antwort2 = "ZurÃ¼ck"; antwort = "BÃ¼roBank"; skipwin = True; break
                                                        case "BÃ¼roMail":
                                                            py.alert("Die Buchung kann einige Zeit in Anspruch nehmen.\nSie erhalten Ihren Pass Ã¼ber BÃ¼roMail.", "Buchung")
                                                            bÃ¼.createPreMail("The Creator", "BÃ¼ro PREMIUM verlÃ¤ngern", f"Ich mÃ¶chte BÃ¼ro PREMIUM verbindlich fÃ¼r {str(preis)}â‚¬ bis {new_date} verlÃ¤ngern.")
                                                            antwort3 = "ZurÃ¼ck"; antwort2 = "ZurÃ¼ck"; antwort = "BÃ¼roMail"; skipwin = True; break
                                                else:
                                                    py.alert("Fehlerhafte Eingabe!", "Fehler")
                                            else:
                                                py.alert("Vorgang abgebrochen!", "Abbruch")
                                        elif antwort4 == "PREMIUM erneuern":
                                            toBook = True
                                    else:
                                        antwort4 = bÃ¼.buttonLog("BÃ¼ro PREMIUM fÃ¼r 1,69â‚¬ fÃ¼r diesen Monat buchen oder Gutscheincode nutzen?", "PREMIUM nicht vorhanden", ("Buchen", "Gutschein", "ZurÃ¼ck"))
                                        if antwort4 == "Buchen":
                                            match bÃ¼.buttonLog("Wollen Sie Ã¼ber BÃ¼roBank Ã¼berweisen oder Ihre Buchung verbindlich Ã¼ber BÃ¼roMail ankÃ¼ndigen?", "Zahlung", ["BÃ¼roBank", "BÃ¼roMail"]):
                                                case "BÃ¼roBank":
                                                    py.alert("Die Buchung kann einige Zeit in Anspruch nehmen.\nSie erhalten Ihren Pass Ã¼ber BÃ¼roMail.", "Buchung")
                                                    bÃ¼.createPreBank("The Creator", "1.69 â‚¬", "Ich mÃ¶chte fÃ¼r 1.69â‚¬ BÃ¼ro Premium verbindlich fÃ¼r diesen Monat kaufen. Hier mein Geld.")
                                                    antwort3 = "ZurÃ¼ck"; antwort2 = "ZurÃ¼ck"; antwort = "BÃ¼roBank"; skipwin = True; break
                                                case "BÃ¼roMail":
                                                    py.alert("Die Buchung kann einige Zeit in Anspruch nehmen.\nSie erhalten Ihren Pass Ã¼ber BÃ¼roMail.", "Buchung")
                                                    bÃ¼.createPreMail("The Creator", "BÃ¼ro Premium buchen", "Ich mÃ¶chte fÃ¼r 1.69â‚¬ BÃ¼ro Premium verbindlich fÃ¼r diesen Monat kaufen.")
                                                    antwort3 = "ZurÃ¼ck"; antwort2 = "ZurÃ¼ck"; antwort = "BÃ¼roMail"; skipwin = True; break
                                        elif antwort4 == "Gutschein":
                                            toBook = True
                                    if toBook and bÃ¼.buttonLog("Die PREMIUM-Buchung wird initiiert.\nBitte bestÃ¤tigen:") == "Fortfahren":
                                        toBook = False
                                        if not OFFLINE:
                                            if bÃ¼.buttonLog("Wollen Sie einen Gutscheincode oder einen Pass angeben?", "Code", ("Gutscheincode", "Pass")) == "Gutscheincode":
                                                a = bÃ¼.web_content("https://lkunited.pythonanywhere.com/checkerC", {"message": py.prompt("Gutscheincode eingeben:", "Code"), "pw": "lkunited"})
                                            else:
                                                a = py.prompt("Pass eingeben:", "Pass")
                                            if a != "INCORRECT" and a != "FALSE":
                                                py.alert(f"Ihr ermittelter Pass:\n{a}", "Gutscheincode eingelÃ¶st")
                                                a = a.format(py.prompt("Geben Sie Ihren Namen ein, um den Pass zu vervollstÃ¤ndigen.", "Name", USER)); dLg.entry(a)
                                                with open("./premiumpass.txt", "w", encoding="utf-8") as f:
                                                    f.write(a)
                                                bÃ¼.restart()
                                            else:
                                                py.alert(a, "Error")
                                        else:
                                            py.alert("Sie sind offline", "Netzwerkfehler")
                            elif antwort3 == "Gewinnspiele":
                                if bÃ¼.PIN_check(PIN_e, lenge, act):
                                    while True:
                                        games = os.listdir("./programdata/win"); dLg.entry(games)
                                        for i in range(len(games)):
                                            games[i] = games[i].rstrip(".txt")
                                        game = bÃ¼.buttonLog("Welches der installierten Gewinnspiele wollen Sie wÃ¤hlen?\n"+\
                                                          "Neue Gewinnspiele werden bei Updates automatisch hinzugefÃ¼gt oder kÃ¶nnen mit der Fehleranalyse eingespielt werden.", "Gewinnspiele", games+["ZurÃ¼ck"])
                                        if game != "ZurÃ¼ck":
                                            with open("./programdata/win/"+game+".txt", "r", encoding="utf-8") as gdata:
                                                toWin, maxTime, addInf = gdata.read().split("#**#")
                                            antwort4 = bÃ¼.buttonLog(f"Informationen zu gewÃ¤hltem Gewinnspiel:\nmÃ¶gliche Gewinne: {toWin}\nDeadline: {maxTime}\nandere Informationen: {addInf}", "Gewinnspiel", ("Teilnehmen", "LÃ¶schen", "ZurÃ¼ck"))
                                            if antwort4 == "Teilnehmen":
                                                if not "BÃ¼roMail" in installiert:
                                                    py.alert("Sie benÃ¶tigen BÃ¼roMail zur Teilnahme!", "Fehler")
                                                else:
                                                    bÃ¼.createPreMail("The Creator", "Gewinnspiel", "Ich mÃ¶chte am aktuellen Gewinnspiel teilnehmen."+\
                                                                     "Der Verifikationscode lautet {}. Meine Daten sind {}.".format(game, str(version)+";"+(str(pre_z) if PREMIUM else "kein PREMIUM")))
                                                    py.alert("Ã–ffnen Sie BÃ¼roMail, um teilzunehmen.\nBitte beachten Sie, dass Sie bei mehreren Gewinnspielen nur hintereinander teilnehmen kÃ¶nnen.")
                                                    antwort3 = "ZurÃ¼ck"; antwort2 = "ZurÃ¼ck"; antwort = "BÃ¼roMail"; skipwin = True; break
                                            elif antwort4 == "LÃ¶schen":
                                                os.remove("./programdata/win/"+game+".txt")
                                        else:
                                            break
                            elif antwort3 == "Feedback & FunktionsvorschlÃ¤ge":
                                bÃ¼.shareViaMail("The Creator", "Feedback/neue Funktion", py.prompt("Feedback/FunktionsvorschlÃ¤ge eingeben", "Feedback"))
                            elif antwort3 == "AGB ablehnen":
                                if bÃ¼.PIN_check(PIN_e, lenge, act):
                                    if bÃ¼.buttonLog("Wirklich ablehnen? Sie werden nicht mehr auf die Einstellungen zugreifen kÃ¶nnen.") == "Fortfahren":
                                        dLg.entry("AGB ablehnend...")
                                        with open(BPATH+"agb.txt", "w") as f:
                                            f.write("False")
                                        AGB = False; antwort2 = "ZurÃ¼ck"; skipagb = True; break
                            elif antwort3 == "PIN Ã¤ndern":
                                if bÃ¼.PIN_check(PIN_e, lenge, act):
                                    PIN_e, lenge = bÃ¼.PIN_erstellen(PIN_e, lenge)
                            elif antwort3 == "PIN-Status Ã¤ndern":
                                if bÃ¼.PIN_check(PIN_e, lenge, act):
                                    with open(BPATH+"PIN_opt.txt", "r") as pin_opt:
                                        akt = pin_opt.read()
                                    if akt == "True":
                                        antwort4 = bÃ¼.buttonLog("PIN deaktivieren?", "PIN aktiv", ("JA", "NEIN"))
                                        if antwort4 == "JA":
                                            with open(BPATH+"PIN_opt.txt", "w") as pin_opt:
                                                pin_opt.write("False")
                                            act = "False"
                                    elif akt == "False":
                                        antwort4 = bÃ¼.buttonLog("PIN aktivieren?", "PIN inaktiv", ("JA", "NEIN"))
                                        if antwort4 == "JA":
                                            with open(BPATH+"PIN_opt.txt", "w") as pin_opt:
                                                pin_opt.write("True")
                                            os.remove(BPATH+"PIN.txt")
                                            py.alert("Ihre PIN wurde zurÃ¼ckgesetzt.", "PIN aktiviert")
                                            bÃ¼.restart()
                                    else:
                                       pyimager.message.errorMessageB("Einige Daten sind fehlerhaft.\nEventuell wurden Sie gehackt.")
                            elif antwort3 == "Nutzernamen Ã¤ndern":
                                if bÃ¼.PIN_check(PIN_e, lenge, act) and not OFFLINE and bÃ¼.buttonLog("Bitte beachten Sie,\ndass dies alle auf Ihren Nutzernamen gespeicherten Daten lÃ¶scht.") == "Fortfahren":
                                    old_user = USER; try_user = old_user
                                    while try_user == old_user or bÃ¼.web_content("https://lkunited.pythonanywhere.com/cN", {"message": try_user, "pw": "lkunited"}) != "valid":
                                        try_user = py.prompt("Neuen Nutzernamen eingeben:\nHinweis: der Name darf nicht bereits existieren.", "Nutzernamen Ã¤ndern", try_user)
                                        if try_user == None:
                                            break
                                    if try_user != None:
                                        USER = try_user
                                        with open(BPATH+"username.txt", "w", encoding="utf-8") as f:
                                            f.write(USER)
                                        if BETA:
                                            requests.post("https://lkunited.pythonanywhere.com/rB", {"message": "-"+old_user, "pw": "lkunited", "devidcheck": DEVID})
                                            requests.post("https://lkunited.pythonanywhere.com/rB", {"message": USER, "pw": "lkunited", "devidcheck": DEVID})
                                        requests.post("https://lkunited.pythonanywhere.com/rU", {"message": "-"+old_user, "pw": "lkunited", "devidcheck": DEVID, "devid": DEVID})
                                        requests.post("https://lkunited.pythonanywhere.com/rU", {"message": USER, "pw": "lkunited", "devidcheck": DEVID, "devid": DEVID})
                                        py.alert("Neuen Nutzernamen erfolgreich registriert.", "Nutzernamen Ã¤ndern")
                                    else:
                                        py.alert("Sie haben den Vorgang abgebrochen.", "Vorgang abgebrochen")
                            elif antwort3 == "Nutzernamen ansehen":
                                if bÃ¼.buttonLog("Ihr Nutzername ist: "+USER, "Nutzernamen ansehen", ("ZurÃ¼ck", "Jetzt Ã¤ndern")) == "Jetzt Ã¤ndern":
                                    skip = True; antwort3 = "Nutzernamen Ã¤ndern"
                            elif antwort3 == "DeviceID ansehen":
                                if bÃ¼.PIN_check(PIN_e, lenge, act):
                                    if bÃ¼.buttonLog("Ihre DeviceID lautet:\n"+DEVID, "DeviceID ansehen", buttons=("Kopieren", "ZurÃ¼ck")) == "Kopieren":
                                        pyperclip.copy(DEVID)
                            elif antwort3 == "Online einloggen":
                                match bÃ¼.buttonLog("Wollen Sie das Login nur Ã¶ffnen oder auch einen Code generieren?", "Login", ("Code generieren", "Nur Login", "ZurÃ¼ck")):
                                    case "Code generieren":
                                        if bÃ¼.PIN_check(PIN_e, lenge, act) and not OFFLINE:
                                            code_ = bÃ¼.web_content("https://lkunited.pythonanywhere.com/getCode", {"username": USER,\
                                                                   "id": "True" if bÃ¼.web_content("https://lkunited.pythonanywhere.com/cB", {"message": USER, "pw": "lkunited"}) == "registered" else "False", "devid": DEVID, "password": "lkunited"})
                                            match bÃ¼.buttonLog("Ihr Code lautet:\n"+code_, "BestÃ¤tigungscode", buttons=("Einloggen", "Kopieren", "ZurÃ¼ck")):
                                                case "Kopieren":
                                                    pyperclip.copy(code_)
                                                case "Einloggen":
                                                    wb.open(f"https://lkunited.pythonanywhere.com/menu?counter=0&name={USER}&code={code_}")
                                        else:
                                            py.alert("Sie benÃ¶tigen Ihre PIN und eine Internetverbingung zum Online-Login!", "Fehler")
                                    case "Nur Login":
                                        wb.open("https://lkunited.pythonanywhere.com/login")
                                    case "ZurÃ¼ck":
                                        continue
                                    case _:
                                        bÃ¼.error_quit()
                            elif antwort3 == "Ãœber BÃ¼ro":
                                wb.open("https://lkunited.pythonanywhere.com/aboutBuero")
                            elif antwort3 == "statische DeviceID":
                                if bÃ¼.PIN_check(PIN_e, lenge, act):
                                    if bÃ¼.buttonLog("Sie haben {}eine statische DeviceID.\nWollen Sie das Ã¤ndern?\nHinweise:\nDie statische ID macht das Login fÃ¼r Sie zwar einfacher, aber auch unsicherer.\n".format("" if devidst else "k")+\
                                                    "Falls Sie eine statische DeviceID haben, sollten Sie diese regelmÃ¤ÃŸig auf die neueste Version aktualisieren.","statische DeviceID", buttons=("Ja", "Nein")) == "Ja":
                                        devidst = reverse(devidst)
                                        with open(BPATH+"deviceidstatic.txt", "w", encoding="utf-8") as f:
                                            f.write(str(devidst))
                            elif antwort3 == "DeviceID aktualisieren":
                                if not OFFLINE:
                                    if bÃ¼.PIN_check(PIN_e, lenge, act):
                                        devidold = DEVID
                                        DEVID = version.split(".")[0]+"-"+devidold.split("-")[1]+"-"+version.split(".")[1]+"."+version.split(".")[2]
                                        with open(BPATH+"devid.txt", "w", encoding="utf-8") as f:
                                            f.write(DEVID)
                                        if bÃ¼.web_content("https://lkunited.pythonanywhere.com/rU",\
                                           {"message":USER, "pw": "lkunited", "devid": DEVID, "devidcheck": devidold, "version": version}) == "success":
                                            py.alert(f"DeviceID erfolgreich aktualisiert.\nAlte DeviceID: {devidold}\nNeue DeviceID: {DEVID}", "DeviceID aktualisiert")
                                        else:
                                            py.alert("Aktualisierung der DeviceID fehlgeschlagen.", "Fehler")
                                else:
                                    py.alert("FÃ¼r diese Aktion benÃ¶tigen Sie eine Internetverbindung.", "OFFLINE")
                            elif antwort3 == "Status personalisieren":
                                x = []
                                for i in range(5):
                                    match i:
                                        case 0:
                                            use = "Diese Farbe wird fÃ¼r den Namen des Vorgangs und den Status der SpeicherInfo verwendet."
                                        case 1:
                                            use = "Diese Farbe wird fÃ¼r den aktuellen Vorgang bei allen Statusbalken verwendet."
                                        case _:
                                            use = "Diese Farbe wird fÃ¼r Statusbalken sowie Ampelfunktionen (z.B. SpeicherInfo) verwendet."
                                    y = py.prompt("WÃ¤hlen Sie die "+bÃ¼.numeral(i+1, sex="f")+" Farbe.\n"+use, "Personalisieren", COLORS_[i])
                                    try:
                                        cOl.col(y);x.append(y)
                                    except:
                                        x.append("WHITE")
                                with open(BPATH+"color.txt", "w") as f:
                                    for i in x:
                                        f.write(i+"#*#")
                                COLORS_ = x.copy();COLORS = COLORS_[0:2];TCOLORS = COLORS_[2:5]
                            elif antwort3 == "StartmenÃ¼ personalisieren":
                                x = []
                                for i in range(3):
                                    z = PLUS[i] if len(PLUS) > i else ""
                                    a = py.prompt("FÃ¼gen Sie bis zu drei personalisierte Optionen zum HauptmenÃ¼ hinzu.", "MenÃ¼ personalisieren", z)
                                    while a not in installiert and a != "":
                                        py.alert("Fehler!\nSie mÃ¼ssen die entsprechenden Pakete bereits installiert haben!\nVersuchen Sie es erneut.", "Fehler")
                                        a = py.prompt("FÃ¼gen Sie bis zu drei personalisierte Optionen zum HauptmenÃ¼ hinzu.", "MenÃ¼ personalisieren", z)
                                    x.append(a)
                                PLUS = x.copy()
                                with open(BPATH+"menu.txt","w", encoding="utf-8") as f:
                                    for i in PLUS:
                                        f.write(i+"#*#")
                                bÃ¼.restart()
                            elif antwort3 == "Erfolge ansehen":
                                for i in unlocked:
                                    bÃ¼.display_achievement(i)
                                    for j in range(len(achs)):
                                        if i in achs[j]:
                                            target = j; tgt2 = achs[j].index(i)
                                    print(i, texts[target].format(str(needs[target][tgt2]))); sleep(1.2)
                                if len(unlocked) == 0:
                                    print("Sie haben noch keine Erfolge freigeschaltet.")
                            elif antwort3 == "Fortschritt ansehen":
                                for i in range(len(achs)):
                                    for j in range(len(achs[i])):
                                        if achs[i][j] not in unlocked:
                                            bÃ¼.display_achievement("Hidden")
                                            print(achs[i][j], texts[i].format(str(needs[i][j]))); sleep(1.2)
                                            init_values = bÃ¼.round_agent(int(targets[i]), int(needs[i][j]))
                                            s = bÃ¼.status("Fortschritt: ", init_values[1], init_values[0], "+", colors=COLORS, tcolors=TCOLORS)
                                            s.send_message(" "+str(targets[i])+" von "+str(needs[i][j]))
                                if len(unlocked) == gesamt:
                                    print("Sie haben bereits alle Erfolge freigeschaltet.")
                            elif antwort3 == "schnelle Fehleranalyse":
                                try:
                                    os.system("python ./fehleranalyse.py")
                                except:
                                    print("Etwas ist schiefgelaufen...")
                            elif antwort3 == "PREMIUM funktioniert nicht":
                                anl = bÃ¼.buttonLog("Eventuell wurde Ihnen bereits ein neuer PREMIUM-Pass zugesandt.")
                                if anl == "JA":
                                    wb.open("mailto:leander@kafemann.berlin?subject=PREMIUM disfunktional&body==Mein gÃ¼ltiger PREMIUM-Pass funktioniert nicht.")
                                    py.alert("Bitte hÃ¤ngen Sie Ihren PREMIUM-Pass an.", "PREMIUM funktioniert nicht")
                            elif antwort3 in ["Debug-Log Ã¼bermitteln", "PIN vergessen", "Erfolge aktualisieren"]:
                                py.alert("Bitte nutzen Sie die Option in der schnellen Fehleranalyse.")
                            elif antwort3 == "aktuelles Log":
                                if bÃ¼.buttonLog("Wollen Sie das aktuelle Log {}?".format("aktivieren" if dLg.canceled else "deaktivieren"), "Log konfigurieren", ("JA", "NEIN")) == "JA":
                                    dLg.cancel_()
                            elif antwort3 == "jedes Log":
                                if bÃ¼.PIN_check(PIN_e, lenge, act):
                                    with open(BPATH+"log.txt", "r") as lg:
                                        lg_a = lg.read()
                                    if bÃ¼.buttonLog("Wollen Sie jedes Log {}?".format("aktivieren" if lg_a == "True" else "deaktivieren"), "Logs konfigurieren", ("JA", "NEIN")) == "JA":
                                        if str(dLg.canceled) == lg_a:
                                            dLg.cancel_()
                                        with open(BPATH+"log.txt", "w") as lg:
                                            lg.write(str(dLg.canceled))
                            elif antwort3 == "SpeicherInfo":
                                st = bÃ¼.status("SpeicherInfo: ", parts=len(installiert)+4, fill="~", colors=COLORS, tcolors=TCOLORS)
                                x = 5*"-";at = "\nFolgender Speicherplatz wird von den einzelnen Paketen belegt:\nBeispiel: {} GrÃ¶ÃŸe {} ( Programme - / Daten {} / Bilder {} / Audio {} )".format(14*"-", x, x, 4*"-", x)
                                in2 = installiert.copy();in2 += ["Events", "BÃ¼ro", "System", "Hintergrundsystem", "gesamt"]
                                ges5 = [];ges6 = [];ges7 = [];ges8 = [];ges9 = []
                                st.init_one_bar()
                                for i in in2:
                                    ges1 = 0;ges2 = 0;ges3 = 0;ges4 = 0
                                    st.draw_one_bar()
                                    if i == "VerschlÃ¼sseler":
                                        ges3 = bÃ¼.get_size("./shopping/images")
                                        ges1 = bÃ¼.get_sizes(["./verschlÃ¼sseln.py", "./shopping"]) - ges3                                   
                                        ges2 = bÃ¼.get_size("./programdata/verschlÃ¼sseln")
                                    elif i == "Haustier":
                                        ges1 = bÃ¼.get_size("./Haustier.py")
                                        ges2 = bÃ¼.get_sizes(["./programdata/haustier/saved", "./programdata/haustier/aktien"])
                                        ges4 = bÃ¼.get_size("./programdata/haustier/music")
                                    elif i == "Ballonfahrt":
                                        ges1 = bÃ¼.get_sizes(["./Ballonfahrt.py", "./Ballonfahrt-M2_1.py", "./Ballonfahrt-M2_2.py"])
                                        ges2 = bÃ¼.get_size("./programdata/ballonfahrt")
                                        ges3 = bÃ¼.get_sizes(balims, prepath="./images/")
                                    elif i == "SchingSchangSchongIQ":
                                        ges1 = bÃ¼.get_size("./SchingSchangSchongIntelligent.py")
                                        ges2 = bÃ¼.get_size("./programdata/schingschangschongiq")
                                    elif i == "abstrakte Verzerrung":
                                        ges1 = bÃ¼.get_size("./abstrakt.py")
                                        ges3 = bÃ¼.get_size("./programdata/abstrakt")
                                    elif i == "im Verlies":
                                        ges1 = bÃ¼.get_sizes(["./quest.py", "./level-editor.py"])
                                        ges2 = bÃ¼.get_size("./programdata/verlies")
                                        ges3 = bÃ¼.get_sizes(imlist, prepath="./images/")
                                    elif i == "Passwortgenerator":
                                        ges1 = bÃ¼.get_size("./Passwortgenerator.py")
                                        ges2 = bÃ¼.get_size("./programdata/password")
                                    elif i == "Musik":
                                        ges1 = bÃ¼.get_size("./Musik.py")
                                        ges2 = bÃ¼.get_size("./programdata/music")
                                    elif i == "Garten im GlÃ¼ck":
                                        ges1 = bÃ¼.get_size("./Garten-im-GlÃ¼ck.py")
                                        ges3 = bÃ¼.get_sizes(gigims, prepath="./images/")
                                    elif i == "Lebensmittel":
                                        ges1 = bÃ¼.get_size("./lebensmittel.py")
                                        ges2 = bÃ¼.get_size("./programdata/lebensmittel")
                                    elif i == "Das groÃŸe Quiz":
                                        ges1 = bÃ¼.get_size("./quiz.py")
                                        ges4 = bÃ¼.get_sizes(quizmusic, prepath="./music/")
                                    elif i == "Rechnungen":
                                        ges1 = bÃ¼.get_size("./Rechnung.pyw")
                                        ges3 = bÃ¼.get_size("./programdata/rechnungen/rechnung.ico")
                                        ges2 = bÃ¼.get_size("./programdata/rechnungen") - ges3
                                    elif i == "BÃ¼roMail":
                                        ges1 = bÃ¼.get_sizes(["./mail.py", "./mail_agent.pyw"])
                                        ges2 = bÃ¼.get_size("./programdata/mail")
                                    elif i == "BÃ¼roBank":
                                        ges1 = bÃ¼.get_size("./bank.py")
                                        ges3 = bÃ¼.get_size("./programdata/bank/money.ico")
                                        ges2 = bÃ¼.get_size("./programdata/bank") - ges3
                                    elif i == "LTP Agent":
                                        ges1 = bÃ¼.get_size("./ltp_agent.py")
                                        ges2 = bÃ¼.get_size("./programdata/ltp")
                                    elif i == "BÃ¼roBonus":
                                        ges1 = bÃ¼.get_size("./bonus.py")
                                        ges2 = bÃ¼.get_size("./programdata/bonus")
                                    elif i == "Kaffee Manager":
                                        ges1 = bÃ¼.get_size("./kaffee.py")
                                        ges2 = bÃ¼.get_size("./programdata/kaffee")
                                    elif i == "GoodFood":
                                        ges1 = bÃ¼.get_size("./goodFood.py")
                                        ges2 = bÃ¼.get_size("./programdata/goodFood")
                                    elif i == "Events":
                                        ges3 = bÃ¼.get_sizes(["./programdata/ads", "./programdata/lkims"])
                                        ges2 = bÃ¼.get_size("./programdata/win")
                                        if PREMIUM:
                                            ges2 += bÃ¼.get_size("./premiumpass.txt")
                                    elif i == "BÃ¼ro":
                                        ges1 = bÃ¼.get_sizes(["./bÃ¼ro.py", "./bueroUtils.py"])
                                        ges2 = bÃ¼.get_sizes(["./programdata/buero", "./programdata/run"])
                                        ges3 = bÃ¼.get_size("./programdata/achievements")
                                    elif i == "System":
                                        ges1 = bÃ¼.get_sizes(["./fehleranalyse.py", "./update.py"])
                                        ges2 = bÃ¼.get_size("./programdata/update")
                                    elif i == "Hintergrundsystem":
                                        ges1 = bÃ¼.get_size("./systemupdate.py")
                                    elif i == "gesamt":
                                        ges1 = listToInt(ges5)
                                        ges2 = listToInt(ges6)
                                        ges3 = listToInt(ges7)
                                        ges4 = listToInt(ges8)
                                    ges5.append(ges1);ges6.append(ges2);ges7.append(ges3);ges8.append(ges4)
                                    ges9.append(ges1+ges2+ges3+ges4)
                                ges9Compare = ges9.copy()
                                ges9Compare.remove(max(ges9Compare))
                                for i in in2:
                                    idx = in2.index(i)
                                    a = ges5[idx];b = ges6[idx];c = ges7[idx];d = ges8[idx];e = ges9[idx]
                                    at += "\n"+i+": "+(22-len(i))*"-"+" "+bÃ¼.trafficer(e, min(ges9Compare), max(ges9Compare), duo=False, mthd=nsize, traffic_col=TCOLORS)+cOl.RESET_ALL+" "+(10-len(nsize(e)))*"-"+\
                                          " ( "+bÃ¼.trafficer(a, min(ges5), max(ges5[0:-1]), duo=False, mthd=nsize, traffic_col=TCOLORS)+cOl.RESET_ALL+" "+(10-len(nsize(a)))*"-"+\
                                          " / "+bÃ¼.trafficer(b, min(ges6), max(ges6[0:-1]), duo=False, mthd=nsize, traffic_col=TCOLORS)+cOl.RESET_ALL+" "+(10-len(nsize(b)))*"-"+\
                                          " / "+bÃ¼.trafficer(c, min(ges7), max(ges7[0:-1]), duo=False, mthd=nsize, traffic_col=TCOLORS)+cOl.RESET_ALL+" "+(10-len(nsize(c)))*"-"+\
                                          " / "+bÃ¼.trafficer(d, min(ges8), max(ges8[0:-1]), duo=False, mthd=nsize, traffic_col=TCOLORS)+cOl.RESET_ALL+" "+(10-len(nsize(d)))*"-"+" )"
                                st.finish_one_bar()
                                print(at)
                            elif antwort3 == "Deinstallieren":
                                if bÃ¼.PIN_check(PIN_e, lenge, act):
                                    deinstalllist = installiert.copy()
                                    deinstalllist.append("BÃ¼ro");deinstalllist.append("Quit")
                                    antwort4 = bÃ¼.buttonLog("Welches der installierten Programme wollen Sie deinstallieren?", "Deinstallation", deinstalllist)
                                    if antwort4 != "Quit" and antwort4 != "":
                                        antwort5 = bÃ¼.buttonLog(title=antwort4+" deinstallieren")
                                        if antwort5 == "Fortfahren":
                                            if antwort4 != "BÃ¼ro":
                                                os.remove("./programdata/buero/versioninfo_"+antwort4+".txt")
                                            if antwort4 == "VerschlÃ¼sseler":
                                                os.remove("./verschlÃ¼sseln.py")
                                                shutil.rmtree("./shopping")
                                                shutil.rmtree("./programdata/verschlÃ¼sseln")
                                            elif antwort4 == "Haustier":
                                                os.remove("./Haustier.py")
                                                shutil.rmtree("./programdata/haustier")
                                            elif antwort4 == "Ballonfahrt":
                                                bÃ¼.remove_(["Ballonfahrt.py", "Ballonfahrt-M2_1.py", "Ballonfahrt-M2_2.py"])
                                                bÃ¼.remove_(balims, "./images/")
                                                shutil.rmtree("./programdata/ballonfahrt")
                                            elif antwort4 == "SchingSchangSchongIQ":
                                                os.remove("./SchingSchangSchongIntelligent.py")
                                                shutil.rmtree("./programdata/schingschangschongiq")
                                            elif antwort4 == "abstrakte Verzerrung":
                                                os.remove("./abstrakt.py")
                                                shutil.rmtree("./programdata/abstrakt")
                                            elif antwort4 == "im Verlies":
                                                bÃ¼.remove_(["quest.py", "level-editor.py"])
                                                shutil.rmtree("./programdata/im Verlies")
                                                bÃ¼.remove_(imlist, "./images/")
                                            elif antwort4 == "Passwortgenerator":
                                                os.remove("./Passwortgenerator.py")
                                                shutil.rmtree("./programdata/password")
                                            elif antwort4 == "Musik":
                                                os.remove("./Musik.py")
                                                shutil.rmtree("./programdata/music")
                                            elif antwort4 == "Garten im GlÃ¼ck":
                                                os.remove("./Garten-im-GlÃ¼ck.py")
                                                bÃ¼.remove_(gigims, "./images/")
                                            elif antwort4 == "Lebensmittel":
                                                os.remove("./lebensmittel.py")
                                                shutil.rmtree("./programdata/lebensmittel")
                                            elif antwort4 == "Das groÃŸe Quiz":
                                                os.remove("./quiz.py")
                                                bÃ¼.remove_(quizmusic, "./music/")
                                            elif antwort4 == "Rechnungen":
                                                os.remove("./Rechnung.pyw")
                                                shutil.rmtree("./programdata/rechnungen")
                                            elif antwort4 == "BÃ¼roMail":
                                                bÃ¼.remove_(["./mail.py", "./mail_agent.pyw"])
                                                shutil.rmtree("./programdata/mail")
                                            elif antwort4 == "BÃ¼roBank":
                                                os.remove("./bank.py")
                                                shutil.rmtree("./programdata/bank")
                                            elif antwort4 == "LTP Agent":
                                                os.remove("./ltp_agent.py")
                                                shutil.rmtree("./programdata/ltp")
                                            elif antwort4 == "BÃ¼roBonus":
                                                os.remove("./bonus.py")
                                                shutil.rmtree("./programdata/bonus")
                                            elif antwort4 == "Kaffee Manager":
                                                os.remove("./kaffee.py")
                                                shutil.rmtree("./programdata/kaffee")
                                            elif antwort4 == "GoodFood":
                                                os.remove("./goodFood.py")
                                                shutil.rmtree("./programdata/goodFood")
                                            elif antwort4 == "BÃ¼ro":
                                                antwort6 = py.confirm("WARNUNG!\nDiese Ã„nderung ist nicht umkehrbar!",\
                                                                      "WARNUNG", buttons=("Fortfahren", "Abbrechen"))
                                                dLg.entry(antwort6)
                                                if antwort6 == "Fortfahren":
                                                    threading.Thread(target=bÃ¼.uninstallmessage).start()
                                                    shutil.rmtree("./")
                                                    print("BÃ¼ro wurde deinstalliert!"); quit(code="BÃœRO UNINSTALLED!")
                                            else:
                                                dLg.entry("Fehlerhafter Wert zum Deinstallieren angegeben!!!")
                                                bÃ¼.error_quit()
                                            installiert.remove(antwort4)
                                            for i in list_container + [PLUS]:
                                                if antwort4 in i:
                                                    i.remove(antwort4)
                                            bÃ¼.restart()
                            elif antwort3 == "DebugLogInfo":
                                antwort4 = bÃ¼.buttonLog("Ihre BÃ¼ro-DebugLogs verbrauchen aktuell {} Speicherplatz".format(nsize(bÃ¼.get_size("./programdata/buero/debug"))),\
                                                      "DebugLogInfo", ("ZurÃ¼ck", "Logs lÃ¶schen"))
                                if antwort4 == "Logs lÃ¶schen":
                                    if bÃ¼.PIN_check(PIN_e, lenge, act):
                                        bÃ¼.remove_(os.listdir(BPATH+"debug"), BPATH+"/debug/")
                            elif antwort3 == "AufrÃ¤umen":
                                py.alert("Momentan kann nichts aufgerÃ¤umt werden.", "AufrÃ¤umen")
                            elif antwort3 == "More coming soon...":
                                py.alert("Ihre Auswahl beinhaltet keine Aktionen und wird daher abgebrochen.", "invalide Auswahl")
                            elif antwort3 == "ZurÃ¼ck":
                                break
                            else:
                                bÃ¼.error_quit()        
                    else:
                        if not skipwin:
                            antwort = "TEST"; break
                        else:
                            dLg.entrys("skipwin var reached TEST barrier", "letting skipwin mode pass"); break   
            elif antwort == "ZurÃ¼ck":
                break
            elif antwort == "Quit":
                bÃ¼.normal_quit()
            else:
                bÃ¼.error_quit()
