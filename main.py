# coding=UTF-8

# Laser Pong
#
# by Sam Neurohack
#
# Based on Laser Pinball
#

import pygame

# STDLIB
import math
import itertools
import sys
import os
import thread
import time
import random

from globalVars import *
import gstt
import ball
import score
import score2
import borders
import filet
import flips
import logo
import text


import frame
from vectors import Vector2D
import renderer
import dac

# 

def StartPlaying(first_time = False):
	gstt.score.Reset()
	gstt.score2.Reset()
	gstt.fs = GAME_FS_LAUNCH
	gstt.x = ball_origin[0]
	gstt.y = ball_origin[1]

	
def dac_thread():
#	global PLAYERS, DRAW

	while True:
		try:

			d = dac.DAC(dac.find_first_dac())
			d.play_stream(laser)

		except Exception as e:

			import sys, traceback
			print '\n---------------------'
			print 'Exception: %s' % e
			print '- - - - - - - - - - -'
			traceback.print_tb(sys.exc_info()[2])
			print "\n"
			pass

def DrawTestPattern(f):
	l,h = screen_size
	L_SLOPE = 30
	
	f.Line((0, 0), (l, 0), 0xFFFFFF)
	f.LineTo((l, h), 0xFFFFFF)
	f.LineTo((0, h), 0xFFFFFF)
	f.LineTo((0, 0), 0xFFFFFF)
	
	f.LineTo((2*L_SLOPE, h), 0)
	for i in xrange(1,7):
		c = (0xFF0000 if i & 1 else 0) | (0xFF00 if i & 2 else 0) | (0xFF if i & 4 else 0)
		f.LineTo(((2 * i + 1) * L_SLOPE, 0), c)
		f.LineTo(((2 * i + 2) * L_SLOPE, h), c)
	f.Line((l*.5, h*.5), (l*.75, -h*.5), 0xFF00FF)
	f.LineTo((l*1.5, h*.5), 0xFF00FF)
	f.LineTo((l*.75, h*1.5), 0xFF00FF)
	f.LineTo((l*.5, h*.5), 0xFF00FF)
		
		
def Align(f):
	l,h = screen_size
	L_SLOPE = 30
	
	f.Line((0, 0), (l, 0), 0xFFFFFF)
	f.LineTo((l, h), 0xFFFFFF)
	f.LineTo((0, h), 0xFFFFFF)
	f.LineTo((0, 0), 0xFFFFFF)
	laser = renderer.LaserRenderer(fwork_holder, gstt.centerx, gstt.centery, gstt.zoomx, gstt.zoomy, gstt.sizex, gstt.sizey)

	print str(gstt.centerx) + "," + str(gstt.centery) + "," + str(gstt.zoomx) + "," + str(gstt.zoomy) + "," + str(gstt.sizex) + "," + str(gstt.sizey)
	
app_path = os.path.dirname(os.path.realpath(__file__))

pygame.init()


screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Textes")
clock = pygame.time.Clock()

gstt.centerx = LASER_CENTER_X
gstt.centery = LASER_CENTER_Y
gstt.zoomx = LASER_ZOOM_X
gstt.zoomy = LASER_ZOOM_Y
gstt.sizex = LASER_SIZE_X
gstt.sizey = LASER_SIZE_Y

fwork_holder = frame.FrameHolder()
laser = renderer.LaserRenderer(fwork_holder, gstt.centerx, gstt.centery, gstt.zoomx, gstt.zoomy, gstt.sizex, gstt.sizey)


thread.start_new_thread(dac_thread, ())

update_screen = False

gstt.score = score.Score()
gstt.score2 = score2.Score2()
gstt.bll = ball.Ball()
gstt.flp = flips.Flips()
gstt.txt = text.Text()
gstt.flt = filet.Filet()
gstt.xvel = - 1
gstt.yvel = 0
gstt.lscore = 0
gstt.rscore = 0
gstt.ly = FLIPS_lorigin[1]
gstt.ry = FLIPS_rorigin[1]
flipsy = [gstt.ly, gstt.ry]
gstt.stick = 0
gstt.x = ball_origin[0]
gstt.y = ball_origin[1]
gstt.remain = BALL_MAX	

