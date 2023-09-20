POINTS_FOR_STRIKE = 10

class BowlingPlayer(object):
    def __init__(self, name, overall=0):
        self.name = name
        self.total_points = overall

    def frames(self):
        for frame in range(1, 11):
            print(f'Frame {frame}:')
            shot_one = int(input('how many pins on first shot:'))
            if shot_one == POINTS_FOR_STRIKE:
                # this is a strike
                shot_two_after_strike = int(input('how many pins on shot after strike:'))
                self.total_points += shot_two_after_strike + shot_one
                if shot_two_after_strike == POINTS_FOR_STRIKE:
                     # you got another strike. continue the frame!
                    shot_three_after_strike = int(input('how many pins on shot after two strikes:'))
                    self.total_points += shot_three_after_strike
            elif shot_one < POINTS_FOR_STRIKE:
                shot_two = int(input('how many pins on second shot:'))
                shots = shot_one + shot_two
                self.total_points += shots
                if shots == POINTS_FOR_STRIKE:
                    # this is a spare
                    shot_three_after_spare = int(input('how many pins on shot after spare'))
                    self.total_points += shot_three_after_spare

        return self.total_points

if __name__ == '__main__':
    craig = BowlingPlayer('craig')
    print(craig.frames())