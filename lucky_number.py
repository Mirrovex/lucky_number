from tkinter import *

def center(win):
    win.update_idletasks()
    width = 620
    frame_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frame_width
    height = 900
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frame_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y - 50))

root = Tk()
root.title('Szczesliwa liczba')
center(root)

frame0 = Frame(root)
frame0.pack(pady = 15)

frame_label = Frame(frame0)
frame_label.grid(row = 0, column = 0)
label_date = Label(frame_label, text = 'Wpisz date urodzenia:')
label_date.grid(row = 0, column = 0, pady = 2)
label_name = Label(frame_label, text = 'Wpisz imie i nazwisko:')
label_name.grid(row = 1, column = 0, pady = 2)
label_age = Label(frame_label, text = 'Wpisz dzisiejszy rok:')
label_age.grid(row = 2, column = 0, pady = 2)

frame_entry = Frame(frame0)
frame_entry.grid(row = 0, column = 1)
date = StringVar()
entry_date = Entry(frame_entry, textvariable = date, width = 35)
entry_date.grid(row = 0, column = 0, pady = 2)
name = StringVar()
entry_name = Entry(frame_entry, textvariable = name, width = 35)
entry_name.grid(row = 1, column = 0, pady = 2)
age = StringVar()
entry_age = Entry(frame_entry, textvariable = age, width = 35)
entry_age.grid(row = 21, column = 0, pady = 2)


frame1_1 = Frame(root)
frame1_1.pack()
frame_1 = Frame(frame1_1)
frame_1.grid(row = 0, column = 0)
frame1_2 = Frame(frame1_1)
frame1_2.grid(row = 0, column = 1, sticky = N, pady = 3)

liczba = IntVar()
liczba.set(1)

def wyswietl_znaczenie():
    if liczba.get() == 0:
        znaczenie.set(lista[int(text0.get()[-7])])
    elif liczba.get() == 1:
        znaczenie.set(lista[int(text1.get()[-7])])
    elif liczba.get() == 2:
        znaczenie.set(lista[int(text2.get()[-7])])
    elif liczba.get() == 3:
        znaczenie.set(lista[int(text3.get()[-7])])
    elif liczba.get() == 4:
        znaczenie.set(lista[int(text4.get()[-7])])
    elif liczba.get() == 5:
        znaczenie.set(lista[int(text5.get()[-7])])
    elif liczba.get() == 6:
        znaczenie.set(lista[int(text6.get()[-7])])


text1 = StringVar()
text1.set('Liczba urodzeniowa:        ')
label_1 = Label(frame_1, textvariable = text1)
label_1.pack(anchor = W, pady = 3)
radio1 = Radiobutton(frame1_2, variable = liczba, value = 1, command = wyswietl_znaczenie)
radio1.pack()

text2 = StringVar()
text2.set('Liczba imienia:        ')
label_2 = Label(frame_1, textvariable = text2)
label_2.pack(anchor = W, pady = 1)
radio2 = Radiobutton(frame1_2, variable = liczba, value = 2, command = wyswietl_znaczenie)
radio2.pack()

text3 = StringVar()
text3.set('Liczba nazwiska:        ')
label_3 = Label(frame_1, textvariable = text3)
label_3.pack(anchor = W, pady = 3)
radio3 = Radiobutton(frame1_2, variable = liczba, value = 3, command = wyswietl_znaczenie)
radio3.pack()

text4 = StringVar()
text4.set('Liczba imienia i nazwiska:        ')
label_4 = Label(frame_1, textvariable = text4)
label_4.pack(anchor = W, pady = 1)
radio4 = Radiobutton(frame1_2, variable = liczba, value = 4, command = wyswietl_znaczenie)
radio4.pack()

frame_2 = Frame(frame_1)
frame_2.pack(pady = 13)

frame_2_2 = Frame(frame1_2)
frame_2_2.pack(pady = 13)

