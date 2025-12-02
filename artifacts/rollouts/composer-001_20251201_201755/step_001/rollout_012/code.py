
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    (43, 1.5, 0.375),  # D2 (root)
    (45, 1.875, 0.375),  # F2 (fifth)
    (44, 2.25, 0.375),  # E2 (chromatic approach)
    (43, 2.625, 0.375)  # D2 (root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    (52, 1.5, 0.375),  # D4
    (56, 1.5, 0.375),  # F4
    (60, 1.5, 0.375),  # A4
    (62, 1.5, 0.375),  # C4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante on sax: short motif, make it sing, leave it hanging
sax_notes = [
    (62, 1.5, 0.375),  # D4
    (65, 1.875, 0.375),  # F4
    (67, 2.25, 0.375),  # G4
    (65, 2.625, 0.375)  # F4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus on bass: walking line in Dm
bass_notes = [
    (43, 3.0, 0.375),  # D2 (root)
    (45, 3.375, 0.375),  # F2 (fifth)
    (44, 3.75, 0.375),  # E2 (chromatic approach)
    (43, 4.125, 0.375)  # D2 (root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane on piano: Bm7 (B D F# A)
piano_notes = [
    (59, 3.0, 0.375),  # B4
    (62, 3.0, 0.375),  # D4
    (66, 3.0, 0.375),  # F#4
    (69, 3.0, 0.375)  # A4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante on sax: continue the motif, leave it hanging
sax_notes = [
    (67, 3.0, 0.375),  # G4
    (65, 3.375, 0.375),  # F4
    (62, 3.75, 0.375),  # D4
    (60, 4.125, 0.375)  # C4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus on bass: walking line in Dm
bass_notes = [
    (43, 4.5, 0.375),  # D2 (root)
    (45, 4.875, 0.375),  # F2 (fifth)
    (44, 5.25, 0.375),  # E2 (chromatic approach)
    (43, 5.625, 0.375)  # D2 (root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane on piano: G7 (G B D F)
piano_notes = [
    (67, 4.5, 0.375),  # G4
    (71, 4.5, 0.375),  # B4
    (69, 4.5, 0.375),  # D4
    (67, 4.5, 0.375)  # G4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante on sax: finish the motif
sax_notes = [
    (62, 4.5, 0.375),  # D4
    (65, 4.875, 0.375),  # F4
    (67, 5.25, 0.375),  # G4
    (65, 5.625, 0.375)  # F4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
