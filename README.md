# DatadogScripts
Place cloudflare API key in start_host.sh

Webhooks are not customizable and can only send POST requests.
This script listens for post request on a given port and redirects for my usage.

Endpoints
POST /lucianp2dr
Connects to Cloudflare API service updating my A record to Azure DR. This webhook will be triggered by datadog upon self-hosted server connection failure.
