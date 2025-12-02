
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in C, chromatic approaches
bass_notes = [
    (60, 1.5), (61, 1.75), (62, 2.0), (60, 2.25),
    (62, 2.5), (63, 2.75), (64, 3.0), (62, 3.25),
    (64, 3.5), (65, 3.75), (67, 4.0), (65, 4.25),
    (67, 4.5), (68, 4.75), (70, 5.0), (68, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 2.0), (69, 2.0), (71, 2.0), (72, 2.0),  # C7
    # Bar 3
    (67, 3.0), (72, 3.0), (74, 3.0), (76, 3.0),  # E7
    # Bar 4
    (65, 4.0), (70, 4.0), (72, 4.0), (74, 4.0),  # G7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Dante: Tenor sax motif
# Start with a short phrase, leave it hanging, then complete it
sax_notes = [
    (62, 1.5), (64, 1.75), (65, 2.0), (62, 2.25),  # Bar 2
    (64, 2.5), (67, 2.75), (69, 3.0), (67, 3.25),  # Bar 3
    (65, 3.5), (67, 3.75), (69, 4.0), (67, 4.25),  # Bar 4
    (65, 4.5), (67, 4.75), (69, 5.0), (67, 5.25)   # Bar 4
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Continue pattern for bars 2-4
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
