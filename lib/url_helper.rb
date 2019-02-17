module UrlHelper
  def root_path
    config[:http_prefix]
  end
end
