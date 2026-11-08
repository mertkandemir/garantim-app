"""Builds privacy.html, support.html and index.html for Garantim's public site.

Run: python3 build.py   (writes the HTML files next to this script)
"""
import html
from pathlib import Path

UPDATED = {"en": "8 November 2026", "tr": "8 Kasım 2026", "de": "8. November 2026",
           "fr": "8 novembre 2026", "ja": "2026年11月8日", "ko": "2026년 11월 8일"}
EMAIL = "mertkandemir01@gmail.com"
ADDRESS = "Mert Kandemir, Erler Caddesi 83/1 Yaman Apt., 35310 İzmir, Türkiye"
LANGS = [("en", "English"), ("tr", "Türkçe"), ("de", "Deutsch"), ("fr", "Français"), ("ja", "日本語"), ("ko", "한국어")]

# Each section: (heading, [paragraphs]). Paragraphs may contain {email} and {address}.
PRIVACY = {
    "en": ("Privacy Policy", "Last updated", [
        ("In short", ["Garantim keeps your receipts and products on your iPhone. We have no servers, no accounts, no analytics and no ads, so we never receive your data."]),
        ("Who we are", ["Garantim is made by an independent developer: {address}. Contact: {email}."]),
        ("What stays on your iPhone", [
            "Receipt photos, the text read from them, your products, warranty dates, trips, tax free notes and settings are stored only in the app’s storage on your device.",
            "Receipts are read on the device with Apple’s Vision framework. Images and text are not sent anywhere.",
            "Deleting a product deletes its receipt photo. Deleting the app deletes everything."]),
        ("Camera and photos", ["The app asks for the camera and your photo library only so you can scan or pick a receipt. It never reads other photos."]),
        ("Notifications", ["Warranty, return and trip reminders are scheduled on your iPhone. No notification service of ours is involved."]),
        ("Purchases", ["Garantim Pro is sold through the App Store. Apple handles payment; we do not receive your name, email or payment details. Apple’s privacy policy applies to the purchase: apple.com/legal/privacy."]),
        ("iCloud backup", ["If you turn on iCloud backup, your data is stored in your own private iCloud account. We cannot access it."]),
        ("Data we collect", ["None. We do not collect, sell or share personal data, and we do not track you across apps or websites."]),
        ("Your rights", ["Because we hold no data about you, there is nothing for us to access, correct or delete. Your data is under your control in the app. For any privacy question under the GDPR, KVKK or other law, write to {email}."]),
        ("Changes", ["If this policy changes, the new version will be published on this page with a new date."]),
    ]),
    "tr": ("Gizlilik Politikası", "Son güncelleme", [
        ("Kısaca", ["Garantim fişlerini ve ürünlerini iPhone’unda saklar. Sunucumuz, hesap sistemimiz, analitik ve reklam aracımız yok; bu yüzden verilerin bize hiç ulaşmaz."]),
        ("Biz kimiz", ["Garantim bağımsız bir geliştirici tarafından yapılıyor: {address}. İletişim: {email}."]),
        ("iPhone’unda kalanlar", [
            "Fiş fotoğrafları, onlardan okunan metin, ürünlerin, garanti tarihleri, seyahatler, tax free notları ve ayarlar yalnızca cihazındaki uygulama alanında saklanır.",
            "Fişler cihazda Apple’ın Vision teknolojisiyle okunur. Görseller ve metinler hiçbir yere gönderilmez.",
            "Bir ürünü silince fiş fotoğrafı da silinir. Uygulamayı silince her şey silinir."]),
        ("Kamera ve fotoğraflar", ["Uygulama kameraya ve fotoğraf arşivine yalnızca fiş taraman ya da seçmen için erişir. Diğer fotoğraflarına bakmaz."]),
        ("Bildirimler", ["Garanti, iade ve seyahat hatırlatmaları iPhone’unda planlanır. Bizim bir bildirim sunucumuz yoktur."]),
        ("Satın almalar", ["Garantim Pro App Store üzerinden satılır. Ödemeyi Apple alır; adın, e-postan ya da ödeme bilgilerin bize gelmez. Satın almada Apple’ın gizlilik politikası geçerlidir: apple.com/legal/privacy."]),
        ("iCloud yedeği", ["iCloud yedeğini açarsan verilerin kendi özel iCloud hesabında saklanır. Biz erişemeyiz."]),
        ("Topladığımız veriler", ["Hiçbiri. Kişisel veri toplamıyor, satmıyor, paylaşmıyoruz; seni başka uygulama ya da sitelerde izlemiyoruz."]),
        ("Hakların", ["Hakkında hiçbir veri tutmadığımız için erişilecek, düzeltilecek ya da silinecek bir kayıt da yok; verilerin uygulamada senin kontrolünde. KVKK, GDPR ya da başka bir mevzuat kapsamındaki soruların için: {email}."]),
        ("Değişiklikler", ["Bu politika değişirse yeni hali bu sayfada yeni tarihle yayınlanır."]),
    ]),
    "de": ("Datenschutzerklärung", "Zuletzt aktualisiert", [
        ("Kurz gesagt", ["Garantim speichert deine Belege und Artikel auf deinem iPhone. Wir haben keine Server, keine Konten, keine Analyse- und keine Werbetools und erhalten deine Daten daher nie."]),
        ("Verantwortlicher", ["Garantim wird von einem unabhängigen Entwickler entwickelt: {address}. Kontakt: {email}."]),
        ("Was auf deinem iPhone bleibt", [
            "Belegfotos, der daraus gelesene Text, deine Artikel, Garantiedaten, Reisen, Tax-free-Notizen und Einstellungen werden nur im Speicher der App auf deinem Gerät abgelegt.",
            "Belege werden auf dem Gerät mit Apples Vision-Framework gelesen. Bilder und Text werden nirgendwohin gesendet.",
            "Wenn du einen Artikel löschst, wird auch sein Belegfoto gelöscht. Wenn du die App löschst, wird alles gelöscht."]),
        ("Kamera und Fotos", ["Die App nutzt Kamera und Fotomediathek nur, damit du einen Beleg scannen oder auswählen kannst. Andere Fotos liest sie nicht."]),
        ("Mitteilungen", ["Erinnerungen an Garantie, Rückgabe und Reisen werden auf deinem iPhone geplant. Ein eigener Mitteilungsdienst ist nicht beteiligt."]),
        ("Käufe", ["Garantim Pro wird über den App Store verkauft. Apple wickelt die Zahlung ab; wir erhalten weder Namen noch E-Mail noch Zahlungsdaten. Für den Kauf gilt Apples Datenschutzrichtlinie: apple.com/legal/privacy."]),
        ("iCloud-Backup", ["Wenn du das iCloud-Backup einschaltest, liegen deine Daten in deinem eigenen privaten iCloud-Konto. Wir haben keinen Zugriff darauf."]),
        ("Erhobene Daten", ["Keine. Wir erheben, verkaufen und teilen keine personenbezogenen Daten und verfolgen dich nicht über Apps oder Websites hinweg."]),
        ("Deine Rechte", ["Da wir keine Daten über dich speichern, gibt es bei uns nichts einzusehen, zu berichtigen oder zu löschen. Deine Daten bleiben in der App unter deiner Kontrolle. Fragen nach der DSGVO oder anderen Gesetzen: {email}. Du hast außerdem das Recht, dich bei einer Datenschutz-Aufsichtsbehörde zu beschweren."]),
        ("Änderungen", ["Wenn sich diese Erklärung ändert, wird die neue Fassung mit neuem Datum auf dieser Seite veröffentlicht."]),
    ]),
    "fr": ("Politique de confidentialité", "Dernière mise à jour", [
        ("En bref", ["Garantim conserve vos tickets et vos produits sur votre iPhone. Nous n’avons ni serveur, ni compte, ni outil d’analyse ou de publicité : nous ne recevons donc jamais vos données."]),
        ("Responsable du traitement", ["Garantim est développé par un développeur indépendant : {address}. Contact : {email}."]),
        ("Ce qui reste sur votre iPhone", [
            "Les photos de tickets, le texte lu, vos produits, dates de garantie, voyages, notes de détaxe et réglages sont enregistrés uniquement dans l’espace de l’app sur votre appareil.",
            "Les tickets sont lus sur l’appareil avec le framework Vision d’Apple. Les images et le texte ne sont envoyés nulle part.",
            "Supprimer un produit supprime la photo de son ticket. Supprimer l’app supprime tout."]),
        ("Appareil photo et photos", ["L’app accède à l’appareil photo et à la photothèque uniquement pour scanner ou choisir un ticket. Elle ne lit pas vos autres photos."]),
        ("Notifications", ["Les rappels de garantie, de retour et de voyage sont programmés sur votre iPhone, sans service de notification de notre part."]),
        ("Achats", ["Garantim Pro est vendu via l’App Store. Apple gère le paiement ; nous ne recevons ni votre nom, ni votre e-mail, ni vos données de paiement. La politique de confidentialité d’Apple s’applique à l’achat : apple.com/legal/privacy."]),
        ("Sauvegarde iCloud", ["Si vous activez la sauvegarde iCloud, vos données sont stockées dans votre propre compte iCloud privé. Nous n’y avons pas accès."]),
        ("Données collectées", ["Aucune. Nous ne collectons, ne vendons ni ne partageons de données personnelles, et nous ne vous suivons pas d’une app ou d’un site à l’autre."]),
        ("Vos droits", ["Comme nous ne détenons aucune donnée vous concernant, il n’y a rien à consulter, rectifier ou effacer chez nous ; vos données restent sous votre contrôle dans l’app. Pour toute question relative au RGPD : {email}. Vous pouvez aussi saisir la CNIL ou l’autorité de contrôle de votre pays."]),
        ("Modifications", ["Si cette politique change, la nouvelle version sera publiée sur cette page avec une nouvelle date."]),
    ]),
    "ja": ("プライバシーポリシー", "最終更新日", [
        ("概要", ["Garantimはレシートと商品の情報をお使いのiPhoneに保存します。サーバー、アカウント、解析ツール、広告はなく、開発者がお客様のデータを受け取ることはありません。"]),
        ("運営者", ["Garantimは個人の開発者が開発しています：{address}。連絡先：{email}"]),
        ("iPhoneに保存されるもの", [
            "レシートの写真、読み取ったテキスト、商品、保証期間、旅行、免税のメモ、設定は、端末内のアプリ領域にのみ保存されます。",
            "レシートはAppleのVisionフレームワークを使って端末上で読み取ります。画像やテキストが外部に送信されることはありません。",
            "商品を削除するとレシートの写真も削除されます。アプリを削除するとすべてのデータが削除されます。"]),
        ("カメラと写真", ["カメラと写真ライブラリは、レシートを撮影または選択するためだけに使用します。それ以外の写真を読み取ることはありません。"]),
        ("通知", ["保証・返品・旅行のリマインダーはiPhone上で設定されます。開発者の通知サーバーは使用しません。"]),
        ("購入", ["Garantim ProはApp Storeで販売されます。決済はAppleが行い、開発者がお名前、メールアドレス、支払い情報を受け取ることはありません。購入にはAppleのプライバシーポリシーが適用されます：apple.com/legal/privacy"]),
        ("iCloudバックアップ", ["iCloudバックアップをオンにすると、データはお客様ご自身の非公開のiCloudアカウントに保存されます。開発者はアクセスできません。"]),
        ("収集するデータ", ["ありません。個人情報を収集、販売、共有することはなく、他のアプリやウェブサイトをまたいだトラッキングも行いません。"]),
        ("お客様の権利", ["開発者はお客様のデータを保有していないため、開示・訂正・削除の対象となる情報はありません。データはアプリ内でお客様が管理できます。個人情報保護法などに関するお問い合わせ：{email}"]),
        ("変更", ["本ポリシーを変更する場合は、新しい日付とともにこのページで公開します。"]),
    ]),
    "ko": ("개인정보 처리방침", "최종 업데이트", [
        ("요약", ["Garantim은 영수증과 제품 정보를 사용자의 iPhone에 저장합니다. 서버, 계정, 분석 도구, 광고가 없으므로 개발자는 사용자의 데이터를 받지 않습니다."]),
        ("운영자", ["Garantim은 개인 개발자가 만듭니다: {address}. 연락처: {email}"]),
        ("iPhone에 남는 정보", [
            "영수증 사진, 읽어 낸 텍스트, 제품, 보증 기간, 여행, 택스 프리 메모, 설정은 기기의 앱 저장 공간에만 저장됩니다.",
            "영수증은 Apple의 Vision 프레임워크로 기기에서 읽습니다. 이미지와 텍스트는 어디로도 전송되지 않습니다.",
            "제품을 삭제하면 영수증 사진도 삭제됩니다. 앱을 삭제하면 모든 데이터가 삭제됩니다."]),
        ("카메라와 사진", ["앱은 영수증을 촬영하거나 선택할 때만 카메라와 사진 보관함을 사용합니다. 다른 사진은 읽지 않습니다."]),
        ("알림", ["보증, 반품, 여행 알림은 iPhone에서 예약됩니다. 개발자의 알림 서버는 사용하지 않습니다."]),
        ("구매", ["Garantim Pro는 App Store에서 판매됩니다. 결제는 Apple이 처리하며, 개발자는 이름, 이메일, 결제 정보를 받지 않습니다. 구매에는 Apple의 개인정보 처리방침이 적용됩니다: apple.com/legal/privacy"]),
        ("iCloud 백업", ["iCloud 백업을 켜면 데이터는 사용자 본인의 비공개 iCloud 계정에 저장됩니다. 개발자는 접근할 수 없습니다."]),
        ("수집하는 정보", ["없습니다. 개인정보를 수집, 판매, 공유하지 않으며 다른 앱이나 웹사이트에 걸쳐 추적하지 않습니다."]),
        ("사용자의 권리", ["개발자는 사용자에 관한 데이터를 보유하지 않으므로 열람, 정정, 삭제할 정보가 없습니다. 데이터는 앱 안에서 사용자가 직접 관리합니다. 개인정보 보호법 등에 관한 문의: {email}"]),
        ("변경", ["이 방침이 바뀌면 새 날짜와 함께 이 페이지에 게시합니다."]),
    ]),
}