keystates = pygame.key.get_pressed()

gstt.fs = GAME_FS_MENU

while gstt.fs != GAME_FS_QUIT:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gstt.fs = GAME_FS_QUIT
		#elif event.type ==
	
	keystates_prev = keystates[:]
	keystates = pygame.key.get_pressed()[:]


	# Etats du jeu
	
	
	if gstt.fs == GAME_FS_MENU:
		if keystates[pygame.K_ESCAPE] and not keystates_prev[pygame.K_ESCAPE]:
			gstt.fs = GAME_FS_QUIT
		elif keystates[pygame.K_SPACE] and not keystates_prev[pygame.K_SPACE]:
			StartPlaying(True)
		gstt.lscore = 0
		gstt.rscore = 0
		


	elif gstt.fs == GAME_FS_PLAY:

		if keystates[pygame.K_ESCAPE] and not keystates_prev[pygame.K_ESCAPE]:
			gstt.fs = GAME_FS_MENU
			
	# Lost ball / first to ten points ?
		
		#print " ball : " , gstt.x, gstt.y, " left : ", gstt.ly, " right : ", gstt.ry
		
		if gstt.x < FLIPS_lorigin[0] + PADDLE_width:

			print "ball.y : ", gstt.y, " ly : ", gstt.ly
			if gstt.y > (gstt.ly + PADDLE_height + 1) or gstt.y < (gstt.ly - BALL_SIZE_Y - 1):
				gstt.score.Increase(1)
				gstt.rscore += 1
				gstt.xvel = random.uniform(-1,-0.6)
				if gstt.rscore == 11:
					gstt.fs = GAME_FS_MENU
				else: 
					gstt.fs = GAME_FS_LAUNCH
			else:
				gstt.x = FLIPS_lorigin[0] + PADDLE_width
				gstt.xvel *= -1
			
				
		if gstt.x > FLIPS_rorigin[0] - PADDLE_width:
		
			print "ball.y : ", gstt.y, " ry : ", gstt.ry

			if gstt.y < (gstt.ry - BALL_SIZE_Y - 1) or gstt.y > (gstt.ry + PADDLE_height + 1):
				gstt.score2.Increase(1)
				gstt.lscore += 1
				gstt.xvel = random.uniform(1,0.6)
				if gstt.lscore == 11:
					gstt.fs = GAME_FS_MENU
				else: 
					gstt.fs = GAME_FS_LAUNCH
			else:
				gstt.xvel *= -1
				gstt.x = FLIPS_rorigin[0] - PADDLE_width	
				



		# wall detect
		
		if gstt.y < 0:
			gstt.y = 1
			gstt.yvel *= -1

		
		if gstt.y > screen_size[1]:
			gstt.y = screen_size[1] - 1
			gstt.yvel *= -1
			
		# Anim 
		
		gstt.x += BALL_SPEED * gstt.xvel 
		gstt.y += BALL_SPEED * gstt.yvel
		gstt.yvel += GRAVITY
		gstt.bll.Move(gstt.x,gstt.y)
		flipsy =  gstt.flp.Move(keystates[pygame.K_a],keystates[pygame.K_q],keystates[pygame.K_UP],keystates[pygame.K_DOWN])
		gstt.ly = flipsy[0]
		gstt.ry = flipsy[1]


	elif gstt.fs == GAME_FS_LAUNCH:
	
		
		if keystates[pygame.K_ESCAPE] and not keystates_prev[pygame.K_ESCAPE]:
			gstt.fs = GAME_FS_MENU
		if keystates[pygame.K_SPACE] and not keystates_prev[pygame.K_SPACE]:
			gstt.fs = GAME_FS_PLAY
			#gstt.xvel = 0
			gstt.yvel = 0
			
			while math.fabs(gstt.xvel + gstt.yvel) < 1:
				#gstt.xvel = random.uniform(-1,1)
				gstt.yvel = random.uniform(-1,1)
			
		gstt.x = ball_origin[0]
		gstt.y = ball_origin[1]
		gstt.bll.Move(gstt.x,gstt.y)
		flipsy = gstt.flp.Move(keystates[pygame.K_a],keystates[pygame.K_q],keystates[pygame.K_UP],keystates[pygame.K_DOWN])
		gstt.ly = flipsy[0]
		gstt.ry = flipsy[1]
		#print gstt.ly, gstt.ry



	elif gstt.fs == GAME_FS_GAMEOVER:

		#TODO : MODE GAME OVER, autres opérations d'animation
		# Remarque : on peut supprimer le mode GAME OVER et le gérer dans le mode jeu
		# si les traitements sont les mêmes

		if keystates[pygame.K_SPACE] and not keystates_prev[pygame.K_SPACE]:
			StartPlaying(False)
		elif keystates[pygame.K_ESCAPE] and not keystates_prev[pygame.K_ESCAPE]:
			gstt.fs = GAME_FS_MENU
			# Peut-être aussi réinitialiser l'état dans le mode menu


	# OPERATIONS D'AFFICHAGE


	# On efface l'écran avant
	screen.fill(0)

	# Création de la nouvelle frame vide où les objets du jeu vont dessiner
	fwork = frame.Frame()
	
	# Verification des touches pour la mire ou le recentrage.
	
	if keystates[pygame.K_p]:
		DrawTestPattern(fwork)
		
	if keystates[pygame.K_x]:
		Align(fwork)
		
	if keystates[pygame.K_r]:
		gstt.centerx += 20
		Align(fwork)

	if keystates[pygame.K_t]:
		gstt.centerx -= 20
		Align(fwork)
		
	if keystates[pygame.K_y]:
		gstt.centery += 20
		Align(fwork)

	if keystates[pygame.K_u]:
		gstt.centery -= 20
		Align(fwork)

	if keystates[pygame.K_f]:
		gstt.zoomx += 0.1
		Align(fwork)

	if keystates[pygame.K_g]:
		gstt.zoomx -= 0.1
		Align(fwork)
		
	if keystates[pygame.K_h]:
		gstt.zoomy += 0.1
		Align(fwork)

	if keystates[pygame.K_j]:
		gstt.zoomy -= 0.1
		Align(fwork)
	
	if keystates[pygame.K_c]:
		gstt.sizex -= 50
		Align(fwork)
		
	if keystates[pygame.K_v]:
		gstt.sizex += 50
		Align(fwork)
		
	if keystates[pygame.K_b]:
		gstt.sizey -= 50
		Align(fwork)
		
	if keystates[pygame.K_n]:
		gstt.sizey += 50
		Align(fwork)

	else:
		display_plyr = gstt.fs == GAME_FS_PLAY or gstt.fs == GAME_FS_GAMEOVER or gstt.fs == GAME_FS_LAUNCH
		if display_plyr:
			
			gstt.score.Draw(fwork)
			gstt.score2.Draw(fwork)
			gstt.flp.Draw(fwork)
			gstt.bll.Draw(fwork)
			gstt.flt.Draw(fwork)

		if gstt.fs == GAME_FS_MENU:
			logo.Draw(fwork)
			#gstt.txt.Draw(fwork)
	
	# Affecter la frame construite à l'objet conteneur de frame servant au système de rendu par laser
	fwork_holder.f = fwork

	if update_screen:
		update_screen = False
		fwork.RenderScreen(screen)
		pygame.display.flip()
	else:
		update_screen = True

	# Opérations d'animation autres (traitements après l'affichage)'
	
	
	# TODO : rendre indépendante la fréquence de rafraîchissement de l'écran par
	# rapport à celle de l'animation du jeu
	clock.tick(100)

pygame.quit()

