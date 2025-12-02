
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.125),  # Hihat on 1
    (42, 0.125, 0.125),  # Hihat on 2
    (38, 0.125, 0.375),  # Snare on 2
    (42, 0.25, 0.125),  # Hihat on 3
    (36, 0.375, 0.375),  # Kick on 3
    (42, 0.375, 0.125),  # Hihat on 3
    (42, 0.5, 0.125),  # Hihat on 4
    (38, 0.5, 0.375),  # Snare on 4
    (42, 0.625, 0.125),  # Hihat on 4
    (42, 0.75, 0.125),  # Hihat on 1 of next bar
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full band in (1.5 - 3.0s)
# Bass: walking line in Fm, chromatic approach to F
# Fm = F, Ab, C, Eb
# Walking line: F -> Gb -> G -> Ab -> A -> Bb -> B -> C -> Db -> D -> Eb -> F
bass_notes = [
    (84, 1.5, 0.375),  # F
    (83, 1.875, 0.375),  # Gb
    (85, 2.25, 0.375),  # G
    (83, 2.625, 0.375),  # Ab
    (86, 3.0, 0.375),  # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on Fm7 (F, Ab, C, Eb)
piano_notes = [
    (84, 1.5, 0.375),  # F
    (87, 1.5, 0.375),  # Ab
    (89, 1.5, 0.375),  # C
    (91, 1.5, 0.375),  # Eb
    (87, 2.25, 0.375),  # Ab
    (89, 2.25, 0.375),  # C
    (91, 2.25, 0.375),  # Eb
    (84, 2.25, 0.375),  # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: short motif - F, Ab, Bb, F (whisper at first, then cry)
sax_notes = [
    (84, 1.5, 0.125),  # F
    (87, 1.625, 0.125),  # Ab
    (88, 1.75, 0.125),  # Bb
    (84, 1.875, 0.125),  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full band (3.0 - 4.5s)
# Bass: walking line in Fm, chromatic approach to F
bass_notes = [
    (83, 3.0, 0.375),  # Gb
    (85, 3.375, 0.375),  # G
    (83, 3.75, 0.375),  # Ab
    (86, 4.125, 0.375),  # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on Fm7 (F, Ab, C, Eb)
piano_notes = [
    (87, 3.0, 0.375),  # Ab
    (89, 3.0, 0.375),  # C
    (91, 3.0, 0.375),  # Eb
    (84, 3.0, 0.375),  # F
    (87, 3.75, 0.375),  # Ab
    (89, 3.75, 0.375),  # C
    (91, 3.75, 0.375),  # Eb
    (84, 3.75, 0.375),  # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: continuation of motif, resolving on Bb
sax_notes = [
    (84, 3.0, 0.125),  # F
    (87, 3.125, 0.125),  # Ab
    (88, 3.25, 0.125),  # Bb
    (84, 3.375, 0.125),  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full band (4.5 - 6.0s)
# Bass: walking line in Fm, chromatic approach to F
bass_notes = [
    (86, 4.5, 0.375),  # A
    (88, 4.875, 0.375),  # Bb
    (86, 5.25, 0.375),  # A
    (84, 5.625, 0.375),  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on Fm7 (F, Ab, C, Eb)
piano_notes = [
    (88, 4.5, 0.375),  # Bb
    (84, 4.5, 0.375),  # F
    (87, 4.5, 0.375),  # Ab
    (89, 4.5, 0.375),  # C
    (88, 5.25, 0.375),  # Bb
    (84, 5.25, 0.375),  # F
    (87, 5.25, 0.375),  # Ab
    (89, 5.25, 0.375),  # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: last part of motif, resolving on F (crying out)
sax_notes = [
    (84, 4.5, 0.125),  # F
    (87, 4.625, 0.125),  # Ab
    (88, 4.75, 0.125),  # Bb
    (84, 4.875, 0.125),  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for Bar 3 and 4
for i in range(2):
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 3.0 + i * 1.5, end=start + duration + 3.0 + i * 1.5))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
