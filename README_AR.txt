AZEL OTC SIGNALS PRO — دليل التشغيل من الآيفون

ماذا يفعل؟
- TradingView يحلل الشارت ويرسل تنبيه CALL أو PUT عند إغلاق الشمعة.
- سيرفر سحابي يستقبل التنبيه ويرسله إلى محادثتك في Telegram.
- هذا مشروع إشارات فقط، ولا يفتح صفقات تلقائياً.

تنبيه مهم:
1) إشارات Pine تعتمد على بيانات الشارت المفتوح في TradingView.
2) بيانات OTC الخاصة بـ Pocket Option قد تختلف عن TradingView. لا تستخدم الإشارات على المال الحقيقي قبل مقارنة الأسعار واختبارها.
3) الإشارة تظهر بعد إغلاق الشمعة للتأكيد، وليست قبل افتتاحها.
4) لا توجد نسبة نجاح مضمونة.

الخطوة 1 — إنشاء بوت Telegram:
1. افتح Telegram وابحث عن @BotFather.
2. أرسل /newbot واتبع التعليمات.
3. اختر اسماً واسم مستخدم للبوت.
4. انسخ TOKEN واحتفظ به سرياً. لا ترسله لأي شخص.
5. افتح البوت الجديد واضغط Start.
6. لمعرفة chat_id: افتح هذا الرابط في Safari بعد استبدال TOKEN:
   https://api.telegram.org/botTOKEN/getUpdates
   ابحث عن "chat":{"id":...} وخذ الرقم. لا تشارك الرابط أو نتيجته مع أحد.

الخطوة 2 — نشر السيرفر:
1. أنشئ حساباً في Render من Safari.
2. ارفع ملفات هذا المشروع إلى مستودع GitHub خاص (Private) أو استخدم طريقة النشر التي يدعمها Render.
3. في Render اختر New > Web Service واربط المستودع.
4. Build Command: pip install -r requirements.txt
5. Start Command: gunicorn app:app
6. أضف Environment Variables:
   TELEGRAM_BOT_TOKEN = التوكن من BotFather
   TELEGRAM_CHAT_ID = رقم المحادثة
   WEBHOOK_SECRET = كلمة طويلة عشوائية من اختيارك
7. انشر الخدمة وانتظر ظهور رابط مثل:
   https://your-service.onrender.com
ملاحظة: خطة الاستضافة المجانية قد تتوقف أو تنام عند عدم الاستخدام؛ قد تتأخر التنبيهات. للتشغيل الأكثر اعتمادية تحتاج استضافة مدفوعة.

الخطوة 3 — إضافة المؤشر إلى TradingView:
1. افتح TradingView في Safari أو التطبيق.
2. افتح Pine Editor على الويب، وأنشئ مؤشراً جديداً.
3. انسخ محتوى Azel_OTC_Signals_PRO.pine والصقه ثم اضغط Save و Add to chart.
4. غيّر CHANGE_THIS_SECRET في إعدادات المؤشر إلى نفس WEBHOOK_SECRET الذي وضعته في Render.
5. افتح شارت الدقيقة الواحدة. لا تفترض أن رمز OTC في TradingView يطابق Pocket Option.

الخطوة 4 — إنشاء التنبيه:
1. اضغط Alert في TradingView.
2. Condition: Azel OTC Signals PRO.
3. اختر Any alert() function call.
4. فعّل Webhook URL وضع:
   https://your-service.onrender.com/webhook
5. أنشئ التنبيه.

الاختبار:
- انتظر إشارة على حساب تجريبي.
- تأكد من وصولها إلى Telegram.
- قارن رمز الزوج والسعر والتوقيت مع Pocket Option.
- سجل 100 إشارة على الأقل قبل التفكير باستخدام أموال حقيقية.

استكشاف الأخطاء:
- إذا لم يصل شيء: تأكد أن البوت بدأته بزر Start وأن chat_id والتوكن صحيحان.
- إذا ظهر 401: WEBHOOK_SECRET في TradingView لا يطابق الموجود في Render.
- إذا ظهر 500: راجع متغيرات البيئة في Render.
- إذا لا تظهر إشارات: هذا طبيعي مع الفلاتر المشددة؛ لا تخففها قبل فهم سبب قلة الإشارات.
