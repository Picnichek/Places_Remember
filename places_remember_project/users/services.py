import requests


def update_user_photo_from_vk(user):
    token = user.social_user.access_token
    url = f"https://api.vk.com/method/users.get?user_ids={
        user.username}&fields=photo_max&access_token={token}&v=5.131"
    response = requests.get(url)
    data = response.json()
    if 'response' in data and len(data['response']) > 0:
        photo_url = data['response'][0]['photo_max']
        user.photo_max = photo_url
        user.save()
