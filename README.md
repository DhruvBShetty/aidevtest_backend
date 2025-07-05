# AI Developer Test Backend - Ecommerce app

Build a small e-commerce product catalog app and integrate one AI feature that enhances user interaction or decision-making.

## Installation guide

Dependencies - Python 3.10+

```
git clone https://github.com/DhruvBShetty/aidevtest_backend.git
cd aidevtest_backend
pip install -r requirements.txt #(Either in virtual environment or Docker container)
uvicorn main:app --reload
```
Configure your OpenAI API key with either .env if in Windows or .zshrc or .bashrc if Linux with 
```
export OPENAI_API_KEY = XXXXXXXXX
```


## Smart Product Search (Backend)

Implemented with Open AI API with correct parameters, output, prompt engineering and roles to ensure that the user can describe the products they are interested in natural language and get relevant results.
<p>
<img src="https://github.com/user-attachments/assets/8cafabc6-8531-48b7-b93f-9d06f6136896" height="400" width="400" />
</p>

### Tools used

TypeScript, React, FastAPI, OpenAI, Pydantic
Note: please refer to https://github.com/DhruvBShetty/aidevtest for the frontend

### Assumptions

Users want to describe their needs in natural language and get relevant results besides simply searching strictly by category, price, description etc. They want the products to show up immediately after describing their needs rather than just receive results in text and then search for them.

For example:  A user can ask for all exercise and fitness related products under $100 and rated above 4 and those results will show up immediately.
