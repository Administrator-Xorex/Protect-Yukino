import sys
import pygame

from bullet import Bullet
from teacher import Teacher
from time import sleep

def check_keydown_events(event,number,screen,yukino,bullets):
    if event.key==pygame.K_RIGHT:
        yukino.moving_right=True
    elif event.key==pygame.K_LEFT:
        yukino.moving_left=True
    elif event.key==pygame.K_SPACE:
        if len(bullets)<number.bullets_allowed:
            new_bullet=Bullet(number,screen,yukino)
            bullets.add(new_bullet)
    elif event.key==pygame.K_q:
        sys.exit()

def check_keyup_events(event,yukino):
    if event.key==pygame.K_RIGHT:
        yukino.moving_right=False
    elif event.key==pygame.K_LEFT:
        yukino.moving_left=False

def check_events(number,screen,stats,sb,play_button,yukino,teachers,bullets):
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                check_keydown_events(event,number,screen,yukino,bullets)
            elif event.type==pygame.KEYUP:
                check_keyup_events(event,yukino)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                check_play_button(number,screen,stats,sb,play_button,
                yukino,teachers,bullets,mouse_x,mouse_y)

def check_play_button(number,screen,stats,sb,play_button,yukino,teachers,bullets,mouse_x,mouse_y):
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        number.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        if play_button.rect.collidepoint(mouse_x,mouse_y):
            stats.reset_stats()
            stats.game_active=True

            sb.prep_score()
            sb.prep_high_score()
            sb.prep_level()
            sb.prep_yukino()

            teachers.empty()
            bullets.empty()
            create_fleet(number,screen,yukino,teachers)
            yukino.center_yukino()

def check_fleet_edges(number,teachers):
    for teacher in teachers.sprites():
        if teacher.check_edges():
            change_fleet_direction(number,teachers)
            break

def check_bullet_teacher_collisions(number,screen,stats,sb,yukino,teachers,bullets):
    collisions=pygame.sprite.groupcollide(bullets,teachers,True,True)

    if collisions:
        for teachers in collisions.values():
            stats.score+=number.teacher_points*len(teachers)
            sb.prep_score()
        check_high_score(stats,sb)

    if len(teachers)==False:
        bullets.empty()
        number.increase_speed()
        stats.level+=1
        sb.prep_level()
        create_fleet(number,screen,yukino,teachers)

def check_teachers_bottom(number,screen,stats,sb,yukino,teachers,bullets):
    screen_rect=screen.get_rect()
    for teacher in teachers.sprites():
        if teacher.rect.bottom>=screen_rect.bottom:
            yukino_hit(number,stats,screen,sb,yukino,teacher,bullets)
            break

def check_high_score(stats,sb):
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()

def change_fleet_direction(number,teachers):
    for teacher in teachers.sprites():
        teacher.rect.y+=number.fleet_drop_speed
    number.fleet_direction*=-1

def update_screen(number,screen,stats,sb,yukino,teachers,bullets,play_button):
    screen.fill(number.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    yukino.blitme()
    teachers.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(number,screen,stats,sb,yukino,teachers,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_bullet_teacher_collisions(number,screen,stats,sb,yukino,teachers,bullets)

def update_teachers(number,screen,stats,sb,yukino,teachers,bullets):
    check_fleet_edges(number,teachers)
    teachers.update()
    
    if pygame.sprite.spritecollideany(yukino,teachers):
        yukino_hit(number,screen,stats,sb,yukino,teachers,bullets)

    check_teachers_bottom(number,screen,stats,sb,yukino,teachers,bullets)


def get_number_teachers_x(number,teacher_width):
    available_space_x=number.screen_width-2*teacher_width
    number_teachers_x=int(available_space_x/(2*teacher_width))
    return number_teachers_x

def get_number_rows(number,yukino_height,teacher_height):
    available_space_y=(number.screen_height-(3*teacher_height)-yukino_height)
    number_rows=int(available_space_y/(2*teacher_height))
    return number_rows

def create_teacher(number,screen,teachers,teacher_number,row_number):
    teacher=Teacher(number,screen)
    teacher_width=teacher.rect.width
    teacher.x=teacher_width+2*teacher_width*teacher_number
    teacher.rect.x=teacher.x
    teacher.rect.y=teacher.rect.height+2*teacher.rect.height*row_number
    teachers.add(teacher)

def create_fleet(number,screen,yukino,teachers):
    teacher=Teacher(number,screen)
    number_teachers_x=get_number_teachers_x(number,teacher.rect.width)
    number_rows=get_number_rows(number,yukino.rect.height,teacher.rect.height)

    for row_number in range(number_rows):
        for teacher_number in range(number_teachers_x):
            create_teacher(number,screen,teachers,teacher_number,row_number)

def yukino_hit(number,screen,stats,sb,yukino,teachers,bullets):
    if stats.yukino_left>0:
        stats.yukino_left-=1
        sb.prep_yukino()
        teachers.empty()
        bullets.empty()
        create_fleet(number,screen,yukino,teachers)
        yukino.center_yukino()
        sleep(number.stop_time)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
