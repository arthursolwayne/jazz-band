
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat on 1 &
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2 &
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3 &
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.1875)  # Hihat on 4 &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5s)
    (53, 1.5, 0.375),  # F
    (57, 1.875, 0.375), # Bb
    (55, 2.25, 0.375),  # Ab (chromatic approach)
    (53, 2.625, 0.375), # F
    # Bar 3 (3.0s)
    (53, 3.0, 0.375),  # F
    (57, 3.375, 0.375), # Bb
    (55, 3.75, 0.375),  # Ab
    (53, 4.125, 0.375), # F
    # Bar 4 (4.5s)
    (53, 4.5, 0.375),  # F
    (57, 4.875, 0.375), # Bb
    (55, 5.25, 0.375),  # Ab
    (53, 5.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    (53, 1.5, 0.375),  # F
    (60, 1.5, 0.375),  # C
    (64, 1.5, 0.375),  # Eb
    (57, 1.5, 0.375),  # Ab
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    (57, 3.0, 0.375),  # Bb
    (62, 3.0, 0.375),  # D
    (53, 3.0, 0.375),  # F
    (57, 3.0, 0.375),  # Ab
])
# Bar 4: Ab7 (Ab, C, Eb, Gb)
piano_notes.extend([
    (55, 4.5, 0.375),  # Ab
    (60, 4.5, 0.375),  # C
    (64, 4.5, 0.375),  # Eb
    (61, 4.5, 0.375),  # Gb
])
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif - start with a short phrase, leave it hanging, then come back and finish it
# Motif: F (53), Ab (57), C (60)
sax_notes = [
    (53, 1.5, 0.5),  # F
    (57, 2.0, 0.5),  # Ab
    (60, 2.5, 0.5),  # C
    (53, 3.0, 0.5),  # F
    (57, 3.5, 0.5),  # Ab
    (60, 4.0, 0.5),  # C
    (53, 4.5, 0.5),  # F
    (57, 5.0, 0.5),  # Ab
    (60, 5.5, 0.5)   # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
# Bar 2 (1.5s)
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.1875),   # Hihat on 1 &
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2 &
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.1875),  # Hihat on 3 &
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.1875)  # Hihat on 4 &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3 (3.0s)
drum_notes = [
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.1875),   # Hihat on 1 &
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2 &
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.1875),  # Hihat on 3 &
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.1875)  # Hihat on 4 &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4 (4.5s)
drum_notes = [
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.1875),   # Hihat on 1 &
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2 &
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.1875),  # Hihat on 3 &
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.1875)  # Hihat on 4 &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
