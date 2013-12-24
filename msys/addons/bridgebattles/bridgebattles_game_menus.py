from header_game_menus import *
from module_constants import *
from header_items import *
from header_parties import *
from header_music import *

bridge_battles_snip = [
 (else_try), #Arch3r & Swyter#
  (party_get_position, pos1, "p_main_party"),
  
  (assign,":closest_distance", 100),
  (assign,":closest_bridge",    -1)
  
  #swy--itinerate along all the existing bridges and find the closest one
  (try_for_range,":cur_bridge", "p_bridge_1", p_bridge_14 + 1),
    
      #swy--compare the distance between the player and the current bridge
      (party_get_position,pos2, ":cur_bridge"),
      (get_distance_between_positions, ":cur_distance", pos1, pos2),
      
      #swy--if this bridge is closer than anything else, select it
      (try_begin),
        (lt, ":cur_distance", ":closest_distance"),
        #swy-- closest_bridge = :cur_bridge - p_bridge_1
        #      4th bridge  ->   64            61 (-1)
        (store_sub,":closest_bridge", ":cur_bridge", p_bridge_1 - 1),
        (assign, ":closest_distance", ":cur_distance"),
      (try_end),
      
  (try_end),
    
  #swy--if a bridge has been selected in the loop, choose it!
  (gt,":closest_bridge", -1),
  
  #swy-- scene_to_use = :cur_bridge + scn_bridge_1
  #      93th scene ->  4             89 (-1)
  (store_add,":scene_to_use", ":cur_bridge", scn_bridge_1 - 1),
  
  (set_jump_mission,"mt_lead_charge"),
  (jump_to_scene, ":scene_to_use"),
]


from util_wrappers import *
from util_common import *

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "game_menus"
        orig_game_menus = var_set[var_name_1]
        
        
        #swy--inject the bridge battles scene selection snippet
        try:
          find_i = list_find_first_match_i(orig_game_menus, "simple_encounter")
          codeblock = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOption("encounter_attack").GetConsequenceBlock()
        
          pos = codeblock.FindLineMatching(
            (eq, "$g_encounter_type", enctype_catched_during_village_raid),
          )
    
          codeblock.InsertAfter(pos+4, bridge_battles_snip)

        except:
          import sys
          print "Injection failed:", sys.exc_info()[1]
          raise
        
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)