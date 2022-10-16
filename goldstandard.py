#!/usr/bin/python3

#this file contains a gold standard of case markers for Latin, Modern Greek, German, Russian, Turkish and Finnish
#for each language, a nested dictionary in three-levels is created
#the first level keys are the inflected parts of speech, the second level keys the differentiated numbers and the third level keys the respective cases whose final value is a set of their markers
#word boundaries are indicated by $ to differentiate suffixes ('a$') from prefixes ('$a'), infixes ('a') and complete word forms ('$a$')


#gold standard of Latin case markers
latin = {}

#POS
latin['noun'] = {}
latin['adjective'] = {}
latin['numeral'] = {}
latin['pronoun'] = {}

#NUM
latin['noun']['singular'] = {}
latin['adjective']['singular'] = {}
latin['numeral']['singular'] = {}
latin['pronoun']['singular'] = {}

latin['noun']['plural'] = {}
latin['adjective']['plural'] = {}
latin['numeral']['plural'] = {}
latin['pronoun']['plural'] = {}

#CAS
#nouns
latin['noun']['singular']['nominative'] = {'a$', 'us$', 'um$', 'is$', 's$', 'e$', 'o$', 'u$', 'es$'}
latin['noun']['singular']['vocative'] = {'a$', 'e$', 'um$', 'is$', 's$', 'us$', 'u$', 'es$'}
latin['noun']['singular']['genitive'] = {'ae$', 'i$', 'is$', 'us$', 'ei$'}
latin['noun']['singular']['dative'] = {'ae$', 'o$', 'i$', 'ui$', 'u$', 'ei$'}
latin['noun']['singular']['accusative'] = {'am$', 'um$', 'em$', 'e$', 'im$', 'u$'}
latin['noun']['singular']['ablative'] = {'a$', 'o$', 'e$', 'i$', 'u$'}

latin['noun']['plural']['nominative'] = {'ae$', 'i$', 'a$', 'es$', 'ia$', 'us$', 'ua$'}
latin['noun']['plural']['vocative'] = {'ae$', 'i$', 'a$', 'es$', 'ia$', 'us$', 'ua$'}
latin['noun']['plural']['genitive'] = {'arum$', 'orum$', 'um$', 'ium$', 'm$', 'uum$', 'erum$'}
latin['noun']['plural']['dative'] = {'is$', 'ibus$', 'bus$', 'ebus$'}
latin['noun']['plural']['accusative'] = {'as$', 'os$', 'a$', 'es$', 'is$', 'ia$', 'us$', 'ua$'}
latin['noun']['plural']['ablative'] = {'is$', 'ibus$', 'bus$', 'ebus$'}

#adjectives
latin['adjective']['singular']['nominative'] = {'us$', 'a$', 'um$', 'is$', 'e$', 's$'}
latin['adjective']['singular']['vocative'] = {'us$', 'a$', 'um$', 'is$', 'e$', 's$'}
latin['adjective']['singular']['genitive'] = {'i$', 'ae$', 'is$'}
latin['adjective']['singular']['dative'] = {'i$', 'ae$', 'o$'}
latin['adjective']['singular']['accusative'] = {'am$', 'um$', 'em$', 'e$', 's$'}
latin['adjective']['singular']['ablative'] = {'a$', 'o$', 'i$', 'e$'}

latin['adjective']['plural']['nominative'] = {'i$', 'ae$', 'a$', 'es$', 'ia$'}
latin['adjective']['plural']['vocative'] = {'i$', 'ae$', 'a$', 'es$', 'ia$'}
latin['adjective']['plural']['genitive'] = {'orum$', 'arum$', 'ium$', 'um$'}
latin['adjective']['plural']['dative'] = {'is$', 'ibus$'}
latin['adjective']['plural']['accusative'] = {'os$', 'as$', 'a$', 'es$', 'is$', 'ia$'}
latin['adjective']['plural']['ablative'] = {'is$', 'ibus$'}

#numerals
latin['numeral']['singular']['nominative'] = {'us$', 'a$', 'um$'}
latin['numeral']['singular']['vocative'] = {'e$', 'a$', 'um$'}
latin['numeral']['singular']['genitive'] = {'i$', 'ae$', 'ius$'}
latin['numeral']['singular']['dative'] = {'o$', 'ae$', 'i$'}
latin['numeral']['singular']['accusative'] = {'um$', 'am$'}
latin['numeral']['singular']['ablative'] = {'o$', 'a$'}

latin['numeral']['plural']['nominative'] = {'i$', 'ae$', 'a$', 'o$', 'es$', 'ia$'}
latin['numeral']['plural']['vocative'] = {'i$', 'ae$', 'a$', 'o$', 'es$', 'ia$'}
latin['numeral']['plural']['genitive'] = {'orum$', 'arum$', 'ium$'}
latin['numeral']['plural']['dative'] = {'is$', 'obus$', 'abus$', 'ibus$'}
latin['numeral']['plural']['accusative'] = {'os$', 'as$', 'a$', 'o$', 'es$', 'ia$'}
latin['numeral']['plural']['ablative'] = {'is$', 'obus$', 'abus$', 'ibus$'}

