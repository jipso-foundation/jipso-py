import pytest, logging


logger = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_ClientOpenai():
  from jipso.Client import ClientOpenai
  response = ClientOpenai().chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [{'role': 'user', 'content': 'Hello ChatGPT!'}],
    temperature = 0,
    seed = 100,
    max_tokens = 100,
  )
  assert response.choices[0].message.content == 'Hello! How can I assist you today?'


@pytest.mark.asyncio
async def test_ClientAnthropic():
  from jipso.Client import ClientAnthropic
  response = ClientAnthropic().messages.create(
    model = 'claude-3-haiku-20240307',
    max_tokens = 100,
    messages = [{'role': 'user', 'content': 'Hello Claude!'}],
    temperature = 0,
  )
  assert response.content[0].text == "Hello! It's nice to meet you. How can I assist you today?"


@pytest.mark.asyncio
async def test_ClientGemini():
  from jipso.Client import ClientGemini
  client = ClientGemini()
  generation_config = client.GenerationConfig(temperature=0, max_output_tokens=100)
  model = client.GenerativeModel('models/gemini-1.5-flash')
  response = model.generate_content('Hello Gemini!', generation_config=generation_config)
  assert response.text.strip() == 'Hello there!  How can I help you today?'


@pytest.mark.asyncio
async def test_ClientXai():
  from jipso.Client import ClientXai
  from xai_sdk.chat import user
  client = ClientXai()
  chat = client.chat.create(
    model = 'grok-3-mini-fast',
    messages = [user('Hello Grok!')],
    temperature = 0,
    seed = 100,
    max_tokens = 500,
  )
  assert isinstance(chat.sample().content, str)


@pytest.mark.asyncio
async def test_ClientAlibabacloud():
  from jipso.Client import ClientAlibabacloud
  response = ClientAlibabacloud().chat.completions.create(
    model = 'qwen-turbo',
    messages = [{'role': 'user', 'content': 'Hello Qwen!'}],
    temperature = 0,
    seed = 100,
    max_tokens = 100,
  )
  assert response.choices[0].message.content == "Hello! It's great to see you. How can I assist you today? 😊"


@pytest.mark.asyncio
async def test_ClientTencentcloud():
  from jipso.Client import ClientTencentcloud
  assert True

@pytest.mark.asyncio
async def test_ClientByteplus():
  from jipso.Client import ClientByteplus
  assert True


@pytest.mark.asyncio
async def test_ClientSberbank():
  from jipso.Client import ClientSberbank
  assert True


@pytest.mark.asyncio
async def test_ClientCloudHuggingface():
  from jipso.Client import ClientCloudHuggingface
  assert True


@pytest.mark.asyncio
async def test_ClientLocalHuggingface():
  from jipso.Client import ClientLocalHuggingface
  assert True


@pytest.mark.asyncio
async def test_ClientOllama():
  from jipso.Client import ClientOllama
  assert True


if __name__ == '__main__':
  pytest.main([__file__])
