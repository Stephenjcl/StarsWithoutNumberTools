from bisect import bisect_left
import numpy as np
import random


class OptionsWeightsLengthMismatchException(BaseException):
    """Raises when the number of elements in the options list doesn't match the
    number of elements in the weight list."""
    pass


# Using an class
class RollTable:

    def __init__(self, options: list, weights: np.array) -> "RollTable":
        self.options = options
        self.weights = weights
        self._validate_inputs()
        pdf = weights/np.sum(weights)
        self.cdf = np.cumsum(pdf)

    def _validate_inputs(self) -> None:
        if len(self.options) != self.weights.size:
            raise OptionsWeightsLengthMismatchException(f"options and weights must have the same number of elements.")
        if max(self.weights.shape) != np.prod(self.weights.shape): # i.e. make sure it's 1D
            raise ValueError("Weights must be 1D, i.e. only one non-singular dimension.")

    def get_item(self):
        roll = np.random.random()
        idx = bisect_left(self.cdf, roll)
        return self.options[idx]

class NPC:
    def __init__(self, dispo = "Unknown"):
        if random.random() < 0.5:
            self.gender = "Male"
        else:
            self.gender = "Female"
        self.age = random.randint(18,65)
        self.motive = ["Unknown", "Unknown"]
        self.capabilities = "Unknown"
        self.sources = "Unknown"
        self.disposition = dispo
        if self.disposition is "Unknown":
            self.disposition = random.choice(["Friendly", "Neutral", "Hostile"])
        self.opportunities = "Unknown"
        self.appearance = "Unknown"
        self.attributes = {
                "HD":0,
                "AC":0,
                "Atk.":0,
                "Dmg.":"By Weapon",
                "Move":"10m",
                "ML":0,
                "Skills":0,
                "Saves":0
                }
        self.social = {
            "Initial":"Unknown",
            "Offer":"Unknown",
            "Refused":"Unknown",
            "Insulted":"Unknown",
            "More":"Unknown",
            "General":"Unknown"
        }
        self.gen_new()

    def gen_new(self):
        self.motive[0] = POI_motives.get_item()
        self.motive[1] = POI_motives.get_item()
        self.capabilities = POI_capabilities.get_item()
        self.sources = POI_sources.get_item()
        if self.disposition is "Hostile":
            if "Ambition - " in self.motive[0]:
                self.opportunities = POI_opp_amb_neg.get_item()
            if "Avarice - " in self.motive[0]:
                self.opportunities = POI_opp_ava_neg.get_item()
            if "Craving - " in self.motive[0]:
                self.opportunities = POI_opp_cra_neg.get_item()
            if "Curiosity - " in self.motive[0]:
                self.opportunities = POI_opp_cur_neg.get_item()
            if "Desire - " in self.motive[0]:
                self.opportunities = POI_opp_des_neg.get_item()
            if "Excitement - " in self.motive[0]:
                self.opportunities = POI_opp_exc_neg.get_item()
            if "Glory - " in self.motive[0]:
                self.opportunities = POI_opp_glo_neg.get_item()
            if "Hatred - " in self.motive[0]:
                self.opportunities = POI_opp_hat_neg.get_item()
            if "Piety - " in self.motive[0]:
                self.opportunities = POI_opp_pie_neg.get_item()
            if "Protection - " in self.motive[0]:
                self.opportunities = POI_opp_pro_neg.get_item()
            if "Revenge - " in self.motive[0]:
                self.opportunities = POI_opp_rev_neg.get_item()
            if "Safety - " in self.motive[0]:
                self.opportunities = POI_opp_saf_neg.get_item()
        elif self.disposition is not "Hostile":
            if "Ambition - " in self.motive[0]:
                self.opportunities = POI_opp_amb_pos.get_item()
            if "Avarice - " in self.motive[0]:
                self.opportunities = POI_opp_ava_pos.get_item()
            if "Craving - " in self.motive[0]:
                self.opportunities = POI_opp_cra_pos.get_item()
            if "Curiosity - " in self.motive[0]:
                self.opportunities = POI_opp_cur_pos.get_item()
            if "Desire - " in self.motive[0]:
                self.opportunities = POI_opp_des_pos.get_item()
            if "Excitement - " in self.motive[0]:
                self.opportunities = POI_opp_exc_pos.get_item()
            if "Glory - " in self.motive[0]:
                self.opportunities = POI_opp_glo_pos.get_item()
            if "Hatred - " in self.motive[0]:
                self.opportunities = POI_opp_hat_pos.get_item()
            if "Piety - " in self.motive[0]:
                self.opportunities = POI_opp_pie_pos.get_item()
            if "Protection - " in self.motive[0]:
                self.opportunities = POI_opp_pro_pos.get_item()
            if "Revenge - " in self.motive[0]:
                self.opportunities = POI_opp_rev_pos.get_item()
            if "Safety - " in self.motive[0]:
                self.opportunities = POI_opp_saf_pos.get_item()
        self.appearance = POI_appearance.get_item()
        #Check for secondary appearance attribute.
        if random.random() < 0.167:
            self.appearance = self.appearance + " " + POI_appearance.get_item()

        #Roll Stats
        self.attributes["HD"] = POI_HD.get_item()
        self.attributes["AC"] = POI_AC.get_item()
        self.attributes["Atk."] = POI_Atk.get_item()
        self.attributes["Dmg."] = POI_Dmg.get_item()
        self.attributes["ML"] = POI_ML.get_item()
        self.attributes["Skills"] = POI_Skills.get_item()
        self.attributes["Saves"] = POI_Saves.get_item()

        #Social Attributes
        self.social["Initial"] = POI_social_init.get_item()
        self.social["Offer"] = POI_social_offer.get_item()
        self.social["Refused"] = POI_social_refused.get_item()
        self.social["Insulted"] = POI_social_insulted.get_item()
        self.social["More"] = POI_social_more.get_item()
        self.social["General"] = POI_social_general.get_item()

    def get_summary(self):
        print("----Background----", flush = True)
        print("Gender:", self.gender, '\n')
        print("Age:", self.age, '\n')
        print("Primary Motive:", self.motive[0])
        print("Secondary Motive:", self.motive[1], '\n')
        print("Capabilities:", self.capabilities, '\n')
        print("Source of Capabilities:", self.sources, '\n')
        print("Disposition:", self.disposition, '\n')
        print("Opportunities:", self.opportunities, '\n')
        print("Appearance:", self.appearance)

        print('\n', "----Statistics----")
        print("HD:", self.attributes["HD"])
        print("AC:", self.attributes["AC"])
        print("Atk.:", self.attributes["Atk."])
        print("Dmg.:", self.attributes["Dmg."])
        print("Move:", self.attributes["Move"])
        print("ML:", self.attributes["ML"])
        print("Skills:", self.attributes["Skills"])
        print("Saves:", self.attributes["Saves"])

        print('\n', "----Social Interaction----")
        print("Style of initial interaction: ", self.social["Initial"], '\n')
        print("The way the deal is offered: ", self.social["Offer"], '\n')
        print("When balked or refused: ", self.social["Refused"], '\n')
        print("When insulted or threatened: ", self.social["Insulted"], '\n')
        print("When the PCs want more: ", self.social["More"], '\n')
        print("General conversational habits: ", self.social["General"])


