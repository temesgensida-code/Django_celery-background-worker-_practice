# Host This Project On Azure From VS Code (Azure Extensions)

This guide uses the Azure extensions inside VS Code so you can deploy without memorizing CLI commands.

## 1) Install VS Code extensions

Install these from Extensions view:

- Azure Account (`ms-vscode.azure-account`)
- Azure App Service (`ms-azuretools.vscode-azureappservice`)
- Azure Resources (`ms-azuretools.vscode-azureresourcegroups`)
- Azure Static Web Apps (`ms-azuretools.vscode-azurestaticwebapps`) (optional, for frontend hosting)

## 2) Sign in to Azure in VS Code

1. Open Command Palette.
2. Run `Azure: Sign In`.
3. In the Azure side panel, confirm your subscription is visible.

## 3) Prepare required cloud values

Before deployment, prepare these values (from your Azure resources):

- PostgreSQL connection string for `DATABASE_URL`
- Redis connection string for `CELERY_BROKER_URL`
- A strong random value for `DJANGO_SECRET_KEY`

Use `.env.azure.example` as the source for required setting names.

## 4) Create three Linux App Services (web, worker, beat)

In the Azure panel:

1. Expand App Service.
2. Click `+` and create a new Web App (Linux) for each role:
   - `<name>-web`
   - `<name>-worker`
   - `<name>-beat`
3. Use Python runtime for all three.
4. Keep all three in the same resource group and region.

## 5) Deploy code to each App Service from VS Code

For each app (`web`, `worker`, `beat`):

1. In Explorer, right-click project root.
2. Choose `Deploy to Web App...`.
3. Pick the target app in Azure.
4. Confirm deployment.

Use the same repository deployment package for all three apps.

## 6) Configure App Settings for all three apps

For each app in Azure panel:

1. Right-click app and open in portal.
2. Go to Environment variables.
3. Add the values from `.env.azure.example`.

Minimum required in production:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_CSRF_TRUSTED_ORIGINS`
- `DATABASE_URL`
- `CELERY_BROKER_URL`

## 7) Set Startup Command per app

Use values from `deploy/azure-start-commands.txt`.

- web app startup command: migration + collectstatic + gunicorn
- worker app startup command: celery worker
- beat app startup command: celery beat

Set the correct command for each app in App Service configuration.

## 8) Restart and verify

1. Restart all three apps from Azure panel or portal.
2. Open Log Stream for each app:
   - web logs should show gunicorn startup
   - worker logs should show celery worker ready
   - beat logs should show `DatabaseScheduler` and scheduled task dispatch
3. Open the web URL and test:
   - `/api/joke/`
   - `/api/joke/stream/`

## 9) Optional frontend hosting from VS Code

You can host `displayer` in Azure Static Web Apps:

1. Open Azure panel and create a Static Web App.
2. Set app location to `displayer`.
3. Build command: `npm run build`.
4. Output location: `dist`.

Then set CORS and frontend origin values in backend app settings.

## Troubleshooting

- If web starts but API errors on DB calls, verify `DATABASE_URL` format and SSL requirement.
- If tasks are not processed, verify worker app is running and uses same `CELERY_BROKER_URL` as beat.
- If beat starts but no periodic jobs fire, verify migration `api.0002_seed_periodic_task` applied and beat logs show `DatabaseScheduler`.
