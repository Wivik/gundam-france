# Garbage Collector Hugo Theme

This is a Hugo Theme I've made for my blog [Garbage Collector](https://blog.zedas.fr) for the static site generator [Hugo](https://gohugo.io). It is based on the [Simple.css](https://simplecss.org) framework with some customization and have some inspiration took from the [Casper3](https://github.com/jonathanjanssens/hugo-casper3) theme previously used for this blog.

This theme was made for my own blog, so there is not warranty that it'll fit for any other Hugo site. However, feel free to use it, customize it, enhance it, and so on.

Supports pagination, multilingual, categories, and RSS generator.

As I'm not a web developer, if some code parts of this theme makes your eyes bleed, please forgive me.

![theme](theme.png)

## How to use

Just clone this repository as a submodule of your Hugo site repository.

```bash
git submodule add https://github.com/Wivik/garbage-collector-theme.git
```

Then, in your config file (YAML example) :

```yaml
theme: garbage-collector-theme
```

The main pages from top menu should be created inside `content/<lang>` folder.

The blog posts must be created inside the `content/<lang>/posts` folder.

To create a new blog post :

```bash
hugo new posts/my-new-post.md
```

The file will be created inside the default language, which is French.

## Config example

Here is an example of `config.yaml` file, with multilingual support.

```yaml
---
baseURL: https://yoursite.com
languageCode: fr-FR
title: Your Site Name
theme: garbage-collector-theme
footnoteReturnLinkContents: "^"

DefaultContentLanguage: fr
DefaultContentLanguageInSubdir: true

params:
  ## all content must be in content/posts
  mainSections: ["posts"]
  author: "Your Name"
  avatar: "/your_avatar.png"
  backgroundImage: "/images/background.jpg"
  ## number of posts per pages
  pagination: 10
  ## set true or false to enable pagination or not
  paginate: true

languages:
  fr:
    contentDir: "content/fr"
    languageName: 'Français'
    weight: 1
    description: "Mon Site"
    menu:
      main:
        - identifier: "about"
          name: "👤 A Propos"
          url: "/fr/a-propos/"
          weight: 10
        - identifier: "contact"
          name: "💬 Contact"
          url: "/fr/contact/"
          weight: 20
        - identifier: "rss"
          name: "📰 RSS"
          url: "/fr/index.xml"
          weight: 99
  en:
    contentDir: "content/en"
    languageName: "English"
    weight: 2
    description: "Your Site"
    menu:
      main:
        - identifier: "about"
          name: "👤 About"
          url: "/en/about/"
          weight: 10
        - identifier: "contact"
          name: "💬 Contact"
          url: "/en/contact/"
          slug: "contact"
          weight: 20
        - identifier: "rss"
          name: "📰 RSS"
          url: "/en/index.xml"
          weight: 99

taxonomies:
  category: "categories"
  tag: "tags"
  series: "series"

privacy:

  vimeo:
    disabled: false
    simple: true

  twitter:
    disabled: false
    enableDNT: true
    simple: true

  instagram:
    disabled: false
    simple: true

  youtube:
    disabled: false
    privacyEnhanced: true
```

## Multilingual support

You will find in the `i18n` folder two languages files for the template textes.

## License

This theme is licenced under GPL V3.0. See [LICENSE](LICENSE) file for more details.