#pronouns
latin['pronoun']['singular']['nominative'] = {'$ego$', '$tu$', 'us$', 'a$', 'um$', '$qui$', '$quae$', '$quod$', '$quis$', '$quid$', '$qua$', 'quis$', 'quid$', 'qui$', 'qua$', 'quod$', '$quis', '$quid', '$qui', '$quae', '$quod', '$quic', 'e$', 'ud$', '$hic$', '$haec$', '$hoc$', '$is$', '$ea$', '$id$', '$i', '$ea', '$uter', '$utra', '$utrum', '$nihil$', '$nemo$'}
latin['pronoun']['singular']['genitive'] = {'$mei$', '$tui$', '$sui$', 'i$', 'ae$', '$cuius$', 'cuius$', '$cuius', 'ius$', '$huius$', '$eius$', '$eius', '$utrius', '$neminis$'}
latin['pronoun']['singular']['dative'] = {'$mihi$', '$tibi$', '$sibi$', 'o$', 'ae$', '$cui$', 'cui$', '$cui', 'i$', '$huic$', '$ei$', '$ei', '$utri', '$nemini$'}
latin['pronoun']['singular']['accusative'] = {'$me$', '$te$', '$se$', 'um$', 'am$', '$quem$', '$quam$', '$quod$', 'quem$', 'quid$', 'quam$', 'quod$', '$quem', '$quid', '$quam', '$quod', '$quic', '$quen', '$quan', 'um$', 'ud$', '$hunc$', '$hanc$', '$hoc$', '$eum$', '$eam$', '$id$', '$eun', '$ean', '$i', '$utrum', '$utram', '$nihil$', '$neminem$'}
latin['pronoun']['singular']['ablative'] = {'$me$', '$te$', '$se$', '$mecum$', '$tecum$', '$secum$', 'o$', 'a$', '$quo$', '$qua$', 'quo$', 'qua$', '$quo', '$qua', '$hoc$', '$hac$', '$eo$', '$ea$', '$eo', '$ea', '$utro', '$utra'}

latin['pronoun']['plural']['nominative'] = {'$nos$', '$vos$', '$uos$', 'i$', 'ae$', 'a$', '$qui$', '$quae$', '$qua$', 'qui$', 'quae$', 'quod$', '$qui', '$quae', '$hi$', '$hae$', '$haec$', '$ei$', '$ii$', '$i$', '$eae$', '$ea$', '$i', '$ii', '$eae', '$ea', '$utri', '$utrae', '$utra'}
latin['pronoun']['plural']['genitive'] = {'$nostri$', '$nostrum$', '$vestri$', '$vestrum$', '$uestri$', '$uestrum$', 'orum$', 'arum$', '$quorum$', '$quarum$', 'quorum$', 'quarum$', '$quorum', '$quarum', '$quorun', '$quarun', '$horum$', '$horunc$', '$harum$', '$harunc$', '$eorum$', '$earum$', '$eorun', '$earun', '$utrorum', '$utrarum'}
latin['pronoun']['plural']['dative'] = {'$nobis$', '$vobis$', '$uobis$', 'is$', '$quibus$', 'quibus$', '$quibus', '$his$', '$eis$', '$iis$', '$is$', '$eis', '$iis', '$is', '$utris'}
latin['pronoun']['plural']['accusative'] = {'$nos$', '$vos$', '$uos$', 'os$', 'as$', 'a$', '$quos$', '$quas$', '$quae$', '$qua$', 'quos$', 'quas$', 'qua$', '$quos', '$quas', '$quae', 'ud$', '$hos$', '$has$', '$haec$', '$eos$', '$eas$', '$ea$', '$eos' , '$eas', '$ea', '$utros', '$utras', '$utra'}
latin['pronoun']['plural']['ablative'] = {'$nobis$', '$vobis$', '$uobis$', '$nobiscum$', '$vobiscum$', '$uobiscum$', 'is$', '$quibus$', 'quibus$', '$quibus', '$his$', '$eis$', '$iis$', '$is$', '$eis', '$iis', '$is', '$utris'}


#gold standard of Modern Greek case markers

modern_greek = {}

#POS 
modern_greek['noun'] = {}
modern_greek['adjective'] = {}
modern_greek['numeral'] = {}
modern_greek['article'] = {}
modern_greek['pronoun'] = {}

#NUM
modern_greek['noun']['singular'] = {}
modern_greek['adjective']['singular'] = {}
modern_greek['numeral']['singular'] = {}
modern_greek['article']['singular'] = {}
modern_greek['pronoun']['singular'] = {}

modern_greek['noun']['plural'] = {}
modern_greek['adjective']['plural'] = {}
modern_greek['numeral']['plural'] = {}
modern_greek['article']['plural'] = {}
modern_greek['pronoun']['plural'] = {}

#CAS
#nouns
modern_greek['noun']['singular']['nominative'] = {'ος$', 'ης$', 'ας$', 'ες$', 'ους$', 'εας$', 'ου$', 'η$', 'α$', 'ω$', 'ι$', 'ο$', 'μα$', 'ιμο$'}
modern_greek['noun']['singular']['accusative'] = {'ου$', 'ο$', 'η$', 'α$', 'ε$', 'εα$', 'ω$', 'ι$', 'ο$', 'μα$', 'ιμο$'}
modern_greek['noun']['singular']['genitive'] = {'ου$', 'ο$', 'η$', 'α$', 'ε$', 'εα$', 'ας$', 'ης$', 'εως$', 'ους$', 'ως$', 'ιου$', 'ματος$', 'ιματος$'}
modern_greek['noun']['singular']['vocative'] = {'ου$', 'ο$', 'η$', 'α$', 'ε$', 'εα$', 'ω$', 'ι$', 'μα$', 'ιμο$'}

modern_greek['noun']['plural']['nominative'] = {'οι$', 'ες$', 'εις$', 'ηδες$',  'αδες$', 'εδες$', 'ουδες$', 'α$', 'ια$', 'η$', 'ματα$', 'ιματα$'}
modern_greek['noun']['plural']['accusative'] = {'ους$', 'ες$', 'εις$', 'ηδες$', 'αδες$',  'εδες$', 'ουδες$', 'α$', 'ια$', 'η$', 'ματα$', 'ιματα$'}
modern_greek['noun']['plural']['genitive'] = {'ων$', 'εων$', 'ηδων$', 'αδων$', 'εδων$', 'ουδων$', 'ιων$', 'ματων$', 'ιματων$'}
modern_greek['noun']['plural']['vocative'] = {'οι$', 'ες$', 'εις$', 'ηδες$',  'αδες$', 'εδες$', 'ουδες$', 'α$', 'ια$', 'η$', 'ματα$', 'ιματα$'}

