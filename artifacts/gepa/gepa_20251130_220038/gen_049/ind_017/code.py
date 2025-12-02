
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
drum_notes = [
    (0.0, 36, 100),       # Kick on 1
    (0.75, 42, 100),      # Hihat on 2
    (1.125, 42, 100),     # Hihat on 3
    (1.5, 38, 100),       # Snare on 4
    (1.5, 42, 100)        # Hihat on 4
]

for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone melody: Fm (F, Ab, Bb, D, Eb, G, A)
# Melody: F (1.5) -> Eb (1.75) -> Bb (2.0) -> rest (2.25) -> Ab (2.5) -> D (2.75) -> rest (3.0)
sax_notes = [
    (1.5, 65, 100, 0.25),  # F
    (1.75, 62, 100, 0.25), # Eb
    (2.0, 67, 100, 0.25),  # Bb
    (2.25, 65, 100, 0.0),  # Rest
    (2.5, 64, 100, 0.25),  # Ab
    (2.75, 62, 100, 0.25), # D
    (3.0, 65, 100, 0.0)    # Rest
]

for time, pitch, velocity, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration))

# Bass line - walking line in Fm (F, G, Ab, A, Bb, C, Db, D)
# Bar 2: F (1.5) -> G (1.75) -> Ab (2.0) -> A (2.25)
# Bar 3: Bb (2.5) -> C (2.75) -> Db (3.0) -> D (3.25)
bass_notes = [
    (1.5, 65, 70, 0.25),  # F
    (1.75, 67, 70, 0.25), # G
    (2.0, 64, 70, 0.25),  # Ab
    (2.25, 66, 70, 0.25), # A
    (2.5, 62, 70, 0.25),  # Bb
    (2.75, 64, 70, 0.25), # C
    (3.0, 61, 70, 0.25),  # Db
    (3.25, 65, 70, 0.25)  # D
]

for time, pitch, velocity, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration))

# Piano: 7th chords on 2 and 4
# Bar 2: F7 on 2 (1.75)
# Bar 3: Bb7 on 2 (2.75)
# Bar 4: Eb7 on 2 (3.75)
# Bar 4: F7 on 4 (4.5)
piano_notes = [
    # F7 (F, A, Bb, C) on 1.75 (beat 2)
    (1.75, 65, 80, 0.25),
    (1.75, 69, 80, 0.25),
    (1.75, 67, 80, 0.25),
    (1.75, 64, 80, 0.25),
    # Bb7 (Bb, D, Eb, F) on 2.75 (beat 2)
    (2.75, 62, 80, 0.25),
    (2.75, 67, 80, 0.25),
    (2.75, 64, 80, 0.25),
    (2.75, 65, 80, 0.25),
    # Eb7 (Eb, G, Ab, Bb) on 3.75 (beat 2)
    (3.75, 64, 80, 0.25),
    (3.75, 69, 80, 0.25),
    (3.75, 67, 80, 0.25),
    (3.75, 66, 80, 0.25),
    # F7 on 4.5 (beat 4)
    (4.5, 65, 80, 0.25),
    (4.5, 69, 80, 0.25),
    (4.5, 67, 80, 0.25),
    (4.5, 64, 80, 0.25)
]

for time, pitch, velocity, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration))

# Bar 3: Drums (3.0 - 4.5s)
# Kick on 1 (3.0), snare on 2 (3.75), hihat on 2 and 4
drum_notes_bar3 = [
    (3.0, 36, 100),       # Kick on 1
    (3.375, 42, 100),     # Hihat on 2
    (3.75, 38, 100),      # Snare on 2
    (4.125, 42, 100),     # Hihat on 3
    (4.5, 36, 100),       # Kick on 4
    (4.875, 42, 100),     # Hihat on 4
    (4.5, 38, 100)        # Snare on 4
]

for time, note, velocity in drum_notes_bar3:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Bar 4: Drums (4.5 - 6.0s)
# Kick on 1 (4.5), snare on 2 (5.25), hihat on 2 and 4
drum_notes_bar4 = [
    (4.5, 36, 100),       # Kick on 1
    (4.875, 42, 100),     # Hihat on 2
    (5.25, 38, 100),      # Snare on 2
    (5.625, 42, 100),     # Hihat on 3
    (6.0, 36, 100),       # Kick on 4
    (6.375, 42, 100),     # Hihat on 4
    (6.0, 38, 100)        # Snare on 4
]

for time, note, velocity in drum_notes_bar4:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_4bar_intro.mid")
