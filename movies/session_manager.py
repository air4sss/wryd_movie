import aiohttp


# 여러 위치에서 세션을 요청할 때 이미 생성된 세션을 재사용하기 위한 클래스
class ClientSessionManager:
    _session = None

    @classmethod
    async def get_session(cls):
        if cls._session is None or cls._session.closed:
            cls._session = aiohttp.ClientSession()
        return cls._session

    @classmethod
    async def close_session(cls):
        if cls._session and not cls._session.closed:
            await cls._session.close()
            cls._session = None