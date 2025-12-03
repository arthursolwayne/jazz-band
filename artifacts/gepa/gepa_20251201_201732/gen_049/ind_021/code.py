
import pretty_midi
from pretty_midi import note_number_to_name

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time in seconds per bar (160 BPM, 4/4 time)
bar_length = 6.0 / 4  # 6 seconds for 4 bars, so 1.5 seconds per bar
note_duration = bar_length / 4  # 0.375 seconds per beat

# Set up instruments
# 1. Tenor Sax (You) - Program: 64 (Tenor Saxophone)
sax_program = 64
sax = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax)

# 2. Bass (Marcus) - Program: 33 (Double Bass)
bass_program = 33
bass = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass)

# 3. Piano (Diane) - Program: 0 (Acoustic Grand Piano)
piano_program = 0
piano = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano)

# 4. Drums (Little Ray) - Program: 0 (Acoustic Grand Piano, but we'll use percussion)
# We'll use MIDI note numbers for percussion
drums = pretty_midi.Instrument(program=0)
pm.instruments.append(drums)

# Define key: F major
key = 'F'

# Bar 1: Drums Only - Build tension
# Kick on 1 and 3, snare on 2 and 4, hihat every eighth
def play_drums(time, kick_note=36, snare_note=38, hihat_note=42):
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=kick_note, start=time, end=time + note_duration)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=kick_note, start=time + 2 * note_duration, end=time + 3 * note_duration)
    drums.notes.append(kick)

    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=snare_note, start=time + note_duration, end=time + 2 * note_duration)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=snare_note, start=time + 3 * note_duration, end=time + 4 * note_duration)
    drums.notes.append(snare)

    # Hi-hat on every eighth note
    for i in range(0, 4):
        hihat = pretty_midi.Note(velocity=80, pitch=hihat_note, start=time + i * note_duration, end=time + (i + 1) * note_duration)
        drums.notes.append(hihat)

# Bar 1
play_drums(0.0)

# Bar 2: All instruments in, Tenor Sax takes melody
# Tenor Sax melody - motif: F - G - Bb - D (F, G, Bb, D)
sax_notes = [
    (48, 0.0, 0.375),  # F4
    (50, 0.375, 0.75), # G4
    (52, 0.75, 1.125), # Bb4
    (55, 1.125, 1.5)   # D5
]
for note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2])
    sax.notes.append(n)

# Bass line: walking line in F, roots and fifths with chromatic approaches
# Bar 2: F - Gb - G - A
bass_notes = [
    (81, 1.5, 1.875),  # F (MIDI 81)
    (80, 1.875, 2.25), # Gb (MIDI 80)
    (82, 2.25, 2.625), # G (MIDI 82)
    (84, 2.625, 3.0)   # A (MIDI 84)
]
for note in bass_notes:
    n = pretty_midi.Note(velocity=70, pitch=note[0], start=note[1], end=note[2])
    bass.notes.append(n)

# Piano comp: Open voicings, resolving on the last chord
# Bar 2: Fmaj7 - Bbmaj7 (chords on 2 and 4)
# Fmaj7: F, A, C, E
# Bbmaj7: Bb, D, F, A
# Play on 2 and 4

def play_piano_chord(start, chord_notes):
    for note in chord_notes:
        n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375)
        piano.notes.append(n)

# Bbmaj7 on beat 2
piano_notes_bar2 = [71, 74, 76, 78]  # Bb, D, F, A
play_piano_chord(1.5, piano_notes_bar2)

# Fmaj7 on beat 4
piano_notes_bar4 = [76, 79, 81, 83]  # F, A, C, E
play_piano_chord(3.0, piano_notes_bar4)

# Bar 3: Tenor Sax continues motif, resolves
# F - C (F to C), resolving the tension
sax_notes = [
    (55, 3.0, 3.375),  # D5
    (48, 3.375, 4.0)   # F4 (end at the end of the bar)
]
for note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2])
    sax.notes.append(n)

# Bass: Continue walking line
# Bar 3: Bb - C - Db - D
bass_notes = [
    (71, 3.0, 3.375),  # Bb (MIDI 71)
    (72, 3.375, 3.75), # C (MIDI 72)
    (73, 3.75, 4.125), # Db (MIDI 73)
    (74, 4.125, 4.5)   # D (MIDI 74)
]
for note in bass_notes:
    n = pretty_midi.Note(velocity=70, pitch=note[0], start=note[1], end=note[2])
    bass.notes.append(n)

# Piano: Chromatic motion, resolving on the last chord
# Bar 3: Cm7 - Fmaj7 (chords on 2 and 4)
# Cm7: C, Eb, G, Bb
# Fmaj7: F, A, C, E
# Play on 2 and 4

# Cm7 on beat 2
piano_notes_bar3_2 = [72, 69, 76, 71]  # C, Eb, G, Bb
play_piano_chord(3.0, piano_notes_bar3_2)

# Fmaj7 on beat 4
play_piano_chord(4.5, piano_notes_bar4)

# Bar 4: Drums again, Tenor Sax resolves
# Drums: Same pattern
play_drums(3.0)

# Tenor Sax: Final resolution - F (sustained)
sax_notes = [
    (48, 4.5, 6.0)  # F4
]
for note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2])
    sax.notes.append(n)

# Save the MIDI file
pm.write("jazz_intro.mid")
print("MIDI file generated: jazz_intro.mid")
