from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

data = [
  {
    "id": "1",
    "attributes": {
      "name": "Шоколадный торт",
      "description": "Нежный торт с какао",
      "calories": "350 ккал на порцию",
      "image": "https://example.com/images/chocolate_cake.jpg"
    }
  },
  {
    "id": "2",
    "attributes": {
      "name": "Цезарь с курицей",
      "description": "Легкий салат с курицей",
      "calories": "250 ккал на порцию",
      "image": "https://example.com/images/chicken_caesar.jpg"
    }
  },
  {
    "id": "3",
    "attributes": {
      "name": "Борщ",
      "description": "Традиционный суп со свеклой",
      "calories": "150 ккал на порцию",
      "image": "https://example.com/images/borscht.jpg"
    }
  },
  {
    "id": "4",
    "attributes": {
      "name": "Пицца Маргарита",
      "description": "Классическая пицца с томатами",
      "calories": "270 ккал на порцию",
      "image": "https://example.com/images/margherita.jpg"
    }
  },
  {
    "id": "5",
    "attributes": {
      "name": "Паста Карбонара",
      "description": "Итальянская паста с беконом",
      "calories": "600 ккал на порцию",
      "image": "https://example.com/images/carbonara.jpg"
    }
  },
  {
    "id": "6",
    "attributes": {
      "name": "Сырники",
      "description": "Пышные сырники с творогом",
      "calories": "250 ккал на порцию",
      "image": "https://example.com/images/syrniki.jpg"
    }
  },
  {
    "id": "7",
    "attributes": {
      "name": "Оливье",
      "description": "Классический салат с колбасой",
      "calories": "200 ккал на порцию",
      "image": "https://example.com/images/olivier.jpg"
    }
  },
  {
    "id": "8",
    "attributes": {
      "name": "Том Ям",
      "description": "Острый тайский суп с креветками",
      "calories": "180 ккал на порцию",
      "image": "https://example.com/images/tom_yum.jpg"
    }
  },
  {
    "id": "9",
    "attributes": {
      "name": "Блины",
      "description": "Тонкие и нежные блины",
      "calories": "200 ккал на порцию",
      "image": "https://example.com/images/pancakes.jpg"
    }
  },
  {
    "id": "10",
    "attributes": {
      "name": "Греческий салат",
      "description": "Салат с фетой и оливками",
      "calories": "150 ккал на порцию",
      "image": "https://example.com/images/greek_salad.jpg"
    }
  }
]


@app.get("/recipes/")
async def get_characters(
    fullName: Optional[str] = Query(None, description="Поиск по имени"),
    page: int = Query(1, ge=1, description="Номер страницы"),
    size: int = Query(10, ge=1, description="Размер страницы")
) -> dict:
    filtered_data = (
        [item for item in data if fullName.lower() in item["fullName"].lower()]
        if fullName else data
    )

    start_index = (page-1) * size
    end_index = page * size
    paginated_data = filtered_data[start_index:end_index]

    return {
        "meta": {
          "pagination": {
              "next": page
          }
        },
        "data": paginated_data
    }