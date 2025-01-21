from telegram import Update
from telegram.ext import ContextTypes

import logging as logger
import model as model


async def start(update: Update, _):
    """
    Handle the /start command. Logs user information and sends a welcome message.

    Args:
        update (Update): Incoming update.
    """
    first_name = update.message.from_user.first_name
    username = update.message.from_user.username
    user = first_name if first_name else username
    logger.info("Bot started.")
    logger.info("User ID: %s", update.message.from_user.id)
    logger.info("User name: %s", username)
    logger.info("User first name: %s", first_name)
    await update.message.reply_text(
        f"RAWR! I'm Botzilla 🦖 running locally.\nHey {user}, ask me anything!"
    )


async def handle_message(update: Update, pipe):
    """
    Handle incoming user messages. Generates a response using the model and sends it back.

    Args:
        update (Update): Incoming update.
        pipe: Model pipeline for generating responses.
    """
    user_message = update.message.text
    messages = [
        {"role": "system", "content": "You are a friendly assistant."},
        {"role": "user", "content": user_message},
    ]

    response = model.generate_response(pipe, messages)
    await update.message.reply_text(response)


async def random_trivia(update: Update, pipe):
    """
    Handle the /trivia command.
    Generates a random trivia or fun fact using the model and sends it back.

    Args:
        update (Update): Incoming update.
        pipe: Model pipeline for generating responses.
    """
    await update.message.reply_text("I'm thinking of a random trivia or fun fact...'")
    messages = [
        {
            "role": "system",
            "content": "You are a friendly AI assistant who loves sharing funny trivia, fun facts only related to animals and dinosaurs.",
        },
        {"role": "user", "content": "Tell me a random fact or trivia."},
    ]
    response = model.generate_response(pipe, messages)
    await update.message.reply_text(response)


async def help_command(update: Update, _):
    """
    Handle the /help command. Sends a help message to the user.

    Args:
        update (Update): Incoming update.
    """
    # show all available commands
    help_message = (
        "Here are the available commands:\n"
        "/start - Start the bot\n"
        "/trivia - Enjoy random trivia or facts\n"
        "/help - Show this help message"
    )
    await update.message.reply_text(help_message)