#adjectives
modern_greek['adjective']['singular']['nominative'] = {'ος$', 'η$', 'ο$', 'α$', 'ια$', 'υς$', 'υ$', 'ης$', 'ι$', 'ες$', 'ας$', 'ου$', 'ικο$', 'αδικο$', 'ων$', 'ουσα$', 'ον$'}
modern_greek['adjective']['singular']['accusative'] = {'ο$', 'η$', 'α$', 'ια$', 'υ$', 'η$', 'ι$', 'ες$', 'ου$', 'ικο$', 'αδικο$', 'οντα$', 'ουσα$', 'ον$'}
modern_greek['adjective']['singular']['genitive'] = {'ον$', 'ης$', 'ας$', 'ιας$', 'ιου$', 'υ$', 'η$', 'ι$', 'ονς$', 'ικον$', 'αδικου$', 'οντος$', 'ουσας$'}
modern_greek['adjective']['singular']['vocative'] = {'ε$', 'η$', 'ο$', 'α$', 'ια$', 'υ$', 'η$', 'ι$', 'ικο$', 'αδικο$', 'ων$', 'ουσα$', 'ον$'}

modern_greek['adjective']['plural']['nominative'] = {'οι$', 'ες$', 'α$', 'ιοι$', 'ιες$', 'ια$', 'εις$', 'η$', 'ηδες$', 'ικα$', 'αδες$', 'ουδες$', 'αδικα$', 'οντες$', 'ουσες$', 'οντα$'}
modern_greek['adjective']['plural']['accusative'] = {'ους$', 'ες$', 'α$', 'ιους$', 'ιες$', 'ια$', 'εις$', 'η$', 'ηδες$', 'ικα$', 'αδες$', 'ουδες$', 'αδικα$', 'οντες$', 'ουσες$', 'οντα$'}
modern_greek['adjective']['plural']['genitive'] = {'ωυν$', 'ιων$', 'ηδων$', 'ικων$', 'αδων$', 'ουδων$', 'αδικων$',  'οντων$', 'ουσων$'}
modern_greek['adjective']['plural']['vocative'] = {'οι$', 'ες$', 'α$', 'ιοι$', 'ιες$', 'ια$', 'ηδες$', 'ικα$', 'αδες$', 'ουδες$', 'αδικα$', 'ουτες$', 'ουσες$', 'ουτα$'}

#numerals
modern_greek['numeral']['singular']['nominative'] = {'ας$', 'α$'}
modern_greek['numeral']['singular']['accusative'] = {'α$', 'αν$'}
modern_greek['numeral']['singular']['genitive'] = {'ος$', 'ας$'}

modern_greek['numeral']['plural']['nominative'] = {'εις$', 'ις$', 'ια$', 'α$', 'οι$', 'ες$'}
modern_greek['numeral']['plural']['accusative'] = {'εις$', 'ις$', 'ια$', 'α$', 'ους$', 'ες$'}
modern_greek['numeral']['plural']['genitive'] = {'ων$'}

#articles
modern_greek['article']['singular']['nominative'] = {'$ο$', '$η$', '$το$', '$ενας$', '$μια$', '$ενα$'}
modern_greek['article']['singular']['accusative'] = {'$το$', '$τον$', '$τη$', '$την$', '$ενα$', '$εναν$', '$μια$', '$μιαν$'}
modern_greek['article']['singular']['genitive'] = {'$τον$', '$της$', '$ενος$', '$μιας$'}
modern_greek['article']['singular']['dative'] = {'$οτο$', '$οτον$', '$οτη$', '$οτην$', '$ενα$', '$εναν$', '$μια$'}

modern_greek['article']['plural']['nominative'] = {'$οι$', '$τα$'}
modern_greek['article']['plural']['accusative'] = {'$τους$', '$τις$', '$τα$'}
modern_greek['article']['plural']['genitive'] = {'$των$'}
modern_greek['article']['plural']['dative'] = {'$οτους$', '$οτις$', '$οτα$'}

#pronouns
modern_greek['pronoun']['singular']['nominative'] = {'$τος$', '$τη$', '$το$', '$εγω$', '$εσυ$', '$αυτος$', '$αυτη$', '$αυτο$', 'ος$', 'η$', 'ο$', 'ια$', 'α$', 'ις$', 'ας$', 'να$'}
modern_greek['pronoun']['singular']['accusative'] = {'$με$', '$σε$', '$τον$', '$τη$', '$την$', '$το$', '$εμενα$', '$εσενα$', '$αυτον$', '$αυτη$', '$αυτην$', '$αυτο$', 'ο$', 'η$', 'ια$', 'ν$', 'ον$', 'α$', 'αν$', 'να$', 'ναν$'}
modern_greek['pronoun']['singular']['genitive'] = {'$μου$', '$σου$', '$του$', '$της$', '$εμενα$', '$εσενα$', '$αυτου$', '$αυτης$', '$αυτουν$', '$αυτην$', 'ου$', 'ης$', 'ιας$', 'ανου$',  'ας$', 'ανης$', 'νος$'}

modern_greek['pronoun']['plural']['nominative'] = {'$τοι$', '$τες$', '$τα$', '$εμεις$', '$εσεις$', '$αυτοι$', '$αυτες$', '$αυτα$', 'οι$', 'ες$', 'α$'}
modern_greek['pronoun']['plural']['accusative'] = {'$μας$', '$σας$', '$τους$', '$τις$', '$τες$', '$τα$', '$εμας$', '$εσας$', '$αυτους$', '$αυες$', '$αυτα$', 'ους$', 'ες$', 'α$'}
modern_greek['pronoun']['plural']['genitive'] = {'$μας$', '$σας$', '$τους$', '$εμας$', '$εσας$', '$αυτων$', 'ων$', 'ανων$'}


#gold standard of German case markers

german = {}

#POS
german['noun'] = {}
german['adjective'] = {}
german['article'] = {}
german['pronoun'] = {}

#NUM
german['noun']['singular'] = {}
german['adjective']['singular'] = {}
german['article']['singular'] = {}
german['pronoun']['singular'] = {}

