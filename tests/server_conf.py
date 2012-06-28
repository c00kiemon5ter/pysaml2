try:
    from xmlsec_location import xmlsec_path
except ImportError:
    xmlsec_path = '/opt/local/bin/xmlsec1'

CONFIG={
    "entityid" : "urn:mace:example.com:saml:roland:sp",
    "name" : "urn:mace:example.com:saml:roland:sp",
    "description": "My own SP",
    "service": {
        "sp": {
            "endpoints":{
                "assertion_consumer_service": ["http://lingon.catalogix.se:8087/"],
            },
            "required_attributes": ["surName", "givenName", "mail"],
            "optional_attributes": ["title"],
            "idp": ["urn:mace:example.com:saml:roland:idp"],
        }
    },
    "debug" : 1,
    "key_file" : "test.key",
    "cert_file" : "test.pem",
    "ca_certs": "cacerts.txt",
    "xmlsec_binary" : xmlsec_path,
    "metadata": {
        "local": ["idp.xml", "vo_metadata.xml"],
    },
    "virtual_organization" : {
        "urn:mace:example.com:it:tek":{
            "nameid_format" : "urn:oid:1.3.6.1.4.1.1466.115.121.1.15-NameID",
            "common_identifier": "umuselin",
        }
    },
    "subject_data": "subject_data.db",
    "accepted_time_diff": 60,
    "attribute_map_dir" : "attributemaps",
    "organization": {
        "name": ("AB Exempel", "se"),
        "display_name": ("AB Exempel", "se"),
        "url": "http://www.example.org",
    },
    "contact_person": [{
            "given_name": "Roland",
            "sur_name": "Hedberg",
            "telephone_number": "+46 70 100 0000",
            "email_address": ["tech@eample.com", "tech@example.org"],
            "contact_type": "technical"
        },
    ],
    "logger": {
        "rotating": {
            "filename": "sp.log",
            "maxBytes": 100000,
            "backupCount": 5,
        },
        "loglevel": "info",
    }
}
