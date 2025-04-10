from langchain_datura.tools import DesearchTool,BasicWebSearchTool,BasicTwitterSearchTool,FetchTweetsByUrlsTool,FetchTweetsByIdTool,FetchLatestTweetsTool,FetchTweetsAndRepliesByUserTool,FetchRepliesByPostTool,FetchRetweetsByPostTool,FetchTwitterUserTool

tool = DesearchTool()
result = tool._run(
    prompt="Bittensor",
    tool="desearch_web",
    model="NOVA",
    date_filter="PAST_24_HOURS",
    streaming=False
)
print(result)

tool = BasicWebSearchTool()
result = tool._run(
    query="Whats going on with Bittensor",
    num=5,
    start=1
)
print(result)

tool = BasicTwitterSearchTool()
result = tool._run(
    query="Whats going on with Bittensor",
    sort="Top",
    count=5
)
print(result)

tool = FetchTweetsByUrlsTool()
result = tool._run(
    urls=["https://twitter.com/elonmusk/status/1234567890"],
)
print(result)

tool = FetchTweetsByIdTool()
result = tool._run(
    id="1234567890",
)
print(result)

tool = FetchLatestTweetsTool()
result = tool._run(
    user="elonmusk",
    count=5
)
print(result)

tool = FetchTweetsAndRepliesByUserTool()
result = tool._run(
    user="elonmusk",
    query="Bittensor",
    count=5
)
print(result)

tool = FetchRepliesByPostTool()
result = tool._run(
    post_id="1234567890",
    count=5,
    query="Bittensor"
)
print(result)

tool = FetchRetweetsByPostTool()
result = tool._run(
    post_id="1234567890",
    count=5,
    query="Bittensor"
)
print(result)

tool = FetchTwitterUserTool()
result = tool._run(
    user="elonmusk"
)
print(result)