german['noun']['plural'] = {}
german['adjective']['plural'] = {}
german['article']['plural'] = {}
german['pronoun']['plural'] = {}

#CAS
#nouns
german['noun']['singular']['nominative'] = {}
german['noun']['singular']['genitive'] = {'s$','n$','es$','en$','ns$'}
german['noun']['singular']['accusative'] = {'n$', 'en$'}
german['noun']['singular']['dative'] = {'e$', 'en$', 'n$'}

german['noun']['plural']['nominative'] = {'e$','er$','en$','n$','s$'}
german['noun']['plural']['genitive'] = {'e$','er$','en$','n$','s$'}
german['noun']['plural']['accusative'] = {'e$','er$','en$','n$','s$'}
german['noun']['plural']['dative'] = {'en$','n$','s$','ern$'}

#adjectives
german['adjective']['singular']['nominative'] = {'e$','er$','es$'}
german['adjective']['singular']['genitive'] = {'en$','er$'}
german['adjective']['singular']['accusative'] = {'e$','es$','en$'}
german['adjective']['singular']['dative'] = {'en$','er$','em$'}

german['adjective']['plural']['nominative'] = {'e$','en$'}
german['adjective']['plural']['genitive'] = {'en$','er$'}
german['adjective']['plural']['accusative'] = {'e$','en$'}
german['adjective']['plural']['dative'] = {'en$'}

#articles
german['article']['singular']['nominative'] = {'$der$','$die$','$das$','$ein$','$eine$'}
german['article']['singular']['genitive'] = {'$des$','$der$','$einer$','$eines$'}
german['article']['singular']['accusative'] = {'$den$','$das$','$die$','$einen$','$ein$','$eine$'}
german['article']['singular']['dative'] = {'$dem$','$der$','$einem$','$einer$'}

german['article']['plural']['nominative'] = {'$die$'}
german['article']['plural']['genitive'] = {'$der$'}
german['article']['plural']['accusative'] = {'$die$'}
german['article']['plural']['dative'] = {'$den$'}

#pronouns
german['pronoun']['singular']['nominative'] = {'er$', 'es$', 'e$', '$der', '$das', '$die','$der$', '$das$', '$die$', '$ich$', '$du$', '$er$', '$sie$', '$es$'}
german['pronoun']['singular']['genitive'] = {'es$', 'er$', 'en$', 's$', '$des', '$der', '$des$', '$der$', '$dessen$', '$derer$', '$deren$', '$meiner$', '$deiner$', '$seiner$', '$ihrer$'}
german['pronoun']['singular']['accusative'] = {'en$', 'es$', 'e$', '$den', '$das', '$die', '$den$', '$das$', '$die$', '$mich$', '$dich$', '$ihn$', '$es$', '$sie$'}
german['pronoun']['singular']['dative'] = {'em$', 'er$', 'en$', '$dem', '$der', '$dem$', '$der$', '$mir$', '$dir$', '$ihm$', '$ihr$'}

german['pronoun']['plural']['nominative'] = {'e$', 'en$', '$die', '$die$', '$wir$', '$ihr$', '$sie$'}
german['pronoun']['plural']['genitive'] = {'er$', 'en$', '$der', '$der$', '$derer$', '$deren$', '$unser$', '$euer$', '$ihrer$'}
german['pronoun']['plural']['accusative'] = {'e$', 'en$', '$die', '$die$', '$uns$', '$euch$', '$sie$'}
german['pronoun']['plural']['dative'] = {'en$', '$den$', '$denen$', '$uns$', '$euch$', '$ihnen$'}


#gold standard of Russian case markers

russian = {}

#POS
russian['noun'] = {}
russian['adjective'] = {}
russian['numeral'] = {}
russian['pronoun'] = {}

#NUM
russian['noun']['singular'] = {}
russian['adjective']['singular'] = {}
russian['numeral']['singular'] = {}
russian['pronoun']['singular'] = {}

russian['noun']['plural'] = {}
russian['adjective']['plural'] = {}
russian['numeral']['plural'] = {}
russian['pronoun']['plural'] = {}

#CAS
#nouns
russian['noun']['singular']['nominative'] = {'й$', 'ъ$', 'о$', 'е$', 'ё$', 'а$', 'я$', 'мя$'}
russian['noun']['singular']['accusative'] = {'й$', 'ъ$', 'о$', 'е$', 'ё$', 'а$', 'я$', 'мя$', 'ы$', 'и$', 'у$', 'ю$', 'ени$'}
russian['noun']['singular']['genitive'] = {'а$', 'я$', 'ы$', 'и$', 'у$', 'ю$', 'ени$'}
russian['noun']['singular']['dative'] = {'у$', 'ю$', 'е$', 'и$', 'ени$'}
russian['noun']['singular']['instrumental'] = {'ем$', 'ом$', 'ём$', 'ей$', 'ой$', 'ёй$', 'ъю$', 'ою$', 'енем$'}
russian['noun']['singular']['prepositional'] = {'е$', 'и$', 'у$', 'ю$', 'ени$'}

russian['noun']['plural']['nominative'] = {'ы$', 'и$', 'а$', 'я$', 'ъя$', 'е$', 'ата$', 'ята$', 'ен$'}
russian['noun']['plural']['accusative'] = {'ы$', 'и$', 'а$', 'я$', 'ов$', 'ев$', 'ей$', 'ъя$', 'е$', 'ата$', 'ята$', 'ена$', 'й$', 'ёв$', 'ён$'}
russian['noun']['plural']['genitive'] = {'ов$', 'ев$', 'ей$', 'й$', 'ёв$', 'ён$'}
russian['noun']['plural']['dative'] = {'ам$', 'ям$', 'енам$'}
russian['noun']['plural']['instrumental'] = {'ами$', 'ями$', 'енами$'}
russian['noun']['plural']['prepositional'] = {'ах$', 'ях$', 'енах$'}

