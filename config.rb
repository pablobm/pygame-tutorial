# Activate and configure extensions
# https://middlemanapp.com/advanced/configuration/#configuring-extensions

activate :autoprefixer do |prefix|
  prefix.browsers = "last 2 versions"
end

activate :livereload

set :markdown_engine, :redcarpet

class SyntaxHighlighting < Redcarpet::Render::HTML
  def block_code(code, language)
    language = 'ruby' if language.to_s.strip.empty?
    Albino.colorize(code, language)
  end
end

set(
  :markdown,

  renderer: SyntaxHighlighting,

  no_intra_emphasis:   true,
  tables:              true,
  fenced_code_blocks:  true,
  autolink:            true,
  strikethrough:       true,
  lax_html_blocks:     true,
  space_after_headers: true,
  superscript:         true,
)


# Layouts
# https://middlemanapp.com/basics/layouts/

# Per-page layout changes
page '/*.xml', layout: false
page '/*.json', layout: false
page '/*.txt', layout: false

# With alternative layout
# page '/path/to/file.html', layout: 'other_layout'

# Proxy pages
# https://middlemanapp.com/advanced/dynamic-pages/

# proxy(
#   '/this-page-has-no-template.html',
#   '/template-file.html',
#   locals: {
#     which_fake_page: 'Rendering a fake page with a local variable'
#   },
# )

# Helpers
# Methods defined in the helpers block are available in templates
# https://middlemanapp.com/basics/helper-methods/

# helpers do
#   def some_helper
#     'Helping'
#   end
# end

# Build-specific configuration
# https://middlemanapp.com/advanced/configuration/#environment-specific-settings

# configure :build do
#   activate :minify_css
#   activate :minify_javascript
# end
