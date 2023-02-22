from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5632503519:AAEu0iGqS_z_kxUQGgOqocXJezobEUhshNo" # Bot toekn
ADMINS = [1435473812]  # adminlar ro'yxati


DB_USER = "postgres"
DB_PASS = "uzbsobirov"
DB_NAME = "Template"
DB_HOST = "localhost"