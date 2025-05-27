from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from requests import *
import psycopg2
import finalbot_2

# Open connection to Database

conn = psycopg2.connect(
    dbname="european_countries",
    user="postgres",
    password="291410",
    host="127.0.0.1",
    port="5432")

cur = conn.cursor()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    countries = [
                "Albania",
                "Andorra",
                "Austria",
                "Belarus",
                "Belgium",
                "Bosnia and Herzegovina",
                "Bulgaria",
                "Croatia",
                "Cyprus",
                "Czech Republic",
                "Denmark",
                "Estonia",
                "Finland",
                "France",
                "Germany",
                "Greece",
                "Vatican City State (Holy See)",
                "Hungary",
                "Iceland",
                "Ireland",
                "Italy",
                "Latvia",
                "Liechtenstein",
                "Lithuania",
                "Luxembourg",
                "Malta",
                "Moldova",
                "Monaco",
                "Montenegro",
                "Netherlands",
                "North Macedonia",
                "Norway",
                "Poland",
                "Portugal",
                "Romania",
                "San Marino",
                "Serbia",
                "Slovakia",
                "Slovenia",
                "Spain",
                "Sweden",
                "Switzerland",
                "Turkey" ,
                "Ukraine",
                "United Kingdom"
                ]
    keyboard = [[InlineKeyboardButton(country, callback_data=country)] for country in countries]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_html(f"Hi {user.mention_html()}!")
    await update.message.reply_html(
    f"Now you are with european country Bot.\nPlease, choose the country:\n\n\
    * /info - get more information about country\n\
    ** /start - restart Bot\n\
    *** /about - about developer", reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query

    await query.answer()
    global country_name
    country_name=query.data

# Get information about country from Database

    cur.execute("SELECT capital, biggest_city FROM european_countries WHERE country=%s;", (country_name,))
    rows = cur.fetchall()
    for row in rows:
        await query.edit_message_text(text=f"Country: {country_name}\nCapital: {row[0]}\nBiggest city: {row[1]}")
        
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
# Get information about country from function country_info() from external API

    country_info_text = finalbot_2.country_info(country_name)
    await update.message.reply_text(f"Now, you can read more information about {country_name}:\n{country_info_text}")

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Developer: Oleksii Prorochenko\nYear: 2024\nLocation: Kyiv, Ukraine\nE-mail: a.prorochenko@gmail.com")

def main() -> None:
    application = Application.builder().token("6557550649:AAHa8-_TpvRm0S5xlWEcQ82VWPK7mmsP0dU").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("about", about_command))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

cur.close()
conn.close()
        