SUPPORT = {
    "en": ("Garantim Support", "Contact", "Write to {email}. Please include your iPhone model, iOS version and a screenshot if something looks wrong. We usually answer within two working days.", [
        ("How do I restore my Pro purchase?", "Open Settings in Garantim and tap “Restore purchases”. Use the same Apple Account you bought Pro with."),
        ("How do I cancel my subscription?", "On your iPhone: Settings › your name › Subscriptions › Garantim Pro › Cancel. Pro stays active until the end of the period you paid for."),
        ("A receipt was read wrongly.", "Every field can be corrected before saving. Faded thermal receipts read best in good light, flat and filling the frame."),
        ("Are tax free amounts exact?", "No. They are estimates from the standard tax rate and typical refund fees. The store and the refund company decide the final amount."),
        ("How do I delete my data?", "Delete products in the app, or delete the app to remove everything. We hold no copy of your data."),
    ]),
    "tr": ("Garantim Destek", "İletişim", "{email} adresine yaz. Bir sorun varsa iPhone modelini, iOS sürümünü ve bir ekran görüntüsü ekle. Genellikle iki iş günü içinde yanıtlıyoruz.", [
        ("Pro satın alımımı nasıl geri yüklerim?", "Garantim’de Ayarlar’ı aç ve “Satın alımları geri yükle”ye dokun. Pro’yu aldığın Apple Hesabı’yla giriş yapmış olmalısın."),
        ("Aboneliğimi nasıl iptal ederim?", "iPhone’da: Ayarlar › adın › Abonelikler › Garantim Pro › Aboneliği İptal Et. Pro, ödediğin dönemin sonuna kadar açık kalır."),
        ("Bir fiş yanlış okundu.", "Kaydetmeden önce her alanı düzeltebilirsin. Soluk termal fişler iyi ışıkta, düz ve kadrajı dolduracak şekilde en iyi okunur."),
        ("Tax free tutarları kesin mi?", "Hayır. Standart vergi oranı ve olağan iade komisyonuyla hesaplanan tahminlerdir. Kesin tutarı mağaza ve iade şirketi belirler."),
        ("Verilerimi nasıl silerim?", "Ürünleri uygulamada sil ya da her şeyi kaldırmak için uygulamayı sil. Bizde verilerinin kopyası yok."),
    ]),
    "de": ("Garantim Support", "Kontakt", "Schreib an {email}. Wenn etwas nicht stimmt, gib bitte iPhone-Modell, iOS-Version und einen Screenshot an. Wir antworten meist innerhalb von zwei Werktagen.", [
        ("Wie stelle ich meinen Pro-Kauf wieder her?", "Öffne in Garantim die Einstellungen und tippe auf „Käufe wiederherstellen“. Nutze denselben Apple Account wie beim Kauf."),
        ("Wie kündige ich mein Abo?", "Auf dem iPhone: Einstellungen › dein Name › Abonnements › Garantim Pro › Abo kündigen. Pro bleibt bis zum Ende des bezahlten Zeitraums aktiv."),
        ("Ein Beleg wurde falsch gelesen.", "Jedes Feld lässt sich vor dem Speichern korrigieren. Verblasste Thermobelege werden bei gutem Licht, flach und formatfüllend am besten gelesen."),
        ("Sind die Tax-free-Beträge genau?", "Nein. Es sind Schätzungen aus dem Normalsteuersatz und üblichen Gebühren. Den genauen Betrag bestimmen Geschäft und Erstattungsfirma."),
        ("Wie lösche ich meine Daten?", "Lösche Artikel in der App oder lösche die App, um alles zu entfernen. Wir haben keine Kopie deiner Daten."),
    ]),
    "fr": ("Assistance Garantim", "Contact", "Écrivez à {email}. En cas de problème, indiquez votre modèle d’iPhone, la version d’iOS et joignez une capture d’écran. Nous répondons en général sous deux jours ouvrés.", [
        ("Comment restaurer mon achat Pro ?", "Ouvrez les réglages de Garantim et touchez « Restaurer les achats ». Utilisez le compte Apple avec lequel vous avez acheté Pro."),
        ("Comment résilier mon abonnement ?", "Sur l’iPhone : Réglages › votre nom › Abonnements › Garantim Pro › Annuler l’abonnement. Pro reste actif jusqu’à la fin de la période payée."),
        ("Un ticket a été mal lu.", "Chaque champ peut être corrigé avant l’enregistrement. Les tickets thermiques pâlis se lisent mieux sous une bonne lumière, à plat et en remplissant le cadre."),
        ("Les montants de détaxe sont-ils exacts ?", "Non. Ce sont des estimations fondées sur le taux normal et des frais habituels. Le magasin et la société de détaxe fixent le montant final."),
        ("Comment supprimer mes données ?", "Supprimez les produits dans l’app, ou supprimez l’app pour tout effacer. Nous n’avons aucune copie de vos données."),
    ]),
    "ja": ("Garantim サポート", "お問い合わせ", "{email} までご連絡ください。不具合の場合は、iPhoneの機種、iOSのバージョン、スクリーンショットを添えてください。通常2営業日以内に返信します。", [
        ("Proの購入を復元するには？", "Garantimの設定を開き、「購入を復元」をタップしてください。Proを購入したApple Accountでサインインしている必要があります。"),
        ("サブスクリプションを解約するには？", "iPhoneの「設定」›ユーザ名›「サブスクリプション」›「Garantim Pro」›「サブスクリプションをキャンセル」。支払い済みの期間が終わるまでProは有効です。"),
        ("レシートが正しく読み取られません。", "保存する前にすべての項目を修正できます。薄くなった感熱紙のレシートは、明るい場所で平らにし、画面いっぱいに写すとよく読み取れます。"),
        ("免税額は正確ですか？", "いいえ。標準税率と一般的な手数料から計算した見込み額です。最終的な金額は店舗と払い戻し会社が決めます。"),
        ("データを削除するには？", "アプリ内で商品を削除するか、アプリを削除するとすべて消去されます。開発者はデータのコピーを持っていません。"),
    ]),
    "ko": ("Garantim 지원", "문의", "{email}로 연락해 주세요. 문제가 있다면 iPhone 모델, iOS 버전, 스크린샷을 함께 보내 주세요. 보통 영업일 기준 2일 안에 답변합니다.", [
        ("Pro 구매를 복원하려면?", "Garantim의 설정을 열고 ‘구매 복원’을 누르세요. Pro를 구매한 Apple 계정으로 로그인되어 있어야 합니다."),
        ("구독을 해지하려면?", "iPhone에서 설정 › 사용자 이름 › 구독 › Garantim Pro › 구독 취소. 결제한 기간이 끝날 때까지 Pro는 유지됩니다."),
        ("영수증이 잘못 읽혔어요.", "저장하기 전에 모든 항목을 고칠 수 있습니다. 흐려진 감열지 영수증은 밝은 곳에서 평평하게 놓고 화면을 가득 채우면 잘 읽힙니다."),
        ("택스 프리 금액은 정확한가요?", "아닙니다. 표준 세율과 일반적인 수수료로 계산한 예상액입니다. 최종 금액은 매장과 환급 대행사가 정합니다."),
        ("데이터를 삭제하려면?", "앱에서 제품을 삭제하거나, 앱을 삭제하면 모두 지워집니다. 개발자는 데이터 사본을 갖고 있지 않습니다."),
    ]),
}

