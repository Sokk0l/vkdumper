import vk_api
import os


path, filename = os.path.split(os.path.abspath(__file__))


token = input("Token: ") 

vk_session = vk_api.VkApi(token=token) 
vk = vk_session.get_api()
photo = open(f'{path}/photo_pre.html', 'r', encoding="utf8")
file = photo.read()
file2 = photo.read()
file1 = photo.read()
photo.close()

try:
    getinfo = vk.account.getProfileInfo() 
    iddd = getinfo["id"]
    vk_name = getinfo["first_name"] 
    vk_rename = getinfo["last_name"] 

    test = vk.messages.getConversations(count=200) #
    num = test["count"] 
    print(f"Всего найдено диалогов: {num}")
    print(f"Начинаю выгрузку фотографий | {vk_name} {vk_rename} - vk.com/id{iddd}")
    for i in test["items"]: 
        idd = i["conversation"]["peer"]["id"] 
        peer_type = i['conversation']['peer']['type'] 
        if peer_type == "user": 
            if idd > 0: 
                print(f"Выгрузка фотографий - {idd}")
                testtt = vk.users.get(user_ids=idd, fields="sex") 
                for b in testtt: 
                    pol_ebaniy = b["sex"] 
                    if pol_ebaniy == 1: 
                        fo = vk.messages.getHistoryAttachments(peer_id=idd, media_type='photo', start_from=0,
                                                                count=200,
                                                                preserve_order=1, max_forwards_level=45)
                        for i in fo["items"]: 
                            for j in i["attachment"]["photo"]["sizes"]:
                                if j["height"] > 500 and j["height"] < 650: 
                                    url = j["url"] 
                                    file += f'<img class="photos" src="{url}" alt="Failed to load (:" title="Found in dialog - vk.com/id{idd}">' 
                    elif pol_ebaniy == 2: 
                        fo = vk.messages.getHistoryAttachments(peer_id=idd, media_type='photo', start_from=0,
                                                                count=200,
                                                                preserve_order=1, max_forwards_level=45)
                        for i in fo["items"]:
                            for j in i["attachment"]["photo"]["sizes"]:
                                if j["height"] > 500 and j["height"] < 650:
                                    url = j["url"]
                                    file1 += f'<img class="photos" src="{url}" alt="Failed to load (:" title="Found in dialog - vk.com/id{idd}">'
                    else: 
                        fo = vk.messages.getHistoryAttachments(peer_id=idd, media_type='photo', start_from=0,
                                                                count=200,
                                                                preserve_order=1, max_forwards_level=45)
                        for i in fo["items"]:
                            for j in i["attachment"]["photo"]["sizes"]:
                                if j["height"] > 500 and j["height"] < 650:
                                    url = j["url"]
                                    file2 += f'<img class="photos" src="{url}" alt="Failed to load (:" title="Found in dialog - vk.com/id{idd}">'
            else:
                print("not person")
        else:
            print("not person")

        save_photo = open(f'{path}/Girls - id{iddd}.html', 'w+', encoding="utf8") 
        save_photo.write(file) 
        save_photo.close() 
        save_photos = open(f'{path}/Boys - id{iddd}.html', 'w+', encoding="utf8")
        save_photos.write(file1)
        save_photos.close()
        save_photoss = open(f'{path}/Undefined - id{iddd}.html', 'w+', encoding="utf8")
        save_photoss.write(file2)
        save_photoss.close()


except Exception as e:
    print(e)