#adjectives
russian['adjective']['singular']['nominative'] = {'ый$', 'ая$', 'ое$', 'ий$', 'ее$', 'ой$', 'яя$', 'я$', 'е$', 'а$', 'о$'}
russian['adjective']['singular']['accusative'] = {'ый$', 'ого$', 'его$', 'ую$', 'ое$', 'ая$', 'ий$', 'ее$', 'ой$', 'юю$', 'ю$', 'е$', 'у$', 'о$'}
russian['adjective']['singular']['genitive'] = {'ого$', 'ой$', 'ей$', 'его$'}
russian['adjective']['singular']['dative'] = {'ому$', 'ой$', 'ему$', 'ей$', 'у$'}
russian['adjective']['singular']['instrumental'] = {'ым$', 'ой$', 'ою$', 'им$', 'ей$', 'ею$'}
russian['adjective']['singular']['prepositional'] = {'ом$', 'ой$', 'ем$', 'ей$'}

russian['adjective']['plural']['nominative'] = {'ые$', 'ие$', 'и$', 'ы$'}
russian['adjective']['plural']['accusative'] = {'ые$', 'ых$', 'ие$', 'их$', 'и$', 'ы$'}
russian['adjective']['plural']['genitive'] = {'ых$', 'их$'}
russian['adjective']['plural']['dative'] = {'ым$', 'им$'}
russian['adjective']['plural']['instrumental'] = {'ыми$', 'ими$'}
russian['adjective']['plural']['prepositional'] = {'ых$', 'их$'}

#numerals
russian['numeral']['singular']['nominative'] = {'а$', 'о$', 'ый$', 'ая$', 'ое$'}
russian['numeral']['singular']['accusative'] = {'ого$', 'у$', 'о$', 'ый$', 'ую$', 'ое$'}
russian['numeral']['singular']['genitive'] = {'ого$', 'ой$', 'и$', 'а$'}
russian['numeral']['singular']['dative'] = {'ому$', 'ой$', 'е$', 'у$'}
russian['numeral']['singular']['instrumental'] = {'им$', 'ой$', 'ою$', 'ей$', 'ом$', 'ым$'}
russian['numeral']['singular']['prepositional'] = {'ом$', 'ой$', 'е$'}

russian['numeral']['plural']['nominative'] = {'и$', 'е$', 'а$', 'о$', 'ы$', 'ые$'}
russian['numeral']['plural']['accusative'] = {'и$', 'их$', 'а$', 'е$', 'ух$', 'ёх$', 'ых$', 'ы$', 'ые$'}
russian['numeral']['plural']['genitive'] = {'их$', 'ух$', 'ёх$', 'и$', 'а$', 'ых$', 'ов$'}
russian['numeral']['plural']['dative'] = {'им$', 'ум$', 'ём$', 'и$', 'а$', 'ам$', 'ым$'}
russian['numeral']['plural']['instrumental'] = {'ими$', 'умя$', 'емя$', 'мя$', 'ю$', 'ью$', 'а$', 'ами$', 'ыми$', 'ьмя$'}
russian['numeral']['plural']['prepositional'] = {'их$', 'ух$', 'ёх$', 'и$', 'а$', 'ах$', 'ых$'}

#pronouns
russian['pronoun']['singular']['nominative'] = {'$я$', '$ты$', '$он$', '$она$', '$оно$', 'и$', 'я$', 'ё$', 'а$', 'е$', 'й$', '$его$', '$её$', '$кто$', '$что$', '$чей$', '$чья$', '$чьё$', 'ой$', 'ое$', 'ая$', 'ый$', '$зтот$', '$зта$', '$зто$', '$тот$', '$та$', '$то$', '$сей$', '$сия$', '$сие$', '$зкий$', '$зкая$', '$зкое$', 'о$', 'ий$', '$никто$', '$ничто$', '$ничей$', '$ничья$', '$ничьё$'}
russian['pronoun']['singular']['accusative'] = {'$меня$', '$тебя$', '$его$', '$её$', '$оно$', '$себя$', 'и$', 'его$', 'ю$', 'ё$', 'у$', 'е$', 'й$', '$кого$', '$что$', '$чей$', '$чьего$', '$чью$', '$чьё$', 'ой$', 'ое$', 'ая$', 'ый$', 'ую$', 'ого$', '$зтот$', '$зтого$', '$зту$', '$зто$', '$тот$', '$того$', '$ту$', '$то$', '$сей$', '$сего$', '$сию$', '$сие$', '$зкий$', '$зкоего$', '$зкую$', 'оё$', 'о$', 'ий$', '$никого$', '$ничто$', '$ничей$', '$ничьего$', '$ничью$', '$ничьё$', 'оего$'}
russian['pronoun']['singular']['genitive'] = {'$меня$', '$тебя$', '$его$', '$её$', '$оно$', '$себя$', 'его$', 'ей$', '$кого$', '$чего$', '$чьего$', '$чьей$', 'ого$', 'ой$', '$зтого$', '$зтой$', '$того$', '$той$', '$сего$', '$сей$', '$зкоего$', '$зкой$', 'ого$', 'ой$', '$никого$', '$ничего$', '$ничьего$', '$ничьей$', 'оего$', 'оей$'}
russian['pronoun']['singular']['dative'] = {'$мне$', '$тебе$', '$ему$', '$ей$', '$себе$', 'ему$', 'ей$', '$его$', '$её$', '$кому$', '$чему$', '$чьему$', '$чьей$', 'ому$', 'ой$', '$зтому$', '$зтой$', '$тому$', '$той$', '$сему$', '$сей$', '$зкоему$', '$зкой$', 'ому$', 'ой$', '$никому$', '$ничему$', '$ничьему$', '$ничьей$', 'оему$', 'оей$'}
russian['pronoun']['singular']['instrumental'] = {'$мной$', '$тебой$', '$им$', '$ей$', '$ею$', '$мною$', '$тебою$', '$собой$', '$собою$', 'им$', 'ей$', 'ею$', '$его$', '$её$', '$кем$',  '$чем$', '$чьим$', '$чьей$', '$чью$', 'ым$', 'ой$', 'им$', '$зтим$', '$зтой$', '$зтою$', '$тем$', '$той$', '$тою$', '$сим$', '$сей$', '$сею$', '$зким$', '$зкой$', '$зкою$', 'ой$', 'ою$', 'ем$', '$никем$',  '$ничем$', '$ничьим$', '$ничьей$', '$ничью$', 'оим$', 'оей$'}
russian['pronoun']['singular']['prepositional'] = {'$мне$', '$тебе$', '$нём$', '$ней$', '$себе$', 'ём$', 'ей$', 'ем$', '$его$', '$её$', '$ком$', '$чём$', '$чьём$', '$чьей$', 'ом$', 'ой$', '$зтом$', '$зтой$', '$том$', '$той$', '$сём$', '$сей$', '$зком$', '$зкой$', 'ом$', 'ой$', '$ником$', '$ничём$', '$ничьём$', '$ничьей$', 'оем$', 'оей$'}

