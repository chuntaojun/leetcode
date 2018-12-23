#
# @lc app=leetcode id=841 lang=python
#
# [841] Keys and Rooms
#
# https://leetcode.com/problems/keys-and-rooms/description/
#
# algorithms
# Medium (58.18%)
# Total Accepted:    21.3K
# Total Submissions: 36.6K
# Testcase Example:  '[[1],[2],[3],[]]'
#
# There are N rooms and you start in room 0.  Each room has a distinct number
# in 0, 1, 2, ..., N-1, and each room may have some keys to access the next
# room. 
# 
# Formally, each room i has a list of keys rooms[i], and each key rooms[i][j]
# is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j]
# = v opens the room with number v.
# 
# Initially, all the rooms start locked (except for room 0). 
# 
# You can walk back and forth between rooms freely.
# 
# Return true if and only if you can enter every room.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1],[2],[3],[]]
# Output: true
# Explanation:  
# We start in room 0, and pick up key 1.
# We then go to room 1, and pick up key 2.
# We then go to room 2, and pick up key 3.
# We then go to room 3.  Since we were able to go to every room, we return
# true.
# 
# 
# Example 2:
# 
# 
# Input: [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can't enter the room with number 2.
# 
# 
# Note:
# 
# 
# 1 <= rooms.length <= 1000
# 0 <= rooms[i].length <= 1000
# The number of keys in all rooms combined is at most 3000.
# 
# 
#
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        l = len(rooms)
        self.graph = [[0 for i in range(l)] for j in range(l)]
        self.room = [0 for i in range(l)]
        self.room[0] = 1
        for i in range(l):
            for j in range(len(rooms[i])):
                if i != rooms[i][j]:
                    self.graph[i][rooms[i][j]] = 1
        self.graph[0][0] = 1
        # for k in self.graph:
        #     print(k)
        q = [0]
        while len(q) != 0:
            _t = []
            for _ in range(len(q), 0, -1):
                nowLoc = q.pop(0)
                for i in range(1, l):
                    if self.graph[nowLoc][i] == 1 and self.room[i] != 1:
                        if i not in _t:
                            _t.append(i)
                            q.append(i)
                        self.room[i] = 1
        return sum(self.room) == l


