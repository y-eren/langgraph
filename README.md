# 📊 LangGraph - Graph Tabanlı LLM İş Akışı

![graph](https://github.com/user-attachments/assets/e8dff863-dc93-41ac-992a-de9a6c4fd175)


## 🚀 Proje Açıklaması
LangGraph, **graph tabanlı bir iş akışı modelini** kullanarak **LLM tabanlı karar mekanizmaları** oluşturmayı amaçlayan bir projedir. 

Bu proje, **LangChain** ve **LangGraph** kütüphanelerini kullanarak **otomatik belge değerlendirme, bilgi sorgulama ve yanıt üretme süreçlerini** yönetir.

---

## 🏗 Proje Mimarisi

Bu projede bir **state graph (durum grafiği)** kullanılarak farklı bileşenlerin etkileşimi sağlanmaktadır:

- 🔍 **Bilgi Getirme (Retrieve)** → Kullanıcının sorduğu soruya uygun belgeleri getirir.
- 📄 **Doküman Değerlendirme (Grade Documents)** → Getirilen belgelerin geçerliliğini değerlendirir.
- 🤖 **Yanıt Üretme (Generate)** → LangChain LLM modeli ile yanıt oluşturur.
- 🌎 **Web Arama (Web Search)** → Eğer ilgili belge bulunamazsa, web araması yaparak ek bilgi alır.

Bu akış, **LangGraph kütüphanesi** ile **StateGraph** modeli kullanılarak yönetilmektedir.

---

## 📌 Kullanım Senaryosu

1️⃣ Kullanıcı bir soru sorar.  
2️⃣ **Retrieve** bileşeni, mevcut bilgileri sorgular.  
3️⃣ **Grade Documents**, getirilen belgelerin geçerli olup olmadığını değerlendirir.  
4️⃣ Eğer yeterli bilgi yoksa, **Web Search** bileşeni devreye girer.  
5️⃣ **Generate** bileşeni, tüm bilgileri kullanarak bir yanıt oluşturur.  
6️⃣ Yanıt, değerlendirme aşamalarından geçerek **LLM tarafından optimize edilir** ve kullanıcıya sunulur.  

---

## 🔧 Kullanılan Teknolojiler

- **Python 3.x**
- **LangGraph**
- **LangChain**
- **OpenAI API**
- **ChromaDB**
- **Tavily Web Search API**
- **Pydantic**
- **FastAPI (Gelecekte eklenebilir)**

---

## 📂 Proje Klasör Yapısı

```
langgraph/
│── graph/
│   ├── graph.py                 # Ana iş akışı (StateGraph)
│   ├── node_constants.py        # Düğümlerin sabitleri
│   ├── nodes/
│   │   ├── retrieve.py          # Bilgi getirme düğümü
│   │   ├── grade_documents.py   # Belgeleri değerlendirme düğümü
│   │   ├── web_search.py        # Web arama düğümü
│   │   ├── generate.py          # Yanıt üretme düğümü
│   ├── chains/
│   │   ├── retrieval_grader.py  # Belgelerin alaka düzeyini değerlendirme
│   │   ├── rooter.py            # Soru yönlendirme sistemi
│   │   ├── answer_grader.py     # Yanıt doğrulama
│   ├── state.py                 # Uygulama durumu yönetimi
│── ingestion.py                  # Veri yükleme modülü
│── main.py                        # Çalıştırma dosyası
│── requirements.txt               # Gerekli bağımlılıklar
│── .gitignore                     # Hassas ve gereksiz dosyaları dışlama
│── README.md                      # Bu doküman
```



## 📊 **Graph Yapısı**

Aşağıdaki görsel, projenin nasıl çalıştığını gösteren **iş akışı diagramını (workflow)** temsil etmektedir:

![graph](https://github.com/user-attachments/assets/c3971f60-85fb-4b87-8fe5-49c802291062)


- **Başlangıç:** Kullanıcı bir **soru sorar**.
- **Retrieve:** Sistem, vektör tabanlı bir veri deposundan en uygun dokümanları alır.
- **Grade Documents:** Alınan dokümanlar, soruyla ne kadar uyumlu olduklarına göre değerlendirilir.
- **Web Search:** Eğer yeterli bilgi bulunamazsa, web araması yapılır.
- **Generate:** LangChain modeli ile yanıt oluşturulur ve optimizasyon yapılır.


---

## 📌 Projede Öğrendiklerim

- **LangGraph ile State-Based Workflow Kullanımı**
- **LangChain ile LLM Tabanlı Yanıt Üretimi**
- **Tavily API ile Web Arama Entegrasyonu**
- **ChromaDB ile Vektör Tabanlı Bilgi Getirme**
- **Pydantic ile Veri Doğrulama**
- **Graph Yapısında İş Akışı Modelleme**

---


