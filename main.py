from openai import OpenAI
from fastapi import FastAPI,HTTPException
from openai import OpenAIError, RateLimitError, APIConnectionError, AuthenticationError
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
client =  OpenAI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextPayload(BaseModel):
    productsearch: str

@app.post("/api/productsearches")
async def productsearch(payload:TextPayload):

    try:
        response = client.responses.create(model="gpt-3.5-turbo", input=[
            {
                "role": "system",
                "content": "This is a csv of how data on my ecommerce website looks like ->\
                Name,Price,Category,Rating,Description \
        Wireless Headphones,99.99,Electronics,4.5,Noise-cancelling over-ear headphones with long battery life. \
        Organic Green Tea,15.5,Groceries,4.8,Premium organic green tea leaves sourced from Japan. \
        Yoga Mat,25.0,Fitness,4.2,Eco-friendly, non-slip yoga mat for all types of workouts.\
        Smart Watch,199.99,Electronics,4.3,Water-resistant smartwatch with heart rate monitor and GPS.\
        LED Desk Lamp,45.0,Home & Office,4.0,Adjustable brightness LED lamp with USB charging port.\
        Stainless Steel Water Bottle,22.99,Outdoors,4.6,Insulated bottle keeps drinks cold or hot for 12 hours.\
        Bluetooth Speaker,59.99,Electronics,4.4,Portable speaker with high-quality sound and deep bass.\
        Running Shoes,120.0,Fitness,4.3,Lightweight and durable shoes designed for runners.\
        "
            },{
                "role":"system",
                "content":"### Given a search statement please return the exact names of the product that match as a list, if not available, please return an empty list as well for any irrelevant prompts the output will either be the name of a relevant product or an empty list. Do not output anything else. reply only with JSON with key as 'message'### \
                    Example: Please find me a bottle that keeps drinks hot or cold \
                    Answer: ['Stainless Steel Water Bottle']"

            }
            ,{
                "role":"user",
                "content":f"{payload.productsearch}"
            }
        ]
        ,temperature=0.1
        )

        return response.output_text

    except RateLimitError:
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Please try again later.")

    except AuthenticationError:
        raise HTTPException(status_code=401, detail="Invalid API key or authentication failed.")

    except APIConnectionError:
        raise HTTPException(status_code=503, detail="Failed to connect to OpenAI API. Please try again later.")

    except OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected server error: {str(e)}")
    