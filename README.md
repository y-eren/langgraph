# LangGraph - Graph Tabanlı LLM İş Akışı

![graph](https://github.com/user-attachments/assets/e8dff863-dc93-41ac-992a-de9a6c4fd175)


## Proje Açıklaması
LangGraph, **graph tabanlı bir iş akışı modelini** kullanarak **LLM tabanlı karar mekanizmaları** oluşturmayı amaçlayan bir projedir. 

Bu proje, **LangChain** ve **LangGraph** kütüphanelerini kullanarak **otomatik belge değerlendirme, bilgi sorgulama ve yanıt üretme süreçlerini** yönetir.

---



## Kullanım Senaryosu

1 Kullanıcı bir soru sorar.  
2 **Retrieve** bileşeni, mevcut bilgileri sorgular.  
3 **Grade Documents**, getirilen belgelerin geçerli olup olmadığını değerlendirir.  
4  Eğer yeterli bilgi yoksa, **Web Search** bileşeni devreye girer.  
5 **Generate** bileşeni, tüm bilgileri kullanarak bir yanıt oluşturur.  
6 Yanıt, değerlendirme aşamalarından geçerek **LLM tarafından optimize edilir** ve kullanıcıya sunulur.  



---





##  **Graph Yapısı**

Aşağıdaki görsel, projenin nasıl çalıştığını gösteren **iş akışı diagramını (workflow)** temsil etmektedir:

![graph](https://github.com/user-attachments/assets/c3971f60-85fb-4b87-8fe5-49c802291062)


- **Başlangıç:** Kullanıcı bir **soru sorar**.
- **Retrieve:** Sistem, vektör tabanlı bir veri deposundan en uygun dokümanları alır.
- **Grade Documents:** Alınan dokümanlar, soruyla ne kadar uyumlu olduklarına göre değerlendirilir.
- **Web Search:** Eğer yeterli bilgi bulunamazsa, web araması yapılır.
- **Generate:** LangChain modeli ile yanıt oluşturulur ve optimizasyon yapılır.


---

