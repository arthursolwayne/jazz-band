
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Build tension with space and subtle dynamics
drum_notes = [
    (0.0, 38, 80),   # snare on 2
    (0.5, 42, 60),   # hihat on &2
    (1.0, 36, 100),  # kick on 3
    (1.5, 38, 80),   # snare on 4
    (1.75, 42, 60),  # hihat on &4
]

for time, note, velocity in drum_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif (Dante)
sax_notes = [
    (1.5, 64, 100),  # Fm7 - F
    (1.75, 67, 90),  # Ab
    (2.0, 69, 110),  # Bb
    (2.25, 64, 95),  # F
    (2.5, 67, 100),  # Ab
    (2.75, 71, 110), # D
    (3.0, 69, 100),  # Bb
    (3.25, 67, 95),  # Ab
    (3.5, 64, 100),  # F
    (3.75, 66, 110), # G
    (4.0, 69, 100),  # Bb
    (4.25, 67, 95),  # Ab
    (4.5, 64, 100),  # F
    (4.75, 66, 110), # G
    (5.0, 69, 100),  # Bb
    (5.25, 71, 110), # D
    (5.5, 69, 100),  # Bb
    (5.75, 64, 95),  # F
]

for time, note, velocity in sax_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Bass line (Marcus) - chromatic, melodic, active
bass_notes = [
    (1.5, 57, 90),   # F (root)
    (1.75, 55, 95),  # Eb (chromatic)
    (2.0, 58, 90),   # G
    (2.25, 60, 85),  # A
    (2.5, 58, 95),   # G
    (2.75, 55, 90),  # Eb
    (3.0, 53, 85),   # Db
    (3.25, 57, 90),  # F
    (3.5, 58, 95),   # G
    (3.75, 60, 85),  # A
    (4.0, 58, 90),   # G
    (4.25, 55, 95),  # Eb
    (4.5, 53, 85),   # Db
    (4.75, 57, 90),  # F
    (5.0, 58, 95),   # G
    (5.25, 60, 85),  # A
    (5.5, 58, 90),   # G
    (5.75, 57, 85),  # F
]

for time, note, velocity in bass_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano comping (Diane) - 7th chords, on 2 and 4
piano_notes = [
    (2.0, 64, 80),   # F7 - F
    (2.0, 67, 75),   # Ab
    (2.0, 71, 70),   # D
    (2.0, 72, 65),   # Eb
    (2.25, 64, 80),  # F
    (2.25, 67, 75),  # Ab
    (2.25, 71, 70),  # D
    (2.25, 72, 65),  # Eb
    (3.0, 64, 80),   # F
    (3.0, 67, 75),   # Ab
    (3.0, 71, 70),   # D
    (3.0, 72, 65),   # Eb
    (3.25, 64, 80),  # F
    (3.25, 67, 75),  # Ab
    (3.25, 71, 70),  # D
    (3.25, 72, 65),  # Eb
    (4.0, 64, 80),   # F
    (4.0, 67, 75),   # Ab
    (4.0, 71, 70),   # D
    (4.0, 72, 65),   # Eb
    (4.25, 64, 80),  # F
    (4.25, 67, 75),  # Ab
    (4.25, 71, 70),  # D
    (4.25, 72, 65),  # Eb
    (5.0, 64, 80),   # F
    (5.0, 67, 75),   # Ab
    (5.0, 71, 70),   # D
    (5.0, 72, 65),   # Eb
    (5.25, 64, 80),  # F
    (5.25, 67, 75),  # Ab
    (5.25, 71, 70),  # D
    (5.25, 72, 65),  # Eb
]

for time, note, velocity in piano_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Drums for bars 2-4 (Little Ray)
drum_notes = [
    # Bar 2
    (1.5, 36, 100),  # Kick on 1
    (1.75, 42, 60),  # Hihat on &2
    (2.0, 38, 80),   # Snare on 2
    (2.25, 42, 60),  # Hihat on &3
    (2.5, 36, 100),  # Kick on 3
    (2.75, 42, 60),  # Hihat on &4
    (3.0, 38, 80),   # Snare on 4
    (3.25, 42, 60),  # Hihat on &1
    # Bar 3
    (3.5, 36, 100),  # Kick on 1
    (3.75, 42, 60),  # Hihat on &2
    (4.0, 38, 80),   # Snare on 2
    (4.25, 42, 60),  # Hihat on &3
    (4.5, 36, 100),  # Kick on 3
    (4.75, 42, 60),  # Hihat on &4
    (5.0, 38, 80),   # Snare on 4
    (5.25, 42, 60),  # Hihat on &1
    # Bar 4
    (5.5, 36, 100),  # Kick on 1
    (5.75, 42, 60),  # Hihat on &2
    (6.0, 38, 80),   # Snare on 2
    (6.25, 42, 60),  # Hihat on &3
    (6.5, 36, 100),  # Kick on 3
    (6.75, 42, 60),  # Hihat on &4
]

for time, note, velocity in drum_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
