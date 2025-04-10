# LangChain Datura Integration

This project integrates the Datura API with LangChain tools to enable various search and data-fetching functionalities, such as web searches, Twitter data retrieval, and AI-powered searches.

## Features

- **Grouped Tools**:
  - **Search Tools**: General-purpose search tools for AI, web, and Twitter searches.
  - **Twitter Tools**: Tools specifically for Twitter-related operations.

## Installation

Install the package using pip:

```bash
pip install langchain-datura
```

## Usage

### Grouped Tools

#### Search Tools
The `search_tools` group contains tools for general-purpose searches:
- `DesearchTool`: Perform AI searches, web link searches, and Twitter post searches.
- `BasicWebSearchTool`: Conduct basic web searches.
- `BasicTwitterSearchTool`: Perform advanced Twitter searches with filters.

#### Twitter Tools
The `twitter_tools` group contains tools specifically for Twitter-related operations:
- `BasicTwitterSearchTool`: Perform a basic Twitter search using Datura.
- `FetchTweetsByUrlsTool`: Retrieve tweets from specific URLs.
- `FetchTweetsByIdTool`: Fetch tweets using their unique IDs.
- `FetchLatestTweetsTool`: Get the latest tweets from a specific user.
- `FetchTweetsAndRepliesByUserTool`: Retrieve tweets and replies from a user.
- `FetchRepliesByPostTool`: Fetch replies to a specific Twitter post.
- `FetchRetweetsByPostTool`: Retrieve retweets of a specific post.
- `FetchTwitterUserTool`: Get detailed information about a Twitter user.

### Using the LangChain Agent

You can create a LangChain agent that uses the `search_tools` for various operations.

#### Example
```python
from langchain_datura.agent import create_search_agent

# Initialize the agent
agent = create_search_agent(openai_api_key="your-openai-api-key")

# Use the agent to perform a task
response = agent.run("Find the latest news about AI.")
print(response)
```

### Running Tests

#### Dummy Tests
Run the dummy tests to verify the tools' functionality with mocked data:
```bash
pytest tests/test_tools.py
```

#### Real API Tests
Run the real tests to verify the tools' functionality with the Datura API:
```bash
pytest tests/test_tools_real.py
```

> **Note**: Ensure you have a valid `DATURA_API_KEY` in your `.env` file before running real tests.

### Example Usage

#### Importing Grouped Tools
```python
from langchain_datura.search_tools import search_tools, twitter_tools
```

#### Using a Search Tool
```python
from langchain_datura.search_tools import search_tools

tool = search_tools[0]()  # DesearchTool
result = tool._run(
    prompt="Bittensor",
    tool="desearch_ai",
    model="NOVA",
    date_filter="PAST_24_HOURS",
    streaming=False
)
print(result)
```

#### Using a Twitter Tool
```python
from langchain_datura.search_tools import twitter_tools

tool = twitter_tools[1]()  # FetchTweetsByUrlsTool
result = tool._run(
    urls=["https://twitter.com/elonmusk/status/1613000000000000000"]
)
print(result)
```

## Project Structure

```
langchain_datura/
├── langchain_datura/
│   ├── __init__.py
│   ├── tools.py
├── tests/
│   ├── test_tools.py
│   ├── test_tools_real.py
├── .env
├── README.md
└── requirements.txt
```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or support, please contact [your-email@example.com].