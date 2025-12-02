
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
    (42, 0.0, 0.125), (42, 0.125, 0.125), (42, 0.25, 0.125), (42, 0.375, 0.125),
    (42, 0.5, 0.125), (42, 0.625, 0.125), (42, 0.75, 0.125), (42, 0.875, 0.125),
    (42, 1.0, 0.125), (42, 1.125, 0.125), (42, 1.25, 0.125), (42, 1.375, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (37, 1.5, 0.375), (38, 1.875, 0.375), (36, 2.25, 0.375), (35, 2.625, 0.375),
    (37, 2.625, 0.375), (38, 3.0, 0.375), (36, 3.375, 0.375), (35, 3.75, 0.375),
    (37, 3.75, 0.375), (38, 4.125, 0.375), (36, 4.5, 0.375), (34, 4.875, 0.375),
    (37, 4.875, 0.375), (38, 5.25, 0.375), (36, 5.625, 0.375), (35, 6.0, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, Bb, D)
    (53, 1.5, 0.375), (55, 1.5, 0.375), (58, 1.5, 0.375), (62, 1.5, 0.375),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (58, 2.25, 0.375), (62, 2.25, 0.375), (53, 2.25, 0.375), (55, 2.25, 0.375),
    # Bar 4: Eb7 (Eb, G, Bb, D)
    (56, 3.0, 0.375), (59, 3.0, 0.375), (58, 3.0, 0.375), (62, 3.0, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Saxophone: short motif, start on beat 1 of bar 2, leave it hanging
# Motif: F, Ab, Bb, D (Fm7), then leave on the D
sax_notes = [
    (53, 1.5, 0.375), (55, 1.875, 0.375), (58, 2.25, 0.375), (62, 2.625, 0.375),
    (62, 2.625, 0.875)  # D held for the rest of the measure
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 * bar
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(kick2)
    drums.notes.append(snare2)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
