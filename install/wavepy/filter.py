#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#       filter.py
#       
#       Copyright 2011 Rafat Hussain
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
# 

import sys
from math import sqrt

def filtcoef(name):
	lp1=[]
	hp1=[]
	lp2=[]
	hp2=[]
	if name == "db1":
		lp1=[1.0/sqrt(2),1.0/sqrt(2)]
		hp1=[-1.0/sqrt(2),1.0/sqrt(2)]
		lp2=[1.0/sqrt(2),1.0/sqrt(2)]
		hp2=[1.0/sqrt(2),-1.0/sqrt(2)]
	elif name =="db2":
		lp1=[-0.12940952255092145,0.22414386804185735,0.83651630373746899,0.48296291314469025]
		hp1=[-0.48296291314469025,0.83651630373746899,-0.22414386804185735,-0.12940952255092145]
		lp2=[0.48296291314469025,0.83651630373746899,0.22414386804185735,-0.12940952255092145]
		hp2=[-0.12940952255092145,-0.22414386804185735,0.83651630373746899,-0.48296291314469025]
	elif name == "db3":
		lp1=[0.035226291882100656, -0.085441273882241486, -0.13501102001039084,
						0.45987750211933132, 0.80689150931333875, 0.33267055295095688]
		hp1=[-0.33267055295095688, 0.80689150931333875, -0.45987750211933132,
						-0.13501102001039084, 0.085441273882241486, 0.035226291882100656]
		lp2=[0.33267055295095688, 0.80689150931333875, 0.45987750211933132,
						-0.13501102001039084, -0.085441273882241486, 0.035226291882100656]
		hp2=[0.035226291882100656, 0.085441273882241486, -0.13501102001039084,
						-0.45987750211933132, 0.80689150931333875, -0.33267055295095688]
	elif name == "db4":
		lp1=[-0.010597401784997278, 0.032883011666982945, 0.030841381835986965, 
		-0.18703481171888114, -0.027983769416983849, 0.63088076792959036,
		0.71484657055254153, 0.23037781330885523]
		hp1=[-0.23037781330885523, 0.71484657055254153, -0.63088076792959036,
						-0.027983769416983849, 0.18703481171888114, 0.030841381835986965,
						-0.032883011666982945, -0.010597401784997278]
		lp2=[0.23037781330885523, 0.71484657055254153, 0.63088076792959036,
						-0.027983769416983849, -0.18703481171888114, 0.030841381835986965,
						0.032883011666982945, -0.010597401784997278]
		hp2=[-0.010597401784997278, -0.032883011666982945, 0.030841381835986965,
						0.18703481171888114, -0.027983769416983849, -0.63088076792959036,
						0.71484657055254153, -0.23037781330885523]   
	elif name == "db5":
		lp1=[0.0033357252850015492, -0.012580751999015526, -0.0062414902130117052,
						0.077571493840065148, -0.03224486958502952, -0.24229488706619015,
						0.13842814590110342, 0.72430852843857441, 0.60382926979747287,
				0.16010239797412501]
		hp1=[-0.16010239797412501, 0.60382926979747287, -0.72430852843857441,
						0.13842814590110342, 0.24229488706619015, -0.03224486958502952,
						-0.077571493840065148, -0.0062414902130117052, 0.012580751999015526,
						0.0033357252850015492]
		lp2=[0.16010239797412501, 0.60382926979747287, 0.72430852843857441,
						0.13842814590110342, -0.24229488706619015, -0.03224486958502952,
						0.077571493840065148, -0.0062414902130117052, -0.012580751999015526,
						0.0033357252850015492 ]
		hp2=[0.0033357252850015492, 0.012580751999015526, -0.0062414902130117052,
						-0.077571493840065148, -0.03224486958502952, 0.24229488706619015,
						0.13842814590110342, -0.72430852843857441, 0.60382926979747287,
						-0.16010239797412501]      
	elif name == "db6":
		lp1=[-0.0010773010849955799, 0.0047772575110106514,0.0005538422009938016,
						-0.031582039318031156,0.027522865530016288,0.097501605587079362,
						-0.12976686756709563,-0.22626469396516913,0.3152503517092432,
						0.75113390802157753,0.49462389039838539,0.11154074335008017]
		hp1=[-0.11154074335008017,0.49462389039838539,-0.75113390802157753,
						0.3152503517092432,0.22626469396516913,-0.12976686756709563,
						-0.097501605587079362,0.027522865530016288,0.031582039318031156,
						0.0005538422009938016,-0.0047772575110106514,-0.0010773010849955799]
		lp2=[0.11154074335008017,0.49462389039838539,0.75113390802157753,
						0.3152503517092432,-0.22626469396516913,-0.12976686756709563,
						0.097501605587079362,0.027522865530016288,-0.031582039318031156,
						0.0005538422009938016,0.0047772575110106514,-0.0010773010849955799]
		hp2=[-0.0010773010849955799, -0.0047772575110106514,0.0005538422009938016,
						0.031582039318031156, 0.027522865530016288, -0.097501605587079362,
						-0.12976686756709563,0.22626469396516913,0.3152503517092432,
						-0.75113390802157753,0.49462389039838539,-0.11154074335008017]
	elif name == "db7":
		lp1=[0.00035371380000103988,-0.0018016407039998328,0.00042957797300470274,
				0.012550998556013784,-0.01657454163101562,-0.038029936935034633,
				0.080612609151065898,0.071309219267050042,-0.22403618499416572,
				-0.14390600392910627,0.4697822874053586,0.72913209084655506,
				0.39653931948230575,0.077852054085062364]
		hp1=[-0.077852054085062364,0.39653931948230575,-0.72913209084655506,
				0.4697822874053586,0.14390600392910627,-0.22403618499416572,
				-0.071309219267050042,0.080612609151065898,0.038029936935034633,
				-0.01657454163101562,-0.012550998556013784,0.00042957797300470274,
				0.0018016407039998328,0.00035371380000103988]
		lp2=[0.077852054085062364,0.39653931948230575,0.72913209084655506,
				0.4697822874053586,-0.14390600392910627,-0.22403618499416572,
				0.071309219267050042,0.080612609151065898,-0.038029936935034633,
				-0.01657454163101562,0.012550998556013784,0.00042957797300470274,
				-0.0018016407039998328,0.00035371380000103988]
		hp2=[0.00035371380000103988,0.0018016407039998328,0.00042957797300470274,
				-0.012550998556013784,-0.01657454163101562,0.038029936935034633,
				0.080612609151065898,-0.071309219267050042,-0.22403618499416572,
				0.14390600392910627,0.4697822874053586,-0.72913209084655506,
				0.39653931948230575,-0.077852054085062364]
	elif name == "db8":
		lp1=[-0.00011747678400228192,0.00067544940599855677,-0.00039174037299597711,
				-0.0048703529930106603,0.0087460940470156547,0.013981027917015516,
				-0.044088253931064719,-0.017369301002022108,0.12874742662018601,
				0.00047248457399797254,-0.28401554296242809,-0.015829105256023893,
				0.58535468365486909,0.67563073629801285,0.31287159091446592,
				0.054415842243081609]
		hp1=[-0.054415842243081609,0.31287159091446592,-0.67563073629801285,
				0.58535468365486909,0.015829105256023893,-0.28401554296242809,
				-0.00047248457399797254,0.12874742662018601,0.017369301002022108,
				-0.044088253931064719,-0.013981027917015516,0.0087460940470156547,
				0.0048703529930106603,-0.00039174037299597711,-0.00067544940599855677,
				-0.00011747678400228192]
		lp2=[0.054415842243081609,0.31287159091446592,0.67563073629801285,
				0.58535468365486909,-0.015829105256023893,-0.28401554296242809,
				0.00047248457399797254,0.12874742662018601,-0.017369301002022108,
				-0.044088253931064719,0.013981027917015516,0.0087460940470156547,
				-0.0048703529930106603,-0.00039174037299597711,0.00067544940599855677,
				-0.00011747678400228192]
		hp2=[-0.00011747678400228192,-0.00067544940599855677,-0.00039174037299597711,
				0.0048703529930106603,0.0087460940470156547,-0.013981027917015516,
				-0.044088253931064719,0.017369301002022108,0.12874742662018601,
				-0.00047248457399797254,-0.28401554296242809,0.015829105256023893,
				0.58535468365486909,-0.67563073629801285,0.31287159091446592,
				-0.054415842243081609]
	elif name =="db9":
		lp1=[3.9347319995026124e-05,-0.00025196318899817888,0.00023038576399541288,
				0.0018476468829611268,-0.0042815036819047227,-0.004723204757894831,
				0.022361662123515244,0.00025094711499193845,-0.067632829059523988,
				0.030725681478322865,0.14854074933476008,-0.096840783220879037,
				-0.29327378327258685,0.13319738582208895,0.65728807803663891,
				0.6048231236767786,0.24383467463766728,0.038077947363167282]
		hp1=[-0.038077947363167282,0.24383467463766728,-0.6048231236767786,
				0.65728807803663891,-0.13319738582208895,-0.29327378327258685,
				0.096840783220879037,0.14854074933476008,-0.030725681478322865,
				-0.067632829059523988,-0.00025094711499193845,0.022361662123515244,
				0.004723204757894831,-0.0042815036819047227,-0.0018476468829611268,
				0.00023038576399541288,0.00025196318899817888,3.9347319995026124e-05]
		lp2=[0.038077947363167282,0.24383467463766728,0.6048231236767786,
				0.65728807803663891,0.13319738582208895,-0.29327378327258685,
				-0.096840783220879037,0.14854074933476008,0.030725681478322865,
				-0.067632829059523988,0.00025094711499193845,0.022361662123515244,
				-0.004723204757894831,-0.0042815036819047227,0.0018476468829611268,
				0.00023038576399541288,-0.00025196318899817888,3.9347319995026124e-05]
		hp2=[3.9347319995026124e-05,0.00025196318899817888,0.00023038576399541288,
				-0.0018476468829611268,-0.0042815036819047227,0.004723204757894831,
				0.022361662123515244,-0.00025094711499193845,-0.067632829059523988,
				-0.030725681478322865,0.14854074933476008,0.096840783220879037,
				-0.29327378327258685,-0.13319738582208895,0.65728807803663891,
				-0.6048231236767786,0.24383467463766728,-0.038077947363167282]
	elif name == "db10":
		lp1=[-1.3264203002354869e-05,9.3588670001089845e-05,-0.0001164668549943862,
				-0.00068585669500468248,0.0019924052949908499,0.0013953517469940798,
				-0.010733175482979604,0.0036065535669883944,0.033212674058933238,
				-0.029457536821945671,-0.071394147165860775,0.093057364603806592,
				0.12736934033574265,-0.19594627437659665,-0.24984642432648865,
				0.28117234366042648,0.68845903945259213,0.52720118893091983,
				0.18817680007762133,0.026670057900950818]
		hp1=[-0.026670057900950818,0.18817680007762133,-0.52720118893091983,
				0.68845903945259213,-0.28117234366042648,-0.24984642432648865,
				0.19594627437659665,0.12736934033574265,-0.093057364603806592,
				-0.071394147165860775,0.029457536821945671,0.033212674058933238,
				-0.0036065535669883944,-0.010733175482979604,-0.0013953517469940798,
				0.0019924052949908499,0.00068585669500468248,-0.0001164668549943862,
				-9.3588670001089845e-05,-1.3264203002354869e-05]
		lp2=[0.026670057900950818,0.18817680007762133,0.52720118893091983,
				0.68845903945259213,0.28117234366042648,-0.24984642432648865,
				-0.19594627437659665,0.12736934033574265,0.093057364603806592,
				-0.071394147165860775,-0.029457536821945671,0.033212674058933238,
				0.0036065535669883944,-0.010733175482979604,0.0013953517469940798,
				0.0019924052949908499,-0.00068585669500468248,-0.0001164668549943862,
				9.3588670001089845e-05,-1.3264203002354869e-05]
		hp2=[-1.3264203002354869e-05,-9.3588670001089845e-05,-0.0001164668549943862,
				0.00068585669500468248,0.0019924052949908499,-0.0013953517469940798,
				-0.010733175482979604,-0.0036065535669883944,0.033212674058933238,
				0.029457536821945671,-0.071394147165860775,-0.093057364603806592,
				0.12736934033574265,0.19594627437659665,-0.24984642432648865,
				-0.28117234366042648,0.68845903945259213,-0.52720118893091983,
				0.18817680007762133,-0.026670057900950818]
	elif name == "db11":
		lp1=[4.4942742772363519e-06,-3.4634984186983789e-05,5.4439074699366381e-05,
				0.00024915252355281426,-0.00089302325066623663,-0.00030859285881515924,
				0.0049284176560587777,-0.0033408588730145018,-0.015364820906201324,
				0.020840904360180039,0.031335090219045313,-0.066438785695020222,
				-0.04647995511667613,0.14981201246638268,0.066043588196690886,
				-0.27423084681792875,-0.16227524502747828,0.41196436894789695,
				0.68568677491617847,0.44989976435603013,0.14406702115061959,
				0.018694297761470441]
		hp1=[-0.018694297761470441,0.14406702115061959,-0.44989976435603013,
				0.68568677491617847,-0.41196436894789695,-0.16227524502747828,
				0.27423084681792875,0.066043588196690886,-0.14981201246638268,
				-0.04647995511667613,0.066438785695020222,0.031335090219045313,
				-0.020840904360180039,-0.015364820906201324,0.0033408588730145018,
				0.0049284176560587777,0.00030859285881515924,-0.00089302325066623663,
				-0.00024915252355281426,5.4439074699366381e-05,3.4634984186983789e-05,
				4.4942742772363519e-06]
		lp2=[0.018694297761470441,0.14406702115061959,0.44989976435603013,
				0.68568677491617847,0.41196436894789695,-0.16227524502747828,
				-0.27423084681792875,0.066043588196690886,0.14981201246638268,
				-0.04647995511667613,-0.066438785695020222,0.031335090219045313,
				0.020840904360180039,-0.015364820906201324,-0.0033408588730145018,
				0.0049284176560587777,-0.00030859285881515924,-0.00089302325066623663,
				0.00024915252355281426,5.4439074699366381e-05,-3.4634984186983789e-05,
				4.4942742772363519e-06]
		hp2=[4.4942742772363519e-06,3.4634984186983789e-05,5.4439074699366381e-05,
				-0.00024915252355281426,-0.00089302325066623663,0.00030859285881515924,
				0.0049284176560587777,0.0033408588730145018,-0.015364820906201324,
				-0.020840904360180039,0.031335090219045313,0.066438785695020222,
				-0.04647995511667613,-0.14981201246638268,0.066043588196690886,
				0.27423084681792875,-0.16227524502747828,-0.41196436894789695,
				0.68568677491617847,-0.44989976435603013,0.14406702115061959,
				-0.018694297761470441]
	elif name == "db12":
		lp1=[-1.5290717580684923e-06,1.2776952219379579e-05,-2.4241545757030318e-05,
				-8.8504109208203182e-05,0.00038865306282092672,6.5451282125215034e-06,
				-0.0021795036186277044,0.0022486072409952287,0.0067114990087955486,
				-0.012840825198299882,-0.01221864906974642,0.041546277495087637,
				0.010849130255828966,-0.09643212009649671,0.0053595696743599965,
				0.18247860592758275,-0.023779257256064865,-0.31617845375277914,
				-0.044763885653777619,0.51588647842780067,0.65719872257929113,
				0.37735513521420411,0.10956627282118277,0.013112257957229239]
		hp1=[-0.013112257957229239,0.10956627282118277,-0.37735513521420411,
				0.65719872257929113,-0.51588647842780067,-0.044763885653777619,
				0.31617845375277914,-0.023779257256064865,-0.18247860592758275,
				0.0053595696743599965,0.09643212009649671,0.010849130255828966,
				-0.041546277495087637,-0.01221864906974642,0.012840825198299882,
				0.0067114990087955486,-0.0022486072409952287,-0.0021795036186277044,
				-6.5451282125215034e-06,0.00038865306282092672,8.8504109208203182e-05,
				-2.4241545757030318e-05,-1.2776952219379579e-05,-1.5290717580684923e-06]
		lp2=[0.013112257957229239,0.10956627282118277,0.37735513521420411,
				0.65719872257929113,0.51588647842780067,-0.044763885653777619,
				-0.31617845375277914,-0.023779257256064865,0.18247860592758275,
				0.0053595696743599965,-0.09643212009649671,0.010849130255828966,
				0.041546277495087637,-0.01221864906974642,-0.012840825198299882,
				0.0067114990087955486,0.0022486072409952287,-0.0021795036186277044,
				6.5451282125215034e-06,0.00038865306282092672,-8.8504109208203182e-05,
				-2.4241545757030318e-05,1.2776952219379579e-05,-1.5290717580684923e-06]
		hp2=[-1.5290717580684923e-06,-1.2776952219379579e-05,-2.4241545757030318e-05,
				8.8504109208203182e-05,0.00038865306282092672,-6.5451282125215034e-06,
				-0.0021795036186277044,-0.0022486072409952287,0.0067114990087955486,
				0.012840825198299882,-0.01221864906974642,-0.041546277495087637,
				0.010849130255828966,0.09643212009649671,0.0053595696743599965,
				-0.18247860592758275,-0.023779257256064865,0.31617845375277914,
				-0.044763885653777619,-0.51588647842780067,0.65719872257929113,
				-0.37735513521420411,0.10956627282118277,-0.013112257957229239]
	elif name == "db13":
		lp1=[5.2200350984547998e-07,-4.7004164793608082e-06,1.0441930571407941e-05,
				3.0678537579324358e-05,-0.00016512898855650571,4.9251525126285676e-05,
				0.00093232613086724904,-0.0013156739118922766,-0.002761911234656831,
				0.0072555894016171187,0.0039239414487955773,-0.023831420710327809,
				0.0023799722540522269,0.056139477100276156,-0.026488406475345658,
				-0.10580761818792761,0.072948933656788742,0.17947607942935084,
				-0.12457673075080665,-0.31497290771138414,0.086985726179645007,
				0.58888957043121193,0.61105585115878114,0.31199632216043488,
				0.082861243872901946,0.0092021335389622788]
		hp1=[-0.0092021335389622788,0.082861243872901946,-0.31199632216043488,
				0.61105585115878114,-0.58888957043121193,0.086985726179645007,
				0.31497290771138414,-0.12457673075080665,-0.17947607942935084,
				0.072948933656788742,0.10580761818792761,-0.026488406475345658,
				-0.056139477100276156,0.0023799722540522269,0.023831420710327809,
				0.0039239414487955773,-0.0072555894016171187,-0.002761911234656831,
				0.0013156739118922766,0.00093232613086724904,-4.9251525126285676e-05,
				-0.00016512898855650571,-3.0678537579324358e-05,1.0441930571407941e-05,
				4.7004164793608082e-06,5.2200350984547998e-07]
		lp2=[0.0092021335389622788,0.08286124387290194,0.31199632216043488,
				0.61105585115878114,0.58888957043121193,0.086985726179645007,
				-0.31497290771138414,-0.12457673075080665,0.17947607942935084,
				0.072948933656788742,-0.10580761818792761,-0.026488406475345658,
				0.056139477100276156,0.0023799722540522269,-0.023831420710327809,
				0.0039239414487955773,0.0072555894016171187,-0.002761911234656831,
				-0.0013156739118922766,0.00093232613086724904,4.9251525126285676e-05,
				-0.00016512898855650571,3.0678537579324358e-05,1.0441930571407941e-05,
				-4.7004164793608082e-06,5.2200350984547998e-07]
		hp2=[5.2200350984547998e-07,4.7004164793608082e-06,1.0441930571407941e-05,
				-3.0678537579324358e-05,-0.00016512898855650571,-4.9251525126285676e-05,
				0.00093232613086724904,0.0013156739118922766,-0.002761911234656831,
				-0.0072555894016171187,0.0039239414487955773,0.023831420710327809,
				0.0023799722540522269,-0.056139477100276156,-0.026488406475345658,
				0.10580761818792761,0.072948933656788742,-0.17947607942935084,-0.12457673075080665,
				0.31497290771138414,0.086985726179645007,-0.58888957043121193,0.61105585115878114,
				-0.31199632216043488,0.082861243872901946,-0.0092021335389622788]
	elif name == "db14":
		lp1=[-1.7871399683109222e-07,1.7249946753674012e-06,-4.3897049017804176e-06,
				-1.0337209184568496e-05,6.875504252695734e-05,-4.1777245770370672e-05,
				-0.00038683194731287514,0.00070802115423540481,0.001061691085606874,
				-0.003849638868019787,-0.00074621898926387534,0.012789493266340071,
				-0.0056150495303375755,-0.030185351540353976,0.026981408307947971,
				0.05523712625925082,-0.071548955503983505,-0.086748411568110598,
				0.13998901658445695,0.13839521386479153,-0.21803352999321651,
				-0.27168855227867705,0.21867068775886594,0.63118784910471981,
				0.55430561794077093,0.25485026779256437,0.062364758849384874,
				0.0064611534600864905]
		hp1=[-0.0064611534600864905,0.062364758849384874,-0.25485026779256437,
				0.55430561794077093,-0.63118784910471981,0.21867068775886594,
				0.27168855227867705,-0.21803352999321651,-0.13839521386479153,
				0.13998901658445695,0.086748411568110598,-0.071548955503983505,
				-0.05523712625925082,0.026981408307947971,0.030185351540353976,
				-0.0056150495303375755,-0.012789493266340071,-0.00074621898926387534,
				0.003849638868019787,0.001061691085606874,-0.00070802115423540481,
				-0.00038683194731287514,4.1777245770370672e-05,6.875504252695734e-05,
				1.0337209184568496e-05,-4.3897049017804176e-06,-1.7249946753674012e-06,
				-1.7871399683109222e-07]
		lp2=[0.0064611534600864905,0.062364758849384874,0.25485026779256437,
				0.55430561794077093,0.63118784910471981,0.21867068775886594,
				-0.27168855227867705,-0.21803352999321651,0.13839521386479153,
				0.13998901658445695,-0.086748411568110598,-0.071548955503983505,
				0.05523712625925082,0.026981408307947971,-0.030185351540353976,
				-0.0056150495303375755,0.012789493266340071,-0.00074621898926387534,
				-0.003849638868019787,0.001061691085606874,0.00070802115423540481,
				-0.00038683194731287514,-4.1777245770370672e-05,6.875504252695734e-05,
				-1.0337209184568496e-05,-4.3897049017804176e-06,1.7249946753674012e-06,
				-1.7871399683109222e-07]
		hp2=[-1.7871399683109222e-07,-1.7249946753674012e-06,-4.3897049017804176e-06,
				1.0337209184568496e-05,6.875504252695734e-05,4.1777245770370672e-05,
				-0.00038683194731287514,-0.00070802115423540481,0.001061691085606874,
				0.003849638868019787,-0.00074621898926387534,-0.012789493266340071,
				-0.0056150495303375755,0.030185351540353976,0.026981408307947971,
				-0.05523712625925082,-0.071548955503983505,0.086748411568110598,
				0.13998901658445695,-0.13839521386479153,-0.21803352999321651,
				0.27168855227867705,0.21867068775886594,-0.63118784910471981,
				0.55430561794077093,-0.25485026779256437,0.062364758849384874,
				-0.0064611534600864905]
	elif name =="db15":
		lp1=[6.1333599133037138e-08,-6.3168823258794506e-07,1.8112704079399406e-06,
				3.3629871817363823e-06,-2.8133296266037558e-05,2.579269915531323e-05,
				0.00015589648992055726,-0.00035956524436229364,-0.00037348235413726472,
				0.0019433239803823459,-0.00024175649075894543,-0.0064877345603061454,
				0.0051010003604228726,0.015083918027862582,-0.020810050169636805,
				-0.025767007328366939,0.054780550584559995,0.033877143923563204,
				-0.11112093603713753,-0.039666176555733602,0.19014671400708816,
				0.065282952848765688,-0.28888259656686216,-0.19320413960907623,
				0.33900253545462167,0.64581314035721027,0.49263177170797529,
				0.20602386398692688,0.046743394892750617,0.0045385373615773762]
		hp1=[-0.0045385373615773762,0.046743394892750617,-0.20602386398692688,
				0.49263177170797529,-0.64581314035721027,0.33900253545462167,
				0.19320413960907623,-0.28888259656686216,-0.065282952848765688,
				0.19014671400708816,0.039666176555733602,-0.11112093603713753,
				-0.033877143923563204,0.054780550584559995,0.025767007328366939,
				-0.020810050169636805,-0.015083918027862582,0.0051010003604228726,
				0.0064877345603061454,-0.00024175649075894543,-0.0019433239803823459,
				-0.00037348235413726472,0.00035956524436229364,0.00015589648992055726,
				-2.579269915531323e-05,-2.8133296266037558e-05,-3.3629871817363823e-06,
				1.8112704079399406e-06,6.3168823258794506e-07,6.1333599133037138e-08]
		lp2=[0.0045385373615773762,0.046743394892750617,0.20602386398692688,
				0.49263177170797529,0.64581314035721027,0.33900253545462167,
				-0.19320413960907623,-0.28888259656686216,0.065282952848765688,
				0.19014671400708816,-0.039666176555733602,-0.11112093603713753,
				0.033877143923563204,0.054780550584559995,-0.025767007328366939,
				-0.020810050169636805,0.015083918027862582,0.0051010003604228726,
				-0.0064877345603061454,-0.00024175649075894543,0.0019433239803823459,
				-0.00037348235413726472,-0.00035956524436229364,0.00015589648992055726,
				2.579269915531323e-05,-2.8133296266037558e-05,3.3629871817363823e-06,
				1.8112704079399406e-06,-6.3168823258794506e-07,6.1333599133037138e-08]
		hp2=[6.1333599133037138e-08,6.3168823258794506e-07,1.8112704079399406e-06,
				-3.3629871817363823e-06,-2.8133296266037558e-05,-2.579269915531323e-05,
				0.00015589648992055726,0.00035956524436229364,-0.00037348235413726472,
				-0.0019433239803823459,-0.00024175649075894543,0.0064877345603061454,
				0.0051010003604228726,-0.015083918027862582,-0.020810050169636805,
				0.025767007328366939,0.054780550584559995,-0.033877143923563204,
				-0.11112093603713753,0.039666176555733602,0.19014671400708816,
				-0.065282952848765688,-0.28888259656686216,0.19320413960907623,
				0.33900253545462167,-0.64581314035721027,0.49263177170797529,
				-0.20602386398692688,0.046743394892750617,-0.0045385373615773762]
	elif name=="bior1.1":
		lp1=[0.70710678118654757,0.70710678118654757]
		hp1=[-0.70710678118654757,0.70710678118654757]
		lp2=[0.70710678118654757,0.70710678118654757]
		hp2=[0.70710678118654757,-0.70710678118654757]
	elif name=="bior1.3":
		lp1=[-0.088388347648318447,0.088388347648318447,0.70710678118654757,
		0.70710678118654757,0.088388347648318447,-0.088388347648318447]
		hp1=[0.0,0.0,-0.70710678118654757,0.70710678118654757,0.0,0.0]
		lp2=[0.0,0.0,0.70710678118654757,0.70710678118654757,0.0,0.0]
		hp2=[-0.088388347648318447,-0.088388347648318447,0.70710678118654757,
		-0.70710678118654757,0.088388347648318447,0.088388347648318447]
	elif name=="bior1.5":
		lp1=[0.01657281518405971,-0.01657281518405971,-0.12153397801643787,
				0.12153397801643787,0.70710678118654757,0.70710678118654757,
				0.12153397801643787,-0.12153397801643787,-0.01657281518405971,
				0.01657281518405971]
		hp1=[0.0,0.0,0.0,0.0,-0.70710678118654757,0.70710678118654757,0.0,0.0,0.0,0.0]
		lp2=[0.0,0.0,0.0,0.0,0.70710678118654757,0.70710678118654757,0.0,0.0,0.0,0.0]
		hp2=[0.01657281518405971,0.01657281518405971,-0.12153397801643787,
				-0.12153397801643787,0.70710678118654757,-0.70710678118654757,
				0.12153397801643787,0.12153397801643787,-0.01657281518405971,
				-0.01657281518405971]
	elif name=="bior2.2":
		lp1=[0,-0.176777,0.353553,1.06066,0.353553,-0.176777]
		hp1=[0,0.353553,-0.707107,0.353553,0,0]
		lp2=[0,0.353553,0.707107,0.353553,0,0]
		hp2=[0,0.176777,0.353553,-1.06066,0.353553,0.176777]
	elif name=="bior2.4":
		lp1=[0,0.0331456,-0.0662913,-0.176777,0.419845,0.994369,
		0.419845,-0.176777,-0.0662913,0.0331456]
		hp1=[0,0,0,0.353553,-0.707107,0.353553,0,0,0,0]
		lp2=[0,0,0,0.353553,0.707107,0.353553,0,0,0,0]
		hp2=[0,-0.0331456,-0.0662913,0.176777,0.419845,-0.994369,
		0.419845,0.176777,-0.0662913,-0.0331456]
	elif name=="bior2.6":
		lp1=[0,-0.00690534,0.0138107,0.0469563,-0.107723,-0.169871,
		0.447466,0.966748,0.447466,-0.169871,-0.107723,0.0469563,
		0.0138107,-0.00690534]
		hp1=[0,0,0,0,0,0.353553,-0.707107,0.353553,0,0,0,0,0,0]
		lp2=[0,0,0,0,0,0.353553,0.707107,0.353553,0,0,0,0,0,0]
		hp2=[0,0.00690534,0.0138107,-0.0469563,-0.107723,0.169871,
		0.447466,-0.966748,0.447466,0.169871,-0.107723,-0.0469563,
		0.0138107,0.00690534]
	elif name=="bior2.8":
		lp1=[0,0.00151054,-0.00302109,-0.0129475,0.0289161,0.0529985,
		-0.134913,-0.163829,0.462571,0.951642,0.462571,-0.163829,
		-0.134913,0.0529985,0.0289161,-0.0129475,-0.00302109,0.00151054]
		hp1=[0,0,0,0,0,0,0,0.353553,-0.707107,0.353553,0,0,0,0,0,0,0,0]
		lp2=[0,0,0,0,0,0,0,0.353553,0.707107,0.353553,0,0,0,0,0,0,0,0]
		hp2=[0,-0.00151054,-0.00302109,0.0129475,0.0289161,-0.0529985,
		-0.134913,0.163829,0.462571,-0.951642,0.462571,0.163829,
		-0.134913,-0.0529985,0.0289161,0.0129475,-0.00302109,-0.00151054]
	elif name=="bior3.1":
		lp1=[-0.353553,1.06066,1.06066,-0.353553]
		hp1=[-0.176777,0.53033,-0.53033,0.176777]
		lp2=[0.176777,0.53033,0.53033,0.176777]
		hp2=[-0.353553,-1.06066,1.06066,0.353553]
	elif name=="bior3.3":
		lp1=[0.0662913,-0.198874,-0.15468,0.994369,0.994369,-0.15468,
		-0.198874,0.0662913]
		hp1=[0,0,-0.176777,0.53033,-0.53033,0.176777,0,0]
		lp2=[0,0,0.176777,0.53033,0.53033,0.176777,0,0]
		hp2=[0.0662913,0.198874,-0.15468,-0.994369,0.994369,0.15468,
		-0.198874,-0.0662913]
	elif name=="bior3.5":
		lp1=[-0.0138107,0.041432,0.0524806,-0.267927,-0.0718155,
		0.966748,0.966748,-0.0718155,-0.267927,0.0524806,0.041432,
		-0.0138107]
		hp1=[0,0,0,0,-0.176777,0.53033,-0.53033,0.176777,0,0,0,0]
		lp2=[0,0,0,0,0.176777,0.53033,0.53033,0.176777,0,0,0,0]
		hp2=[-0.0138107,-0.041432,0.0524806,0.267927,-0.0718155,
		-0.966748,0.966748,0.0718155,-0.267927,-0.0524806,0.041432,
		0.0138107]
	elif name=="bior3.7":
		lp1=[0.00302109,-0.00906326,-0.0168318,0.074664,0.031333,
		-0.301159,-0.0264992,0.951642,0.951642,-0.0264992,-0.301159,
		0.031333,0.074664,-0.0168318,-0.00906326,0.00302109]
		hp1=[0,0,0,0,0,0,-0.176777,0.53033,-0.53033,0.176777,0,0,0,0,0,0]
		lp2=[0,0,0,0,0,0,0.176777,0.53033,0.53033,0.176777,0,0,0,0,0,0]
		hp2=[0.00302109,0.00906326,-0.0168318,-0.074664,0.031333,
		0.301159,-0.0264992,-0.951642,0.951642,0.0264992,-0.301159,
		-0.031333,0.074664,0.0168318,-0.00906326,-0.00302109]
	elif name=="bior3.9":
		lp1=[-0.000679744,0.00203923,0.00506032,-0.0206189,-0.0141128,
		0.0991348,0.0123001,-0.320192,0.00205002,0.942126,0.942126,
		0.00205002,-0.320192,0.0123001,0.0991348,-0.0141128,-0.0206189,
		0.00506032,0.00203923,-0.000679744]
		hp1=[0,0,0,0,0,0,0,0,-0.176777,0.53033,-0.53033,0.176777,0,0,
		0,0,0,0,0,0]
		lp2=[0,0,0,0,0,0,0,0,0.176777,0.53033,0.53033,0.176777,0,0,0,
		0,0,0,0,0]
		hp2=[-0.000679744,-0.00203923,0.00506032,0.0206189,-0.0141128,
		-0.0991348,0.0123001,0.320192,0.00205002,-0.942126,0.942126,
		-0.00205002,-0.320192,-0.0123001,0.0991348,0.0141128,-0.0206189,
		-0.00506032,0.00203923,0.000679744]
	elif name=="bior4.4":
		lp1=[0,0.0378285,-0.0238495,-0.110624,0.377403,0.852699,
		0.377403,-0.110624,-0.0238495,0.0378285]
		hp1=[0,-0.0645389,0.0406894,0.418092,-0.788486,
		0.418092,0.0406894,-0.0645389,0,0]
		lp2=[0,-0.0645389,-0.0406894,0.418092,0.788486,0.418092,
		-0.0406894,-0.0645389,0,0]
		hp2=[0,-0.0378285,-0.0238495,0.110624,0.377403,-0.852699,
		0.377403,0.110624,-0.0238495,-0.0378285]
	elif name=="bior5.5":
		lp1=[0,0,0.0396871,0.00794811,-0.0544638,0.345605,0.73666,
		0.345605,-0.0544638,0.00794811,0.0396871,0]
		hp1=[-0.0134567,-0.00269497,0.136707,-0.0935047,-0.476803,
		0.899506,-0.476803,-0.0935047,0.136707,-0.00269497,-0.0134567,0]
		lp2=[0.0134567,-0.00269497,-0.136707,-0.0935047,0.476803,
		0.899506,0.476803,-0.0935047,-0.136707,-0.00269497,0.0134567,0]
		hp2=[0,0,0.0396871,-0.00794811,-0.0544638,-0.345605,
		0.73666,-0.345605,-0.0544638,-0.00794811,0.0396871,0]
	elif name=="bior6.8":
		lp1=[0,0.00190883,-0.00191429,-0.0169906,0.0119346,0.0497329,
		-0.0772632,-0.0940592,0.420796,0.825923,0.420796,-0.0940592,
		-0.0772632,0.0497329,0.0119346,-0.0169906,-0.00191429,0.00190883]
		hp1=[0,0,0,0.0144263,-0.0144675,-0.078722,0.040368,0.417849,
		-0.758908,0.417849,0.040368,-0.078722,-0.0144675,0.0144263,
		0,0,0,0]
		lp2=[0,0,0,0.0144263,0.0144675,-0.078722,-0.040368,
		0.417849,0.758908,0.417849,-0.040368,-0.078722,0.0144675,
		0.0144263,0,0,0,0]
		hp2=[0,-0.00190883,-0.00191429,0.0169906,0.0119346,-0.0497329,
		-0.0772632,0.0940592,0.420796,-0.825923,0.420796,
		0.0940592,-0.0772632,-0.0497329,0.0119346,0.0169906,
		-0.00191429,-0.00190883]
	elif name=="coif1":
		lp1=[-0.0156557,-0.0727326,0.384865,0.852572,0.337898,-0.0727326]
		hp1=[0.0727326,0.337898,-0.852572,0.384865,0.0727326,-0.0156557]
		lp2=[-0.0727326,0.337898,0.852572,0.384865,-0.0727326,-0.0156557]
		hp2=[-0.0156557,0.0727326,0.384865,-0.852572,0.337898,0.0727326]
	elif name=="coif2":
		lp1=[-0.000720549,-0.00182321,0.00561143,0.0236802,-0.0594344,
		-0.0764886,0.417005,0.812724,0.38611,-0.0673726,-0.0414649,
		0.0163873]
		hp1=[-0.0163873,-0.0414649,0.0673726,0.38611,-0.812724,
		0.417005,0.0764886,-0.0594344,-0.0236802,0.00561143,0.00182321,
		-0.000720549]
		lp2=[0.0163873,-0.0414649,-0.0673726,0.38611,0.812724,0.417005,
		-0.0764886,-0.0594344,0.0236802,0.00561143,-0.00182321,
		-0.000720549]
		hp2=[-0.000720549,0.00182321,0.00561143,-0.0236802,
		-0.0594344,0.0764886,0.417005,-0.812724,0.38611,0.0673726,
		-0.0414649,-0.0163873]
	elif name=="coif3":
		lp1=[-3.45998e-05,-7.09833e-05,0.000466217,0.00111752,
		-0.00257452,-0.00900798,0.0158805,0.034555,-0.0823019,
		-0.0717998,0.428483,0.793777,0.405177,-0.0611234,-0.0657719,
		0.0234527,0.0077826,-0.00379351]
		hp1=[0.00379351,0.0077826,-0.0234527,-0.0657719,0.0611234,
		0.405177,-0.793777,0.428483,0.0717998,-0.0823019,-0.034555,
		0.0158805,0.00900798,-0.00257452,-0.00111752,0.000466217,
		7.09833e-05,-3.45998e-05]
		lp2=[-0.00379351,0.0077826,0.0234527,-0.0657719,-0.0611234,
		0.405177,0.793777,0.428483,-0.0717998,-0.0823019,0.034555,
		0.0158805,-0.00900798,-0.00257452,0.00111752,0.000466217,
		-7.09833e-05,-3.45998e-05]
		hp2=[-3.45998e-05,7.09833e-05,0.000466217,-0.00111752,
		-0.00257452,0.00900798,0.0158805,-0.034555,-0.0823019,0.0717998,
		0.428483,-0.793777,0.405177,0.0611234,-0.0657719,-0.0234527,
		0.0077826,0.00379351]
	elif name=="coif4":
		lp1=[-1.78499e-06,-3.25968e-06,3.12299e-05,6.2339e-05,
		-0.000259975,-0.000589021,0.00126656,0.00375144,-0.00565829,
		-0.0152117,0.0250823,0.0393344,-0.0962204,-0.0666275,0.434386,
		0.782239,0.415308,-0.0560773,-0.0812667,0.0266823,0.0160689,
		-0.00734617,-0.00162949,0.000892314]
		hp1=[-0.000892314,-0.00162949,0.00734617,0.0160689,-0.0266823,
		-0.0812667,0.0560773,0.415308,-0.782239,0.434386,0.0666275,
		-0.0962204,-0.0393344,0.0250823,0.0152117,-0.00565829,
		-0.00375144,0.00126656,0.000589021,-0.000259975,-6.2339e-05,
		3.12299e-05,3.25968e-06,-1.78499e-06]
		lp2=[0.000892314,-0.00162949,-0.00734617,0.0160689,0.0266823,
		-0.0812667,-0.0560773,0.415308,0.782239,0.434386,-0.0666275,
		-0.0962204,0.0393344,0.0250823,-0.0152117,-0.00565829,
		0.00375144,0.00126656,-0.000589021,-0.000259975,6.2339e-05,
		3.12299e-05,-3.25968e-06,-1.78499e-06]
		hp2=[-1.78499e-06,3.25968e-06,3.12299e-05,-6.2339e-05,
		-0.000259975,0.000589021,0.00126656,-0.00375144,-0.00565829,
		0.0152117,0.0250823,-0.0393344,-0.0962204,0.0666275,0.434386,
		-0.782239,0.415308,0.0560773,-0.0812667,-0.0266823,0.0160689,
		0.00734617,-0.00162949,-0.000892314]
	elif name=="coif5":
		lp1=[-9.51766e-08,-1.67443e-07,2.06376e-06,3.73466e-06,
		-2.1315e-05,-4.13404e-05,0.000140541,0.00030226,-0.000638131,
		-0.00166286,0.00243337,0.00676419,-0.00916423,-0.0197618,
		0.0326836,0.0412892,-0.105574,-0.062036,0.437992,0.77429,
		0.421566,-0.0520432,-0.09192,0.028168,0.0234082,-0.0101311,
		-0.00415936,0.00217824,0.00035859,-0.000212081]
		hp1=[0.000212081,0.00035859,-0.00217824,-0.00415936,0.0101311,
		0.0234082,-0.028168,-0.09192,0.0520432,0.421566,-0.77429,
		0.437992,0.062036,-0.105574,-0.0412892,0.0326836,0.0197618,
		-0.00916423,-0.00676419,0.00243337,0.00166286,-0.000638131,
		-0.00030226,0.000140541,4.13404e-05,-2.1315e-05,-3.73466e-06,
		2.06376e-06,1.67443e-07,-9.51766e-08]
		lp2=[-0.000212081,0.00035859,0.00217824,-0.00415936,-0.0101311,
		0.0234082,0.028168,-0.09192,-0.0520432,0.421566,0.77429,0.437992,
		-0.062036,-0.105574,0.0412892,0.0326836,-0.0197618,-0.00916423,
		0.00676419,0.00243337,-0.00166286,-0.000638131,0.00030226,
		0.000140541,-4.13404e-05,-2.1315e-05,3.73466e-06,2.06376e-06,
		-1.67443e-07,-9.51766e-08]
		hp2=[-9.51766e-08,1.67443e-07,2.06376e-06,-3.73466e-06,
		-2.1315e-05,4.13404e-05,0.000140541,-0.00030226,-0.000638131,
		0.00166286,0.00243337,-0.00676419,-0.00916423,0.0197618,
		0.0326836,-0.0412892,-0.105574,0.062036,0.437992,-0.77429,
		0.421566,0.0520432,-0.09192,-0.028168,0.0234082,0.0101311,
		-0.00415936,-0.00217824,0.00035859,0.000212081]
	elif name=="sym2":
		lp1=[-0.12941,0.224144,0.836516,0.482963]
		hp1=[-0.482963,0.836516,-0.224144,-0.12941]
		lp2=[0.482963,0.836516,0.224144,-0.12941]
		hp2=[-0.12941,-0.224144,0.836516,-0.482963]
	elif name=="sym3":
		lp1=[0.0352263,-0.0854413,-0.135011,0.459878,0.806892,0.332671]
		hp1=[-0.332671,0.806892,-0.459878,-0.135011,0.0854413,0.0352263]
		lp2=[0.332671,0.806892,0.459878,-0.135011,-0.0854413,0.0352263]
		hp2=[0.0352263,0.0854413,-0.135011,-0.459878,0.806892,-0.332671]
	elif name=="sym4":
		lp1=[-0.0757657,-0.0296355,0.497619,0.803739,0.297858,
		-0.0992195,-0.012604,0.0322231]
		hp1=[-0.0322231,-0.012604,0.0992195,0.297858,-0.803739,
		0.497619,0.0296355,-0.0757657]
		lp2=[0.0322231,-0.012604,-0.0992195,0.297858,0.803739,
		0.497619,-0.0296355,-0.0757657]
		hp2=[-0.0757657,0.0296355,0.497619,-0.803739,0.297858,
		0.0992195,-0.012604,-0.0322231]
	elif name=="sym5":
		lp1=[0.0273331,0.0295195,-0.0391342,0.199398,0.723408,
		0.633979,0.0166021,-0.175328,-0.0211018,0.0195389]
		hp1=[-0.0195389,-0.0211018,0.175328,0.0166021,-0.633979,
		0.723408,-0.199398,-0.0391342,-0.0295195,0.0273331]
		lp2=[0.0195389,-0.0211018,-0.175328,0.0166021,0.633979,
		0.723408,0.199398,-0.0391342,0.0295195,0.0273331]
		hp2=[0.0273331,-0.0295195,-0.0391342,-0.199398,0.723408,
		-0.633979,0.0166021,0.175328,-0.0211018,-0.0195389]
	elif name=="sym6":
		lp1=[0.0154041,0.00349071,-0.11799,-0.0483117,0.491056,
		0.787641,0.337929,-0.0726375,-0.0210603,0.0447249,
		0.00176771,-0.00780071]
		hp1=[0.00780071,0.00176771,-0.0447249,-0.0210603,0.0726375,
		0.337929,-0.787641,0.491056,0.0483117,-0.11799,-0.00349071,
		0.0154041]
		lp2=[-0.00780071,0.00176771,0.0447249,-0.0210603,-0.0726375,
		0.337929,0.787641,0.491056,-0.0483117,-0.11799,0.00349071,
		0.0154041]
		hp2=[0.0154041,-0.00349071,-0.11799,0.0483117,0.491056,
		-0.787641,0.337929,0.0726375,-0.0210603,-0.0447249,
		0.00176771,0.00780071]
	elif name=="sym7":
		lp1=[0.00268181,-0.00104738,-0.0126363,0.0305155,0.0678927,
		-0.0495528,0.0174413,0.536102,0.767764,0.28863,-0.140047,
		-0.107808,0.00401024,0.0102682]
		hp1=[-0.0102682,0.00401024,0.107808,-0.140047,-0.28863,
		0.767764,-0.536102,0.0174413,0.0495528,0.0678927,-0.0305155,
		-0.0126363,0.00104738,0.00268181]
		lp2=[0.0102682,0.00401024,-0.107808,-0.140047,0.28863,0.767764,
		0.536102,0.0174413,-0.0495528,0.0678927,0.0305155,-0.0126363,
		-0.00104738,0.00268181]
		hp2=[0.00268181,0.00104738,-0.0126363,-0.0305155,0.0678927,
		0.0495528,0.0174413,-0.536102,0.767764,-0.28863,-0.140047,
		0.107808,0.00401024,-0.0102682]
	elif name=="sym8":
		lp1=[-0.00338242,-0.000542132,0.0316951,0.00760749,-0.143294,
		-0.0612734,0.48136,0.777186,0.364442,-0.0519458,-0.027219,
		0.0491372,0.00380875,-0.0149523,-0.000302921,0.00188995]
		hp1=[-0.00188995,-0.000302921,0.0149523,0.00380875,-0.0491372,
		-0.027219,0.0519458,0.364442,-0.777186,0.48136,0.0612734,
		-0.143294,-0.00760749,0.0316951,0.000542132,-0.00338242]
		lp2=[0.00188995,-0.000302921,-0.0149523,0.00380875,0.0491372,
		-0.027219,-0.0519458,0.364442,0.777186,0.48136,-0.0612734,
		-0.143294,0.00760749,0.0316951,-0.000542132,-0.00338242]
		hp2=[-0.00338242,0.000542132,0.0316951,-0.00760749,-0.143294,
		0.0612734,0.48136,-0.777186,0.364442,0.0519458,-0.027219,
		-0.0491372,0.00380875,0.0149523,-0.000302921,-0.00188995]
	elif name=="sym9":
		lp1=[0.00140092,0.000619781,-0.013272,-0.0115282,0.0302249,
		0.000583463,-0.054569,0.238761,0.717897,0.617338,0.0352725,
		-0.191551,-0.0182338,0.0620778,0.00885927,-0.0102641,
		-0.000473154,0.00106949]
		hp1=[-0.00106949,-0.000473154,0.0102641,0.00885927,-0.0620778,
		-0.0182338,0.191551,0.0352725,-0.617338,0.717897,-0.238761,
		-0.054569,-0.000583463,0.0302249,0.0115282,-0.013272,
		-0.000619781,0.00140092]
		lp2=[0.00106949,-0.000473154,-0.0102641,0.00885927,0.0620778,
		-0.0182338,-0.191551,0.0352725,0.617338,0.717897,0.238761,
		-0.054569,0.000583463,0.0302249,-0.0115282,-0.013272,
		0.000619781,0.00140092]
		hp2=[0.00140092,-0.000619781,-0.013272,0.0115282,0.0302249,
		-0.000583463,-0.054569,-0.238761,0.717897,-0.617338,0.0352725,
		0.191551,-0.0182338,-0.0620778,0.00885927,0.0102641,-0.000473154,
		-0.00106949]
	elif name=="sym10":
		lp1=[0.00077016,9.56327e-05,-0.0086413,-0.00146538,0.0459272,
		0.0116099,-0.159494,-0.0708805,0.471691,0.76951,0.383827,
		-0.0355367,-0.0319901,0.049995,0.00576491,-0.0203549,
		-0.000804359,0.00459317,5.70361e-05,-0.000459329]
		hp1=[0.000459329,5.70361e-05,-0.00459317,-0.000804359,
		0.0203549,0.00576491,-0.049995,-0.0319901,0.0355367,0.383827,
		-0.76951,0.471691,0.0708805,-0.159494,-0.0116099,0.0459272,
		0.00146538,-0.0086413,-9.56327e-05,0.00077016]
		lp2=[-0.000459329,5.70361e-05,0.00459317,-0.000804359,
		-0.0203549,0.00576491,0.049995,-0.0319901,-0.0355367,0.383827,
		0.76951,0.471691,-0.0708805,-0.159494,0.0116099,0.0459272,
		-0.00146538,-0.0086413,9.56327e-05,0.00077016]
		hp2=[0.00077016,-9.56327e-05,-0.0086413,0.00146538,0.0459272,
		-0.0116099,-0.159494,0.0708805,0.471691,-0.76951,0.383827,
		0.0355367,-0.0319901,-0.049995,0.00576491,0.0203549,
		-0.000804359,-0.00459317,5.70361e-05,0.000459329]

	else:
		lp1=0
		hp1=0
		lp2=0
		hp2=0
	
	return lp1,hp1,lp2,hp2    
