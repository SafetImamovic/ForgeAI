$packages = @(
    "annotated-types==0.7.0",
    "anyio==4.3.0",
    "asgiref==3.8.1",
    "certifi==2024.2.2",
    "charset-normalizer==3.3.2",
    "crispy-bootstrap5==2024.2",
    "deprecation==2.1.0",
    "Django==5.0.6",
    "django-crispy-forms==2.1",
    "gotrue==2.4.2",
    "h11==0.14.0",
    "httpcore==1.0.5",
    "httpx==0.27.0",
    "idna==3.7",
    "packaging==24.0",
    "pip==24.0",
    "postgrest==0.16.4",
    "psycopg2==2.9.9",
    "pydantic==2.7.1",
    "pydantic-core==2.18.2",
    "python-dateutil==2.9.0.post0",
    "python-dotenv==1.0.1",
    "realtime==1.0.4",
    "requests==2.32.2",
    "six==1.16.0",
    "sniffio==1.3.1",
    "sqlparse==0.5.0",
    "storage3==0.7.4",
    "StrEnum==0.4.15",
    "stripe==9.8.0",
    "supabase==2.4.6",
    "supafunc==0.4.5",
    "typing-extensions==4.12.0",
    "tzdata==2024.1",
    "urllib3==2.2.1",
    "websockets==12.0"
)

foreach ($package in $packages) {
    Write-Output "Instalira $package"
    pip install $package
}
