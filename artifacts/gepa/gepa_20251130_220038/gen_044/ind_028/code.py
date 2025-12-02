
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (42, 0.0, 0.125),
    (38, 0.375, 0.375), (42, 0.375, 0.125),
    (36, 0.75, 0.375), (42, 0.75, 0.125),
    (38, 1.125, 0.375), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches
bass_notes = [
    (57, 1.5, 0.375),  # D
    (58, 1.875, 0.375), # Eb
    (59, 2.25, 0.375),  # E
    (57, 2.625, 0.375), # D
    (55, 2.625, 0.375), # Bb
    (57, 3.0, 0.375),   # D
    (58, 3.375, 0.375), # Eb
    (59, 3.75, 0.375),  # E
    (57, 4.125, 0.375), # D
    (55, 4.5, 0.375),   # Bb
    (57, 4.875, 0.375), # D
    (58, 5.25, 0.375),  # Eb
    (59, 5.625, 0.375), # E
    (57, 6.0, 0.375)    # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.125), (65, 1.5, 0.125), (67, 1.5, 0.125), (69, 1.5, 0.125),  # Dm7
    (65, 2.25, 0.125), (67, 2.25, 0.125), (69, 2.25, 0.125), (71, 2.25, 0.125),  # G7
    # Bar 3 (3.0 - 4.5s)
    (62, 3.0, 0.125), (65, 3.0, 0.125), (67, 3.0, 0.125), (69, 3.0, 0.125),  # Dm7
    (65, 3.75, 0.125), (67, 3.75, 0.125), (69, 3.75, 0.125), (71, 3.75, 0.125),  # G7
    # Bar 4 (4.5 - 6.0s)
    (62, 4.5, 0.125), (65, 4.5, 0.125), (67, 4.5, 0.125), (69, 4.5, 0.125),  # Dm7
    (65, 5.25, 0.125), (67, 5.25, 0.125), (69, 5.25, 0.125), (71, 5.25, 0.125)   # G7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Original motif, one short phrase, make it sing
sax_notes = [
    (62, 1.5, 0.375),  # D
    (67, 1.875, 0.375), # G
    (65, 2.25, 0.375),  # E
    (67, 2.625, 0.375), # G
    (62, 3.0, 0.375),   # D
    (67, 3.375, 0.375), # G
    (65, 3.75, 0.375),  # E
    (67, 4.125, 0.375), # G
    (62, 4.5, 0.375),   # D
    (67, 4.875, 0.375), # G
    (65, 5.25, 0.375),  # E
    (67, 5.625, 0.375)  # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