russian['pronoun']['plural']['nominative'] = {'$нас$', '$вас$', '$их$', 'и$', '$чьи$', 'ые$', 'ие$', '$зти$', '$те$', '$сии$', '$зкие$', 'е$', '$ничьи$'}
russian['pronoun']['plural']['accusative'] = {'$мы$', '$вы$', '$оны$', '$себя$', 'и$', 'их$', '$их$', '$чьи$', '$чьих$', 'ые$', 'йе$', 'ых$', 'их$', '$зти$', '$зтих$', '$те$', '$тех$', '$сии$', '$сих$', '$зкие$', '$зких$', 'е$', 'ех$', 'ие$', '$ничьи$', '$ничьих$', 'оих$'}
russian['pronoun']['plural']['genitive'] = {'$нас$', '$вас$', '$их$', '$себя$', 'их$', '$чьих$', 'ых$', 'их$', '$зтих$', '$тех$', '$сих$', '$зких$', 'ех$', '$ничьих$', 'оих$'}
russian['pronoun']['plural']['dative'] = {'$нам$', '$вам$', '$им$', '$себе$', 'им$', '$их$', '$чьим$', 'ым$', 'им$', '$зтим$', '$тем$', '$сим$', '$зким$', 'ем$', '$ничьим$', 'оим$'}
russian['pronoun']['plural']['instrumental'] = {'$нами$', '$вами$', '$ими$', '$собой$', '$собою$', 'ими$', '$их$', '$чьими$', 'ыми$', 'ими$', '$зтими$', '$теми$', '$сими$', '$зкими$', 'еми$', '$ничьими$', 'оими$'}
russian['pronoun']['plural']['prepositional'] = {'$нас$', '$вас$', '$них$', '$себе$', 'их$', '$их$', '$чьих$', 'ых$', 'их$', '$зтих$', '$тех$', '$сих$', '$зких$', 'ех$', '$ничьих$', 'оих$'}


#gold standard of Turkish case markers

turkish = {}

#POS
turkish['noun'] = {}
turkish['pronoun'] = {}

#NUM
turkish['noun']['singular'] = {}
turkish['pronoun']['singular'] = {}

turkish['noun']['plural'] = {}
turkish['pronoun']['plural'] = {}

#CAS
#nouns
turkish['noun']['singular']['nominative'] = {}
turkish['noun']['singular']['accusative'] = {'ı$', 'i$', 'yi$', 'yü$', 'yı$', 'yu$', 'ü$', 'u$'}
turkish['noun']['singular']['genitive'] = {'ın$', 'nin$', 'nün$', 'nın$', 'nun$', 'in$', 'ün$', 'un$'}
turkish['noun']['singular']['dative'] = {'a$', 'ye$', 'ya$', 'e$'}
turkish['noun']['singular']['locative'] = {'da$', 'de$', 'te$', 'ta$', 'da', 'de', 'te', 'ta'}
turkish['noun']['singular']['ablative'] = {'dan$', 'den$', 'ten$', 'tan$'}

turkish['noun']['plural']['nominative'] = {}
turkish['noun']['plural']['accusative'] = {'ı$', 'i$', 'yi$', 'yü$', 'yı$', 'yu$', 'ü$', 'u$'}
turkish['noun']['plural']['genitive'] = {'ın$', 'nin$', 'nün$', 'nın$', 'nun$', 'in$', 'ün$', 'un$'}
turkish['noun']['plural']['dative'] = {'a$', 'ye$', 'ya$', 'e$'}
turkish['noun']['plural']['locative'] = {'da$', 'de$', 'te$', 'ta$', 'da', 'de', 'te', 'ta'}
turkish['noun']['plural']['ablative'] = {'dan$', 'den$', 'ten$', 'tan$'}

#pronouns
turkish['pronoun']['singular']['nominative'] = {'si$', 'sı$'}
turkish['pronoun']['singular']['accusative'] = {'i$', 'nu$', 'ni$', 'u$', 'yı$', 'yi$'}
turkish['pronoun']['singular']['genitive'] = {'im$', 'in$', 'nun$', 'nin$', 'nın$', 'yin$'}
turkish['pronoun']['singular']['dative'] = {'a$', 'na$', 'n$', 'e$', 'ya$', 'ne$', 'ye$'}
turkish['pronoun']['singular']['locative'] = {'de$', 'nda$', 'nde$'}
turkish['pronoun']['singular']['ablative'] = {'den$', 'dan$', 'nden$', 'ndan$', 'yden$'}

turkish['pronoun']['plural']['nominative'] = {'i$', 'ı$'}
turkish['pronoun']['plural']['accusative'] = {'i$', 'ı$', 'ini$'}
turkish['pronoun']['plural']['genitive'] = {'im$', 'in$', 'ın$', 'inin$'}
turkish['pronoun']['plural']['dative'] = {'i$', 'ı$', 'e$', 'a$', 'ine$'}
turkish['pronoun']['plural']['locative'] = {'de$', 'da$', 'inde$'}
turkish['pronoun']['plural']['ablative'] = {'den$', 'dan$', 'inden$'}