#%%
#### Roll Tables ####
#Motives for patrons, nemeses etc. Roll 1 for simple characters, 2 for more complex.
POI_motives = RollTable([
    "Ambition - Attain a rank that their kind is not allowed.",
    "Ambition - Recover a rank or status they had but lost.",
    "Ambition - Attain it before they're too old or passed over.",
    "Ambition - Attain it before a hated rival gets the rank.",
    "Ambition - Wrest the rank from an 'unworthy' holder.",
    "Ambition - Promote someone else as a stepping-stone up.",
    "Ambition - Prove their own worthiness for higher rank.",
    "Ambition - Create a new hierarchy to be at the top of it.",
    "Ambition - Attain the rank to satisfy family expectations.",
    "Ambition - Insidiously undermine a superior's position.",
    "Avarice - Acquire more money by fair or foul means.",
    "Avarice - Get money to obtain a life-saving service.",
    "Avarice - They have an expensive spouse or lover.",
    "Avarice - They were poor, and live in dread of it again.",
    "Avarice - Get money to repay a very dangerous debt.",
    "Avarice - Their social standing requires vast outlays.",
    "Avarice - Money is points, and they want to win the game.",
    "Avarice - They're being extorded by some powerful person.",
    "Avarice - They're zealous about a very expensive pastime.",
    "Avarice - They're terribly wasteful with money.",
    "Craving - A kind of forbidden offworld art or culture.",
    "Craving - A reprehensible carnal desire.",
    "Craving - The company of a socially-forbidden class.",
    "Craving - A self-destructive chemical.",
    "Craving - Cyberware or body modification beyond reason.",
    "Craving - Extreme gluttony for rare and precious viands.",
    "Craving - A product currently banned from the world.",
    "Craving - Something harmless that society still hates.",
    "Craving - Adulterous or excessive sexual partners.",
    "Craving - An unreasonable appetite for gambling.",
    "Curiosity - Discover the truth behind a family death.",
    "Curiosity - Unlock the secrets of an enigmatic tech object.",
    "Curiosity - Hunt down blackmail material on someone.",
    "Curiosity - Learn the real facts about a current event.",
    "Curiosity - Reveal a fact the government is hiding.",
    "Curiosity - Learn the true identity of a veiled enemy.",
    "Curiosity - Find the culprit behind a wrong they suffered.",
    "Curiosity - Study a topic forbidden in their native culture.",
    "Curiosity - Experience certain socially-unacceptable things.",
    "Curiosity - Track down a socially-disruptive record.",
    "Desire - A family member who's constantly in trouble.",
    "Desire - The spouse of an important or dangerous other.",
    "Desire - An ex who resents and despises them.",
    "Desire - An unattainable celebrity figure.",
    "Desire - An expensive and cynical courtisan.",
    "Desire - A superior's spouse or adult child.",
    "Desire - An alien or other socially-forbidden object.",
    "Desire - A work associate oblivious to their feelings.",
    "Desire - A dead person echoes in a VI or expert system.",
    "Desire - An utterly unacceptable object of longing.",
    "Excitement - Hunt extremely dangerous wild animals.",
    "Excitement - Explore or traverse hazardous locations.",
    "Excitement - Sample a wide range of chemicals.",
    "Excitement - Kill people for the pleasure of it.",
    "Excitement - Seek out new cultures and social groups.",
    "Excitement - Goad and troll powerful local figures.",
    "Excitement - Compete in a semi-lethal illicit sport.",
    "Excitement - Promote favoured bands or music genres.",
    "Excitement - Spearhead a particularily zealous art movement.",
    "Excitement - Commit a particular type of exciting crime.",
    "Glory - Become a famous holovid star.",
    "Glory - Rise to fame in some notorious occupation.",
    "Glory - Eclipse a hated rival with their own glory.",
    "Glory - Prove how wonderful they are to old doubters.",
    "Glory - Show up prejudices against their kind.",
    "Glory - Bask in the laud of groupies and fans.",
    "Glory - Attain renown for supremacy in their profession.",
    "Glory - Redeem some past ignominy or failure.",
    "Glory - Show an ex how wrong they were to leave.",
    "Glory - Seek sector-wide fame in a dreaded profession.",
    "Hatred - Criminals, in general or in a specific type.",
    "Hatred - The government, in general and specific staff.",
    "Hatred - An ethnic group on the world.",
    "Hatred - A religious group in the general locale.",
    "Hatred - A particular corporation and its employees.",
    "Hatred - A specific gang and its members.",
    "Hatred - Offworlders, whether all or of a specific world.",
    "Hatred - Aliens and other non-human sentients.",
    "Hatred - Cyborgs and transhumans.",
    "Hatred - Members of a particular political or social group.",
    "Piety - They're consecrated to serve a particular faith.",
    "Piety - Their family inculcated extreme piety in them.",
    "Piety - They feel their beloved faith is under attack.",
    "Piety - They back a minority sect in their faith.",
    "Piety - They belong to a socially-despised religion.",
    "Piety - The NPC is determined to proselytize the faith.",
    "Piety - They're convinced they have a divine blessing.",
    "Piety - They mean to found a new faith on their beliefs.",
    "Piety - Their faith is in a secular political philosophy.",
    "Piety - They're convinced God loves everything they do.",
    "Protection - A family member is in legal or criminal trouble.",
    "Protection - A precious heirloom is sought by thieves.",
    "Protection - Ancestral lands are threatened by others.",
    "Protection - Their rank or high-status role is under attack.",
    "Protection - Their personal wealth is at risk.",
    "Protection - An affiliated business is facing dire perils.",
    "Protection - A loved one incurred some dangerous disfavour.",
    "Protection - A pretech artifact they have is illegal to own.",
    "Protection - They've stolen something another wants back.",
    "Protection - They know a loved one is seeking their ruin.",
    "Revenge - A crime boss killed one of their loved ones.",
    "Revenge - A government official convicted them of crimes.",
    "Revenge - A former partner betrayed them to an enemy.",
    "Revenge - A former lover broke their heart.",
    "Revenge - They've inherited an inter-family grudge.",
    "Revenge - They were ruined by a careless celebrity's fun.",
    "Revenge - A superior used them for personal advancement.",
    "Revenge - A corrupt official wronged them legally.",
    "Revenge - A family member betrayed them.",
    "Revenge - A rival cheated them in love or business.",
    "Safety - A local law enforcer wants them imprisoned.",
    "Safety - Someone they betrayed is hunting them.",
    "Safety - A local crime boss blames them for some woe.",
    "Safety - The victim of a shady deal they made is furious.",
    "Safety - Their superior is planning to sacrifice them.",
    "Safety - A subordinate is ready to move against them.",
    "Safety - A former lover wants brutal revenge on them.",
    "Safety - A traitor is bartering their secrets to others.",
    "Safety - They're gripped by self-destructive urges.",
    "Saftey - A rival has put a bounty on their ruin."],
    np.array([1]*120)
    )