STYLE = """
:root{--green:#1F6F54;--soft:#E3F0EA;--text:#1A1F1C;--muted:#5B6560;--bg:#F7F8F6;--border:#DDE3DF}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Inter","Segoe UI","Hiragino Sans","Apple SD Gothic Neo",sans-serif}
main{max-width:720px;margin:0 auto;padding:32px 20px 64px}
.brand{color:var(--green);font-weight:700;text-decoration:none;font-size:18px}
nav{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0 28px}
nav a{padding:6px 12px;border:1px solid var(--border);border-radius:999px;color:var(--text);text-decoration:none;font-size:14px;background:#fff}
nav a[aria-current="true"]{background:var(--green);border-color:var(--green);color:#fff}
h1{font-size:30px;line-height:1.2;margin:0 0 4px}
h2{font-size:19px;margin:28px 0 6px}
.updated{color:var(--muted);font-size:14px;margin:0 0 8px}
p{margin:0 0 10px}
a{color:var(--green)}
details{background:#fff;border:1px solid var(--border);border-radius:12px;padding:14px 16px;margin:10px 0}
summary{font-weight:600;cursor:pointer}
details p{margin:10px 0 0}
section[lang]{display:none}
section[lang].on{display:block}
footer{margin-top:40px;color:var(--muted);font-size:13px}
"""

