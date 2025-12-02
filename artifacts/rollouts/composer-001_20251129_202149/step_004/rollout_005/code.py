
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.1875, 0.1875),  # Hihat on 1&
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.5625, 0.1875),  # Hihat on 2&
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.9375, 0.1875),  # Hihat on 3&
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.3125, 0.1875)  # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Sax: 4-note motif
sax_notes = [
    (62, 1.5, 0.25),  # C5
    (65, 1.75, 0.25),  # E5
    (67, 2.0, 0.25),  # G5
    (69, 2.25, 0.25),  # A5
    (67, 2.5, 0.25),  # G5
    (65, 2.75, 0.25),  # E5
    (62, 3.0, 0.25),  # C5
    (60, 3.25, 0.25),  # Bb4
    (62, 3.5, 0.25),  # C5
    (64, 3.75, 0.25),  # D5
    (65, 4.0, 0.25),  # E5
    (67, 4.25, 0.25),  # G5
    (69, 4.5, 0.25),  # A5
    (67, 4.75, 0.25),  # G5
    (65, 5.0, 0.25),  # E5
    (62, 5.25, 0.25)   # C5
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line
bass_notes = [
    (48, 1.5, 0.25),  # C3
    (50, 1.75, 0.25),  # D3
    (49, 2.0, 0.25),  # C#3
    (50, 2.25, 0.25),  # D3
    (52, 2.5, 0.25),  # E3
    (53, 2.75, 0.25),  # F3
    (52, 3.0, 0.25),  # E3
    (50, 3.25, 0.25),  # D3
    (52, 3.5, 0.25),  # E3
    (54, 3.75, 0.25),  # F#3
    (55, 4.0, 0.25),  # G3
    (54, 4.25, 0.25),  # F#3
    (53, 4.5, 0.25),  # F3
    (52, 4.75, 0.25),  # E3
    (50, 5.0, 0.25),  # D3
    (48, 5.25, 0.25)   # C3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.75, 0.25),  # C7 (C E G B)
    (67, 1.75, 0.25),
    (71, 1.75, 0.25),
    (72, 1.75, 0.25),
    # Bar 3
    (64, 3.25, 0.25),  # C7
    (67, 3.25, 0.25),
    (71, 3.25, 0.25),
    (72, 3.25, 0.25),
    # Bar 4
    (64, 4.75, 0.25),  # C7
    (67, 4.75, 0.25),
    (71, 4.75, 0.25),
    (72, 4.75, 0.25)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.6875, 0.1875),  # Hihat on 1&
    (38, 1.875, 0.375),  # Snare on 2
    (42, 2.0625, 0.1875),  # Hihat on 2&
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.4375, 0.1875),  # Hihat on 3&
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.8125, 0.1875),  # Hihat on 4&
    # Bar 3
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.1875, 0.1875),  # Hihat on 1&
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.5625, 0.1875),  # Hihat on 2&
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.9375, 0.1875),  # Hihat on 3&
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.3125, 0.1875),  # Hihat on 4&
    # Bar 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.6875, 0.1875),  # Hihat on 1&
    (38, 4.875, 0.375),  # Snare on 2
    (42, 5.0625, 0.1875),  # Hihat on 2&
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.4375, 0.1875),  # Hihat on 3&
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.8125, 0.1875)  # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