#%% Roll 1 peak capability. Maybe 2 for flavour.
POI_capabilities = RollTable(
    ["Authority, legal or traditional in nature.",
    "Connection, with friends and allies of use.",
    "Debt, owed to them by someone powerfule.",
    "Influence, social and indirect in nature.",
    "Information, knowing useful secrets of things.",
    "Money, being able to buy off problems.",
    "Skills, as a very talented professional.",
    "Sympathy, being irresistible to the players.",
    "Tech, having pretech or other potent gear.",
    "Violence, having goons or other heavies to hand."],
    np.array([1]*10)
)

#Source of their capabilities.
POI_sources = RollTable(
    ["Associates, who lend it to the NPC.",
    "Family, who provide it to the NPC.",
    "Job, where it's a prerequisite of the position.",
    "Personal, created and controlled by the NPC.",
    "Resources, obtained via money or goods.",
    "Society, granted them by their social standing."],
    np.array([1]*6)
)

#%% Opportunities
POI_opp_amb_pos = RollTable(
    ["They've been set up as a scapegoat for a serious error made by a rival.",
    "They need to accomplish a near-impossible feat to obtain the next rung of their ambition.",
    "A past bargain they made to get their current place is now coming back to haunt them.",
    "They've worked their way into a position that's a career or literal deathtrap for its occupants.",
    "The recent pursuit of their ambition has caused a terrible problem for someone they care about.",
    "A rival has blackmail evidence about a past failing the NPC had tried to cover up.",
    "The institution or structure the NPC is trying to climb in is being threatened by an outside force.",
    "They've seriously overplayed their hand and are now at the mercy of their rivals."],
    np.array([1]*8)
)

