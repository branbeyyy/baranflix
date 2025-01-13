import pandas as pd

#Importing database
df=pd.read_csv(
    "C:/Users/Baran/Desktop/VSCode/baranflix/movies/mymoviedb.csv",
    lineterminator="\n"
    )

#Formatting months
def formatMonth(month: str) -> str:
    match month:
        case '01':
            return 'January'
        case '02':
            return 'February'
        case '03':
            return 'March'
        case '04':
            return 'April'
        case '05':
            return 'May'
        case '06':
            return 'June'
        case '07':
            return 'July'
        case '08':
            return 'August'
        case '09':
            return 'September'
        case '10':
            return 'October'
        case '11':
            return 'November'
        case '12':
            return 'December'

#Formatting days
def formatDay(day: str) -> str:
    match day:
        case '01':
            return '1st'
        case '02':
            return '2nd'
        case '03':
            return '3rd'
        case '04':
            return '4th'
        case '05':
            return '5th'
        case '06':
            return '6th'
        case '07':
            return '7th'
        case '08':
            return '8th'
        case '09':
            return '9th'
        case '21':
            return '21st'
        case '22':
            return '22nd'
        case '23':
            return '23rd'
        case '31':
            return '31st'
        case _:
            return f'{day}th'

#Formatting date
def formatDate(date: str) -> str:
    year = date[0:4]
    month = formatMonth(date[5:7])
    day= formatDay(date[8:10])
    return f'{month} {day}, {year}'

#Formatting language
def formatLanguage(language: str) -> str:
    match language:
        case 'en':
            return 'English'
        case 'es':
            return 'Spanish'
        case 'fr':
            return 'French'
        case 'de':
            return 'German'
        case 'it':
            return 'Italian'
        case 'ja':
            return 'Japanese'
        case 'ko':
            return 'Korean'
        case 'zh':
            return 'Chinese'
        case 'ru':
            return 'Russian'
        case 'pt':
            return 'Portuguese'
        case 'ar':
            return 'Arabic'
        case 'hi':
            return 'Hindi'
        case 'tr':
            return 'Turkish'

#Checking if all genres in movie are searched
def checkGenre(genres: list[str], i:int) -> bool:
    genreCounter = 0
    for genre in genres:
        if genre in df.loc[i,'Genre']:
            genreCounter += 1

    if genreCounter == len(genres):
        return True
    else:
        return False

#Filtering the database
def filterMovies(
    title: str = "",
    language: str = "",
    releaseDate: str = "",
    score: int = -1,
    genres: list[str] = [],
    amount: int = 0
    ) -> None:
    counter=0
    for i in range(len(df)):
    #Creating movie variables
        movieTitle=df.loc[i,'Title']
        movieLanguage=df.loc[i,'Original_Language']
        formattedLanguage = formatLanguage(movieLanguage)
        movieDate=df.loc[i,'Release_Date']
        formattedDate=formatDate(movieDate)
        movieScore=df.loc[i,'Vote_Average']
        overview=df.loc[i,'Overview']
        movieGenres = df.loc[i,'Genre']

        #Checking title
        titleCond = (
            title in movieTitle or
            title == ""
            )

        #Checking language
        langCond = (
            language == movieLanguage or
            language == formattedLanguage or
            language == ""
            )

        #Checking genres
        genreCond = checkGenre(genres, i)

        #Checking  score
        scoreCond = (
            score <= movieScore or
            score == -1
            )

        #Checking counter
        countCond = (
            counter < amount or
            amount == 0
        )

        #Checking if all variables are empty
        allEmptyCond = (
            title == "" and
            language == "" and
            releaseDate == "" and
            score == -1 and
            genres == [] and
            amount == 0
        )
        #Combining all conditions into one
        allConds = (
        titleCond and
        langCond and
        genreCond and
        countCond and
        scoreCond and not
        allEmptyCond
        )

        #Filtering with conditions
        if allConds:
            counter += 1
            print(
            f"Movie Index: {i}\n"
            f"Title: {movieTitle}\n"
            f"Language: {formattedLanguage}\n"
            f"Release Date: {formattedDate}\n"
            f"Score: {movieScore:.1f}/10 on IMDb\n"
            f"Overview: {overview}\n"
            f"Genres: {movieGenres}\n"
            )

    print(f"Showing {counter} items\n")
    
#filterMovies(title = "Dark Knight")