SCRIPT = """
(function(){
  var supported=%s;
  var q=new URLSearchParams(location.search).get('lang');
  var pick=q&&supported.indexOf(q)>=0?q:null;
  if(!pick){(navigator.languages||[navigator.language||'en']).some(function(l){var c=String(l).slice(0,2).toLowerCase();if(supported.indexOf(c)>=0){pick=c;return true}return false})}
  pick=pick||'en';
  document.documentElement.lang=pick;
  document.querySelectorAll('section[lang]').forEach(function(s){s.classList.toggle('on',s.lang===pick)});
  document.querySelectorAll('nav a').forEach(function(a){a.setAttribute('aria-current',a.dataset.lang===pick?'true':'false')});
})();
"""


def fill(text: str) -> str:
    out = html.escape(text)
    out = out.replace("{email}", f'<a href="mailto:{EMAIL}">{EMAIL}</a>')
    return out.replace("{address}", html.escape(ADDRESS))


def page(title: str, sections: str, file: str) -> str:
    nav = "".join(f'<a href="{file}?lang={c}" data-lang="{c}">{n}</a>' for c, n in LANGS)
    codes = "[" + ",".join(f"'{c}'" for c, _ in LANGS) + "]"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{STYLE}</style>
</head>
<body>
<main>
<a class="brand" href="index.html">Garantim</a>
<nav>{nav}</nav>
{sections}
<footer>© 2026 Mert Kandemir · <a href="privacy.html">Privacy</a> · <a href="support.html">Support</a></footer>
</main>
<script>{SCRIPT % codes}</script>
</body>
</html>
"""


def privacy() -> str:
    parts = []
    for code, _ in LANGS:
        title, updated, sections = PRIVACY[code]
        body = "".join(f"<h2>{html.escape(h)}</h2>" + "".join(f"<p>{fill(p)}</p>" for p in ps) for h, ps in sections)
        parts.append(f'<section lang="{code}"><h1>{html.escape(title)}</h1>'
                     f'<p class="updated">{html.escape(updated)}: {UPDATED[code]}</p>{body}</section>')
    return page("Garantim – Privacy Policy", "\n".join(parts), "privacy.html")


def support() -> str:
    parts = []
    for code, _ in LANGS:
        title, contact_h, contact, faq = SUPPORT[code]
        items = "".join(f"<details><summary>{html.escape(q)}</summary><p>{fill(a)}</p></details>" for q, a in faq)
        parts.append(f'<section lang="{code}"><h1>{html.escape(title)}</h1>'
                     f"<h2>{html.escape(contact_h)}</h2><p>{fill(contact)}</p>{items}</section>")
    return page("Garantim – Support", "\n".join(parts), "support.html")


def index() -> str:
    return """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Garantim</title><meta http-equiv="refresh" content="0; url=support.html"></head>
<body><a href="support.html">Garantim Support</a> · <a href="privacy.html">Privacy Policy</a></body></html>
"""


if __name__ == "__main__":
    here = Path(__file__).parent
    (here / "privacy.html").write_text(privacy(), encoding="utf-8")
    (here / "support.html").write_text(support(), encoding="utf-8")
    (here / "index.html").write_text(index(), encoding="utf-8")
    assert set(PRIVACY) == set(SUPPORT) == {c for c, _ in LANGS}
    print("written")