text5 = StringVar()
text5.set('Twoja szczesliwa liczba:        ')
label_5 = Label(frame_2, textvariable = text5)
label_5.pack(anchor = W, pady = 3)
radio5 = Radiobutton(frame_2_2, variable = liczba, value = 5, command = wyswietl_znaczenie)
radio5.pack()

text6 = StringVar()
text6.set('Twoja szczesliwa liczba w tym roku:        ')
label_6 = Label(frame_2, textvariable = text6)
label_6.pack(anchor = W, pady = 1)
radio6 = Radiobutton(frame_2_2, variable = liczba, value = 6, command = wyswietl_znaczenie)
radio6.pack()

frame_3 = Frame(root)
frame_3.pack(pady = 15)

label_tytul = Label(frame_3, text = 'Znaczenie:')
label_tytul.pack(pady = 10)

znaczenie = StringVar()
label_znaczenie = Label(frame_3, textvariable = znaczenie)
label_znaczenie.pack()


text_0 = """SEKRETNA LICZBA
Udało ci się odnaleźć sekretną liczbę :D"""

text_1 = """NUMEROLOGICZNA JEDYNKA
Wspaniały otwarty umysł, pełen inicjatyw. Jedynka daje siłę, impuls, rozmach, który porusza świat.
To urodzeni przywódcy, dynamiczni, charyzmatyczni. Posiadają odwagę i zdecydowanie. Ich siła
przekonywania i ekstrawertyczna osobowość inspiruje i pobudza innych do dawania tego, 
co mają w sobie najlepszego.

Jedynki wybrały tę cyfrę, ponieważ ich kosmicznym zobowiązaniem jest inspirowanie innych ludzi w taki
sposób, by uwierzyli we własne siły a także i to, że czyniąc użytek z własnych zasobów mogą zrealizować
każdy postawiony sobie cel. Powinny udowodnić i pokazać na swoim własnym przykładzie, że jest to możliwe.
Natomiast ich osobistym wyzwaniem jest przezwyciężenie pułapek "ego" oraz nauka jak współpracować i
dzielić się z innymi.

CECHY POZYTYWNE
Ambicja, zdolności przywódcze, niezwykła inteligencja, rozwaga i racjonalizm, kreatywność, rozwinięta
wyobraźnia, oryginalność, wiara w siebie, logika, pragmatyzm, wybitna osobowość, potrzeba wyróżniania
się i bycia ważnym, talent, elokwencja, wielka potrzeba wolności i niezależności.

CECHY NEGATYWNE
Nadmierna duma, egocentryzm, charakter władczy, despotyczny i dyktatorski, egoizm, materializm,
nieumiejętność uznawania własnych błędów, łatwość ranienia innych, sarkazm, beznamiętność, nie
przebiera w środkach w dążeniu do celu."""

text_2 = """NUMEROLOGICZNA DWÓJKA
Wyróżniają się łagodnością charakteru, skromnością i dobrocią. Zazwyczaj są istotami miłymi spokojnymi
i tolerancyjnymi. Ich głównym pragnieniem jest życie w pokoju i harmoni ze wszystkimi. Poważne, pracowite,
odpowiedzialne. Ich wyrozumiałość dla bliźnich otwiera im w życiu wiele drzwi, zamkniętych przed innymi.
Potrafią dostosować się do każdej sytuacji i osoby. Przezorne, dyskretne, nieśmiałe i introwertyczne.

Osoby o tej wibracji urodzenia wybrały tę cyfrę, ponieważ ich kosmicznym zobowiązaniem jest uczyć innych
ludzi, że zrozumienie i tolerancja są atrybutami niezbędnymi duszy aby była doskonałą i pełną. Powinny
nauczyć innych, że gdy jesteśmy elastyczni, zdolni do akceptacji i przebaczenia wygrywamy najważniejszą
bitwę - osiągamy naszą wewnętrzną równowagę.
Natomiast ich osobistym wyzwaniem jest nauka poczucia własnej wartości oraz umocnienie go
przezwyciężając słabości i niepewności tej cyfry.

CECHY POZYTYWNE
Dyplomacja, wyrozumiałość, umiejętność współpracy w grupie, łagodność, wrażliwość, ugodowość i
dobrotliwość, uduchowienie, chłonność umysłu, szczerość, prostoduszność, skromność, koleżeńskość i
łatwość adaptacji, zawierania przyjaźni, wybaczania i zrozumienia.

CECHY NEGATYWNE
Niepewnosc, kompleksy, które odbierają wiarę w siebie i mogą powodować usuwanie się na dalszy plan, 
nadwrażliwość i drażliwość, wobec ryzyka paraliżuje je strach, nadmierna pobłażliwość i dobrotliwość,
które mogą być nadużywane przez innych."""