#gold standard of Finnish case markers

finnish = {}

#POS
finnish['noun'] = {}
finnish['adjective'] = {}
finnish['numeral'] = {}
finnish['pronoun'] = {}

#NUM
finnish['noun']['singular'] = {}
finnish['adjective']['singular'] = {}
finnish['numeral']['singular'] = {}
finnish['pronoun']['singular'] = {}

finnish['noun']['plural'] = {}
finnish['adjective']['plural'] = {}
finnish['numeral']['plural'] = {}
finnish['pronoun']['plural'] = {}

#CAS
#nouns
finnish['noun']['singular']['nominative'] = {}
finnish['noun']['singular']['genitive'] = {'n$'}
finnish['noun']['singular']['accusative'] = {'n$'}
finnish['noun']['singular']['partitive'] = {'a$', 'ä$', 'ta$', 'tta$', 'tä$', 'ttä$', 'a', 'ä', 't', 'tta', 'tä', 'ttä'}
finnish['noun']['singular']['inessive'] = {'ssa$', 'ssä$', 'ssa', 'ssä'}
finnish['noun']['singular']['elative'] = {'sta$', 'stä$', 'sta', 'stä'}
finnish['noun']['singular']['illative'] = {'on$', 'ön$', 'an$', 'än$', 'en$', 'in$', 'un$', 'yn$', 'han$', 'hän$', 'hin$', 'hen$', 'hun$', 'hon$', 'hön$', 'seen$', 'o', 'ö', 'a', 'ä', 'e', 'i', 'u', 'y', 'ha', 'hä', 'hi', 'he', 'hu', 'ho', 'hö', 'see'}
finnish['noun']['singular']['adessive'] = {'lla$', 'llä$', 'lla', 'llä'}
finnish['noun']['singular']['ablative'] = {'lta$', 'ltä$', 'lta', 'ltä'}
finnish['noun']['singular']['allative'] = {'lle$', 'lle'}
finnish['noun']['singular']['essive'] = {'na$', 'nä$', 'na', 'nä'}
finnish['noun']['singular']['translative'] = {'ksi$', 'kse'}
finnish['noun']['singular']['comitative'] = {}
finnish['noun']['singular']['abessive'] = {'tta$', 'ttä$', 'tta', 'ttä'}
finnish['noun']['singular']['instructive'] = {'n$'}

finnish['noun']['plural']['nominative'] = {}
finnish['noun']['plural']['genitive'] = {'en$', 'den$', 'ten$', 'tten$', 'e', 'de', 'te', 'tte'}
finnish['noun']['plural']['accusative'] = {'t$'}
finnish['noun']['plural']['partitive'] = {'a$', 'ä$', 'ta$', 'tä$', 'a', 'ä', 'ta', 'tä'}
finnish['noun']['plural']['inessive'] = {'ssa$', 'ssä$', 'ssa', 'ssä'}
finnish['noun']['plural']['elative'] = {'sta$', 'stä$', 'sta', 'stä'}
finnish['noun']['plural']['illative'] = {'in$', 'hin$', 'siin$', 'i', 'hi', 'sii'}
finnish['noun']['plural']['adessive'] = {'lla$', 'llä$', 'lla', 'llä'}
finnish['noun']['plural']['ablative'] = {'lta$', 'ltä$', 'lta', 'ltä'}
finnish['noun']['plural']['allative'] = {'lle$', 'lle'}
finnish['noun']['plural']['essive'] = {'na$', 'nä$', 'na', 'nä'}
finnish['noun']['plural']['translative'] = {'ksi$', 'kse'}
finnish['noun']['plural']['comitative'] = {'ne$', 'ne'}
finnish['noun']['plural']['abessive'] = {'tta$', 'ttä$', 'tta', 'ttä'}
finnish['noun']['plural']['instructive'] = {'n$'}

#adjectives
finnish['adjective']['singular']['nominative'] = {}
finnish['adjective']['singular']['genitive'] = {'n$'}
finnish['adjective']['singular']['accusative'] = {'n$'}
finnish['adjective']['singular']['partitive'] = {'a$', 'ä$', 'ta$', 'tta$', 'tä$', 'ttä$'}
finnish['adjective']['singular']['inessive'] = {'ssa$', 'ssä$'}
finnish['adjective']['singular']['elative'] = {'sta$', 'stä$'}
finnish['adjective']['singular']['illative'] = {'on$', 'ön$', 'an$', 'än$', 'en$', 'in$', 'un$', 'yn$', 'han$', 'hän$', 'hin$', 'hen$', 'hun$', 'hon$', 'hön$', 'seen$'}
finnish['adjective']['singular']['adessive'] = {'lla$', 'llä$'}
finnish['adjective']['singular']['ablative'] = {'lta$', 'ltä$'}
finnish['adjective']['singular']['allative'] = {'lle$'}
finnish['adjective']['singular']['essive'] = {'na$', 'nä$'}
finnish['adjective']['singular']['translative'] = {'ksi$'}
finnish['adjective']['singular']['comitative'] = {}
finnish['adjective']['singular']['abessive'] = {'tta$', 'ttä$'}
finnish['adjective']['singular']['instructive'] = {'n$'}

finnish['adjective']['plural']['nominative'] = {}
finnish['adjective']['plural']['genitive'] = {'en$', 'den$', 'ten$', 'tten$'}
finnish['adjective']['plural']['accusative'] = {'t$'}
finnish['adjective']['plural']['partitive'] = {'a$', 'ä$', 'ta$', 'tä$'}
finnish['adjective']['plural']['inessive'] = {'ssa$', 'ssä$'}
finnish['adjective']['plural']['elative'] = {'sta$', 'stä$'}
finnish['adjective']['plural']['illative'] = {'in$', 'hin$', 'siin$'}
finnish['adjective']['plural']['adessive'] = {'lla$', 'llä$'}
finnish['adjective']['plural']['ablative'] = {'lta$', 'ltä$'}
finnish['adjective']['plural']['allative'] = {'lle$'}
finnish['adjective']['plural']['essive'] = {'na$', 'nä$'}
finnish['adjective']['plural']['translative'] = {'ksi$'}
finnish['adjective']['plural']['comitative'] = {'ne$'}
finnish['adjective']['plural']['abessive'] = {'tta$', 'ttä$'}
finnish['adjective']['plural']['instructive'] = {'n$'}

