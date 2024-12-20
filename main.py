from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

data = [
  {
    "id": "1",
    "attributes": {
        "name": "Chocolate Cake",
        "description": "Delicate cake with cocoa",
        "calories": "350 kcal per serving",
        "image": "https://i.pinimg.com/736x/9b/36/f0/9b36f04319f5e4f615af7abc7679fe8d.jpg"
    }
  },
  {
    "id": "2",
    "attributes": {
        "name": "Chicken Caesar",
        "description": "Light salad with chicken",
        "calories": "250 kcal per serving",
        "image": "https://n1s2.hsmedia.ru/48/2d/63/482d63d02b668677a73a2ffbd791a71b/728x546_1_aaca034dfa8a8c33247bd8cb2ed26817@1700x1275_0xac120003_9749770561671744766.jpeg"
    }
  },
  {
    "id": "3",
    "attributes": {
        "name": "Borscht",
        "description": "Traditional beetroot soup",
        "calories": "150 kcal per serving",
        "image": "https://centspec.ru/uploads/413464-9c183c2f2550e70d5b6ad8165547800d.jpg"
    }
  },
  {
    "id": "4",
    "attributes": {
        "name": "Margherita Pizza",
        "description": "Classic pizza with tomatoes",
        "calories": "270 kcal per serving",
        "image": "https://n1s2.hsmedia.ru/48/2d/63/482d63d02b668677a73a2ffbd791a71b/728x546_1_aaca034dfa8a8c33247bd8cb2ed26817@1700x1275_0xac120003_9749770561671744766.jpeg"
    }
  },
  {
    "id": "5",
    "attributes": {
        "name": "Carbonara Pasta",
        "description": "Italian pasta with bacon",
        "calories": "600 kcal per serving",
        "image": "https://avatars.mds.yandex.net/i?id=1224bf48651d06cbe9b554f6e30445b5b7cc503c-12471733-images-thumbs&n=13"
    }
  },
  {
    "id": "6",
    "attributes": {
        "name": "Syrniki",
        "description": "Fluffy cottage cheese pancakes",
        "calories": "250 kcal per serving",
        "image": "https://avatars.mds.yandex.net/i?id=bd36f8dcbe6db752433057b288a5ad78c73c246e-9237081-images-thumbs&ref=rim&n=33&w=339&h=250"
    }
  },
  {
    "id": "7",
    "attributes": {
        "name": "Olivier Salad",
        "description": "Classic salad with sausage",
        "calories": "200 kcal per serving",
        "image": "https://avatars.mds.yandex.net/i?id=bd36f8dcbe6db752433057b288a5ad78c73c246e-9237081-images-thumbs&ref=rim&n=33&w=339&h=250"
    }
  },
  {
    "id": "8",
    "attributes": {
        "name": "Tom Yum",
        "description": "Spicy Thai soup with shrimp",
        "calories": "180 kcal per serving",
        "image": "https://avatars.mds.yandex.net/i?id=bd36f8dcbe6db752433057b288a5ad78c73c246e-9237081-images-thumbs&ref=rim&n=33&w=339&h=250"
    }
  },
  {
    "id": "9",
    "attributes": {
        "name": "Pancakes",
        "description": "Thin and tender pancakes",
        "calories": "200 kcal per serving",
        "image": "https://avatars.mds.yandex.net/i?id=bd36f8dcbe6db752433057b288a5ad78c73c246e-9237081-images-thumbs&ref=rim&n=33&w=339&h=250"
    }
  },
  {
    "id": "10",
    "attributes": {
        "name": "Greek Salad",
        "description": "Salad with feta and olives",
        "calories": "150 kcal per serving",
        "image": "https://avatars.mds.yandex.net/i?id=bd36f8dcbe6db752433057b288a5ad78c73c246e-9237081-images-thumbs&ref=rim&n=33&w=339&h=250"
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
        [item for item in data if fullName.lower() in item["attributes"]["name"].lower()]
        if fullName else data
    )

    start_index = (page-1) * size
    end_index = page * size
    paginated_data = filtered_data[start_index:end_index]

    return {
        "meta": {
          "pagination": {
              "next": page + 1
          }
        },
        "data": paginated_data
    }
