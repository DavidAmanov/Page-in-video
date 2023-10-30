Привет! Сначала небольшая предыстория для большего понимания того, что код будет выполнять и почему он делает именно это. 
Я написал код на python, используя библиотеку openCV для одной конкретной задачи - архивация документации. В фирме где я 
работал(одна из многих аккредитованных лаборатории в России) в обязательном порядке ставится задача создания резервной электронной 
копии документов(в основном рабочих журналов) каждый квартал, чаще всего такая копия представляет собой просто фотографии 
каждой страницы документа, поскольку делать фотографии например 50-60 страниц за один раз довольно утомительно и долго, плюс 
очень легко в таком количестве фотографий заблудится, мне показалось более продуктивным снимать видео журнала используя штатив, 
а код бы уже вытаскивал фотографии страниц документа.

Код не определяет, что на видео страницы или текст! Он исходит из другой логики, когда мы листаем документ, мы совершаем движения,
что как раз легко можно определить с помощью библиотеки openCV, следовательно в тот момент когда документ открыт и просто лежит на столе,
а наших рук в этот момент в кадре нет, то код определит что движения нет и если этого движения нет какое-то время, то он просто сохранит 
этот кадр. Потому когда мы будем перелистывать страницы документа, сохранения этих кадров не будет, а когда мы перелестнули страницу и 
подождали какой-то незначительный промежуток времени, то опять произойдет сохранение кадра и так до конца видео.

Определение движения в кадре происходит за счет сравнения текущего кадра и предыдущего, если они ничем не отличаются, то значит 
движения нет. 


Translate(It may not be perfect):
Hi! First, a little background for a better understanding of what the code will do and why it does exactly that. 
I wrote python code using the OpenCV library for one specific task - archiving documentation. In the company where I
worked (one of many accredited laboratories in Russia), it is mandatory to create a backup electronic
copy of documents (mainly work journals) every quarter, most often such a copy is just photographs 
since taking photos of, for example, 50-60 pages at a time is quite tedious, plus
it's very easy to get lost in so many photos, it seemed to me more productive to shoot a video of the magazine using a tripod,
and the code would have already pulled out photos of the pages of the document.

The code does not determine what is on the video page or text! It proceeds from a different logic, when we scroll through a document, we make movements,
which can be easily determined using the OpenCV library, therefore, at the moment when the document is open and just lying on the table,
and our hands are not in the frame at that moment, the code will determine that there is no movement and if there is no movement for a while, then it will just save 
this frame. Therefore, when we turn over the pages of the document, there will be no saving of these frames, and when we turn over the page and 
we waited for some insignificant period of time, then the frame will be saved again and so on until the end of the video.

Motion detection in the frame occurs by comparing the current frame and the previous one, if they are no different, then it means 
there is no movement.