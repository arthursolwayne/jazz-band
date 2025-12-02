
from mido import MidiFile, MidiTrack, Message, MetaMessage
import mido

# Set up MIDI file and track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Tempo: 160 BPM = 600000 / 160 = 3750 microseconds per beat
track.append(MetaMessage('set_tempo', tempo=3750))

# Time signature 4/4
track.append(MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=24, notations=32))

# Define time in ticks per beat (MIDI default is 480 ticks per beat)
ticks_per_beat = 480
time_per_bar = ticks_per_beat * 4  # 4 bars = 16 beats = 6 seconds at 160 BPM

# Keys: Dm = D, F, A, C
# Dm7 = D, F, A, C
# Cm7 = C, Eb, G, Bb
# G7 = G, B, D, F
# F7 = F, A, C, E

# Drum Track: Little Ray
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def play_drums():
    time = 0
    for bar in range(4):
        for beat in range(4):
            if beat == 0 or beat == 2:
                track.append(Message('note_on', note=36, velocity=100, time=time))  # Kick
                track.append(Message('note_off', note=36, velocity=100, time=120))  # Kick
            if beat == 1 or beat == 3:
                track.append(Message('note_on', note=38, velocity=100, time=time))  # Snare
                track.append(Message('note_off', note=38, velocity=100, time=120))  # Snare
            # Hi-hat on every eighth
            for eighth in range(2):
                track.append(Message('note_on', note=42, velocity=100, time=60))  # Hi-hat
                track.append(Message('note_off', note=42, velocity=100, time=60))  # Hi-hat
            time += 120  # 120 ticks per beat

# Bass Track: Marcus
# Walking line: D2-G2, roots and fifths with chromatic approaches
def play_bass():
    time = 0
    # Dm7 -> Cm7 -> G7 -> F7
    chords = ['Dm7', 'Cm7', 'G7', 'F7']
    bass_notes = [38, 37, 50, 57]  # D2, C2, G3, F3 (approx. roots with chromatic approach)
    for note in bass_notes:
        track.append(Message('note_on', note=note, velocity=100, time=time))
        track.append(Message('note_off', note=note, velocity=100, time=120))
        time += 120

# Piano Track: Diane
# Open voicings, different chord each bar, resolve on the last
def play_piano():
    time = 0
    chords = [
        [57, 60, 64, 67],  # Dm7 (D, F, A, C)
        [60, 63, 67, 71],  # Cm7 (C, Eb, G, Bb)
        [67, 71, 74, 77],  # G7 (G, B, D, F)
        [65, 69, 72, 76],  # F7 (F, A, C, E)
    ]
    for chord in chords:
        # Play the chord on beat 2 and 4
        for beat in range(4):
            if beat == 1 or beat == 3:
                for note in chord:
                    track.append(Message('note_on', note=note, velocity=100, time=time))
                time += 120
                for note in chord:
                    track.append(Message('note_off', note=note, velocity=100, time=0))
            else:
                time += 120
    # Just in case, add an extra time to align
    track.append(Message('note_off', note=0, velocity=0, time=0))

# Tenor Sax: You
# Motif: D - F - A - C (Dm7) with a breathless, unfinished feel
def play_sax():
    # Bar 1: Motif starts, leaves it hanging
    time = 0
    # D (D4) -> F (F4) -> A (A4) -> C (C5)
    # Start on beat 1
    track.append(Message('note_on', note=62, velocity=110, time=time))
    track.append(Message('note_off', note=62, velocity=110, time=60))  # D4
    track.append(Message('note_on', note=65, velocity=110, time=60))
    track.append(Message('note_off', note=65, velocity=110, time=60))  # F4
    track.append(Message('note_on', note=69, velocity=110, time=60))
    track.append(Message('note_off', note=69, velocity=110, time=60))  # A4
    # Leave the C unresolved
    # Bar 2: Bring it back in, but end with a question
    time += 120
    track.append(Message('note_on', note=62, velocity=110, time=0))
    track.append(Message('note_off', note=62, velocity=110, time=60))  # D4
    track.append(Message('note_on', note=65, velocity=110, time=60))
    track.append(Message('note_off', note=65, velocity=110, time=60))  # F4
    track.append(Message('note_on', note=69, velocity=110, time=60))
    track.append(Message('note_off', note=69, velocity=110, time=60))  # A4
    track.append(Message('note_on', note=72, velocity=110, time=60))
    track.append(Message('note_off', note=72, velocity=110, time=60))  # C5

# Play all tracks
play_drums()
play_bass()
play_piano()
play_sax()

# Save the MIDI file
mid.save('dante_intro.mid')
print("MIDI file 'dante_intro.mid' has been created.")
