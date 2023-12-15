{
    "name": "SaaS: Portal",
    "summary": "Allows to customers see their Builds at Portal",
    "version": "17.0.0.0.0",
    "application": False,
    "author": "IT-Projects LLC, Eugene Molotov",
    "support": "it@it-projects.info",
    "license": "AGPL-3",
    "depends": [
        "saas",
        "portal",
        "saas_domain_names",
        "saas_expiration",
        "saas_limit_max_users",
        "saas_build_admin",
        "saas_backups",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "security/ir.model.access.csv",
        "security/saas_db_security.xml",
        "views/saas_db_views.xml",
        "views/portal_templates.xml",
    ],
    "demo": [],
    "qweb": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    "installable": True,
}
