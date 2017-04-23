module LessonsHelper
  PAGES_BASE_PATH = Pathname(__dir__).join('../source')
  LESSONS_RELPATH = 'lessons'

  def all_lessons
    Pathname(__dir__)
      .join(PAGES_BASE_PATH, LESSONS_RELPATH)
      .children
      .map{|path| Lesson.new(path, sitemap: sitemap) }
  end

  class Lesson
    def initialize(fs_path, sitemap:)
      @fs_path = fs_path
      @sitemap = sitemap
    end

    def path
      to_site_path(fs_path)
    end

    def title
      sitemap
        .find_resource_by_destination_path(path_with_file)
        .data
        .title
    end

    private

    attr_reader :fs_path, :sitemap

    def path_with_file
      to_site_path(fs_path.join('index.html'))
    end

    def to_site_path(file_path)
      file_path
        .relative_path_from(PAGES_BASE_PATH)
        .to_s
    end
  end
end
