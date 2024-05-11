from nonebot import require

from liteyuki.utils.base.resource import get_path
from liteyuki.utils.message.html_tool import template2image
from liteyuki.utils.base.language import get_user_lang
from .api import *
from ...utils.base.ly_typing import T_Bot, T_MessageEvent

require("nonebot_plugin_alconna")
from nonebot_plugin_alconna import on_alconna, Alconna, Args, Subcommand, Arparma, UniMessage

status_alc = on_alconna(
    aliases={"状态"},
    command=Alconna(
        "status",
        Subcommand(
            "memory",
            alias={"mem", "m", "内存"},
        ),
        Subcommand(
            "process",
            alias={"proc", "p", "进程"},
        )
    ),
)


@status_alc.handle()
async def _(event: T_MessageEvent, bot: T_Bot):
    ulang = get_user_lang(event.user_id)
    if ulang.lang_code in status_card_cache:
        image = status_card_cache[ulang.lang_code]
    else:
        image = await generate_status_card(
            bot=await get_bots_data(),
            hardware=await get_hardware_data(),
            liteyuki=await get_liteyuki_data(),
            lang=ulang.lang_code,
            bot_id=bot.self_id,
            use_cache=True
        )
    await status_alc.finish(UniMessage.image(raw=image))


@status_alc.assign("memory")
async def _():
    print("memory")


@status_alc.assign("process")
async def _():
    print("process")