from direct.actor import Actor
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import Sequence, Func
from toontown.hood import InteractiveAnimatedProp
from toontown.toonbase import ToontownGlobals, ToontownBattleGlobals, TTLocalizer

class HydrantInteractiveProp(InteractiveAnimatedProp.InteractiveAnimatedProp):
    notify = DirectNotifyGlobal.directNotify.newCategory('HydrantInteractiveProp')
    BattleTrack = ToontownBattleGlobals.SQUIRT_TRACK
    BattleCheerText = TTLocalizer.InteractivePropTrackBonusTerms[BattleTrack]

    ZoneToIdles = {
        ToontownGlobals.ToonIslandCentral: (('tt_a_ara_ttc_hydrant_idle0', 1, 1, None, 3, 10),
                                         ('tt_a_ara_ttc_hydrant_idle2', 1, 1, None, 3, 10),
                                         ('tt_a_ara_ttc_hydrant_idle1', 1, 1, None, 3, 10),
                                         ('tt_a_ara_ttc_hydrant_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.RainbowRise: (('tt_a_ara_ttc_hydrant_idle0', 1, 1, None, 3, 10),
                                     ('tt_a_ara_ttc_hydrant_idle2', 1, 1, None, 3, 10),
                                     ('tt_a_ara_ttc_hydrant_idle1', 1, 1, None, 3, 10),
                                     ('tt_a_ara_ttc_hydrant_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.DaisyGarden: (('tt_a_ara_dga_hydrant_idle0', 3, 10, 'tt_a_ara_dga_hydrant_idle0settle', 3, 10),
                                      ('tt_a_ara_dga_hydrant_idleLook1', 1, 1, None, 3, 10),
                                      ('tt_a_ara_dga_hydrant_idleSneeze2', 1, 1, None, 3, 10),
                                      ('tt_a_ara_dga_hydrant_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.MinniesMelodyland: (('tt_a_ara_mml_hydrant_idle0', 3, 10, 'tt_a_ara_mml_hydrant_idle0settle', 3, 10),
                                           ('tt_a_ara_mml_hydrant_idle2', 3, 10, 'tt_a_ara_mml_hydrant_idle2settle', 3, 10),
                                           ('tt_a_ara_mml_hydrant_idle1', 3, 10, 'tt_a_ara_mml_hydrant_idle1settle', 3, 10),
                                           ('tt_a_ara_mml_hydrant_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.TheBrrrgh: (('tt_a_ara_tbr_hydrant_idleShiver1', 1, 1, None, 3, 10),
                                   ('tt_a_ara_tbr_hydrant_idleRubNose0', 1, 1, None, 3, 10),
                                   ('tt_a_ara_tbr_hydrant_idleSneeze2', 1, 1, None, 3, 10),
                                   ('tt_a_ara_tbr_hydrant_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.DonaldsDreamland: (('tt_a_ara_ddl_hydrant_idle0', 3, 10, None, 0, 0),
                                          ('tt_a_ara_ddl_hydrant_idle1', 1, 1, None, 0, 0),
                                          ('tt_a_ara_ddl_hydrant_idle2', 1, 1, None, 0, 0),
                                          ('tt_a_ara_ddl_hydrant_idleAwesome3', 1, 1, None, 0, 0))}

    ZoneToIdleIntoFightAnims = {
        ToontownGlobals.ToonIslandCentral: 'tt_a_ara_ttc_hydrant_idleIntoFight',
        ToontownGlobals.RainbowRise: 'tt_a_ara_ttc_hydrant_idleIntoFight',
        ToontownGlobals.DaisyGarden: 'tt_a_ara_dga_hydrant_idleIntoFight',
        ToontownGlobals.MinniesMelodyland: 'tt_a_ara_mml_hydrant_idleIntoFight',
        ToontownGlobals.TheBrrrgh: 'tt_a_ara_tbr_hydrant_idleIntoFight',
        ToontownGlobals.DonaldsDreamland: 'tt_a_ara_ddl_hydrant_idleIntoFight'}

    ZoneToVictoryAnims = {
        ToontownGlobals.ToonIslandCentral: 'tt_a_ara_ttc_hydrant_victoryDance',
        ToontownGlobals.RainbowRise: 'tt_a_ara_ttc_hydrant_victoryDance',
        ToontownGlobals.DaisyGarden: 'tt_a_ara_dga_hydrant_victoryDance',
        ToontownGlobals.MinniesMelodyland: 'tt_a_ara_mml_hydrant_victoryDance',
        ToontownGlobals.TheBrrrgh: 'tt_a_ara_tbr_hydrant_victoryDance',
        ToontownGlobals.DonaldsDreamland: 'tt_a_ara_ddl_hydrant_victoryDance'}

    ZoneToSadAnims = {
        ToontownGlobals.ToonIslandCentral: 'tt_a_ara_ttc_hydrant_fightSad',
        ToontownGlobals.RainbowRise: 'tt_a_ara_ttc_hydrant_fightSad',
        ToontownGlobals.DaisyGarden: 'tt_a_ara_dga_hydrant_fightSad',
        ToontownGlobals.MinniesMelodyland: 'tt_a_ara_mml_hydrant_fightSad',
        ToontownGlobals.TheBrrrgh: 'tt_a_ara_tbr_hydrant_fightSad',
        ToontownGlobals.DonaldsDreamland: 'tt_a_ara_ddl_hydrant_fightSad'}

    ZoneToFightAnims = {
        ToontownGlobals.ToonIslandCentral: ('tt_a_ara_ttc_hydrant_fightBoost', 'tt_a_ara_ttc_hydrant_fightCheer', 'tt_a_ara_ttc_hydrant_fightIdle'),
        ToontownGlobals.RainbowRise: ('tt_a_ara_ttc_hydrant_fightBoost', 'tt_a_ara_ttc_hydrant_fightCheer', 'tt_a_ara_ttc_hydrant_fightIdle'),
        ToontownGlobals.DaisyGarden: ('tt_a_ara_dga_hydrant_fightBoost', 'tt_a_ara_dga_hydrant_fightCheer', 'tt_a_ara_dga_hydrant_fightIdle'),
        ToontownGlobals.MinniesMelodyland: ('tt_a_ara_mml_hydrant_fightBoost', 'tt_a_ara_mml_hydrant_fightCheer', 'tt_a_ara_mml_hydrant_fightIdle'),
        ToontownGlobals.TheBrrrgh: ('tt_a_ara_tbr_hydrant_fightBoost', 'tt_a_ara_tbr_hydrant_fightCheer', 'tt_a_ara_tbr_hydrant_fightIdle'),
        ToontownGlobals.DonaldsDreamland: ('tt_a_ara_ddl_hydrant_fightBoost', 'tt_a_ara_ddl_hydrant_fightCheer', 'tt_a_ara_ddl_hydrant_fightIdle')}

    IdlePauseTime = base.config.GetFloat('prop-idle-pause-time', 0.0)

    def __init__(self, node):
        self.leftWater = None
        self.rightWater = None
        InteractiveAnimatedProp.InteractiveAnimatedProp.__init__(self, node)

    def setupActor(self, node):
        InteractiveAnimatedProp.InteractiveAnimatedProp.setupActor(self, node)

        if not self.hoodId == ToontownGlobals.TheBrrrgh:
            water = loader.loadModel('phase_5/models/char/tt_m_efx_hydrantSquirt')
            self.leftWater = water.find('**/efx_hydrantSquirtLeft')
            self.rightWater = water.find('**/efx_hydrantSquirtRight')

            if self.leftWater:
                self.leftWater.reparentTo(self.node.find('**/dx_left_water'))
                base.leftWater = self.leftWater
                self.leftWater.hide()

            if self.rightWater:
                self.rightWater.reparentTo(self.node.find('**/dx_right_water'))
                self.rightWater.hide()

    def hideWater(self):
        if self.leftWater:
            self.leftWater.hide()
        if self.rightWater:
            self.rightWater.hide()

    def showWater(self):
        if self.leftWater:
            self.leftWater.show()
        if self.rightWater:
            self.rightWater.show()

    def hasOverrideIval(self, origAnimName):
        return ('fightBoost' in origAnimName or 'fightCheer' in origAnimName) and not self.hoodId == ToontownGlobals.TheBrrrgh

    def getOverrideIval(self, origAnimName):
        result = Sequence()

        if self.hasOverrideIval(origAnimName):
            result.append(Func(self.showWater))
            animAndSound = self.createAnimAndSoundIval('fight0' if 'fightBoost' in origAnimName else 'fight1')
            result.append(animAndSound)
            result.append(Func(self.hideWater))

        return result
