
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4
drum_notes = [
    (0.0, 36, 100),  # Kick on beat 1
    (0.75, 42, 100), # Hihat on &1
    (1.125, 42, 100), # Hihat on &2
    (1.5, 38, 100),  # Snare on beat 2
    (1.875, 42, 100), # Hihat on &3
    (2.25, 42, 100), # Hihat on &4
    (2.625, 36, 100), # Kick on beat 3
    (3.0, 38, 100),  # Snare on beat 4
    (3.375, 42, 100) # Hihat on &4
]

for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus
# Walking line in Fm: F, Gb, Ab, A, Bb, B, C, Db, etc.
bass_notes = [
    (1.5, 64, 100),  # F (beat 1)
    (1.75, 65, 100),  # Gb (beat &2)
    (2.0, 66, 100),  # Ab (beat 3)
    (2.25, 67, 100),  # A (beat &4)
    (2.5, 67, 100),  # Bb (beat 1)
    (2.75, 68, 100),  # B (beat &2)
    (3.0, 69, 100),  # C (beat 3)
    (3.25, 70, 100),  # Db (beat &4)
    (3.5, 69, 100),  # C (beat 1)
    (3.75, 70, 100),  # Db (beat &2)
    (4.0, 71, 100),  # D (beat 3)
    (4.25, 72, 100),  # Eb (beat &4)
    (4.5, 72, 100),  # Eb (beat 1)
    (4.75, 73, 100),  # E (beat &2)
    (5.0, 74, 100),  # F (beat 3)
    (5.25, 75, 100)  # F# (beat &4)
]

for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano - Diane
# 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (1.5, 64, 100),  # F7 - F
    (1.5, 71, 100),  # F7 - Bb
    (1.5, 76, 100),  # F7 - E
    (1.5, 79, 100),  # F7 - Ab
    (2.0, 64, 100),  # F7 - F
    (2.0, 71, 100),  # F7 - Bb
    (2.0, 76, 100),  # F7 - E
    (2.0, 79, 100),  # F7 - Ab
    # Bar 3
    (2.5, 64, 100),  # Ab7 - Ab
    (2.5, 72, 100),  # Ab7 - Db
    (2.5, 76, 100),  # Ab7 - E
    (2.5, 79, 100),  # Ab7 - Gb
    (3.0, 64, 100),  # Ab7 - Ab
    (3.0, 72, 100),  # Ab7 - Db
    (3.0, 76, 100),  # Ab7 - E
    (3.0, 79, 100),  # Ab7 - Gb
    # Bar 4
    (3.5, 64, 100),  # Bb7 - Bb
    (3.5, 71, 100),  # Bb7 - D
    (3.5, 76, 100),  # Bb7 - F
    (3.5, 79, 100),  # Bb7 - Ab
    (4.0, 64, 100),  # Bb7 - Bb
    (4.0, 71, 100),  # Bb7 - D
    (4.0, 76, 100),  # Bb7 - F
    (4.0, 79, 100),  # Bb7 - Ab
]

for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax - Dante
# Motif: F - Ab - Bb - C, then leave it hanging, then come back with F - Ab - Bb - C
sax_notes = [
    (1.5, 64, 100),  # F (beat 1)
    (1.625, 69, 100),  # Ab
    (1.75, 67, 100),  # Bb
    (1.875, 69, 100),  # C
    (2.5, 64, 100),  # F (beat 1)
    (2.625, 69, 100),  # Ab
    (2.75, 67, 100),  # Bb
    (2.875, 69, 100)  # C
]

for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Drums in Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 5):
    start = i * 1.5
    # Bar 2 drum pattern
    drum_notes = [
        (start, 36, 100),  # Kick on beat 1
        (start + 0.75, 42, 100), # Hihat on &1
        (start + 1.125, 42, 100), # Hihat on &2
        (start + 1.5, 38, 100),  # Snare on beat 2
        (start + 1.875, 42, 100), # Hihat on &3
        (start + 2.25, 42, 100), # Hihat on &4
        (start + 2.625, 36, 100), # Kick on beat 3
        (start + 3.0, 38, 100),  # Snare on beat 4
        (start + 3.375, 42, 100) # Hihat on &4
    ]
    for time, note, velocity in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
