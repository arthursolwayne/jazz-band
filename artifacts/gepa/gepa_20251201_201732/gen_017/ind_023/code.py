
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
drum_notes = [
    (36, 0.0, 1.0),    # Kick on 1
    (38, 0.5, 1.0),    # Snare on 2
    (36, 1.0, 1.0),    # Kick on 3
    (38, 1.5, 1.0),    # Snare on 4
    (42, 0.0, 1.5)     # Hihat on every eighth
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line D2 (38) -> G2 (43) with chromatic approaches
bass_notes = [
    (38, 1.5, 0.5),    # D2 on 1
    (40, 2.0, 0.5),    # Eb2 on 2
    (43, 2.5, 0.5),    # G2 on 3
    (42, 3.0, 0.5)     # F#2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings - D7 (F#, A, C#, D) on 2, G7 (Bb, D, F, G) on 4
piano_notes = [
    (62, 2.0, 0.5),    # A4
    (67, 2.0, 0.5),    # C#5
    (64, 2.0, 0.5),    # D5
    (65, 2.0, 0.5),    # F#5
    (69, 3.0, 0.5),    # D5
    (67, 3.0, 0.5),    # Bb4
    (66, 3.0, 0.5),    # C#5
    (69, 3.0, 0.5)     # F5
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif - D5 (62), F#5 (67), G5 (67), E5 (64)
sax_notes = [
    (62, 1.5, 0.25),   # D5 on 1
    (67, 1.75, 0.25),  # F#5 on 2
    (67, 2.0, 0.25),   # G5 on 3
    (64, 2.25, 0.25)   # E5 on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line C#2 (41) -> F2 (46) with chromatic approaches
bass_notes = [
    (41, 3.0, 0.5),    # C#2 on 1
    (43, 3.5, 0.5),    # D2 on 2
    (46, 4.0, 0.5),    # F2 on 3
    (44, 4.5, 0.5)     # E2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings - G7 (Bb, D, F, G) on 2, C7 (E, G, B, C) on 4
piano_notes = [
    (69, 3.5, 0.5),    # G4
    (67, 3.5, 0.5),    # Bb4
    (66, 3.5, 0.5),    # D4
    (64, 3.5, 0.5),    # F4
    (60, 4.5, 0.5),    # C4
    (65, 4.5, 0.5),    # E4
    (67, 4.5, 0.5),    # G4
    (71, 4.5, 0.5)     # B4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif with resolution - D5 (62), F#5 (67), G5 (67), D5 (62)
sax_notes = [
    (62, 3.0, 0.25),   # D5 on 1
    (67, 3.25, 0.25),  # F#5 on 2
    (67, 3.5, 0.25),   # G5 on 3
    (62, 3.75, 0.25)   # D5 on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line B2 (46) -> D3 (50) with chromatic approaches
bass_notes = [
    (46, 4.5, 0.5),    # B2 on 1
    (47, 5.0, 0.5),    # C3 on 2
    (50, 5.5, 0.5),    # D3 on 3
    (49, 6.0, 0.5)     # C#3 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings - C7 (E, G, B, C) on 2, D7 (F#, A, C#, D) on 4
piano_notes = [
    (60, 5.0, 0.5),    # C4
    (65, 5.0, 0.5),    # E4
    (67, 5.0, 0.5),    # G4
    (71, 5.0, 0.5),    # B4
    (62, 6.0, 0.5),    # D4
    (67, 6.0, 0.5),    # F#4
    (64, 6.0, 0.5),    # A4
    (62, 6.0, 0.5)     # C#4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif with resolution - D5 (62), F#5 (67), G5 (67), D5 (62)
sax_notes = [
    (62, 4.5, 0.25),   # D5 on 1
    (67, 4.75, 0.25),  # F#5 on 2
    (67, 5.0, 0.25),   # G5 on 3
    (62, 5.25, 0.25)   # D5 on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 1.0),    # Kick on 1
    (38, 5.0, 1.0),    # Snare on 2
    (36, 5.5, 1.0),    # Kick on 3
    (38, 6.0, 1.0),    # Snare on 4
    (42, 4.5, 1.5)     # Hihat on every eighth
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