POI_opp_amb_neg = RollTable(
    ["The PCs have offended their superior, and the NPC thinks it worthwhile to punish them.",
    "A PC ally is in the way of the NPC's next step up the ladder of ambition.",
    "They're convinced that foiling the PCs will bring their name greater luster.",
    "The PCs have unwittingly aided a rival of the NPC, and they think the PCs are his allies.",
    "Something the PCs recently did slighted or embarrassed the NPC in a professional sense.",
    "The next step up the ladder somehow involves ruining a group or cause the PCs support.",
    "The NPC feels threatened by a recent success by the PCs and moves to put them in their place.",
    "The PCs somehow ended up with something critical for the NPC's further advancement."],
    np.array([1]*8)
)

POI_opp_ava_pos = RollTable(
    ["The NPC just had an item stolen that is crucial for some profitable plan or deal they've made.",
    "They just laid hands on a treasure that has turned out to be extremely dangerous to own.",
    "They've gambled or risked on a profit opportunity that has turned out to be rigged.",
    "They thought they were keeping their wealth safe, but where they put it has turned perilous.",
    "A seemingly-profitable deal or opportunity they took turns out to have dangerous strings on it.",
    "They've borrowed money they thought they could repay until recent events altered that.",
    "They've risked something or someone they love on a profit opportunity that's turning sour.",
    "The payment they accepted has turned out to be extremely hot property or stolen money."],
    np.array([1]*8)
)

POI_opp_ava_neg = RollTable(
    ["The PCs have a particular treasure that the NPC wants at all costs.",
    "A PC ally risks financial ruin due to the machinations of the greedy NPC.",
    "A dear treasure has been taken from a PC ally by the grasping NPC.",
    "They're planning a financial squeeze on a property or cause owned or backed by the PCs.",
    "They've stolen or diverted money that was due to the PCs.",
    "The PCs accidentally come into possession of a key to much of the NPC's wealth.",
    "The NPC tries to insert himself as a middleman, forcing the PCs to pay him to get service access.",
    "The NPC plans to pay the PCs off with money or items he intends to steal back."],
    np.array([1]*8)
)

POI_opp_cra_pos = RollTable(
    ["They've overindulged and the consequences for doing so require PC help to extricate them.",
    "They've risked someone or something priceless to them in order to obtain their craving.",
    "Someone set them up with a bad dose, bad company, or other extra-injurious indulgence.",
    "Someone's manipulating them ruthlessly by controlling access to the craving.",
    "Their craving is illegal or unacceptable, and they now risk being revealed if they aren't helped.",
    "They did something terrible in the grip of their craving and are trying desperately to fix it.",
    "They want to squelch the craving but someone else is trying to push them back into it.",
    "They were involved in producing or providing the craving but are trying to disentangle from it."],
    np.array([1]*8)
)

POI_opp_cra_neg = RollTable(
    ["A PC ally is the object of a deeply repugnant lust by the hostile NPC.",
    "The PCs somehow ended up cutting off the supply of one of the NPC's favorite vices.",
    "The NPC's appetites are causing misery for a group or ally affiliated with the PCs.",
    "The ruin of the PCs is critical if the NPC is to get access to a splendid example of their craving.",
    "They're convinced the PCs are holding out on them and are in possession of a craved thing.",
    "Their growing appetite is putting pressure on the PCs or their allies or associates.",
    "They indulge horribly in a way the PCs are certain to learn about and be disgusted by.",
    "They mean to use the PCs as catspaws to get them their craving."],
    np.array([1]*8)
)