text_3 = """NUMEROLOGICZNA TRÓJKA
Kochają życie i wszędzie wnoszą radość. Żadna inna wibracja nie daje tyle sympatii, światła i czaru.
Dobre, łagodne i wielkoduszne Trójki to osoby energiczne, entuzjastyczne i pełne życia. Potrafią umilać
życie innym ludziom. Są utalentowane i wszechstronne. Ich umysł jest bystry i lotny. Sympatyczne i urocze.
Mają ogromną łatwość wysławiania się i komunikowania. Bez trudu nawiązują kontakty z wszystkimi. To osoby
w "czepku urodzone".

Osoby o tej wibracji urodzenia wybrały tę cyfrę, ponieważ ich kosmicznym zobowiązaniem jest pokazanie innym,
że optymizmem i pozytywną filozofia można przezwyciężyć wszelkie przeszkody oraz próby dnia codziennego,
że szczęście, wiara i wyobraźnia pomagają nam porozumiewać się z innymi. Łączą nas z ludźmi i otwierają przed
nami wszystkie drzwi.
Natomiast ich osobistym wyzwaniem jest nauka koncentracji i skupienia oraz przezwyciężenie powierzchowności
i "rozbiegania" ich czarującej, ale czasami niedojrzałej osobowości.

CECHY POZYTYWNE
Charyzma, obrotność, artystyczny i twórczy talent, elokwencja, łatwość w kontaktach z innymi ludźmi,
lubi być w centrum zainteresowania, wielkoduszność, idealizm, optymizm, wesołość, serdeczność, pozytywne
myślenie, zapał do działań, natchnienie, łagodność uczuć, błyskotliwa i promienna osobowość.

CECHY NEGATYWNE
Lekkomyślność, próżność, niedojrzałość, niestałość, powierzchowność, brak wytrwałości, nieodpowiedzialność,
unika zobowiązań, ucieka od rzeczywistości i kłopotów, nadmierna podatność na wływy innych, ekstrawagancja,
zadufanie, skłonność do mitomanii."""

text_4 = """NUMEROLOGICZNA CZWÓRKA
Poważne, praktyczne i pracowite. Wytrwałe, odpowiedzialne, godne zaufania. Lubią porządek i dyscyplinę.
Są logiczne, myślą analitycznie i racjonalnie. Cechy te pozwalają im podejmować trafne decyzje i uparcie
podążać do celu. Mówią językiem zwięzłym i precyzyjnym. Często trudno im wyrazić swoje uczucia. Bywają surowe
i szorstkie w obyciu. Wierne i lojalne w przyjaźni. Ich głębokie poczucie sprawiedliwości społecznej sprawia,
że zawsze są gotowe stanąć w obronie pokrzywdzonych.

Osoby o tej wibracji urodzenia wybrały tę cyfrę, ponieważ ich kosmicznym zobowiązaniem jest udowodnienie
reszcie świata, że poczucie odpowiedzialności, praca i uporządkowanie pozwala nam osiągnąć każdy cel. Przyszły
one też na świat by bronić sprawiedliwości i praw człowieka, by być filarami społeczeństwa.
Natomiast ich osobistym wyzwaniem jest nauka jak stać się bardziej otwartymi, wyrozumiałymi i elastycznymi
wobec siebie, jak i innych ludzi.

CECHY POZYTYWNE
Zorganizowanie, zdyscyplinowanie, odpowiedzialność, uporządkowanie, metodyczność, perfekcyjne i sumienne
traktowanie pracy, wytrwałość, skrupulatność, praktyczność, realizm, gospodarność, oszczędność, pogoda ducha,
cierpliwość, lojalność, powściągliwość, niezawodność, poświęcanie się dla osiągnięcia celu, zdolności manualne.

CECHY NEGATYWNE
Szorstkość, surowość, upór, rezerwa, oschłość, powierzchowność myślenia, rutyniarstwo, gnuśność, brak
ekspresywności i poczucia humoru, pesymizm, negatywizm, skąpstwo, chciwość, skrępowanie, bojaźliwość, 
nie okazuje uczuć."""

