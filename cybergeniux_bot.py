#!/usr/bin/env python3
"""
Cybergeniux Bot - Ethical Hacking Learning Bot for Telegram
Created by: Lazaro John (Geniux), Dar es Salaam, Tanzania
Purpose: Teach ethical hacking & cybersecurity legally
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    ContextTypes, MessageHandler, filters
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot Token
TOKEN = "8170127374:AAGv0h8XQqP3EV9Rh0x0h8XQqP3EV9Rh0x0"

# ========== COMMAND HANDLERS ==========

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Welcome message"""
    welcome = """
🛡️ *KARIBU CYBERGENIUX BOT* 🛡️

Mimi ni bot ya kujifunza *Ethical Hacking & Cybersecurity* kwa njia halali.

⚠️ *MUHIMU:* Bot hii ni ya mafunzo tu. Kuhacking bila ruhusa ni kinyume cha sheria.

📚 *Amri zinazopatikana:*
/start - Karibu
/tools - Zana za Ethical Hacking
/cheatsheets - Cheat Sheets
/tutorials - Mafunzo ya GitHub Pages
/learn - Mpango wa Kujifunza
/practice - Mazoezi ya Vitendo
/laws - Sheria za Cybersecurity
/about - Kuhusu Bot

👉 Chagua amri au bonyeza button hapo chini!
"""
    keyboard = [
        [InlineKeyboardButton("🛠️ Zana", callback_data="tools"),
         InlineKeyboardButton("📋 Cheat Sheets", callback_data="cheatsheets")],
        [InlineKeyboardButton("📚 Mafunzo", callback_data="tutorials"),
         InlineKeyboardButton("🎯 Mpango wa Kujifunza", callback_data="learn")],
        [InlineKeyboardButton("💪 Mazoezi", callback_data="practice"),
         InlineKeyboardButton("⚖️ Sheria", callback_data="laws")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome, parse_mode="Markdown", reply_markup=reply_markup)


async def tools(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """List ethical hacking tools"""
    text = """
🛠️ *ZANA ZA ETHICAL HACKING* 🛡️

*KUTAMBUA & KUCHUNGA:*
• Nmap - Network scanning
• Wireshark - Packet analysis
• Masscan - Fast port scanning

*KUSHAURITI & KUHACK:*
• Metasploit - Exploitation framework
• Burp Suite - Web app testing
• SQLMap - SQL injection testing
• John the Ripper - Password cracking
• Hashcat - Advanced password cracking

*KUJINDA & KULINDA:*
• Snort - Intrusion detection
• OSSEC - Host-based IDS
• Fail2Ban - Brute force protection
• ClamAV - Antivirus

*KUJIFUNZA:*
• TryHackMe - Interactive labs
• Hack The Box - Practice platform
• OverTheWire - Wargames
• PicoCTF - CTF for beginners

⚠️ *Tumia zana hizi kwa mafunzo tu na kwa ruhusa!*
"""
    await update.message.reply_text(text, parse_mode="Markdown")


async def cheatsheets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cheat sheets links"""
    text = """
📋 *CHEAT SHEETS ZA CYBERSECURITY* 🛡️

*Linux Commands:*
https://cheatography.com/davechild/cheat-sheets/linux-command-line/

*Nmap Cheat Sheet:*
https://hackertarget.com/nmap-cheatsheet-a-quick-reference-guide/

*Metasploit Cheat Sheet:*
https://www.offensive-security.com/metasploit-unleashed/msfconsole-commands/

*Burp Suite Cheat Sheet:*
https://portswigger.net/burp/documentation/desktop/cheat-sheet

*SQL Injection Cheat Sheet:*
https://portswigger.net/web-security/sql-injection/cheat-sheet

*Python for Hacking:*
https://github.com/0xcybery/ehtk/

*Full Toolkit:*
https://0xcybery.github.io/ehtk/

⚠️ *Kumbuka: Tumia kwa mafunzo tu!*
"""
    await update.message.reply_text(text, parse_mode="Markdown")


async def tutorials(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """GitHub Pages tutorials"""
    text = """
📚 *MAFUNZO YA GITHUB PAGES* 🛡️

*Ethical Hacking Labs (Mazoezi ya Vitendo):*
https://dharmthummar.github.io/ethical-hacking-labs/

*Ethical Hacking Toolkit (Zana Zote):*
https://0xcybery.github.io/ehtk/

*Ethical Hacking Articles (Makala za Kina):*
https://0xma.github.io/hacking/index.html

*Hacking Portal (Blog ya Cybersecurity):*
https://hackingportal.github.io/

*Learning Resources (Rasilimali):*
https://h4ndsh.github.io/2023/myresources/

*OWASP Web Security:*
https://owasp.org/www-project-web-security-testing-guide/

*TryHackMe (Mafunzo Interactive):*
https://tryhackme.com

*Hack The Box (Mazoezi):*
https://www.hackthebox.com

⚠️ *Jifunza kwa vitendo kwa mazingira salama!*
"""
    await update.message.reply_text(text, parse_mode="Markdown")


async def learn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Learning roadmap"""
    text = """
🎯 *MPANGO WA KUJIFUNZA ETHICAL HACKING* 🛡️

*WIKI 1 — Msingi wa Cybersecurity:*
✅ Utangulizi wa hacking
✅ Jinsi mtandao unavyofanya kazi
✅ Linux basics
✅ Networking fundamentals

*WIKI 2 — Network Security:*
✅ Nmap scanning
✅ Wireshark analysis
✅ Firewall configuration
✅ VPN setup

*WIKI 3 — Web Security:*
✅ OWASP Top 10
✅ SQL Injection
✅ XSS attacks
✅ Burp Suite basics

*WIKI 4 — Exploitation:*
✅ Metasploit basics
✅ Password cracking
✅ Privilege escalation
✅ Post-exploitation

*WIKI 5 — Defense:*
✅ Intrusion detection
✅ Log analysis
✅ Incident response
✅ Security auditing

*WIKI 6 — Certification Prep:*
✅ CEH (Certified Ethical Hacker)
✅ CompTIA Security+
✅ OSCP (Offensive Security)

⏳ *Kila wiki: masaa 5-10 ya mazoezi*
"""
    await update.message.reply_text(text, parse_mode="Markdown")


async def practice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Practice platforms"""
    text = """
💪 *MAZOEZI YA VITENDO* 🛡️

*PLATFORMS BURE:*
• TryHackMe — https://tryhackme.com
• Hack The Box — https://www.hackthebox.com
• OverTheWire — https://overthewire.org
• PicoCTF — https://picoctf.org
• CyberDefenders — https://cyberdefenders.org
• VulnHub — https://www.vulnhub.com

*MAZOEZI YAKO MWENYEWE:*
1. Tengeneza lab ya kujifunza kwa VirtualBox
2. Install Kali Linux (https://www.kali.org)
3. Tengeneza vulnerable VMs kwa VitualBox
4. Fanya mazoezi ya Nmap, Metasploit, Burp Suite

*KUJENGA LAB YAKO:*
• VirtualBox (bure) — https://virtualbox.org
• Kali Linux — https://kali.org
• Metasploitable — https://sourceforge.net/projects/metasploitable/
• DVWA — http://dvwa.co.uk

⚠️ *Mazoezi yote yafanywe kwa mazingira yako mwenyewe!*
"""
    await update.message.reply_text(text, parse_mode="Markdown")


async def laws(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cybersecurity laws"""
    text = """
⚖️ *SHERIA ZA CYBERSECURITY* 🛡️

*TANZANIA:*
• Cybercrimes Act, 2015
• Electronic and Postal Communications Act
• Data Protection Act

*MATAIFA MENGINE:*
• Kenya — Computer Misuse and Cybercrimes Act
• Uganda — Computer Miscyimes Act
• USA — Computer Fraud and Abuse Act (CFAA)
• EU — General Data Protection Regulation (GDPR)

*ADHABU ZA KUHACKING BILA RUHUSA:*
❌ Tanzania: Hadithi 5 hadi 10 ya jela
❌ Kenya: Hadithi 2 hadi 5 ya jela
❌ USA: Hadithi 1 hadi 20 ya jela
❌ EU: Euro hadi 500,000

✅ *HALALI:*
• Kuhack kifaa chako mwenyewe
• Kuhack kwa ruhusa ya mmiliki
• Kufanya security audit kwa ajili ya kazi
• Kutumia platforms za mazoezi

⚠️ *Kuhacking bila ruhusa = KINYUME CHA SHERIA*
"""
    await update.message.reply_text(text, parse_mode="Markdown")


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """About the bot"""
    text = """
🤖 *KUHUSU CYBERGENIUX BOT* 🛡️

*Jina:* Cybergeniux Bot
*Mtengenezaji:* Lazaro John (Geniux)
*Makao:* Dar es Salaam, Tanzania
*Lengo:* Kufundisha Ethical Hacking kwa njia halali

*Version:* 1.0
*Lugha:* Python (python-telegram-bot)
*Host:* GitHub + Cloud

📩 *Mawasiliano:*
• GitHub: github.com/lazarojohnie54-a11y
• Telegram: @GeniuxBot

⚠️ *Bot hii ni ya mafunzo tu. Tumia kwa njia halali!*
"""
    await update.message.reply_text(text, parse_mode="Markdown")


# ========== CALLBACK HANDLER ==========

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button presses"""
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "tools":
        await tools(update, context)
    elif data == "cheatsheets":
        await cheatsheets(update, context)
    elif data == "tutorials":
        await tutorials(update, context)
    elif data == "learn":
        await learn(update, context)
    elif data == "practice":
        await practice(update, context)
    elif data == "laws":
        await laws(update, context)


# ========== MAIN ==========

def main():
    """Start the bot"""
    print("🤖 Cybergeniux Bot inaanza...")
    print("🛡️ Ethical Hacking Learning Bot")
    print("🇹🇿 Created by Geniux, Dar es Salaam Tanzania")

    # Create application
    app = Application.builder().token(TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tools", tools))
    app.add_handler(CommandHandler("cheatsheets", cheatsheets))
    app.add_handler(CommandHandler("tutorials", tutorials))
    app.add_handler(CommandHandler("learn", learn))
    app.add_handler(CommandHandler("practice", practice))
    app.add_handler(CommandHandler("laws", laws))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CallbackQueryHandler(button_callback))

    # Run the bot
    print("✅ Bot imewashwa! Inasubiri messages...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