POI_opp_cur_pos = RollTable(
    ["They have half a juicy secret but the other half is very dangerous to acquire.",
    "A rare occasion of their special curiosity is available, but they need protection to investigate it.",
    "They unearthed a very dangerous secret and are trying to dodge those sent to re-conceal it.",
    "They misunderstood something they learned and acted on that error, producing a dire peril.",
    "One of their fellow investigators or minions has fallen into great danger.",
    "While investigating their curiosity they stumbled over an unrelated but very large secret.",
    "The object of their curiosity is being threatened by some outside force.",
    "They have an awful suspicion that must be verified through a perilous inquiry."],
    np.array([1]*8)
)

POI_opp_cur_neg = RollTable(
    ["They're close to obtaining critical blackmail material on the PCs or a PC ally.",
    "They're methodically destroying or burying evidence the PCs need for their own goals.",
    "They have a very destructive curiosity about PC tech, biology, or other perishable belongings.",
    "They're convinced the PCs are the key to a totally unrelated puzzle they're dealing with.",
    "They plan to use the PCs as expendable minions in order to get an answer to some question.",
    "The PCs or something they possess are vital components to an experiment or inquiry.",
    "They mean to learn a truth by putting the object of their curiosity in a terrible revealing situation.",
    "They're convinced the PCs are hiding something from them out of some sinister motive."],
    np.array([1]*8)
)

POI_opp_des_pos = RollTable(
    ["They're in love with an associate of the PCs who is largely oblivious to them.",
    "They're smitten with someone who is totally unacceptable for cultural reasons.",
    "Their beloved is in great danger due to a mistake they made.",
    "They're determined to perform some tremendous deed in order to win their chosen's heart.",
    "They're willfully blind to the dangers of a lover the PCs know is a terrible person.",
    "They can't contact their beloved except through agents like the PCs.",
    "Their object of desire has been kidnapped or compelled into affiliation with someone else.",
    "Their lover is in need of something difficult to obtain, and they're determined to get it."],
    np.array([1]*8)
)

POI_opp_des_neg = RollTable(
    ["They want a romantic rival dead or utterly humiliated before their beloved.",
    "Their beloved has a grudge against the party for some reason and wants the NPC to act on it.",
    "They don't know how to take no for an answer from a beloved who despises them.",
    "They're compelling their beloved to stay with them through threats to their own loved ones.",
    "They path to their beloved's heart lies through the ruin of a PC-supported cause or group.",
    "Their beloved won't have them, so they're determined to ruin all other potential suitors.",
    "Their beloved is a horrible person who goads them on to acts of terrible wickedness.",
    "They're an obsessed stalker of a totally unattainable object of desire."],
    np.array([1]*8)
)

POI_opp_exc_pos = RollTable(
    ["They're addicted to some form of extreme sport that requires help from associates.",
    "They've struck a blow at an unsympathetic NPC just for fun, but now they're paying for it.",
    "A calculated risk proved to be poorly figured and the NPC is dealing with the consequences.",
    "A manipulator is goading the NPC on to greater risks in order to usher them to eventual ruin.",
    "The NPC is determined to go where they shouldn't go and needs PC help to get there.",
    "The NPC gets into trouble just as the PCs are in a position to be induced to help them.",
    "Someone sabotaged their fun and they need help to get out of the ensuing situation.",
    "They want to hire the PCs to help them survive an experience that is not generally survivable."],
    np.array([1]*8)
)

POI_opp_exc_neg = RollTable(
    ["Their idea of fun involves doing horrible things to people the PCs like.",
    "One of their little indulgences has done great harm to a group or cause the PCs support.",
    "They're going to ruin something precious just for the fun of doing so.",
    "They've set up some lethal challenge that's crooked and unfair to everyone else.",
    "They approach the PCs as a charming bon vivant, only to drag them into a real crime.",
    "They take a sporting rivalry with a sympathetic NPC to a murderous extent.",
    "They've got vile minions out raking up forced participants in their idea of fun.",
    "They lost a sporting bet or contest and are now determined to destroy the winner."],
    np.array([1]*8)
)

POI_opp_glo_pos = RollTable(
    ["They're trying to achieve a feat of exploration that has killed those who tried it.",
    "They want to gloriously ruin an infamous NPC who's causing misery for them and their peers.",
    "They're trying to attain fame through sympathetic crimes and social deviations.",
    "They yearn to be associated with a celebrity and think they know how to attract their attention.",
    "They're obsessed with effacing an old failure by great public success at a second attempt.",
    "They can get a big break into public notice if they can do a job for a major producer.",
    "They're not respected by their peers, and are set on doing something to earn their respect.",
    "They want to establish a new noble cause despite the vigorous hostility of the culture to it."],
    np.array([1]*8)
)

