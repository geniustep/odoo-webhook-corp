# 🚀 Odoo Webhook Corp

<div dir="rtl">

## 📋 نظرة عامة

مستودع متكامل يحتوي على مشروعين رئيسيين لإدارة Webhooks من Odoo:

1. **Odoo Webhook Server** - خادم API مبني على FastAPI لاستعلام أحداث Webhook
2. **Custom Model Webhook** - نموذج Odoo مخصص لتسجيل أحداث Webhook

</div>

## 📦 محتويات المستودع

```
odoo-webhook-corp/
├── odoo-webhook-server/      # خادم API FastAPI
│   ├── main.py
│   ├── config.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── webhook/              # معالجة Webhooks
│   ├── core/                 # الوحدات الأساسية
│   └── clients/              # عملاء API
│
└── custom-model-webhook/     # نموذج Odoo المخصص
    ├── __manifest__.py
    ├── models/               # نماذج Odoo
    ├── security/             # أذونات الأمان
    └── views/                # واجهات المستخدم
```

---

## 🔗 العلاقة بين المشروعين

### Custom Model Webhook (Odoo Module)
- **الوظيفة:** نموذج Odoo مخصص (`update.webhook`) يسجل أحداث Webhook
- **المكان:** يعمل داخل Odoo
- **البيانات:** يخزن الأحداث في قاعدة بيانات Odoo

### Odoo Webhook Server (FastAPI)
- **الوظيفة:** خادم API لاستعلام الأحداث من نموذج `update.webhook`
- **المكان:** يعمل كخدمة منفصلة
- **الاتصال:** يتصل بـ Odoo API لقراءة البيانات

---

## 🚀 البدء السريع

### 1. تثبيت Custom Model في Odoo

```bash
# نسخ المجلد إلى مسار Odoo
cp -r custom-model-webhook /opt/odoo18/custom_models/auto_webhook

# تحديث قائمة الوحدات في Odoo
# ثم تفعيل الوحدة من واجهة Odoo
```

### 2. تشغيل Webhook Server

```bash
cd odoo-webhook-server
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 📚 التوثيق

- **Webhook Server:** راجع [odoo-webhook-server/README.md](odoo-webhook-server/README.md)
- **Custom Model:** راجع [custom-model-webhook/__manifest__.py](custom-model-webhook/__manifest__.py)

---

## 🔧 الإعدادات

### متغيرات البيئة (Webhook Server)

أنشئ ملف `.env` في `odoo-webhook-server/`:

```env
ODOO_URL=https://app.propanel.ma
ODOO_DB=your_database
ODOO_USERNAME=admin
ODOO_PASSWORD=your_password
API_HOST=0.0.0.0
API_PORT=8000
```

---

## 📝 الترخيص

هذا المشروع مرخص تحت رخصة MIT.

---

<div align="center">

**Made with ❤️ by GeniusStep Team**

</div>

