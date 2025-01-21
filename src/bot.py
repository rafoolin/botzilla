from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from config import TELEGRAM_TOKEN
import handlers as handlers
import model as model
import utils as utils


def main():
    # Setup logging
    logger = utils.setup_logging()

    # Load the model
    logger.info("Loading model...")
    pipe = model.load_model()

    # Initialize the bot
    logger.info("Initializing bot...")
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    logger.info("Bot initialized.")

    # Add command handlers
    application.add_handler(CommandHandler("start", handlers.start))
    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND, lambda u, _: handlers.handle_message(u, pipe)
        )
    )
    application.add_handler(CommandHandler("trivia", lambda u, _: handlers.random_trivia(u, pipe)))
    application.add_handler(CommandHandler("help", handlers.help_command))

    # Start polling
    logger.info("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