POI_opp_glo_neg = RollTable(
    ["They want a more popular and famous rival to die or be ruined in a humiliating way.",
    "They don't want to be famous; they want to be infamous, viewed with fear and horror.",
    "They want to use the PCs as sacrificial catspaws in a plan to make them look like a hero.",
    "They want to destroy an institution that denied them their rightful place of fame among them.",
    "They steal the credit for some grand deed the PCs or a PC ally has done.",
    "Their fame requires the relentless exploitation of others, including associates of the PCs.",
    "Their fame has left them largely above the law with regards to a sordid plan they're enacting.",
    "They're using star-struck fans as minions to terrorize and extort others."],
    np.array([1]*8)
)

POI_opp_hat_pos = RollTable(
    ["They're engaged in a secret relationship with someone from the group that hates them.",
    "They've been framed for some evildoing by their persecutors, who may have done it themselves.",
    "They're trying to stop some evildoer of their own kind before he makes things even worse.",
    "Their business or cause is being ground down by those who hate them.",
    "An opportunity that was supposed to go to them has been withdrawn due to their persecutors.",
    "Pent-up fury is making them drastically overreact to a specific small slight against them.",
    "They're trying to protect others of their kind who are being assailed by persecutors.",
    "They need the PCs to do something for them that their enemies would never let them do."],
    np.array([1]*8)
)

POI_opp_hat_neg = RollTable(
    ["They're luring the hated into a trap where they'll all be blamed for the ensuing disaster.",
    "They want a champion of those they hate either dead or wholly discredited.",
    "They want to destroy or ruin a resource or facility that those they hate rely on.",
    "They want to install a fellow hater into a position of authority over those they hate.",
    "The hater is profiting by stirring up additional friction between the hated and others.",
    "The hater is secretly supporting the most unsympathetic and vile among the hated.",
    "The hater is employing the hated in tasks or roles that are intended to get them killed.",
    "The hater is setting up a target to spectacularly fail at some important and far-famed role."],
    np.array([1]*8)
)

POI_opp_pie_pos = RollTable(
    ["They need to perform a pilgrimage to or through a very dangerous area.",
    "They're supporting co-religionists who are facing some dire peril.",
    "They're being oppressed by zealots of a rival faith in the area.",
    "They recently did something they count as gravely sinful and are trying to make amends.",
    "They're trying to establish or preserve a temple that's very inconvenient to corrupt local powers.",
    "They need to perform a particular act of faith but enemies or rivals are trying to prevent it.",
    "They need to recover a lost holy artifact that's currently in unknown or dangerous hands.",
    "They need help to protect some relief effort or charitable enterprise against greedy interlopers."],
    np.array([1]*8)
)

POI_opp_pie_neg = RollTable(
    ["They want the local leader of a rival faith to be killed or discredited before the public.",
    "They're convinced a co-religionist is a filthy heretic who needs to be destroyed.",
    "They're using a position of religious influence to personally profit themselves.",
    "Something about the PCs or their recent actions strikes them as damnably blasphemous.",
    "A PC ally is a backslider or apostate of the faith that the NPC is determined to punish.",
    "The NPC has taken control of a center of the faith and is using it as a tool of advancement.",
    "They're convinced that they're favored by God and deserving of every pleasure and desire.",
    "They're working to destroy a competing local faith and demoralize its believers."],
    np.array([1]*8)
)

POI_opp_pro_pos = RollTable(
    ["A family member keeps making stupid choices that the NPC needs to save them from.",
    "Their spouse or loved one is exceptionally vulnerable to a particular hostile NPC's plans.",
    "A business or institution they're devoted to is under attack by others.",
    "They're responsible for protecting some object that many other people want to obtain.",
    "They recently failed at protecting their object and are desperate to redeem their mistake.",
    "Some resource or tool they need to protect their object has been lost or compromised.",
    "Their usual helpers are unavailable so they need the PCs to help them fend off a threat.",
    "The object they're trying to protect has decided that it doesn't need to be protected."],
    np.array([1]*8)
)

POI_opp_pro_neg = RollTable(
    ["They're plotting the eventual destruction of the object due to some sense of past wrong.",
    "They want to destroy the object by bribing or coercing its protector into acquiescing.",
    "They want to use the object as a trap, so that the enemy who seizes it will be destroyed by it.",
    "They hate and resent their guardianship of the object and subconsciously seek to let it be ruined.",
    "They're misusing the object terribly, taking advantage of their protectorship over it.",
    "They aren't the rightful protector, having forced out the real one to take advantage of it.",
    "They're convinced a PC ally or sympathetic figure is a threat to it who must be destroyed.",
    "They have power or resources that can only be accessed after someone else destroys the object."],
    np.array([1]*8)
)