text_5 = """NUMEROLOGICZNA PIĄTKA
Najbardziej niespokojne i żywiołowe. Wszechstronne, zmienne. Genialne pomysły, przenikliwy, lotny umysł.
Intuicja, łatwość percepcji. Wielka potrzeba wolności, niezależności i zmian. Są ludźmi impulsywnymi,
niecierpliwymi. Nie nadają się do pracy monotonnej, rutynowej. Są odważne i zuchwałe. Kochają zmiany i ryzyko.
Skłonne żyć chwilą i poświęcić wszystko dla przygody i wolności. Piątka daje impuls, jest siłą, napędem.
Najlepszym sposobem spalania nadmiaru energii jest dla Piątek sport.

Osoby o tej wibracji urodzenia wybrały tę cyfrę, ponieważ ich kosmicznym zobowiązaniem jest wykorzystanie
własnego entuzjazmu i witalności by pokazać innym ludziom, że życie jest bardzo interesującym wyzwaniem,
jeśli żyje się śmiało i pełnią życia oraz, że w tej grze życia żadne stawki nie są zbyt wysokie,
są tylko mierni gracze.
Natomiast ich osobistym wyzwaniem jest zwalczenie własnego temperamentu i nauka jak żyć w pokoju ze
sobą i z innymi.

CECHY POZYTYWNE
Śmiałość, pomysłowość, żywiołowość, żarliwość, rozmach, ogromna witalność, inteligencja, bystrość, roztropność,
dzielność, energia, spontaniczność, czujny, dociekliwy i wszechstronny umysł, intuicyjność, przenikliwość,
natura poszukująca, potrzebuje żyć intensywnie i swobodnie.

CECHY NEGATYWNE
Niecierpliwość, impulsywność, agresywność przyciągająca problemy, nerwowość, niepokój, napięcie, porywczość,
nierozważność, brak refleksji i przenikliwości, zachowanie gwałtowne, lekkomyślne i nieprzemyślane, tchórzostwo,
wstydliwość, brak spokoju i ustatkowania"""

