
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

# Drums: Bar 1
drum_notes = [
    (36, 0.0, 1.0),    # Kick on 1
    (42, 0.125, 0.25), # Hihat on &1
    (38, 0.5, 1.0),    # Snare on 2
    (42, 0.625, 0.75), # Hihat on &2
    (36, 1.0, 1.5),    # Kick on 3
    (42, 1.125, 1.25), # Hihat on &3
    (38, 1.5, 1.5),    # Snare on 4
    (42, 1.625, 1.75)  # Hihat on &4
]

for note, start, end in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Walking line in Fm
# Fm7: F Ab C Eb
# Bar 2: F (root) -> Eb (flat 7) -> C (5th) -> Bb (chromatic approach to Bb)
bass_notes = [
    (38, 1.5, 1.75), # F2
    (36, 1.75, 2.0), # Eb2
    (40, 2.0, 2.25), # C2
    (41, 2.25, 2.5), # Bb2
]

for note, start, end in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    bass.notes.append(note_obj)

# Piano: Open voicings, bar 2: Fm7 (F Ab C Eb) -> A7 (A C# E G) -> Gm7 (G Bb D F) -> C7 (C E G B)
piano_notes = [
    # Bar 2: Fm7 (F Ab C Eb) - 1.5s
    (53, 1.5, 1.75), # F4
    (60, 1.5, 1.75), # Ab4
    (64, 1.5, 1.75), # C5
    (67, 1.5, 1.75), # Eb5

    # Bar 3: A7 (A C# E G) - 2.0s
    (65, 2.0, 2.25), # A4
    (69, 2.0, 2.25), # C#5
    (72, 2.0, 2.25), # E5
    (71, 2.0, 2.25), # G5

    # Bar 4: Gm7 (G Bb D F) - 2.5s
    (67, 2.5, 2.75), # G4
    (69, 2.5, 2.75), # Bb4
    (74, 2.5, 2.75), # D5
    (69, 2.5, 2.75), # F5

    # Bar 5: C7 (C E G B) - 3.0s
    (60, 3.0, 3.25), # C4
    (64, 3.0, 3.25), # E4
    (67, 3.0, 3.25), # G4
    (71, 3.0, 3.25), # B4
]

for note, start, end in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    piano.notes.append(note_obj)

# Sax: Motif, start on 1.5s (Bar 2), 4 notes, leave it hanging
# Fm7 harmony, but with a haunting, incomplete melody
sax_notes = [
    (66, 1.5, 1.75), # Ab4
    (64, 1.75, 2.0), # C4
    (60, 2.0, 2.25), # F4
    (63, 2.25, 2.5), # Bb4
]

for note, start, end in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(note_obj)

# Bar 3: Full quartet (3.0 - 4.5s)

# Drums: Bar 3
drum_notes = [
    (36, 3.0, 3.5),    # Kick on 1
    (42, 3.125, 3.25), # Hihat on &1
    (38, 3.5, 4.0),    # Snare on 2
    (42, 3.625, 3.75), # Hihat on &2
    (36, 4.0, 4.5),    # Kick on 3
    (42, 4.125, 4.25), # Hihat on &3
    (38, 4.5, 4.5),    # Snare on 4
    (42, 4.625, 4.75)  # Hihat on &4
]

for note, start, end in drum_notes:
    dr = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    drums.notes.append(dr)

# Bass line: Walking line in Fm
# Bar 3: Eb (flat7) -> D (chromatic) -> C (5th) -> Bb (chromatic)
bass_notes = [
    (36, 3.0, 3.25), # Eb2
    (35, 3.25, 3.5), # D2
    (40, 3.5, 3.75), # C2
    (41, 3.75, 4.0), # Bb2
]

for note, start, end in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    bass.notes.append(note_obj)

