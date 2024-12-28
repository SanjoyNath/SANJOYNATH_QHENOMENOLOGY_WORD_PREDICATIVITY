from manim import *
import mido
import tempfile
import os

class SoundExample_Automids(Scene):
    def construct(self):
        # Create a temporary MIDI file
        midi_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mid")
        midi_file.close()

        # Create a MIDI track
        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)

        # Define the duration of each movement in seconds
        durations = [1, 1, 1]

        # Add MIDI notes corresponding to the movements
        for duration in durations:
            track.append(mido.Message('note_on', note=60, velocity=64, time=0))
            track.append(mido.Message('note_off', note=60, velocity=64, time=int(duration * 480)))

        # Save the MIDI file
        mid.save(midi_file.name)

        # Embed the MIDI file into the scene
        self.add_sound(midi_file.name)

        # Create and animate the dot
        dot = Dot().set_color(GREEN)
        self.add(dot)
        self.wait(durations[0])
        
        self.add_sound(midi_file.name)
        dot.set_color(BLUE)
        self.wait(durations[1])
        
        self.add_sound(midi_file.name)
        dot.set_color(RED)
        self.wait(durations[2])

        # Clean up the temporary MIDI file
        os.remove(midi_file.name)

# # # # Create an instance of the scene to trigger the construct method
# # # scene = SoundExample()
# # # scene.render()

# # # print("SoundExample animation with embedded MIDI file has been rendered.")


# # # D:\SANJOY_NATH_MANIMS>manim -pql saansautomids.py SoundExample_Automids
# # # Manim Community v0.18.1

# # # [12/28/24 15:40:00] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\saansautomids\480p15\partial_movie_files\SoundExample_Automids\1185818338_2268332985_1279531144.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\saansautomids\480p15\partial_movie_files\SoundExample_Automids\624642324_3890345977_2352283492.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\saansautomids\480p15\partial_movie_files\SoundExample_Automids\624642324_3890345977_2392899484.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
# # # [12/28/24 15:40:01] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\saansautomids\480p15\SoundExample_Automids.mp4'

                    # # # INFO     Rendered SoundExample_Automids                                                                                                                                          scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\saansautomids\480p15\SoundExample_Automids.mp4'                                          