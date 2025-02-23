#Expert logic updater
#updates unusedLocations

def updateLogic (unusedLocations, locArray, loadout) :
    Missile = ["Missile",
               b"\xdb\xee",
               b"\x2f\xef",
               b"\x83\xef",
               b"\x00"]
    Super = ["Super Missile",
             b"\xdf\xee",
             b"\x33\xef",
             b"\x87\xef",
             b"\x00"]
    PowerBomb = ["Power Bomb",
                 b"\xe3\xee",
                 b"\x37\xef",
                 b"\x8b\xef",
                 b"\x00"]
    Morph = ["Morph Ball",
             b"\x23\xef",
             b"\x77\xef",
             b"\xcb\xef",
             b"\x00"]
    GravityBoots = ["Gravity Boots",
                    b"\x40\xfd",
                    b"\x40\xfd",
                    b"\x40\xfd",
                    b"\x00"]   
    Speedball = ["Speed Ball",
                 b"\x03\xef",
                 b"\x57\xef",
                 b"\xab\xef",
                 b"\x00"]
    Bombs = ["Bombs",
             b"\xe7\xee",
             b"\x3b\xef",
             b"\x8f\xef",
             b"\x00"]
    HiJump = ["HiJump",
              b"\xf3\xee",
              b"\x47\xef",
              b"\x9b\xef",
              b"\x00"]
    GravitySuit = ["Gravity Suit",
                   b"\x0b\xef",
                   b"\x5f\xef",
                   b"\xb3\xef",
                   b"\x00"]
    DarkVisor = ["Dark Visor",
                 b"\xb0\xfd",
                 b"\xb0\xfd",
                 b"\xb0\xfd",
                 b"\x00"]
    Wave = ["Wave Beam",
            b"\xfb\xee",
            b"\x4f\xef",
            b"\xa3\xef",
            b"\x00"]
    SpeedBooster = ["Speed Booster",
                    b"\xf7\xee",
                    b"\x4b\xef",
                    b"\x9f\xef",
                    b"\x00"]
    Spazer = ["Spazer",
              b"\xff\xee",
              b"\x53\xef",
              b"\xa7\xef",
              b"\x00"]
    Varia = ["Varia Suit",
             b"\x07\xef",
             b"\x5b\xef",
             b"\xaf\xef",
             b"\x00"]
    Ice = ["Ice Beam",
           b"\xef\xee",
           b"\x43\xef",
           b"\x97\xef",
           b"\x00"]
    Grapple = ["Grapple Beam",
               b"\x17\xef",
               b"\x6b\xef",
               b"\xbf\xef",
               b"\x00"]
    MetroidSuit = ["Metroid Suit",
                   b"\x20\xfe",
                   b"\x20\xfe",
                   b"\x20\xfe",
                   b"\x00"]
    Plasma = ["Plasma Beam",
              b"\x13\xef",
              b"\x67\xef",
              b"\xbb\xef",
              b"\x00"]
    Screw = ["Screw Attack",
             b"\x1f\xef",
             b"\x73\xef",
             b"\xc7\xef",
             b"\x00"]
    Hypercharge = ["Hypercharge",
                   b"\x80\xf7",
                   b"\x80\xf7",
                   b"\x80\xf7",
                   b"\x00"]
    Charge = ["Charge Beam",
              b"\xeb\xee",
              b"\x3f\xef",
              b"\x93\xef",
              b"\x00"]
    Xray = ["X-Ray Scope",
            b"\x0f\xef",
            b"\x63\xef",
            b"\xb7\xef",
            b"\x00"]
    SpaceJump = ["Space Jump",
                 b"\x1b\xef",
                 b"\x6f\xef",
                 b"\xc3\xef",
                 b"\x00"]
    Energy = ["Energy Tank",
              b"\xd7\xee",
              b"\x2b\xef",
              b"\x7f\xef",
              b"\x00"]
    Refuel = ["Refuel Tank",
              b"\x27\xef",
              b"\x7b\xef",
              b"\xcf\xef",
              b"\x00"]
    SmallAmmo = ["Small Ammo",
                 b"\x00\xf9",
                 b"\x04\xf9",
                 b"\x08\xf9",
                 b"\x05"]
    LargeAmmo = ["Large Ammo",
                 b"\x00\xf9",
                 b"\x04\xf9",
                 b"\x08\xf9",
                 b"\x0a"]
    DamageAmp = ["Damage Amp",
                 b"\x7e\xf8",
                 b"\x7e\xf8",
                 b"\x7e\xf8",
                 b"\x00"]
    ChargeAmp = ["Charge Amp",
                 b"\xa0\xf0",
                 b"\xa0\xf0",
                 b"\xa0\xf0",
                 b"\x00"]
    SpaceJumpBoost = ["Space Jump Boost",
                      b"\xc0\xfc",
                      b"\xc0\xfc",
                      b"\xc0\xfc",
                      b"\x00"]
    spaceDrop = ["Space Drop","","","",""]
    energyCount=0
    for item in loadout :
        if item == Energy :
            energyCount += 1
    exitSpacePort = True
    jumpAble = exitSpacePort and (GravityBoots in loadout)
    underwater = jumpAble and ((HiJump in loadout) or (GravitySuit in loadout))
    pinkDoor = (Missile in loadout) or (Super in loadout)
    canUseBombs = (Morph in loadout) and ((Bombs in loadout) or (PowerBomb in loadout))
    canUsePB = (Morph in loadout) and (PowerBomb in loadout)
    vulnar = jumpAble and pinkDoor
    pirateLab = vulnar and canUseBombs and (((Speedball in loadout) or (SpeedBooster in loadout) or (GravitySuit in loadout)) or ((DarkVisor in loadout) and (Wave in loadout) and canUsePB))
    canFly = (Bombs in loadout) or (SpaceJump in loadout)
    upperVulnar = jumpAble and (energyCount > 2) and ((canFly and canUsePB) or (vulnar and (SpeedBooster in loadout)))
    depthsL = (energyCount > 4) and (Bombs in loadout) and underwater and (Super in loadout)
    hive = (energyCount > 4) and (Super in loadout) and vulnar and canUseBombs and ((depthsL and (canUsePB or (Ice in loadout))) or ((Wave in loadout) and (SpeedBooster in loadout)) or ((SpeedBooster in loadout) and canUsePB and (energyCount > 6)))
    geothermal = (hive and canUsePB and (Ice in loadout)) or (upperVulnar and canUsePB and (Plasma in loadout) and ((MetroidSuit in loadout) or (Screw in loadout)))
    eastLomyr = (vulnar and (Morph in loadout) and (SpeedBooster in loadout)) or (pirateLab and underwater and (Bombs in loadout) and (Super in loadout)) or (geothermal and underwater and ((Screw in loadout) and ((MetroidSuit in loadout) or (Grapple in loadout))))
    oceanDepths = underwater and ((pinkDoor and (Morph in loadout) and (DarkVisor in loadout)) or (Super in loadout))
    suzi = jumpAble and (Super in loadout) and canUsePB and (Wave in loadout) and (GravitySuit in loadout) and (SpeedBooster in loadout) and (Grapple in loadout)
    #print("Updating logic...")
    for thisLoc in unusedLocations :
        #thisLoc is a row. thisLoc['inlogic'] is the logic
        #for each location, check that location names match
        if thisLoc['fullitemname'] == "Impact Crater: AccelCharge":
            thisLoc['inlogic'] = exitSpacePort and (Morph in loadout) and (Spazer in loadout) and ((HiJump in loadout) or (SpeedBooster in loadout) or canFly)
        if thisLoc['fullitemname'] == "Subterranean Burrow":
            thisLoc['inlogic'] = exitSpacePort and ((Morph in loadout) or (GravityBoots in loadout))
        if thisLoc['fullitemname'] == "Sandy Cache":
            thisLoc['inlogic'] = jumpAble and (Missile in loadout) and ((Morph in loadout) or (GravitySuit in loadout))
        if thisLoc['fullitemname'] == "Submarine Nest":
            thisLoc['inlogic'] = underwater and pinkDoor
        if thisLoc['fullitemname'] == "Shrine Of The Penumbra":
            thisLoc['inlogic'] = jumpAble and pinkDoor and (GravitySuit in loadout) and (canUsePB or (canUseBombs and (DarkVisor in loadout)))
        if thisLoc['fullitemname'] == "Benthic Cache Access":
            thisLoc['inlogic'] = jumpAble and underwater and canUsePB and (Super in loadout)
        if thisLoc['fullitemname'] == "Benthic Cache":
            thisLoc['inlogic'] = jumpAble and underwater and canUseBombs and (Super in loadout)
        if thisLoc['fullitemname'] == "Ocean Vent Supply Depot":
            thisLoc['inlogic'] = jumpAble and underwater and (Morph in loadout) and ((Super in loadout) or (Screw in loadout))
        if thisLoc['fullitemname'] == "Sediment Flow":
            thisLoc['inlogic'] = jumpAble and underwater and (Super in loadout)
        if thisLoc['fullitemname'] == "Harmonic Growth Enhancer":
            thisLoc['inlogic'] = jumpAble and pinkDoor and canUseBombs
        if thisLoc['fullitemname'] == "Upper Vulnar Power Node":
            thisLoc['inlogic'] = vulnar and canUsePB and (Screw in loadout) and (MetroidSuit in loadout)
        if thisLoc['fullitemname'] == "Grand Vault":
            thisLoc['inlogic'] = vulnar and (Grapple in loadout)
        if thisLoc['fullitemname'] == "Cistern":
            thisLoc['inlogic'] = vulnar and canUseBombs
        if thisLoc['fullitemname'] == "Warrior Shrine: ETank":
            thisLoc['inlogic'] = vulnar and canUsePB
        if thisLoc['fullitemname'] == "Vulnar Caves Entrance":
            thisLoc['inlogic'] = vulnar
        if thisLoc['fullitemname'] == "Crypt":
            thisLoc['inlogic'] = vulnar and canUseBombs and ((Wave in loadout) or (Bombs in loadout))
        if thisLoc['fullitemname'] == "Archives: SpringBall": # yes it's actually Speed Ball, uses Spring data
            thisLoc['inlogic'] = vulnar and (Speedball in loadout)
        if thisLoc['fullitemname'] == "Archives: SJBoost":
            thisLoc['inlogic'] = vulnar and (Speedball in loadout) and (SpeedBooster in loadout)
        if thisLoc['fullitemname'] == "Sensor Maintenance: ETank": # front
            thisLoc['inlogic'] = vulnar and (Morph in loadout)
        if thisLoc['fullitemname'] == "Eribium Apparatus Room":
            thisLoc['inlogic'] = vulnar and canUseBombs and (DarkVisor in loadout)
        if thisLoc['fullitemname'] == "Hot Spring":
            thisLoc['inlogic'] = vulnar and (Morph in loadout) and (canUseBombs or (Super in loadout) or (Plasma in loadout)) and ((GravitySuit in loadout) or (Speedball in loadout)) and ((HiJump in loadout) or (Ice in loadout))
        if thisLoc['fullitemname'] == "Epiphreatic Crag":
            thisLoc['inlogic'] = vulnar and canUseBombs and (GravitySuit in loadout) and (((DarkVisor in loadout) and (Wave in loadout)) or (pirateLab and canUsePB))
        if thisLoc['fullitemname'] == "Mezzanine Concourse":
            thisLoc['inlogic'] = upperVulnar
        if thisLoc['fullitemname'] == "Greater Inferno":
            thisLoc['inlogic'] = depthsL and canUsePB and (Super in loadout) and (MetroidSuit in loadout)
        if thisLoc['fullitemname'] == "Burning Depths Cache":
            thisLoc['inlogic'] = depthsL and canUsePB and (Super in loadout) and (MetroidSuit in loadout) and ((Spazer in loadout) or (Wave in loadout))
        if thisLoc['fullitemname'] == "Mining Cache":
            thisLoc['inlogic'] = depthsL and canUseBombs
        if thisLoc['fullitemname'] == "Infested Passage":
            thisLoc['inlogic'] = hive
        if thisLoc['fullitemname'] == "Fire's Boon Shrine":
            thisLoc['inlogic'] = hive and ((Ice in loadout) or (SpeedBooster in loadout))
        if thisLoc['fullitemname'] == "Fire's Bane Shrine":
            thisLoc['inlogic'] = hive and ((Ice in loadout) or (SpeedBooster in loadout))
        if thisLoc['fullitemname'] == "Ancient Shaft":
            thisLoc['inlogic'] = hive and (MetroidSuit in loadout) and ((Ice in loadout) or (SpeedBooster in loadout))
        if thisLoc['fullitemname'] == "Gymnasium":
            thisLoc['inlogic'] = hive and (Grapple in loadout) and ((Ice in loadout) or (SpeedBooster in loadout))
        if thisLoc['fullitemname'] == "Electromechanical Engine":
            thisLoc['inlogic'] = geothermal and (Grapple in loadout)
        if thisLoc['fullitemname'] == "Depressurization Valve":
            thisLoc['inlogic'] = geothermal and (((Grapple in loadout) and (Screw in loadout)) or (MetroidSuit in loadout))
        if thisLoc['fullitemname'] == "Loading Dock Storage Area":
            thisLoc['inlogic'] = pirateLab
        if thisLoc['fullitemname'] == "Containment Area":
            thisLoc['inlogic'] = pirateLab and underwater and ((MetroidSuit in loadout) or (Screw in loadout))
        if thisLoc['fullitemname'] == "Briar: SJBoost": # top
            thisLoc['inlogic'] = eastLomyr and canUsePB
        if thisLoc['fullitemname'] == "Shrine Of Fervor":
            thisLoc['inlogic'] = eastLomyr
        if thisLoc['fullitemname'] == "Chamber Of Wind":
            thisLoc['inlogic'] = eastLomyr and pinkDoor and (SpeedBooster in loadout) and (canUseBombs or ((Screw in loadout) and (Speedball in loadout)))
        if thisLoc['fullitemname'] == "Water Garden":
            thisLoc['inlogic'] = eastLomyr and (SpeedBooster in loadout)
        if thisLoc['fullitemname'] == "Crocomire's Energy Station":
            thisLoc['inlogic'] = eastLomyr and (Super in loadout) and (SpeedBooster in loadout)
        if thisLoc['fullitemname'] == "Wellspring Cache":
            thisLoc['inlogic'] = eastLomyr and underwater and (Super in loadout) and (SpeedBooster in loadout)
        if thisLoc['fullitemname'] == "Frozen Lake Wall: DamageAmp":
            thisLoc['inlogic'] = upperVulnar and canFly and (Plasma in loadout)
        if thisLoc['fullitemname'] == "Grand Promenade":
            thisLoc['inlogic'] = upperVulnar
        if thisLoc['fullitemname'] == "Summit Landing":
            thisLoc['inlogic'] = upperVulnar and canUseBombs
        if thisLoc['fullitemname'] == "Snow Cache":
            thisLoc['inlogic'] = upperVulnar and canUseBombs and (Plasma in loadout)
        if thisLoc['fullitemname'] == "Reliquary Access": 
            thisLoc['inlogic'] = upperVulnar and canUseBombs and (Super in loadout) and (DarkVisor in loadout)
        if thisLoc['fullitemname'] == "Syzygy Observatorium":
            thisLoc['inlogic'] = upperVulnar and (((Super in loadout) and (Varia in loadout) and ((MetroidSuit in loadout) or (Hypercharge in loadout))) or (Screw in loadout))
        if thisLoc['fullitemname'] == "Armory Cache 2":
            thisLoc['inlogic'] = upperVulnar and ((canUseBombs and (Super in loadout) and (DarkVisor in loadout)) or (Screw in loadout))
        if thisLoc['fullitemname'] == "Armory Cache 3":
            thisLoc['inlogic'] = upperVulnar and ((canUseBombs and (Super in loadout) and (DarkVisor in loadout)) or (Screw in loadout))
        if thisLoc['fullitemname'] == "Drawing Room":
            thisLoc['inlogic'] = upperVulnar and (Super in loadout)
        if thisLoc['fullitemname'] == "Impact Crater Overlook":
            thisLoc['inlogic'] = canFly and canUseBombs and (canUsePB or (Super in loadout))
        if thisLoc['fullitemname'] == "Magma Lake Cache":
            thisLoc['inlogic'] = depthsL and (Ice in loadout)
        if thisLoc['fullitemname'] == "Shrine Of The Animate Spark":
            thisLoc['inlogic'] = hive and suzi and (Hypercharge in loadout)
        if thisLoc['fullitemname'] == "Docking Port 4": # (4 = letter Omega)
            thisLoc['inlogic'] = (((spaceDrop in loadout) == False) and (Grapple in loadout)) or ((spaceDrop in loadout) and geothermal and (Grapple in loadout) and (Screw in loadout) and (MetroidSuit in loadout))
        if thisLoc['fullitemname'] == "Ready Room":
            thisLoc['inlogic'] = (((spaceDrop in loadout) == False) and (Super in loadout)) or ((spaceDrop in loadout) and geothermal and (Grapple in loadout) and (Screw in loadout) and (MetroidSuit in loadout))
        if thisLoc['fullitemname'] == "Torpedo Bay":
            thisLoc['inlogic'] = ((spaceDrop in loadout) == False) or (((spaceDrop in loadout) and geothermal and (Grapple in loadout) and (Screw in loadout) and (MetroidSuit in loadout)))
        if thisLoc['fullitemname'] == "Extract Storage":
            thisLoc['inlogic'] = (((spaceDrop in loadout) == False) and canUsePB) or ((spaceDrop in loadout) and geothermal and (Grapple in loadout) and (Screw in loadout) and (MetroidSuit in loadout))
        if thisLoc['fullitemname'] == "Impact Crater Alcove":
            thisLoc['inlogic'] = jumpAble and canFly and canUseBombs
        if thisLoc['fullitemname'] == "Ocean Shore: bottom":
            thisLoc['inlogic'] = exitSpacePort
        if thisLoc['fullitemname'] == "Ocean Shore: top":
            thisLoc['inlogic'] = jumpAble
        if thisLoc['fullitemname'] == "Sandy Burrow: ETank": # top
            thisLoc['inlogic'] = underwater and (((GravitySuit in loadout) and ((Screw in loadout) or canUseBombs)) or ((Speedball in loadout) and canUseBombs))
        if thisLoc['fullitemname'] == "Submarine Alcove":
            thisLoc['inlogic'] = underwater and (Morph in loadout) and (((DarkVisor in loadout) and pinkDoor) or (Super in loadout) or (vulnar and underwater and (energyCount > 4) and canUseBombs and (Speedball in loadout)))
        if thisLoc['fullitemname'] == "Sediment Floor":
            thisLoc['inlogic'] = underwater and (Morph in loadout) and ((Super in loadout) or (vulnar and underwater and (energyCount > 4) and canUseBombs and (Speedball in loadout)))
        if thisLoc['fullitemname'] == "Sandy Gully":
            thisLoc['inlogic'] = underwater and (Super in loadout)
        if thisLoc['fullitemname'] == "Hall Of The Elders":
            thisLoc['inlogic'] = vulnar and (Morph in loadout) and ((Missile in loadout) or (GravitySuit in loadout) or (underwater and (Speedball in loadout)))
        if thisLoc['fullitemname'] == "Warrior Shrine: AmmoTank bottom":
            thisLoc['inlogic'] = vulnar and (Morph in loadout) and (Missile in loadout)
        if thisLoc['fullitemname'] == "Warrior Shrine: AmmoTank top":
            thisLoc['inlogic'] = vulnar and (Morph in loadout) and (Missile in loadout) and canUseBombs
        if thisLoc['fullitemname'] == "Path Of Swords":
            thisLoc['inlogic'] = vulnar and (canUseBombs or ((Morph in loadout) and (Screw in loadout)))
        if thisLoc['fullitemname'] == "Auxiliary Pump Room":
            thisLoc['inlogic'] = vulnar and canUseBombs
        if thisLoc['fullitemname'] == "Monitoring Station":
            thisLoc['inlogic'] = vulnar and (Morph in loadout)
        if thisLoc['fullitemname'] == "Sensor Maintenance: AmmoTank": # back
            thisLoc['inlogic'] = vulnar and canUseBombs
        if thisLoc['fullitemname'] == "Causeway Overlook":
            thisLoc['inlogic'] = vulnar and canUseBombs
        if thisLoc['fullitemname'] == "Placid Pool":
            thisLoc['inlogic'] = vulnar and canUsePB and ((geothermal and (Screw in loadout) and energyCount > 4) or ((Super in loadout) and (((energyCount > 4) or (Wave in loadout)) or ((DarkVisor in loadout) and ((Speedball in loadout) or (SpeedBooster in loadout))))))
        if thisLoc['fullitemname'] == "Blazing Chasm":
            thisLoc['inlogic'] = depthsL and canUsePB and (Super in loadout) and (MetroidSuit in loadout)                  
        if thisLoc['fullitemname'] == "Generator Manifold":
            thisLoc['inlogic'] = (depthsL and canUsePB and (Super in loadout) and (MetroidSuit in loadout)) or (geothermal and (Screw in loadout))
        if thisLoc['fullitemname'] == "Fiery Crossing Cache":
            thisLoc['inlogic'] = depthsL and canUsePB
        if thisLoc['fullitemname'] == "Dark Crevice Cache":
            thisLoc['inlogic'] = depthsL and canUseBombs and canFly
        if thisLoc['fullitemname'] == "Ancient Basin":
            thisLoc['inlogic'] = hive
        if thisLoc['fullitemname'] == "Central Corridor: right":
            thisLoc['inlogic'] = vulnar and canUseBombs and (((DarkVisor in loadout) and (Wave in loadout)) or (pirateLab and (canUsePB or (underwater and (Screw in loadout)))) or (eastLomyr and canUsePB and underwater))
        if thisLoc['fullitemname'] == "Briar: AmmoTank": # bottom
            thisLoc['inlogic'] = eastLomyr and (Morph in loadout)
        if thisLoc['fullitemname'] == "Icy Flow":
            thisLoc['inlogic'] = upperVulnar and (SpeedBooster in loadout) and (Plasma in loadout)
        if thisLoc['fullitemname'] == "Ice Cave":
            thisLoc['inlogic'] = upperVulnar and (Plasma in loadout)
        if thisLoc['fullitemname'] == "Antechamber":
            thisLoc['inlogic'] = upperVulnar and canUsePB
        if thisLoc['fullitemname'] == "Eddy Channels":
            thisLoc['inlogic'] = underwater and (Speedball in loadout) and ((pinkDoor and (DarkVisor in loadout)) or (Super in loadout) or (vulnar and (energyCount > 4) and canUseBombs))
        if thisLoc['fullitemname'] == "Tram To Suzi Island":
            thisLoc['inlogic'] = underwater and canUsePB and (Super in loadout) and (SpeedBooster in loadout) and (Spazer in loadout)
        if thisLoc['fullitemname'] == "Portico":
            thisLoc['inlogic'] = suzi
        if thisLoc['fullitemname'] == "Tower Rock Lookout": 
            thisLoc['inlogic'] = suzi and canFly
        if thisLoc['fullitemname'] == "Reef Nook":
            thisLoc['inlogic'] = suzi and canFly
        if thisLoc['fullitemname'] == "Saline Cache":
            thisLoc['inlogic'] = suzi and canFly
        if thisLoc['fullitemname'] == "Enervation Chamber":
            thisLoc['inlogic'] = suzi and (Hypercharge in loadout)
        if thisLoc['fullitemname'] == "Weapon Locker":
            thisLoc['inlogic'] = (((spaceDrop in loadout) == False) and (Missile in loadout)) or ((spaceDrop in loadout) and geothermal and (Grapple in loadout) and (Screw in loadout) and (MetroidSuit in loadout))
        if thisLoc['fullitemname'] == "Aft Battery":
            thisLoc['inlogic'] = (((spaceDrop in loadout) == False) and (Morph in loadout)) or ((spaceDrop in loadout) and geothermal and (Grapple in loadout) and (Screw in loadout) and (MetroidSuit in loadout))
        if thisLoc['fullitemname'] == "Forward Battery":
            thisLoc['inlogic'] = geothermal and (Grapple in loadout) and (Screw in loadout) and (MetroidSuit in loadout)
        if thisLoc['fullitemname'] == "Gantry": 
            thisLoc['inlogic'] = (((spaceDrop in loadout) == False) and (Missile in loadout)) or ((spaceDrop in loadout) and geothermal and (Grapple in loadout) and (Screw in loadout) and (MetroidSuit in loadout))
        if thisLoc['fullitemname'] == "Garden Canal":
            thisLoc['inlogic'] = eastLomyr and canUsePB and (Spazer in loadout)
        if thisLoc['fullitemname'] == "Sandy Burrow: AmmoTank": # bottom
            thisLoc['inlogic'] = underwater and (Morph in loadout) and ((Speedball in loadout) or (GravitySuit in loadout))
        if thisLoc['fullitemname'] == "Trophobiotic Chamber":
            thisLoc['inlogic'] = vulnar and (Morph in loadout) and (Speedball in loadout)
        if thisLoc['fullitemname'] == "Waste Processing":
            thisLoc['inlogic'] = (SpeedBooster in loadout) and ((vulnar and (Wave in loadout)) or (pirateLab and canUsePB))
        if thisLoc['fullitemname'] == "Grand Chasm":
            thisLoc['inlogic'] = upperVulnar and canUseBombs and (Screw in loadout)
        if thisLoc['fullitemname'] == "Mining Site 1": # (1 = letter Alpha)
            thisLoc['inlogic'] = canUseBombs and (vulnar or depthsL)
        if thisLoc['fullitemname'] == "Colosseum": # GT
            thisLoc['inlogic'] = depthsL and (Varia in loadout) and (Charge in loadout)
        if thisLoc['fullitemname'] == "Lava Pool":
            thisLoc['inlogic'] = depthsL and (MetroidSuit in loadout)
        if thisLoc['fullitemname'] == "Hive Main Chamber":
            thisLoc['inlogic'] = hive
        if thisLoc['fullitemname'] == "Crossway Cache":
            thisLoc['inlogic'] = hive and ((Ice in loadout) or (SpeedBooster in loadout))
        if thisLoc['fullitemname'] == "Slag Heap":
            thisLoc['inlogic'] = hive and canUseBombs and (MetroidSuit in loadout) and ((Ice in loadout) or (SpeedBooster in loadout))
        if thisLoc['fullitemname'] == "Hydrodynamic Chamber":
            thisLoc['inlogic'] = pirateLab and underwater and (Spazer in loadout)
        if thisLoc['fullitemname'] == "Central Corridor: left":
            thisLoc['inlogic'] = vulnar and canUseBombs and (Speedball in loadout) and (SpeedBooster in loadout) and (GravitySuit in loadout) and ((DarkVisor in loadout) or (pirateLab and canUsePB))
        if thisLoc['fullitemname'] == "Restricted Area":
            thisLoc['inlogic'] = vulnar and canUseBombs and underwater and (MetroidSuit in loadout) and (((DarkVisor in loadout) and (Wave in loadout)) or ((pirateLab or eastLomyr) and canUsePB))
        if thisLoc['fullitemname'] == "Foundry":
            thisLoc['inlogic'] = vulnar and canUseBombs and underwater and (((DarkVisor in loadout) and (Wave in loadout)) or ((pirateLab or eastLomyr) and canUsePB))
        if thisLoc['fullitemname'] == "Norak Escarpment":
            thisLoc['inlogic'] = eastLomyr and (canFly or (SpeedBooster in loadout))
        if thisLoc['fullitemname'] == "Glacier's Reach":
            thisLoc['inlogic'] = upperVulnar and (energyCount > 3)
        if thisLoc['fullitemname'] == "Sitting Room":
            thisLoc['inlogic'] = upperVulnar and canUsePB
        if thisLoc['fullitemname'] == "Suzi Ruins Map Station Access":
            thisLoc['inlogic'] = suzi
        if thisLoc['fullitemname'] == "Obscured Vestibule": 
            thisLoc['inlogic'] = suzi
        if thisLoc['fullitemname'] == "Docking Port 3": # (3 = letter Gamma)
            thisLoc['inlogic'] = (((spaceDrop in loadout) == False) and (Grapple in loadout)) or ((spaceDrop in loadout) and geothermal and (Grapple in loadout) and (Screw in loadout) and (MetroidSuit in loadout))
        if thisLoc['fullitemname'] == "Arena":
            thisLoc['inlogic'] = vulnar and (Morph in loadout)
        if thisLoc['fullitemname'] == "West Spore Field":
            thisLoc['inlogic'] = vulnar and canUseBombs and (Super in loadout) and (Wave in loadout) and (Speedball in loadout)
        if thisLoc['fullitemname'] == "Magma Chamber":
            thisLoc['inlogic'] = depthsL and (((Varia in loadout) and (Charge in loadout)) or ((MetroidSuit in loadout) and energyCount > 6))
        if thisLoc['fullitemname'] == "Equipment Locker":
            thisLoc['inlogic'] = pirateLab
        if thisLoc['fullitemname'] == "Antelier": # spelled "Antilier" in subversion 1.1
            thisLoc['inlogic'] = pirateLab and underwater
        if thisLoc['fullitemname'] == "Weapon Research":
            thisLoc['inlogic'] = vulnar and canUseBombs and (Wave in loadout) and underwater and ((DarkVisor in loadout) or (pirateLab and (canUsePB or (Screw in loadout))))
        if thisLoc['fullitemname'] == "Crocomire's Lair":
            thisLoc['inlogic'] = eastLomyr and (Super in loadout) and (SpeedBooster in loadout)
    return unusedLocations
