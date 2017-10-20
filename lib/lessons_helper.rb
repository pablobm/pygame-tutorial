module LessonsHelper
  PAGES_BASE_PATH = Pathname(__dir__).join('../source')
  LESSON_PATH_REGEXP = %r{^lessons/[^/]+/index\.html$}

  def all_lessons
    @all_lessons ||= sitemap.resources
      .select{|r| r.path =~ LESSON_PATH_REGEXP }
      .sort_by{|r| r.path }
      .map{|r| LessonResource.new(r) }
  end

  def current_lesson
    in_lesson? && all_lessons[current_lesson_index]
  end

  def next_lesson
    @next_lesson ||= in_lesson? && all_lessons[current_lesson_index + 1]
  end

  def prev_lesson
    @prev_lesson ||= begin
      return nil unless in_lesson?
      prev_index = current_lesson_index - 1
      if prev_index >= 0
        all_lessons[prev_index]
      else
        nil
      end
     end
  end

  def current_lesson_index
    @current_lesson_index ||= all_lessons.find_index{|l| l.path == current_path }
  end

  def in_lesson?
    !! current_lesson_index
  end

  def lesson_path(lesson)
    lesson.path.gsub(%r{/[^/]+$}, '')
  end

  class LessonResource
    def initialize(resource)
      @resource = resource
    end

    def path
      resource.path
    end

    def title
      resource.data['title']
    end

    def url
      resource.url
    end

    private

    attr_reader :resource
  end
end
