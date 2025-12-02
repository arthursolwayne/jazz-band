
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Drums')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Define time information
beat = 0.375  # 160 BPM => 60/160 = 0.375s per beat
bar = 1.5     # 4 beats per bar
four_bar = bar * 4  # 6.0 seconds

# --------------------------
# DRUMS: Little Ray
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Fill the bar, but leave room for space and surprise

for bar_idx in range(4):
    time = bar_idx * bar

    # Kick on 1 and 3
    kick_notes = [36]  # MIDI for kick
    for beat_idx in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=kick_notes[0], start=time + beat_idx * beat, end=time + beat_idx * beat + 0.1)
        drums.notes.append(note)

    # Snare on 2 and 4
    snare_notes = [38]  # MIDI for snare
    for beat_idx in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=snare_notes[0], start=time + beat_idx * beat, end=time + beat_idx * beat + 0.1)
        drums.notes.append(note)

    # Hi-hat on every eighth
    hihat_notes = [42]  # MIDI for open hihat
    for eighth in range(8):
        note = pretty_midi.Note(velocity=80, pitch=hihat_notes[0], start=time + (eighth * beat / 2), end=time + (eighth * beat / 2) + 0.05)
        drums.notes.append(note)

# --------------------------
# BASS: Marcus
# Walking line, roots and fifths with chromatic approaches
# D2-G2 (MIDI 38-43), roots and fifths, chromatic approaches, not scales

# Fm -> F, Ab, C, D
# Chords: Fm (F, Ab, C), Bb7 (Bb, D, F, Ab), Eb7 (Eb, G, Bb, Db), Am7 (A, C, E, G)

# Bar 1: Fm
# Root: F (MIDI 70)
# Fifth: C (MIDI 64)
# Approach: Gb (MIDI 62)
F = 70
C = 64
Gb = 62

# Bar 1: Root (F), chromatic approach (Gb), root again
note1 = pretty_midi.Note(velocity=80, pitch=F, start=0, end=beat)
note2 = pretty_midi.Note(velocity=60, pitch=Gb, start=beat, end=beat + 0.1)
note3 = pretty_midi.Note(velocity=80, pitch=F, start=beat + 0.1, end=beat * 2)
bass.notes.append(note1)
bass.notes.append(note2)
bass.notes.append(note3)

# Bar 2: Bb7 -> Bb (MIDI 62), F (MIDI 70), chromatic approach (Eb, MIDI 60)
Bb = 62
F = 70
Eb = 60
note4 = pretty_midi.Note(velocity=80, pitch=Bb, start=beat * 2, end=beat * 3)
note5 = pretty_midi.Note(velocity=60, pitch=Eb, start=beat * 3, end=beat * 3 + 0.1)
note6 = pretty_midi.Note(velocity=80, pitch=F, start=beat * 3 + 0.1, end=beat * 4)
bass.notes.append(note4)
bass.notes.append(note5)
bass.notes.append(note6)

# Bar 3: Eb7 -> Eb (MIDI 59), Bb (MIDI 62)
Eb = 59
Bb = 62
note7 = pretty_midi.Note(velocity=80, pitch=Eb, start=beat * 4, end=beat * 5)
note8 = pretty_midi.Note(velocity=60, pitch=Eb - 1, start=beat * 5, end=beat * 5 + 0.1)
note9 = pretty_midi.Note(velocity=80, pitch=Bb, start=beat * 5 + 0.1, end=beat * 6)
bass.notes.append(note7)
bass.notes.append(note8)
bass.notes.append(note9)

# Bar 4: Am7 -> A (MIDI 69), C (MIDI 64)
A = 69
C = 64
note10 = pretty_midi.Note(velocity=80, pitch=A, start=beat * 6, end=beat * 7)
note11 = pretty_midi.Note(velocity=60, pitch=A - 1, start=beat * 7, end=beat * 7 + 0.1)
note12 = pretty_midi.Note(velocity=80, pitch=C, start=beat * 7 + 0.1, end=beat * 8)
bass.notes.append(note10)
bass.notes.append(note11)
bass.notes.append(note12)

# --------------------------
# PIANO: Diane
# Open voicings, different chord each bar, resolve on the last
# Comp on 2 and 4, let the chords breathe

# Define chords
Fm = [70, 64, 67, 59]  # F, Ab, C, D
Bb7 = [62, 67, 70, 64]  # Bb, D, F, Ab
Eb7 = [59, 64, 67, 60]  # Eb, G, Bb, Db
Am7 = [69, 72, 64, 67]  # A, C, E, G

# Bar 1: Fm
for pitch in Fm:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=0, end=beat * 2)
    piano.notes.append(note)

# Bar 2: Bb7
for pitch in Bb7:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=beat * 2, end=beat * 4)
    piano.notes.append(note)

# Bar 3: Eb7
for pitch in Eb7:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=beat * 4, end=beat * 6)
    piano.notes.append(note)

# Bar 4: Am7
for pitch in Am7:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=beat * 6, end=beat * 8)
    piano.notes.append(note)

# --------------------------
# SAX: You
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Melody: F (70) -> Ab (67) -> C (64) -> rest -> F (70) -> Ab (67) -> C (64)
# Let it hang, then return and finish it

# Bar 1
note13 = pretty_midi.Note(velocity=110, pitch=70, start=0, end=beat * 0.5)
note14 = pretty_midi.Note(velocity=110, pitch=67, start=beat * 0.5, end=beat * 1)
note15 = pretty_midi.Note(velocity=110, pitch=64, start=beat * 1, end=beat * 1.5)
sax.notes.append(note13)
sax.notes.append(note14)
sax.notes.append(note15)

# Bar 2
note16 = pretty_midi.Note(velocity=110, pitch=70, start=beat * 2, end=beat * 2.5)
note17 = pretty_midi.Note(velocity=110, pitch=67, start=beat * 2.5, end=beat * 3)
note18 = pretty_midi.Note(velocity=110, pitch=64, start=beat * 3, end=beat * 3.5)
sax.notes.append(note16)
sax.notes.append(note17)
sax.notes.append(note18)

# Bar 3: rest
# Bar 4: repeat the motif
note19 = pretty_midi.Note(velocity=110, pitch=70, start=beat * 6, end=beat * 6.5)
note20 = pretty_midi.Note(velocity=110, pitch=67, start=beat * 6.5, end=beat * 7)
note21 = pretty_midi.Note(velocity=110, pitch=64, start=beat * 7, end=beat * 7.5)
sax.notes.append(note19)
sax.notes.append(note20)
sax.notes.append(note21)

# --------------------------
# Write the MIDI file
pm.write("fmin_intro.mid")