# Piano: Open voicings, bar 3: Cm7 (C Eb G Bb) -> F7 (F A C E) -> Bb7 (Bb D F A) -> Gm7 (G Bb D F)
piano_notes = [
    # Bar 3: Cm7 (C Eb G Bb) - 3.0s
    (60, 3.0, 3.25), # C4
    (63, 3.0, 3.25), # Eb4
    (67, 3.0, 3.25), # G4
    (69, 3.0, 3.25), # Bb4

    # Bar 4: F7 (F A C E) - 3.5s
    (53, 3.5, 3.75), # F4
    (65, 3.5, 3.75), # A4
    (64, 3.5, 3.75), # C5
    (69, 3.5, 3.75), # E5

    # Bar 5: Bb7 (Bb D F A) - 4.0s
    (69, 4.0, 4.25), # Bb4
    (74, 4.0, 4.25), # D5
    (64, 4.0, 4.25), # F5
    (65, 4.0, 4.25), # A5

    # Bar 6: Gm7 (G Bb D F) - 4.5s
    (67, 4.5, 4.75), # G4
    (69, 4.5, 4.75), # Bb4
    (74, 4.5, 4.75), # D5
    (69, 4.5, 4.75), # F5
]

for note, start, end in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    piano.notes.append(note_obj)

# Sax: Motif continuation, Bar 3 (3.0s) with variation
# Start with rest, then a different phrase
sax_notes = [
    (63, 3.0, 3.25), # Bb4
    (67, 3.25, 3.5), # G4
    (64, 3.5, 3.75), # C4
    (61, 3.75, 4.0), # Eb4
]

for note, start, end in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(note_obj)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 5.0),    # Kick on 1
    (42, 4.625, 4.75), # Hihat on &1
    (38, 5.0, 5.5),    # Snare on 2
    (42, 5.125, 5.25), # Hihat on &2
    (36, 5.5, 6.0),    # Kick on 3
    (42, 5.625, 5.75), # Hihat on &3
    (38, 6.0, 6.0),    # Snare on 4
    (42, 6.125, 6.25)  # Hihat on &4
]

for note, start, end in drum_notes:
    dr = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    drums.notes.append(dr)

# Bass line: Walking line in Fm
# Bar 4: F (root) -> Eb (flat7) -> C (5th) -> Bb (chromatic)
bass_notes = [
    (38, 4.5, 4.75), # F2
    (36, 4.75, 5.0), # Eb2
    (40, 5.0, 5.25), # C2
    (41, 5.25, 5.5), # Bb2
]

for note, start, end in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    bass.notes.append(note_obj)

# Piano: Open voicings, bar 4: Gm7 (G Bb D F) -> Cm7 (C Eb G Bb) -> F7 (F A C E) -> Bb7 (Bb D F A)
piano_notes = [
    # Bar 4: Gm7 (G Bb D F) - 4.5s
    (67, 4.5, 4.75), # G4
    (69, 4.5, 4.75), # Bb4
    (74, 4.5, 4.75), # D5
    (69, 4.5, 4.75), # F5

    # Bar 5: Cm7 (C Eb G Bb) - 5.0s
    (60, 5.0, 5.25), # C4
    (63, 5.0, 5.25), # Eb4
    (67, 5.0, 5.25), # G4
    (69, 5.0, 5.25), # Bb4

    # Bar 6: F7 (F A C E) - 5.5s
    (53, 5.5, 5.75), # F4
    (65, 5.5, 5.75), # A4
    (64, 5.5, 5.75), # C5
    (69, 5.5, 5.75), # E5

    # Bar 7: Bb7 (Bb D F A) - 6.0s
    (69, 6.0, 6.25), # Bb4
    (74, 6.0, 6.25), # D5
    (64, 6.0, 6.25), # F5
    (65, 6.0, 6.25), # A5
]

for note, start, end in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    piano.notes.append(note_obj)

# Sax: End of motif, return to first note and leave it hanging
# Fm7 harmony, but with a haunting, incomplete melody
sax_notes = [
    (66, 4.5, 4.75), # Ab4
    (64, 4.75, 5.0), # C4
    (60, 5.0, 5.25), # F4
    (63, 5.25, 5.5), # Bb4
]

for note, start, end in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(note_obj)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])
