
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
    (36, 0.0, 0.375), (38, 0.375, 0.375),
    (36, 0.75, 0.375), (38, 1.125, 0.375),
    (42, 0.0, 0.125), (42, 0.125, 0.125),
    (42, 0.25, 0.125), (42, 0.375, 0.125),
    (42, 0.5, 0.125), (42, 0.625, 0.125),
    (42, 0.75, 0.125), (42, 0.875, 0.125),
    (42, 1.0, 0.125), (42, 1.125, 0.125),
    (42, 1.25, 0.125), (42, 1.375, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    (45, 1.5, 0.375), (46, 1.875, 0.375),
    (47, 2.25, 0.375), (48, 2.625, 0.375),
    (47, 2.875, 0.375), (46, 3.25, 0.375),
    (45, 3.625, 0.375), (44, 4.0, 0.375),
    (43, 4.375, 0.375), (42, 4.75, 0.375),
    (43, 5.125, 0.375), (44, 5.5, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (59, 1.5, 0.375), (62, 1.5, 0.375), (64, 1.5, 0.375), (66, 1.5, 0.375),
    (60, 1.875, 0.375), (63, 1.875, 0.375), (65, 1.875, 0.375), (67, 1.875, 0.375),
    # Bar 3
    (59, 2.25, 0.375), (62, 2.25, 0.375), (64, 2.25, 0.375), (66, 2.25, 0.375),
    (60, 2.625, 0.375), (63, 2.625, 0.375), (65, 2.625, 0.375), (67, 2.625, 0.375),
    # Bar 4
    (59, 3.0, 0.375), (62, 3.0, 0.375), (64, 3.0, 0.375), (66, 3.0, 0.375),
    (60, 3.375, 0.375), (63, 3.375, 0.375), (65, 3.375, 0.375), (67, 3.375, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Whisper at first, then a cry. Short motif, leave it hanging, come back and finish it.
# Motif: F - A - Bb - rest - F (bar 2), then repeat and resolve in bar 3
sax_notes = [
    # Bar 2: F - A - Bb - rest
    (65, 1.5, 0.375), (68, 1.875, 0.375), (67, 2.25, 0.375),
    # Bar 3: F - A - Bb - F
    (65, 2.625, 0.375), (68, 2.875, 0.375), (67, 3.25, 0.375), (65, 3.625, 0.375),
    # Bar 4: F - A - Bb - F - G - A - Bb - C
    (65, 4.0, 0.375), (68, 4.375, 0.375), (67, 4.75, 0.375), (66, 5.125, 0.375),
    (68, 5.5, 0.375), (69, 5.875, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add dynamics and expressiveness
sax.notes[0].velocity = 60
sax.notes[1].velocity = 75
sax.notes[2].velocity = 80
sax.notes[3].velocity = 100
sax.notes[4].velocity = 100
sax.notes[5].velocity = 100
sax.notes[6].velocity = 100
sax.notes[7].velocity = 110
sax.notes[8].velocity = 100
sax.notes[9].velocity = 100
sax.notes[10].velocity = 100
sax.notes[11].velocity = 100

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
