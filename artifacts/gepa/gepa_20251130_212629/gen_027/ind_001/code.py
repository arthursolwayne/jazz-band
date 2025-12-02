
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here - build tension with subtle fills and dynamics

# Kick on 1 and 3
kick_1 = pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375)
kick_3 = pretty_midi.Note(velocity=85, pitch=36, start=1.125, end=1.5)

# Snare on 2 and 4
snare_2 = pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875)
snare_4 = pretty_midi.Note(velocity=95, pitch=38, start=1.5, end=1.625)

# Hihat on every eighth note, with a slight dynamic variation
hihat_notes = [
    (0.0, 80), (0.375, 85), (0.75, 80), (1.125, 85),
    (1.5, 80), (1.875, 85), (2.25, 80), (2.625, 85)
]

for start, vel in hihat_notes:
    hihat = pretty_midi.Note(velocity=vel, pitch=42, start=start, end=start + 0.375)
    drums.notes.append(hihat)

drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in D, with chromatic approaches
bass_notes = [
    (1.5, 62, 80), (1.875, 61, 90), (2.25, 64, 85), (2.625, 62, 80),
    (3.0, 65, 85), (3.375, 64, 90), (3.75, 62, 80), (4.125, 60, 85),
    (4.5, 62, 80), (4.875, 61, 90), (5.25, 64, 85), (5.625, 62, 80)
]

for start, pitch, vel in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# D7 (D F# A C) on beat 2, G7 (G B D F) on beat 4

def add_chord_notes(start, chord, vel):
    for note in chord:
        n = pretty_midi.Note(velocity=vel, pitch=note, start=start, end=start + 0.375)
        piano.notes.append(n)

# Bar 2: D7 on beat 2
add_chord_notes(2.25, [62, 67, 69, 64], 85)

# Bar 3: G7 on beat 4
add_chord_notes(4.125, [67, 72, 69, 71], 85)

# Bar 4: D7 on beat 2
add_chord_notes(5.25, [62, 67, 69, 64], 85)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (67), A (69), D (62) - but staggered with rests and dynamics

note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.7)
note2 = pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.0)
note3 = pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.4)
note4 = pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0)

sax.notes.extend([note1, note2, note3, note4])

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
