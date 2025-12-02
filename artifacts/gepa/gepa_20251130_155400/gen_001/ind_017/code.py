
import pretty_midi
import numpy as np

# Initialize MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
track_drums = pretty_midi.Instrument(program=10)
track_piano = pretty_midi.Instrument(program=0)
track_bass = pretty_midi.Instrument(program=33)
track_sax = pretty_midi.Instrument(program=64)

# Time settings (in seconds)
bar_length = 1.5  # 4 bars = 6 seconds
beat_length = 0.375

# Define time for each bar
bar_times = [0, bar_length, 2*bar_length, 3*bar_length, 4*bar_length]

# BAR 1: Drums only (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i, time in enumerate(np.arange(0, bar_length, beat_length / 2)):
    if i % 2 == 0:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        track_drums.notes.append(note)
    elif i % 2 == 1:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.1)
        track_drums.notes.append(note)
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.1)
    track_drums.notes.append(note)

# BAR 2: All instruments enter

# BASS LINE (Marcus) - Walking line in D minor
# Dm7 = D F A C
bass_line = [50, 53, 57, 59, 57, 53, 50, 52, 55, 57, 55, 52, 50, 53, 57, 59, 57, 53, 50]
bass_times = [bar_times[1] + beat_length * i for i in range(len(bass_line))]
for pitch, time in zip(bass_line, bass_times):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    track_bass.notes.append(note)

# PIANO (Diane) - 7th chords on 2 and 4, comping rhythm
# Dm7 = D F A C
# G7 = G B D F
# C7 = C E G B
# F7 = F A C E
chord_notes = [
    [50, 53, 57, 59],  # Dm7 on beat 2
    [67, 71, 69, 65],  # G7 on beat 4
]

for i, chord in enumerate(chord_notes):
    time = bar_times[1] + beat_length * (1 + i)
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
        track_piano.notes.append(note)

# SAX (Dante) - YOUR MOMENT
# D minor motif, start it, leave it hanging, come back and finish it
# Motif: D (50), F (53), D (50), rest
# Then repeat it, leaving a rest in the middle to create tension

# First motif
note1 = pretty_midi.Note(velocity=110, pitch=50, start=bar_times[1], end=bar_times[1] + 0.375)
track_sax.notes.append(note1)
note2 = pretty_midi.Note(velocity=110, pitch=53, start=bar_times[1] + 0.375, end=bar_times[1] + 0.75)
track_sax.notes.append(note2)
note3 = pretty_midi.Note(velocity=110, pitch=50, start=bar_times[1] + 0.75, end=bar_times[1] + 1.125)
track_sax.notes.append(note3)
note4 = pretty_midi.Note(velocity=110, pitch=50, start=bar_times[1] + 1.5, end=bar_times[1] + 1.875)
track_sax.notes.append(note4)
note5 = pretty_midi.Note(velocity=110, pitch=53, start=bar_times[1] + 1.875, end=bar_times[1] + 2.25)
track_sax.notes.append(note5)
note6 = pretty_midi.Note(velocity=110, pitch=50, start=bar_times[1] + 2.25, end=bar_times[1] + 2.625)
track_sax.notes.append(note6)

# BAR 3-4: Repeat with variation
# Motif again but with a rest in the middle
note7 = pretty_midi.Note(velocity=110, pitch=50, start=bar_times[2], end=bar_times[2] + 0.375)
track_sax.notes.append(note7)
note8 = pretty_midi.Note(velocity=110, pitch=53, start=bar_times[2] + 0.375, end=bar_times[2] + 0.75)
track_sax.notes.append(note8)
note9 = pretty_midi.Note(velocity=110, pitch=50, start=bar_times[2] + 0.75, end=bar_times[2] + 1.125)
track_sax.notes.append(note9)
# Rest (no note)
note10 = pretty_midi.Note(velocity=110, pitch=50, start=bar_times[2] + 1.5, end=bar_times[2] + 1.875)
track_sax.notes.append(note10)
note11 = pretty_midi.Note(velocity=110, pitch=53, start=bar_times[2] + 1.875, end=bar_times[2] + 2.25)
track_sax.notes.append(note11)
note12 = pretty_midi.Note(velocity=110, pitch=50, start=bar_times[2] + 2.25, end=bar_times[2] + 2.625)
track_sax.notes.append(note12)

# Add all tracks to MIDI
midi.instruments.append(track_drums)
midi.instruments.append(track_piano)
midi.instruments.append(track_bass)
midi.instruments.append(track_sax)

# Write to file
midi.write("wayne_shorter_intro.mid")