POI_opp_rev_pos = RollTable(
    ["The PCs are ideally positioned to carry out revenge on their behalf.",
    "A particular rival or enemy of the PCs was the person responsible for their wrong.",
    "Their enemy has decided to preemptively crush them before they can take their revenge.",
    "A PC ally or supported cause was collateral damage in the wrong inflicted on the NPC.",
    "The NPC needs help to discern exactly who was responsible for what they suffered.",
    "They've failed pathetically to get revenge and need help to survive the aftermath of it.",
    "They don't want to take revenge but are morally obligated unless hidden facts come to light.",
    "Their foe's hatred is unsatisfied and they are determined to finish what they started."],
    np.array([1]*8)
)

POI_opp_rev_neg = RollTable(
    ["They've decided to destroy the innocent family or associates of the one who wronged them.",
    "They want an utterly disproportionate revenge on the target for the wrong they suffered.",
    "Revenge is actually just a thin excuse they use to justify their sadistic love of inflicting suffering.",
    "PC allies or sympathetic groups are being expended as mere pawns in the NPC's plan.",
    "The NPC wants to hire the PCs to help but conceals the full unsympathetic story from them.",
    "They intentionally avoid completing their revenge so they can continue to torment the foe.",
    "They consider the PCs worthy of vengeance for a minor or unrecognized association with a foe.",
    "They want revenge for something that the rest of the world sees as a favor or kindness."],
    np.array([1]*8)
)

POI_opp_saf_pos = RollTable(
    ["Rescuing something precious would expose them to great peril, so they need outside help.",
    "Their threat has just broken through their best defense, and they need help.",
    "The threat is wreaking havoc on innocent relatives and associates of the NPC.",
    "The NPC's threat stems from a person or situation that threatens the PCs too.",
    "The NPC needs a particular resource or object to continue maintaining their safety.",
    "The threat has unsuccessfully attacked the NPC, but the collateral damage is affecting the PCs.",
    "The NPC's ruin or death would significantly hinder a current goal or ally of the PCs.",
    "The NPC is willing to trade something vital to the PCs for help against the threat."],
    np.array([1]*8)
)

POI_opp_saf_neg = RollTable(
    ["They're willing to cause tremendous collateral damage to deal with the threat.",
    "The threat is entirely justified and wants the PC's help in getting at the NPC.",
    "The threat is subtly using the PCs to attack the NPC, and the NPC knows it.",
    "They mistake the PCs as agents of the threat and act accordingly.",
    "The NPC plans to use the PCs as an ablative shield against an impending attack by the threat.",
    "There's some great reward for the PCs if they join the threat in bringing down the NPC.",
    "The NPC tries to misdirect the threat into clashing with the PCs, hopefully killing them.",
    "They NPC needs something possessed by a PC ally or sympathetic group to maintain safety."],
    np.array([1]*8)
)


#%% Visual Appearances
POI_appearance = RollTable(
    #Unusual clothing styles
    ["Dresses far too young or old for them.",
    "Numerous group-loyalty brands/marks.",
    "Unusually shabby or ill-kept clothing.",
    "Culturally-specific regional clothing style.",
    "Loud offworld clothing style.",
    "Visibly high-tech integrated clothing.",
    "Cutting-edge fashion as they can afford.",
    "Culturally-specific sexualized clothing.",
    #Notable physical qualities
    "Abnormally fat or thin build.",
    "A feature or limb has been badly scarred.",
    "Very feminine/masculine presentation.",
    "Extremely muscular or spindly form.",
    "Disproportionate body part or parts.",
    "Lacking or excessive in hair.",
    "No neck to speak of, or giraffe-like.",
    "Elongated fingers or limbs.",
    "Oddly-textured skin.",
    "Unusually short or tall.",
    #Missing limbs or features
    "Missing a hand or arm.",
    "Missing a leg.",
    "Missing an eye or facial feature.",
    "Has an unusual prosthetic.",
    #Tics and Motion styles
    "Can't talk without gesturing.",
    "Moves with floating grace.",
    "Constantly fiddles with small objects.",
    "Taps toes or fingers constantly.",
    "All motions are rough and vigorous.",
    "Never looks directly at interlocutor.",
    "Licks lips disturbingly often.",
    "Plays with hair incessantly.",
    "Always wearing a particular expression.",
    "Moves in quick, darting fashion.",
    "Limps or moves in hindered ways.",
    "Constantly glancing around.",
    #Peripheral qualities
    "Has a distinctive scent.",
    "Talks extremely slowly or quickly.",
    "Voice is extremely grating and unpleasant.",
    "Has elaborate tattoos or skin-paintings.",
    "Hair colour is very abnormal for the area.",
    "Has a constant air of suspicion.",
    "Flashes expensive-to-them accessories.",
    "Hair and person distinctly unkempt.",
    "Flashy visible cyberware or accessory.",
    "Very obvious religious tokens are worn.",
    "Always seems semi-drugged, but isn't.",
    "Has some speech impediment."
    "Visibly devoted to some consumer brand.",
    "Their compad is constantly going off.",
    "They have a drink or drug close to hand.",
    "They have an unusual accent.",
    "They're of an uncommon race for the area.",
    "Extremely laconic or volube.",
    "Laughs at inappropriate moments.",
    "Very flushed, choleric features."],
    np.array([1]*53)
)

