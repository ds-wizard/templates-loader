# templates-loader

A simple tool for uploading DSW templates

## Usage

```
$ python setup.py install
$ dsw_template_loader <TEMPLATE_DIR> <API_URL> <SERVICE_TOKEN>
```

Arguments:
* `<TEMPLATE_DIR>` = root of your template to be loaded
  * Should contain `template.json` file describing the template
  * All files except `template.json` and `.git` will be uploaded to DSW! (Avoid storing extra files there...)
* `<API_URL>` = URL of API (!not client) of the DSW instance, e.g., `https://api.demo.ds-wizard.org` or `http://localhost:3000`
* `<SERVICE_TOKEN>` = service token set in your `application.yml` configuration of DSW backend (API)

## Note

This is intended just as a temporary solution until we release official "Template Development Kit".

