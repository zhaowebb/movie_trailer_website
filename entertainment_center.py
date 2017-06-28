import media
import fresh_tomatoes

#populate movie objects
toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come alive',
                        'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=vwyZH85NQC4')
avatar = media.Movie('Avatar',
                     'A marine on an alien planet',
                     'http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg',
                     'http://www.youtube.com/watch?v=-9ceBgWV8io')

hangover = media.Movie('The Hangover',
                       'A story of drunk men',
                       'https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg',
                       'https://www.youtube.com/watch?v=tcdUhdOlz9M')

forres_gump = media.Movie('Forrest Gump',
                          'An inspiring story of Forrest Gump',
                          'https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg',
                          'https://www.youtube.com/watch?v=YNh9Es8Ut6U')

                                   
                                   
#store movies into a list and passed it to call funtion to open a page
movies = [toy_story, avatar, hangover, forres_gump]
fresh_tomatoes.open_movies_page(movies)


