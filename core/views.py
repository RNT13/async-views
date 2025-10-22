import asyncio
import httpx
import requests
from django.http import JsonResponse


# View ASSÍNCRONA
async def http_call_async(request):
    print("Iniciando processamento async...")
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(f"[ASYNC] Segundo {num}")

    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/todos/1")

    if response.headers.get("content-type", "").startswith("application/json"):
        data = response.json()
    else:
        data = {
            "error": "Resposta não é JSON",
            "status_code": response.status_code,
            "content": response.text[:200],
        }

    return JsonResponse({"mode": "async", "result": data})


# View SÍNCRONA
def http_call_sync(request):
    print("Iniciando processamento sync...")
    for num in range(1, 6):
        import time
        time.sleep(1)
        print(f"[SYNC] Segundo {num}")

    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

    if response.headers.get("content-type", "").startswith("application/json"):
        data = response.json()
    else:
        data = {
            "error": "Resposta não é JSON",
            "status_code": response.status_code,
            "content": response.text[:200],
        }

    return JsonResponse({"mode": "sync", "result": data})
