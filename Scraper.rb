require 'HTTParty'
require 'Nokogiri'

class Scraper
attr_accessor :parse

  def initialize
    doc = HTTParty.get("https://reddit.com")
    @parse [] = Nokogiri::HTML(doc)
   end


end