text_6 = """NUMEROLOGICZNA SZÓSTKA
Spokojne, wyważone, rozsądne i subtelne. Respektują ustalone prawa i zwyczaje. Romantycy, idealiści.
Miłosierne i dobrotliwe. Bardzo ważna dla nich jest rodzina. Mają tendencje do przywiązywania się z niezwykłą
siłą do osób, które kochają. Przekraczają wówczas granice, okazując zazdrość, zaborczość i zachłanność.
Wymagają miłości i opieki, i obdarzają hojnie innych uczuciami. Nie lubią zmagać się z problemami. Mają obsesję na
tle uczuć. Bywają hipochondrykami. Obdarzone dużym poczuciem rytmu, równowagi, barwy i estetyki.

Osoby o tej wibracji urodzenia wybrały tę cyfrę, ponieważ ich kosmicznym zobowiązaniem jest podkreślenie wagi
więzów i miłości rodzinnej oraz pokazanie , że fundamentem szczęśliwego i harmonijnego życia są hojność oraz
szacunek dla etycznych i moralnych wartości.
Natomiast ich osobistym wyzwaniem jest nauka jak być bardziej aktywnym i walecznym oraz jak nie poddawać
się w dążeniu do swoich celów, oraz zrównoważyć emocje i uczucia.

CECHY POZYTYWNE
Wrażliwość, zrównoważenie, harmonia współpracy z innymi, towarzyskość, łatwość przystosowania, dominacja
uczuć, miłość, uczciwość, wielkoduszność, ofiarność, odpowiedzialność i poświęcenie dla najbliższych, 
powaga, roztropność, rozwaga, zdolności artystyczne, prostolinijność.

CECHY NEGATYWNE
Lenistwo, nieczułość, pasywność, unikanie trudnych zadań, komplikuje sobie życie wyimaginowanymi kłopotami,
zachłanna, obsesyjna i władcza w uczuciach, pesymizm, hipochondria, walczy w interesie innych a nie swoim,
czasem bywa wykorzystywana przez innych ludzi."""

text_7 = """NUMEROLOGICZNA SIÓDEMKA
Najbardziej hermetyczne, zagadkowe i dziwne w całej skali numerologicznej. Wybitna umysłowość, duchowość,
intuicja. Indywidualizm i poczucie niezależności. Nieufne wobec nieznanego. Z natury nieśmiałe. Często
powściągliwe, samotne. Samotność Siódemek jest w ich wnętrzu i nie zależy od otoczenia. Zdystansowane,
eleganckie, wręcz arystokratyczna osobowość. Ich rezerwa i powaga może być złudnie postrzegane jako wyniosłość.
Często są one postrzegane jako osoby zimne. Prawda jest taka, że są to osoby bardzo wrażliwe i w taki sposób
próbują chronić delikatność własnej natury. Może występować inklinacja do depresji lub izolowania się.

Osoby o tej wibracji urodzenia wybrały tę cyfrę, ponieważ ich kosmicznym zobowiązaniem jest wniesienie w nasz
świat oraz pokazanie ludziom swojej duchowej i filozoficznej koncepcji życia. Przekazując innym swoja własną
mądrość czynią ich świadomymi własnych więzów z Wszechświatem.
Natomiast ich osobistym wyzwaniem jest nauka jak otworzyć się oraz komunikować swoje myśli i emocje oraz
dzielić się nimi z ludźmi, by w ten
sposób uniknąć izolacji i samotności.

CECHY POZYTYWNE
Głęboka duchowość i umysłowość, szlachetność, delikatność, elegancja, skupienie, powaga, rezerwa,
analityczność, logika, racjonalizm, zmysł obserwacji, dociekliwość, pilność, badawcza umysłowość,
selektywność, perfekcjonizm, indywidualizm, potrzeba niezależności, mistycyzm, spostrzegawczość,
intuicyjność, marzycielstwo, łatwość medytacji.

CECHY NEGATYWNE
Samoograniczanie, izolowanie się, samotność, beznamiętność, problemy adaptacyjne, egoizm, pesymizm,
melancholia, posępność, która może doprowadzić do depresji, nerwicy lub oziębłości uczuciowej,
skłonność do autodestrukcji."""

