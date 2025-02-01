# PeerFund

P2P Yatırım Projesi
Bu proje, P2P (Peer-to-Peer) yatırım platformu oluşturmayı amaçlayan bir web uygulamasıdır. Kullanıcılar, birbirlerine yatırım yaparak finansal fırsatlar yaratabilir ve yapay zeka (AI) destekli analizler sayesinde daha bilinçli kararlar alabilirler. Proje, Flask web framework'ü kullanılarak geliştirilmiş olup, SQL Server veritabanına bağlanmakta ve çeşitli yapay zeka teknikleriyle kullanıcı deneyimini geliştirmektedir.

Proje Özeti
Flask: Web uygulamasının sunucusu ve backend kısmı için kullanılan framework.
SQL Server: Veritabanı yönetim sistemi olarak kullanıldı ve kullanıcı bilgileri, yatırım verileri ve işlem geçmişi burada saklanır.
Yapay Zeka: Yatırım kararlarını optimize etmek ve kullanıcıların portföylerine yönelik öneriler sunmak için kullanıldı.
Proje, temelde yatırımcıların ve girişimcilerin doğrudan birbirlerine yatırım yapmalarını sağlar. Ayrıca, yapay zeka algoritmaları kullanarak yatırım fırsatlarını değerlendirir, risk analizleri yapar ve kullanıcılara daha iyi yatırım önerileri sunar.

Kullanılan Teknolojiler ve Araçlar
Flask
Flask: Python ile yazılmış bir mikro web framework'üdür. Web uygulamanızın backend kısmını yönetmek için kullanıldı. RESTful API'ler oluşturmak ve kullanıcı etkileşimlerini yönetmek için Flask, hafifliği ve esnekliği sayesinde tercih edilmiştir.

SQL Server
SQL Server: Kullanıcı verilerini ve yatırım bilgilerini saklamak için SQL Server veritabanı kullanıldı. Flask ile SQL Server arasındaki bağlantıyı sağlamak için pyodbc veya SQLAlchemy gibi Python kütüphaneleri kullanıldı. Bu sayede, kullanıcıların veritabanına sorunsuz bir şekilde veri eklemeleri, silmeleri veya güncellemeleri mümkün oldu.

Yapay Zeka (AI)
Yapay Zeka Kütüphaneleri: Projeye entegre edilen yapay zeka algoritmaları, kullanıcıların yatırım portföylerine yönelik öneriler sunmak için kullanıldı. Bu algoritmalar, makine öğrenmesi modelleri (örneğin, regresyon, karar ağaçları, destek vektör makineleri (SVM)) ile eğitildi ve yatırım fırsatlarının değerlendirilmesine yardımcı oldu.

Veri Analizi ve Modelleme: Kullanıcıların finansal verilerini analiz etmek için Pandas ve NumPy gibi Python kütüphaneleri kullanıldı. Yapay zeka için ise, scikit-learn veya daha gelişmiş yöntemler için TensorFlow veya Keras gibi kütüphaneler tercih edilebilir.

HTML, CSS ve JavaScript
HTML ve CSS: Web sitesinin görsel tasarımını yapmak ve kullanıcı dostu bir arayüz sağlamak için kullanıldı.
JavaScript: Kullanıcı etkileşimini sağlamak ve sayfa üzerinde dinamik işlemler gerçekleştirmek için kullanıldı.