#numerals
finnish['numeral']['singular']['nominative'] = {'s$'}
finnish['numeral']['singular']['genitive'] = {'n$'}
finnish['numeral']['singular']['accusative'] = {'n$'}
finnish['numeral']['singular']['partitive'] = {'a$', 'ä$', 'ta$', 'tta$', 'tä$', 'ttä$'}
finnish['numeral']['singular']['inessive'] = {'ssa$', 'ssä$'}
finnish['numeral']['singular']['elative'] = {'sta$', 'stä$'}
finnish['numeral']['singular']['illative'] = {'on$', 'ön$', 'an$', 'än$', 'en$', 'in$', 'un$', 'yn$', 'han$', 'hän$', 'hin$', 'hen$', 'hun$', 'hon$', 'hön$', 'seen$'}
finnish['numeral']['singular']['adessive'] = {'lla$', 'llä$'}
finnish['numeral']['singular']['ablative'] = {'lta$', 'ltä$'}
finnish['numeral']['singular']['allative'] = {'lle$'}
finnish['numeral']['singular']['essive'] = {'na$', 'nä$'}
finnish['numeral']['singular']['translative'] = {'ksi$'}
finnish['numeral']['singular']['comitative'] = {}
finnish['numeral']['singular']['abessive'] = {'tta$', 'ttä$'}
finnish['numeral']['singular']['instructive'] = {'n$'}

finnish['numeral']['plural']['nominative'] = {}
finnish['numeral']['plural']['genitive'] = {'en$', 'den$', 'ten$', 'tten$'}
finnish['numeral']['plural']['accusative'] = {'t$'}
finnish['numeral']['plural']['partitive'] = {'a$', 'ä$', 'ta$', 'tä$'}
finnish['numeral']['plural']['inessive'] = {'ssa$', 'ssä$'}
finnish['numeral']['plural']['elative'] = {'sta$', 'stä$'}
finnish['numeral']['plural']['illative'] = {'in$', 'hin$', 'siin$'}
finnish['numeral']['plural']['adessive'] = {'lla$', 'llä$'}
finnish['numeral']['plural']['ablative'] = {'lta$', 'ltä$'}
finnish['numeral']['plural']['allative'] = {'lle$'}
finnish['numeral']['plural']['essive'] = {'na$', 'nä$'}
finnish['numeral']['plural']['translative'] = {'ksi$'}
finnish['numeral']['plural']['comitative'] = {'ne$'}
finnish['numeral']['plural']['abessive'] = {'tta$', 'ttä$'}
finnish['numeral']['plural']['instructive'] = {'n$'}

#pronouns
finnish['pronoun']['singular']['nominative'] = {}
finnish['pronoun']['singular']['genitive'] = {'n$', 'män$', 'kä$', 'nkä$', 'n', 'ka$', 'nka$'}
finnish['pronoun']['singular']['accusative'] = {'t$', 'kä$'}
finnish['pronoun']['singular']['partitive'] = {'a$', 'ta$', 'tä$', 'ta', 'tä', 'a'}
finnish['pronoun']['singular']['inessive'] = {'ssa$', 'ssä$', 'nä$', 'ssa', 'ssä'}
finnish['pronoun']['singular']['elative'] = {'sta$', 'stä$', 'tä$', 'sta', 'stä'}
finnish['pronoun']['singular']['illative'] = {'un$', 'en$', 'hän$', 'hon$', 'hen$', 'hin$', 'an$', 'hun$', 'hon', 'en', 'hin', 'an', 'hun'}
finnish['pronoun']['singular']['adessive'] = {'lla$', 'llä$', 'lla', 'llä'}
finnish['pronoun']['singular']['ablative'] = {'lta$', 'ltä$', 'lta', 'ltä'}
finnish['pronoun']['singular']['allative'] = {'lle$', 'lle'}
finnish['pronoun']['singular']['essive'] = {'nä$', 'na$', 'na'}
finnish['pronoun']['singular']['translative'] = {'ksi$', 'ksi'}

finnish['pronoun']['plural']['nominative'] = {'kä$'}
finnish['pronoun']['plural']['genitive'] = {'dän$', 'den$', 'kä$', 'den', 'en'}
finnish['pronoun']['plural']['accusative'] = {'dät$', 'kä$'}
finnish['pronoun']['plural']['partitive'] = {'tä$', 'ta$', 'a$', 'ta', 'tä'}
finnish['pronoun']['plural']['inessive'] = {'ssä$', 'ssa$', 'ssa', 'ssä'}
finnish['pronoun']['plural']['elative'] = {'stä$', 'sta$', 'sta', 'stä'}
finnish['pronoun']['plural']['illative'] = {'hin$', 'in$', 'hin', 'in'}
finnish['pronoun']['plural']['adessive'] = {'lla$', 'llä$', 'lla', 'llä'}
finnish['pronoun']['plural']['ablative'] = {'lta$', 'ltä$', 'lta', 'ltä'}
finnish['pronoun']['plural']['allative'] = {'lle$', 'lle'}
finnish['pronoun']['plural']['essive'] = {'nä$', 'na$', 'na'}
finnish['pronoun']['plural']['translative'] = {'ksi$', 'ksi'}

print(latin)
print('\n','------------------------------------------','\n')
print(modern_greek)
print('\n','------------------------------------------','\n')
print(german)
print('\n','------------------------------------------','\n')
print(russian)
print('\n','------------------------------------------','\n')
print(turkish)
print('\n','------------------------------------------','\n')
print(finnish)
print('\n','------------------------------------------','\n')