if __name__ == '__main__':
    s = Solution()
    rooms = [[227,421,143,411,761],[48,332,973],[406,193,755],[117],[378,832],[125,330,859],[735,842],[165,620,363,391],[732,874,953,107,381,98],[401,70,634,831],[34,518],[192],[60,966],[566,665,913,975],[53,433,574,86],[320,68,395],[555,92,320,551],[164,384,502],[482,667,769],[118,340,511,79,748],[515],[534,854,414,572],[910,298],[247,348],[922,85,772,796,822],[300,658,542],[],[735,863],[93,679,409,600],[999],[315,122],[744,89,461,476,809],[647,219],[656,93,33],[665,38,201,205,364,119,496],[105,386,780],[35,43,759,319,586,183,562],[391,976],[572,83],[267,285,596,842,18,459,502,613,788],[293,545,623,845],[688],[63,490,612,845],[58,479,521,552],[195,319,137],[110,862],[286],[],[21,644],[267],[701,262,670],[276,149,179,292],[714,34,549,230],[202,469,691,121],[144,819],[],[458,491,489,910],[550],[357,816,995,300],[50,994,510],[364,76,453],[475,822],[42,389],[897,23],[105,620,246,554,929],[527,778],[304,367,814],[834,993,151,369,185],[843,214,686],[629],[619,714],[558],[224],[481,560,982,214,529,914,308],[166,992],[15],[325,188,460,675],[305,509,700],[426,9,998],[213,673,400],[30,157,520,639,295,784],[865,789],[18,279],[801,174,684,743,184],[92],[904,704],[288,582,159,785,290],[380,156],[358,530],[160,959,995],[1,760,818,323,325],[526,841,281,533],[204,423,700,349,464],[484,232,641],[198,215,542,20,750,922],[171,600,69,557],[422,754,136],[181,306,513,31],[],[661,207,252,500],[444],[287,301,255],[427,29,204,943],[457,187],[1,506,552,203,433,571,954],[606,701],[208],[213,240,799,743],[136,974,683],[46,140,902],[807,868,80,532,586],[826,293,882],[20,245,410,610,546],[223,178,454,747,837,868,893],[73,120,546,987,737],[892,888,892],[790],[194,596,950],[29,261,412,66,792],[],[508,616,649,893,794,506,566,585],[391,479,779],[398,931,940],[632,428,835,132],[724,244,862],[237,634,840,989],[263,551,338],[28,96,147,352],[412,524,254,306],[49,642,42,875,913,945],[],[538,674,272],[2,625],[37,817,826],[453,696,439,376],[187,605,777,181,446,239],[302,709],[37,791,191,715],[61,121],[249,618],[196,377,408,229,587],[222,138],[219,368],[11,379],[471,118,316,673],[919],[632,456,801,864],[767],[588,66,134,195,678],[18],[177,856],[778,151,432,645,930],[969,345,301],[977],[465,77,707],[],[108,427,952,916],[468,736],[],[83,975],[561],[234,55,774],[692,94,608,808],[152,198],[88,186,400,506],[231,682],[740,961,67,545],[172,518,644,954,293,342,739,827,964,990],[608,779,240],[719,326,637,806],[98,180,655],[183,163,215],[],[498,180,333,334],[313,536,633],[104,144],[250,152],[360,372],[150],[],[781,193,467,486],[466],[161,870],[280,563,48,422],[932,210,843],[344],[244,283,425,761,849],[580,597,863],[528,761,798,11,350],[483,356],[67,226],[209,305],[406],[258,337],[648,662,743,804],[486,793,114,620,764],[211,221,860,413],[7,907,182,344,572],[673,745],[343,350,645,740],[713,259,484,853,799,953],[962,223],[310,782],[871,875,291],[5,139,487],[],[343,767],[296,914],[239,881,374],[172,264],[407,36,919],[253,812,531,551,637,589],[808],[963],[890],[877,491],[421],[841,998],[736,156,472,603],[792],[917],[240,901],[35,426,532,246,527,765,847],[593,693],[833],[47,795,321,553,540,694],[477,690,941,392,936],[158,501,87],[411,870],[939],[321,886,775,961],[161,194],[918,556,275,960],[196],[299,585,747,41],[80,299,450,186,398,440],[44,409,925,176],[23,988,638],[721,734],[140,511],[617,635],[852],[159,565,176],[908,798],[206],[],[109,901],[498],[],[578,806,730,867],[228,525,280],[930],[94,515,486,697,430,554,991],[867,256,120,543],[90,787],[193],[567],[883,965,490,786],[200,672,656,912],[],[948,784,457],[331,693,555,697],[725,728,920,229,659],[111,146,51,717],[153,468],[12,757,809,412,598,807],[641,710],[197],[413,820],[57,238,271,251,339,515],[611,615,652,919,161],[],[469],[585,93],[156],[421],[916,201,327],[699,798,922,233,766],[511],[188,243],[356,392],[280,780,466],[715,729,99],[639,718,825,823],[118,921,401],[288,899,200],[807,818],[888,459],[821,873,512,684],[114,861,5],[340],[112,428,870,851],[107,556,645,215,493],[286],[295],[70],[618,222,915,933],[322,708,846],[62,229,499,116,132,340],[768,5,375],[980,408],[699],[464,802],[326,885],[185,894,595,856,864],[613,858,968],[],[],[623,905],[79,765,825,303,103,689,791,833,944],[476,346,872],[519,772],[133],[606,890],[],[924],[449],[541,706],[15],[312,431,952,905],[436,1,314,470],[191,329],[],[635,935,185,568],[388,793,271,938],[537,624,750,755,730,966],[707,394,702],[265],[64,236,599,687,276,503,674],[373,688,241],[351],[27,371,17,670],[46,376,573,548,690,949],[375,873],[117,653],[916,699,948],[434,967,266,803],[115],[241,405,923,728],[45,501,14],[720,273,698],[745,198,165,417],[399,786,428],[214,264],[33,160,171,360,513],[403],[970],[579,891,472,40],[154],[22,335,739],[257,190,315,517],[39,290,355,578,979],[983],[359,622,123],[],[254,749,976,996,608,407,604],[973,355,671],[653,841,912,30,359],[746,560,844,706],[273,395],[817,966,500],[317,128,284,514],[997,57,302],[286],[51,14,609],[978,124,126,866,773],[588,473,477],[437,666,410,583,599,619,812],[287,744,783,918],[512,729,323,146],[258,262,284,697,733,76],[365,668,786,810],[463],[438],[123,521],[102,339,803],[951,231,349,455,610,588,857],[169,210],[769,318,621,738,296],[418,568,722,437,731],[173,857],[717,846,377],[630,828],[216,375],[155,878],[],[553,737,416],[612,801],[141,589,22],[453,611,169],[792,907],[932],[144,830],[797,725],[755,460,651],[43,629],[783,856,520,253,927],[921,907,38],[773],[61,507],[170,247,358,580],[544,519],[239,880],[833,141],[148,446,978],[146,268,902,926,178,627,242,247,994],[],[705,538,768],[654,55],[799],[805,940,759,650],[741,519,934,91],[113,475],[536,335],[242,718,223,686,722,763],[307,366,696],[629,177,594],[960,862],[130,696,25],[396],[153,598],[264,725],[903,874,523],[470,918,181,612],[189],[485,723,463,577],[167],[950,480],[129,336,664],[49,202],[217,681,523,217,894],[282,370,245,655,541],[824,50,296,341,590,648,908],[244,469],[967,133,993,494],[510,773,787,12],[943,114,269,584,895],[78,111,298,384],[886],[54,333,705,231],[196,822],[127,682,145,140],[41,591],[996],[137,317,463,969,2,73,481],[345,758,817,925],[494,644,848],[269,142,495,869,883,999],[877],[89,458,971,403,646,770],[352,394,606,961,356,518],[],[332,986,505],[27,105],[251,126,531],[184,899,851],[100,577,82,659],[371,997],[509,968,313,382],[82,211],[538],[562,10,85,442],[95],[266,78,559],[338,88,867],[],[163,887],[4],[927,100],[85,450,316,879],[220,380,382],[11,110,277],[887,969],[148],[122,164,661,896,795,896,967],[496,990,189,402,872,522],[255,548,557,481],[311,402,757,775],[525,478],[753,958,107,321],[154,733],[103,424,468,207,435,940],[369,473,274,576],[367,411,998],[],[567,649,889,484],[310,851,309,937,631],[576,681,116,167],[754],[516,17,361],[471],[595,618],[36,102,810],[346,908,385,923],[2,884,449],[742],[318,720,839,560],[61,727,71,526,815],[493,537,996,981],[680,900,911,32,137,404],[480,943,222,614],[291,487,758,911],[975,988,103,415,742],[666],[366,383],[684,28,636,661],[386,539,268],[48,442,664,320,434,695,716],[180,324,662],[124,176,393,816,828],[212,775,952],[45,586,406,594,192],[338],[313,546,898,574],[],[72,97,377,448,871],[336,635,64,365],[460,663,157],[294,741,832,917],[590,173,836],[934,648,698,861,977],[261,957,581,715,88],[694,255,388,287],[162,74,111],[224],[260,266,491],[31,134,771,815,823,365,414,575,915,392],[154,488,737,780,245],[456],[39,614,373,106],[225,378],[316,341,802,422,813,974],[398],[470,621,865],[812,513],[869,331,175,794],[148],[345],[53,283,796,24,238,889],[508],[522,877],[472,947],[591,997],[603,933,308],[776,881],[275,617],[116,447,820,881],[304,949,514,777],[839],[310],[363,407,731,854,141],[763,797,410],[751,405],[362,570,758,941],[208,601,130,139,166,569],[408],[381,99,289],[563],[438,928,30,57,102,270,986],[108,601,256],[142,149],[145,679,815],[252,459,285],[558,584],[712,235,158,419,850],[149,785,59,754],[906,962,657],[467,583,594,880,744,873,528,736],[957,524],[507,587,760,949,441,438],[494,818,965,432,336,536,710],[314,609,637,41,622,124,283],[228],[811,979,357,269],[647,649],[104,397,764,13],[135,495,676,946,20],[557,297,664,683,825],[597,868,897,927,462],[790,899],[13,503,162],[991,261],[882],[607,183,972,3,97],[920,541],[119,197,741,983],[832,337,505,708,691],[628,814,353,854],[388,679],[257,311,387,152],[876,182],[675,763,770],[26,278],[],[165,654,166,956],[434,528,485],[],[390],[168,424,510,923,317],[945,999],[462],[431,8],[36,878,703],[938],[831,938,393,722,936],[404,324],[936,467,823],[226,420,552,948],[860,452,354],[461,929,6,357,660],[332],[341],[],[98,322,559,712,885],[752],[581,626,993],[290,212],[638,7],[133,480,849,350],[328,259,573,701],[279,28],[709],[730,195,362,311,658],[829,878,3,953,970,94],[132,609],[329,874],[435,186,437],[362,497,642],[688],[882,886,880],[13,669],[558,253,750],[236,73,658,724,654],[],[942],[487,291,550,840],[646,476],[225,447,564,35],[31,425,781],[667,577,128,150],[660,44],[128,530,615],[457,628,963],[602,981,16,26,762],[55,56,671,858,924,964],[192,871,120,218,499],[651,303,474],[451,581,592,887],[131,800],[739,762,54,91],[86],[647,838],[563,571],[224,909,616,343],[419],[6,348,622],[326,474,478,218],[706],[626,708],[68,493,677,652,964,973],[956,982,220],[182,84,208],[992,702,347],[531,485],[855,75,131,21,189],[805,895],[387,634,883],[417,155,614,675,520,972],[],[719],[327,533,719,836,203],[419,703,32,167,583,860],[],[497,879,597],[153,307],[54,643],[477,891],[716],[101,171,397],[443,784,830,274,600,479,749],[592,123,827],[81,168],[249,478,794,142],[432,726,914,771],[584,757,657,903,844],[445,489,540],[],[455,143,251,426,759],[270,575,380],[3,599,217],[71,561,157],[540,983,272,729],[59,504,905,58,596,732],[212,564],[],[396,631,748,790],[51,834],[327,379],[219,272,394,131,668],[162],[],[791,806,831],[652],[358,452,447],[90,797],[277,43,795],[275,160],[270],[456,689,942,956,19,170],[847,158],[808,565,9,539],[400,522],[738,58,145],[448,544,667,707,884],[74,60,641,642,821],[650,774,40,690],[685,680,138],[179],[24,282,370,604,865],[547,593,226],[76,305,42,373],[379,302],[631,809,691],[309,748,64,396],[959],[796],[687,79,646,777],[829],[497,74,920],[944],[845,590],[574,985],[209,72,328,843],[87,655,643],[323,752,837,45],[351,982],[872,8,507],[],[416,984],[619],[170,376,67],[946,113,347,625,677,344],[278,514,676,636,465,578],[178,787],[695,433,580,727,127],[640,804,50,681],[571,733,828,284],[9,207,413,764],[19],[674,570,81,762],[285,430],[503,968,866],[372,110],[263,602,902],[65,359,527],[72,252,738],[492,235,685],[847,236,369,680,718],[390],[402,660],[199,382,265,504,561],[204,260],[666],[464,875],[482],[97,566,607,12],[939,695,769,34,499],[489],[10,576,989,267,980],[383],[113],[339],[],[150,289,535,436,824,855],[944,553],[896,175,931,909],[14],[232,721,935],[301,168,205,521],[184,430,431,793],[445],[471,753,957],[86,138,474,789,475],[941],[19,355,827,458,632],[],[246,523,101,318,423],[26,928,678,544],[939],[604,892,893],[354,992,569],[201],[95,242,135],[274,711,539,921,951],[33,349,29],[728,900,517,173],[95,210,863,972],[587,610],[516,668,579,248,268,888],[315,850,984,570,672],[106],[735,368],[816],[271,672],[230,564,766,813,894,525,529],[670,746,534,582],[971,127,595,627,904],[38,384],[417,423,714],[500,550,628],[448,547,575],[232,243,281,704,100,234,281,351],[900],[937,361],[122,366],[174,529],[209,465,342],[143,532,6,159],[147,569,592,740,906,946],[720],[861,314,605,194,665,876],[69,462],[169],[],[65,389,906,46,279,288],[435,704,819,15,96,711],[420,444,756,830,427,443,932],[415,671,930,928],[589,626,709,84,712],[22,387,788,260,461],[535,265,607],[66,650,783],[96,199,409,782],[781,147,976,324,424],[294,262,504,452,811,858],[21,206,449,682,934],[811,213,859],[627,69,425,656],[99,163,221,352,951],[630,663,71,669,374,962],[567],[297,693,853,965],[115,404,685,164],[802,826],[346,221,687],[505],[853,25,711,955],[638],[441,199],[864],[926,282],[83,188,307,617],[824,254],[237,371],[119,502],[698,516,805],[347,778],[32],[218,971],[],[155,374,202],[885,911,190,216,418,549,987],[543,803,639],[766,39],[91,334,442,534],[190,731,848,441],[836],[548,312],[884,915,770,501],[334,988],[451],[47,640],[524],[537,726],[702,68],[49,59],[835],[78,125,363,692,857],[981],[],[439,636,473,917],[125],[7,624],[859],[772,445],[890,955,87,933],[378,568,60],[814],[70,842,238,292,401,623,616],[136],[117,429],[683,979,509,556],[134,211],[278,977,129],[241,306,385,429,495],[337,782,669],[395,526,483,542],[330],[517,372,130],[],[439],[848,850,958,591],[108,177,820,821],[121,942],[220,276,367,101,370,451,751],[361,62,418,959],[23,573,63,440,776,602],[547,615,174,535,800],[929,47],[776,200],[335,549,225,562,603,676],[80,329,653,876],[135,879,724,947],[81,243,924,960,333],[197,390,756,488],[925,227,746],[115,633],[498,75],[450,662,721],[235,65,995],[56,77,263,565],[298,613,849],[389,710,492],[89,492,904,991,353,694,834,381],[945,56],[866,248,299,601],[598,774,62,233],[52,837],[659,27,716,593,753],[386,624,852,304],[],[926],[17],[277,216,903],[633,767,250,360],[414,913,172],[191],[303,399],[37,129,838,429],[233,368,466,249],[250,496,768,319],[308,348,543,751,611,835],[621,657,403],[342,678,910,846],[312,717],[788],[819],[227,325],[454,399,689,734],[512,980,139,446,482,713],[895,989,443,206,935],[256,705],[533,605],[415,749,985,897],[],[898,955],[625,454],[686,4,490,44,63,364,745],[789,436,829],[295],[393],[106,891,978],[205,559,840,984,4],[92,383,582],[416,508,545],[420,677,869],[385,700,483,82],[986,974],[84,297,734,752],[126,785],[248,330,723,756],[455],[24,810,112,954,10],[8,289,651,813,855,257],[958],[175,901,950,727],[40,151,703,990],[554,844,52,630],[109,203,985,354,723,931],[838],[852,237,405,444,765,994,53,234,309],[530,987,112,322],[],[294,760],[75,800],[328,488,331],[771,839],[440,643,742,779],[889,579],[16,25,77,726,947,52,663,970],[963],[747,300],[187,732],[179,16,692],[228,898,937],[],[90,109],[259,273,397,713,104,912],[555,640,804,258],[292,353,230,909]]
    print(s.canVisitAllRooms(rooms=rooms))