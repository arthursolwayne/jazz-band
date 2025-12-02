
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Everyone joins in (1.5 - 3.0s)
# Sax: motif in C minor, ascending 3rd then descending
sax_notes = [
    (60, 1.5, 0.375),  # C
    (63, 1.875, 0.375), # E
    (60, 2.25, 0.375),  # C
    (58, 2.625, 0.375)  # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: walking line in C minor
bass_notes = [
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375), # Db
    (62, 2.25, 0.375),  # D
    (63, 2.625, 0.375)  # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: comping on 2 and 4 with 7th chords
piano_notes = [
    (60, 1.875, 0.375),  # C7 (C, E, Bb)
    (60, 1.875, 0.375),
    (64, 1.875, 0.375),
    (67, 1.875, 0.375),
    (60, 2.625, 0.375),  # C7 again on 4
    (60, 2.625, 0.375),
    (64, 2.625, 0.375),
    (67, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: continue the pattern
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 1.5, end=start + 1.5 + duration))

# Bar 3: Sax continues motif, bass walks, piano comps
# Sax
sax_notes = [
    (58, 3.0, 0.375),  # Bb
    (60, 3.375, 0.375),  # C
    (63, 3.75, 0.375),  # E
    (60, 4.125, 0.375)  # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass
bass_notes = [
    (63, 3.0, 0.375),  # E
    (64, 3.375, 0.375),  # F
    (65, 3.75, 0.375),  # G
    (67, 4.125, 0.375)  # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano
piano_notes = [
    (60, 3.375, 0.375),  # C7 on 2
    (60, 3.375, 0.375),
    (64, 3.375, 0.375),
    (67, 3.375, 0.375),
    (60, 4.125, 0.375),  # C7 on 4
    (60, 4.125, 0.375),
    (64, 4.125, 0.375),
    (67, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 3.0, end=start + 3.0 + duration))

# Bar 4: Sax resolves the motif, bass walks, piano comps
# Sax
sax_notes = [
    (60, 4.5, 0.375),  # C
    (63, 4.875, 0.375),  # E
    (60, 5.25, 0.375),  # C
    (58, 5.625, 0.375)  # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass
bass_notes = [
    (67, 4.5, 0.375),  # A
    (68, 4.875, 0.375),  # Bb
    (69, 5.25, 0.375),  # B
    (70, 5.625, 0.375)  # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano
piano_notes = [
    (60, 4.875, 0.375),  # C7 on 2
    (60, 4.875, 0.375),
    (64, 4.875, 0.375),
    (67, 4.875, 0.375),
    (60, 5.625, 0.375),  # C7 on 4
    (60, 5.625, 0.375),
    (64, 5.625, 0.375),
    (67, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 4.5, end=start + 4.5 + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
