
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bassline: Walking line in Fm, chromatic approaches
bass_notes = [
    (53, 1.5, 0.375), (51, 1.875, 0.375), (50, 2.25, 0.375), (52, 2.625, 0.375),
    (53, 3.0, 0.375), (51, 3.375, 0.375), (50, 3.75, 0.375), (52, 4.125, 0.375),
    (53, 4.5, 0.375), (51, 4.875, 0.375), (50, 5.25, 0.375), (52, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comping in Fm
piano_notes = [
    # Bar 2
    (62, 1.875, 0.1875), (65, 1.875, 0.1875), (67, 1.875, 0.1875), (70, 1.875, 0.1875),
    (62, 2.625, 0.1875), (65, 2.625, 0.1875), (67, 2.625, 0.1875), (70, 2.625, 0.1875),
    # Bar 3
    (62, 3.375, 0.1875), (65, 3.375, 0.1875), (67, 3.375, 0.1875), (70, 3.375, 0.1875),
    (62, 4.125, 0.1875), (65, 4.125, 0.1875), (67, 4.125, 0.1875), (70, 4.125, 0.1875),
    # Bar 4
    (62, 4.875, 0.1875), (65, 4.875, 0.1875), (67, 4.875, 0.1875), (70, 4.875, 0.1875),
    (62, 5.625, 0.1875), (65, 5.625, 0.1875), (67, 5.625, 0.1875), (70, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.5),  # Start with a note
    (65, 2.0, 0.5),  # Chromatic up
    (66, 2.5, 0.5),  # Lead into a suspended note
    (62, 3.0, 0.5),  # Return and resolve
    (65, 3.5, 0.5),  # Repeat the motif
    (66, 4.0, 0.5),  # Suspend again
    (62, 4.5, 0.5),  # Resolve
    (65, 5.0, 0.5)   # End on a questioning note
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
