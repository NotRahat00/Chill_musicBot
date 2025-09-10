from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQG587gADBLnA2PHPxL0Ko4Mfy1MBFH0FrRGGIWFgoi_ba4_48qLSFLVutahxruYf04BVaT6I_QqoIVQl59WGmfX_8boed3vHsYrleCmjrhS6eYBgD7-TQIS0HWTpBaCRzK7TfoWxtWnVGIv6QcPZGXm4WJIzuU5csaI8YAd0Tb_98JHc_FrMpOgEAtkfvET3IE5YXx1_FLZ48igvTmHreTWI5UfJiYf-lKR7d0lcw3H-yGfgFAV-DT9FGJME6vIW3Q6k3hHdEvcI4r57ptQxUGI4wKxYZQ9oV9EJLPMYKdLQh98c51-QAV2WIpbIYGmn9zykIO5uXgpxmgMf4AaKruoFZrZlgAAAAHql5IRAA")

BOT_TOKEN = getenv("BOT_TOKEN", "8220026657:AAFDhfABE7Sow68knXM7J-5l4Ny_PGiyBzE")
API_ID = int(getenv("API_ID", "28963768"))
API_HASH = getenv("API_HASH", "9e5e30c6a8658aa797f5dad531475a7a")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "AbishnoiMF")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Abishnoi_bots")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5938660179").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5938660179").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/31e9ecee16a46575267a4.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/d744707634106cf76627a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/bc5556476395a0c8e109b.jpg"
)