#%%Attributes
POI_HD = RollTable([1,2,3,6], np.array([0.64, 0.32, 0.05, 0.01]))
POI_AC = RollTable([10,14,16], np.array([0.32, 0.05, 0.01]))
POI_Atk = RollTable([0,1,2,4,8], np.array([0.64, 0.64, 0.32, 0.05, 0.01]))
POI_Dmg = RollTable(["By Weapon","By Weapon +1","By Weapon +3"], np.array([0.32, 0.05, 0.01]))
POI_ML = RollTable([6,8,9,10,11], np.array([0.64, 0.64, 0.32, 0.05, 0.01]))
POI_Skills = RollTable([1,2,3], np.array([0.32, 0.05, 0.01]))
POI_Saves = RollTable([15,14,12], np.array([0.32, 0.05, 0.01]))

#%%Social attributes
POI_social_init = RollTable(
    ["Unusually friendly and sociable.",
    "Suspicious or wary of the PCs.",
    "Coolly pragmatic or businesslike.",
    "Aggressive and hard-edged manner."],
    np.array([1]*4)
)

POI_social_offer = RollTable(
    ["As a win-win for both parties.",
    "As an act of generosity by the NPC.",
    "Tentatively suggested as a possibility.",
    "Reluctantly, grudgingly offered to the PCs.",
    "Requested in a petitionary fashion.",
    "It's an offer they can't safely refuse."],
    np.array([1]*6)
)

POI_social_refused = RollTable(
    ["Phlegmatic acceptance of the refusal.",
    "Pries at the reason for the refusal.",
    "Upset and aggrieved at the affront.",
    "Apply a threat if the PCs persist in refusal.",
    "Shrug and benevolently offer more.",
    "Grudgingly offer a better inducement.",
    "Amazement at the folly of the PCs.",
    "The NPC takes it as a personal insult."],
    np.array([1]*8)
)

POI_social_insulted = RollTable(
    ["Acts as if they hardly even noticed it.",
    "Immediately applies larger insult or threat.",
    "Seeks to disengage to plan a later reprisal.",
    "Takes it as a good joke or bad-taste jest.",
    "Retaliates in same way, but without heat.",
    "Shrugs it off, ignoring it if at all possible.",
    "Is inclined to be successfully intimidated.",
    "Prone to panic and violent over-reaction.",
    "Acts as if they didn't understand it.",
    "Coldly brings the engagement to an end."],
    np.array([1]*10)
)

POI_social_more = RollTable(
    ["Says will consider more, but won't give it.",
    "Try to find an alternative form of payment.",
    "Protest that it's already too much.",
    "Try to wring extra service for extra pay.",
    "Agree, but set harsh terms for success.",
    "Will agree to more but doesn't have it.",
    "Offers more, but at a later time.",
    "Explains why it isn't worth more to them.",
    "Castigate the avarice of the PCs.",
    "Bemoan the unfairness of their request.",
    "Seek pity or sympathy in lieu of more pay.",
    "Quickly agree to any reasonable exra cost."],
    np.array([1]*12)
)

POI_social_general = RollTable(
    ["Likes to tell stories about their past deeds.",
    "Treats men and women very differently.",
    "Enjoys asking about the PCs' own lives.",
    "Complains about local politics or events.",
    "Talks about the place they're meeting at.",
    "Shares gossip about mutual acquaintances.",
    "Blames a particular group for their woes.",
    "Encourages PCs to join their religion.",
    "Wants to hear about prior PC adventures.",
    "Has strange ideas about outworlder habits.",
    "Practically interrogates PC interlocutors.",
    "Seeks PC opinions about peripheral affairs.",
    "Drones on incessantly about trivia.",
    "Tends to point and gesture in PC's faces.",
    "Only explains things when prompted.",
    "Fascinated about something the PCs have.",
    "Makes comments about PC appearances.",
    "Complains about prior employees.",
    "Expresses doubt about the PCs' abilities.",
    "Dwells on the horrors of their problem."],
    np.array([1]*20)
)

#%% Running area
#MainNPC = NPC()
#MainNPC.get_summary()

#for i in range(10):
#    temp = NPC()
#    temp.get_summary()
#    temp = None

if __name__ == "__main__":
    NPC = NPC()
    NPC.get_summary()
