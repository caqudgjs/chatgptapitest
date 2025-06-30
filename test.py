import openai

# 1. 클라이언트 설정 (신규 방식)
client = openai.OpenAI(api_key="")

# 2. GPT-4 모델 호출
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "안녕, 너는 누구야?"}
    ]
)

# 3. 응답 및 토큰 출력
print("응답 메시지:\n", response.choices[0].message.content)

print("\n--- 사용된 토큰 정보 ---")
print("Prompt tokens:", response.usage.prompt_tokens)
print("Completion tokens:", response.usage.completion_tokens)
print("Total tokens:", response.usage.total_tokens)
