source "https://rubygems.org"

# NOTE: GitHub Pages builds this site server-side with its own pinned
# `github-pages` gem (Jekyll 3.9), so this Gemfile only affects LOCAL preview.
# The classic github-pages stack uses APIs removed in modern Ruby, so for a
# working local server we use native Jekyll 4 here instead.
gem "jekyll", "~> 4.3"
# Pin to the libsass-based converter (like classic GitHub Pages). The newer 3.x
# uses dart-sass, which miscompiles the old vendored susy grid and breaks the
# responsive two-column desktop layout.
gem "jekyll-sass-converter", "~> 2.0"

gem "wdm", "~> 0.1.0" if Gem.win_platform?

# Plugins used by the site (see _config.yml)
group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-sitemap"
  gem "jekyll-redirect-from"
  gem "jekyll-paginate"
  gem "jekyll-gist"
end

gem "webrick", "~> 1.8"

# Stdlib gems unbundled from Ruby 3.4+/4.0
gem "csv"
gem "base64"
gem "bigdecimal"
gem "logger"
gem "ostruct"
gem "fiddle"
