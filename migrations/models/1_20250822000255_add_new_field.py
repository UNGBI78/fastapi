from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `meeting` ADD UNIQUE INDEX `url_code` (`url_code`);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `meeting` DROP INDEX `url_code`;"""
