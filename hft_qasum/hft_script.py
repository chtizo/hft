def init():
    from transformers import pipeline
    summ = pipeline('summarization', model='sshleifer/distilbart-cnn-12-6')
    qa = pipeline('question-answering', model='deepset/roberta-base-squad2', tokenizer='deepset/roberta-base-squad2')
    return {'summ': summ, 'qa': qa}

def summ(pipeline, main_text, max = 130, min = 30):
    summary = pipeline(main_text, max_length=max, min_length=min, do_sample=False)
    return summary

def ques(pipeline, main_text, question):
    ques = {
        'question': question,
        'context': main_text
    }
    ans = pipeline(ques)
    return ans


if __name__ == "__main__":
    main_text = """
    Spider-Man is a superhero appearing in American comic books published by Marvel Comics. 
    Created by writer-editor Stan Lee and artist Steve Ditko, he first appeared in the anthology comic book Amazing Fantasy #15 (August 1962) in the Silver Age of Comic Books. 
    He has since been featured in movies, television shows, video games, and plays. 
    Spider-Man is the alias of Peter Parker, an orphan raised by his Aunt May and Uncle Ben in New York City after his parents Richard and Mary Parker died in a plane crash. 
    Lee and Ditko had the character deal with the struggles of adolescence and financial issues and gave him many supporting characters, such as Flash Thompson, 
    J. Jonah Jameson and Harry Osborn, romantic interests Gwen Stacy, Mary Jane Watson and the Black Cat, and foes such as Doctor Octopus, the Green Goblin and Venom. 
    In his origin story, he gets spider-related abilities from a bite from a radioactive spider; these include clinging to surfaces, superhuman strength and agility, 
    and detecting danger with his "spider-sense." He also builds wrist-mounted "web-shooter" devices that shoot artificial spider webs of his own design.
    """

    pipes = init()

    summar = summ(pipes['summ'], main_text)
    answ = ques(pipes['qa'], main_text, "How does Spiderman feel?")

    print(summar, answ)