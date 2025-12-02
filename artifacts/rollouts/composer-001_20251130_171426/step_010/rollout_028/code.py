
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
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875),
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (48, 1.5, 0.375), (49, 1.875, 0.375), (50, 2.25, 0.375), (51, 2.625, 0.375),
    (53, 2.625, 0.375), (52, 3.0, 0.375), (51, 3.375, 0.375), (50, 3.75, 0.375),
    (49, 4.125, 0.375), (48, 4.5, 0.375), (47, 4.875, 0.375), (46, 5.25, 0.375),
    (48, 5.25, 0.375), (49, 5.625, 0.375), (50, 6.0, 0.375)
]

for note, start, duration in bass_notes:
    nb = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(nb)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (59, 1.5, 0.375), (64, 1.5, 0.375), (61, 1.5, 0.375), (66, 1.5, 0.375),
    # Bar 3
    (59, 3.0, 0.375), (64, 3.0, 0.375), (61, 3.0, 0.375), (66, 3.0, 0.375),
    # Bar 4
    (59, 4.5, 0.375), (64, 4.5, 0.375), (61, 4.5, 0.375), (66, 4.5, 0.375)
]

for note, start, duration in piano_notes:
    np = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    piano.notes.append(np)

# Sax: Motif in F, one phrase, leave it hanging, come back
sax_notes = [
    (62, 1.5, 0.375), (66, 1.875, 0.375), (67, 2.25, 0.375),
    (65, 2.25, 0.375), (62, 2.625, 0.375), (65, 2.625, 0.375),
    (67, 3.0, 0.375), (66, 3.375, 0.375), (62, 3.75, 0.375),
    (65, 4.125, 0.375), (67, 4.5, 0.375), (66, 4.875, 0.375),
    (65, 5.25, 0.375), (62, 5.625, 0.375)
]

for note, start, duration in sax_notes:
    ns = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(ns)

# Add all instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