text_8 = """NUMEROLOGICZNA ÓSEMKA
Ta wibracja obdarza silniejszą osobowością niż inne liczby. Upór, ambicja i siła woli przewyższają
pozostałe wibracje. Energiczność, bojowość. Zawsze walczą o sukces i materialne zdobycze.
Wibracja ta związana jest z władzą, honorami i sukcesem. Ich marzenia nigdy nie sa małe, dla nich
wszystko powinno być najlepsze, największe. Mają szczególnie dobrą rękę do spraw finansowych.
Intuicyjnie wiedzą gdzie, kiedy i ile powinny zainwestować. Praktyczne, realistyczne, zawsze widzą świat
takim, jakim jest. Dzięki umiejętności samokontroli zachowują zimna krew w obliczu zagrożeń. Ósemka jednak,
tak jak wynosi na piedestał, tak może wgnieść w ziemię przy negatywnych wibracjach.

Osoby o tej wibracji urodzenia wybrały tę cyfrę, ponieważ ich kosmicznym zobowiązaniem jest pokazanie
na własnym przykładzie jak podbić świat materialny. Jak zdobyć pieniądze, sukces i posiadanie tego,
co najlepsze. Muszą pokazać, że pilność, pracowitość i zdyscyplinowanie pozwalają osiągnąć każdy cel i
zrealizować nawet najbardziej ambitne marzenia.
Natomiast ich osobistym wyzwaniem jest nauka jak być bardziej eleastycznymi i tolerancyjnymi, oraz
jak osiągnąć równowagę pomiędzy materialną i duchową częścią siebie.

CECHY POZYTYWNE
Skuteczny, sprawny, znakomity organizator, niestrudzony pracownik, praktyczność, konstruktywność, realizm,
upór, energiczność, bojowość, wysokie wymagania, siła, zdyscyplinowanie, wytrwałość,solidność, godność,
zdolności uwodzicielskie, magnetyzm, samokontrola, zimna krew, ambicja, zmysł handlowy, skuteczność
w sprawach handlowych.

CECHY NEGATYWNE
nadmierna powaga, nieustępliwość, nieugiętość, ekstremizm, radykalizm, gwałtowność, tyrania,
nieprzejednanie potrafi wybaczyć, zaślepienie, fanatyzm, egoizm, oschłość, brak poczucia humoru,
niekontrolowana ambicja, gotowa jest zrobić wszystko, aby ją zaspokoić."""

text_9 = """NUMEROLOGICZNA DZIEWIĄTKA
Przede wszystkim pełnia duchowa i bardzo rozwinięta intuicja. Osoby uczuciowe, wrażliwe.
Bezgranicznie szeroki umysł, niezwykłe predyspozycje psychiczne i dar przewidywania. Wydają się być
zawsze w kontakcie i bezpośredniej więzi z siłami Kosmosu i ludzką Duszą. Ofiarne, altruistyczne,
hojne i szlachetne . Skłonne dawać z siebie wszystko, ponieważ trwają w Miłości Uniwersalnej.
Nigdy nie pozostają obojętne wobec cierpienia czy ludzkiej biedy. Dopingują, pocieszają i przydają
wartości innym. Starają się dzielić swoją mądrością i miłością z każdym napotkanym bliźnim.
Dziewiątka czuje się spełniona i szczęśliwa tylko wtedy, gdy służy innym i uczestniczy w przeobrażaniu
świata,sprawiając, ze staje się on dla ludzi miejscem lepszym i bardziej szczęśliwym. Intuicyjnie wyczuwa,
że tak postępując wzbogaca swoje wnętrze i rozwija się duchowo. Charakter silny, władczy i
czasem wybuchowy. Ta wibracja należy do najbardziej niezależnych i indywidualistycznych. Nie uznaje
poddaństwa ani żadnych ograniczeń.

Osoby o tej wibracji urodzenia wybrały tę cyfrę, ponieważ ich kosmicznym zobowiązaniem jest uczyć innych
własnym przykładem akceptacji i wypełniania naszych zobowiązań miłości i służby bliźnim, nade wszystko
podkreślenie wagi moralnych i duchowych wartości, które czynią nas wyjątkowymi istotami świetlistymi.
Natomiast ich osobistym wyzwaniem jest nauka wyciszenia i zrównoważenia swojej ognistej i pełnej
temperamentu osobowości tak, by nie zniweczyły ich rozwoju i kosmicznego połączenia by nie straciły
swojego połączenia z Kosmosem.

CECHY POZYTYWNE
powołanie do pracy społecznej, wielkoduszność, dobrotliwość, szlachetność, wyrozumiałość, altruizm,
idealizm, namiętność, żywiołowość, romantyczność, odwaga, wysokie morale, brak uprzedzeń, nieskrępowanie,
energia, aktywność, bystry umysł, wybitna inteligencja, szczerość, uczciwość, potrzeba wolności,
intuicyjność, jasnowidzenie.

CECHY NEGATYWNE
agresywność, nietolerancja dla cudzych wad, nadmierny temperament, egzaltacja, wybuchowość, władczość,
niecierpliwość, neurotyczne skłonności, wyniosłość, fatalizm, egoizm, egocentryzm, prowokuje konflikty,
zaniedbuje obowiązki rodzinne, obojętność wobec problemów innych ludzi."""

lista = [text_0, text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9]

def button_clicked():
    data = date.get()
    if data == '':
        info.set('Nie ma daty urodzenia')

    if name.get() == '':
        info.set('Nie ma imienia lub nazwiska')
    else:
        try:
            imie = name.get().split()[0].lower()
            nazwisko = name.get().split()[1].lower()
        except:
            imie = name.get().lower()
            nazwisko = '0'

    dzisiejszy_rok = age.get()
    if dzisiejszy_rok == '':
        info.set('Nie ma roku')

    litery = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9,
              'j':1, 'k':2, 'l':3, 'm':4, 'n':5, 'o':6, 'p':7, 'q':8, 'r':9,
              's':1, 't':2, 'u':3, 'v':4, 'w':5, 'x':6, 'y':7, 'z':8, '0':0}

    def licz(z):
        if z > 9:
            y = z
            while True:
                z = 0
                if y <= 9:
                    break
                for x in str(y):
                        z += int(x)
                y = z
            z = y
        return(z)

    if data and imie and nazwisko and dzisiejszy_rok:
        info.set('')

        #data
        liczba_data = 0
        for x in str(data):
            try:
                liczba_data += int(x)
            except:
                pass
        liczba_data = licz(liczba_data)
        text1.set('Liczba urodzeniowa: ' + str(liczba_data) + '      ')

        #imie
        liczba_imie = 0
        for x in imie:
            if x in litery:
                liczba_imie += litery[x]
        liczba_imie = licz(liczba_imie)
        text2.set('Liczba imienia: ' + str(liczba_imie) + '      ')

        #nazwisko
        liczba_nazwisko = 0
        for x in nazwisko:
            if x in litery:
                liczba_nazwisko += litery[x]
        liczba_nazwisko = licz(liczba_nazwisko)
        text3.set('Liczba nazwiska: ' + str(liczba_nazwisko) + '      ')

        #imie + nazwisko
        liczba_nazwa = liczba_imie + liczba_nazwisko
        liczba_nazwa = licz(liczba_nazwa)
        text4.set('Liczba imienia i nazwiska: ' + str(liczba_nazwa) + '      ')

        #rok
        liczba_roku = 0
        for x in dzisiejszy_rok:
            liczba_roku += int(x)
        liczba_roku = licz(liczba_roku)

        #osobista
        liczba_osobista = liczba_nazwa + liczba_data
        liczba_osobista = licz(liczba_osobista)
        text5.set('Twoja szczesliwa liczba: ' + str(liczba_osobista) + '      ')

        #szczesliwa
        liczba_szczesliwa = liczba_roku + liczba_osobista
        liczba_szczesliwa = licz(liczba_szczesliwa)
        text6.set('Twoja szczesliwa liczba w tym roku: ' + str(liczba_szczesliwa) + '      ')
    wyswietl_znaczenie()

button = Button(root, text = 'Licz', command = button_clicked, width = 15, height = 2, bd = 4)
button.pack(side = BOTTOM, pady = 20)

info = StringVar()
label_info = Label(root, textvariable = info)
label_info.pack(side = BOTTOM)

root.mainloop()
